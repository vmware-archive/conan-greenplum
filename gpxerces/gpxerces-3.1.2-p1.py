from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os


class GpxercesConan(ConanFile):
    name = "gpxerces"
    version = "v3.1.2-p1"
    license = "Apache License v2.0"
    url = "http://github.com/greenplum-db/conan"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"

    def source(self):
        self.run("git clone -b v3.1.2-p1 https://github.com/greenplum-db/gp-xerces.git")

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        os.mkdir("build")
        with tools.chdir("build"):
            config_args = []
            if not self.options.shared:
                config_args.append("--enable-shared")
            config_args.append("--prefix=" + self.build_folder + "/install")
            env_build.configure(configure_dir="../gp-xerces/", args=config_args)
            env_build.make()
            env_build.make(args=["install"])


    def package(self):
        self.copy("*", dst="include", src="install/include")
        self.copy("*", dst="lib", src="install/lib", keep_path=True, links=True)
