from conans import ConanFile, CMake, tools
import os
import subprocess


class OrcaConan(ConanFile):
    name = "orca"
    version = "v2.32.0"
    license = "Apache License v2.0"
    url = "http://github.com/greenplum-db/conan"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        self.run("git clone -b v2.32.0 https://github.com/greenplum-db/gporca.git")

    def requirements(self):
        self.requires("gpxerces/v3.1.2-p1@gpdb/stable")

    def build_requirements(self):
    # Normally this would refer to some packages much like requirements
    # but we overload this to ensure that CMake is present
        try:
            vers = subprocess.check_output(["cmake", "--version"]).split()[2]
            if int(vers.split(".")[0]) < 3:
                raise Exception("CMake version 3.0 or higher is required")
        except OSError as e:
            if e.errno == os.errno.ENOENT:
                raise Exception("CMake is not found.  Please ensure the CMake 3.0 or later is installed")
            else:
                raise

    def build(self):
        top_dir=os.getcwd()
        os.mkdir("build")
        os.mkdir("install")
        build_dir =     os.path.join(top_dir, "build")
        install_dir =   os.path.join(top_dir, "install")
        src_dir =       os.path.join(top_dir, "gporca")

        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
	if tools.os_info.is_macos:
		cmake_defines={
			" XERCES_INCLUDE_DIR":   self.deps_cpp_info["gpxerces"].include_paths[0],
			" XERCES_LIBRARY":       self.deps_cpp_info["gpxerces"].lib_paths[0] + "/libxerces-c.dylib",
			" CMAKE_INSTALL_PREFIX": install_dir
			}
	else:
		cmake_defines={
			" XERCES_INCLUDE_DIR":   self.deps_cpp_info["gpxerces"].include_paths[0],
			" XERCES_LIBRARY":       self.deps_cpp_info["gpxerces"].lib_paths[0] + "/libxerces-c.so",
			" CMAKE_INSTALL_PREFIX": install_dir
			}
        cmake.configure(source_dir=src_dir, build_dir=build_dir, defs=cmake_defines)
        cmake.build(target="install")

    def package(self):
        self.copy("*.h", dst="include", src="install/include")
        self.copy("*.dylib*", dst="lib", src="install/lib", keep_path=False, symlinks=True)
        self.copy("*.so*", dst="lib", src="install/lib", keep_path=False, symlinks=True)
        self.copy("*.a*", dst="lib", src="install/lib", keep_path=False, symlinks=True)
