from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os

class GpxercesConan(ConanFile):
    name = "xerces-c"
    version = os.getenv("xerces_version")
    license = "Apache License v2.0"
    url = os.getenv("conan_github_url")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"

    def source(self):
        self.run("git clone -b {0} https://github.com/apache/xerces-c.git".format(self.version))
        self.run("cd xerces-c && ./reconf")


    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        os.mkdir("build")
        os.environ['CC'] = '/usr/bin/gcc'
        os.environ['CXX'] = '/usr/bin/g++'
        with tools.chdir("build"):
            config_args = []
            if not self.options.shared:
                config_args.append("--enable-shared")
            config_args.append("--prefix=" + self.build_folder + "/install")
            env_build.configure(configure_dir="../xerces-c/", args=config_args)
            env_build.make()
            env_build.make(args=["install"])


    def package(self):
        self.copy("*", dst="include", src="install/include")
        self.copy("*", dst="lib", src="install/lib", keep_path=True, links=True)
