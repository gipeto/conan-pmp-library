import os

from conans import ConanFile, CMake, tools


class PmpTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"

    def build(self):
        cmake = CMake(self)
        cmake.definitions['CMAKE_INSTALL_PREFIX']='install'
        cmake.configure()
        cmake.build(target='install')

    def imports(self):
        self.copy("*.dll", dst="install/bin", src="bin")
        self.copy("*.dylib*", dst="install/bin", src="lib")
        self.copy('*.so*', dst='install/bin', src='lib')

    def test(self):
        self.run(os.path.join('install','bin','example'))
