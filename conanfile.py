from conans import ConanFile, CMake, tools


class PmpConan(ConanFile):
    name = "pmp"
    lib_version = '1.1.0'
    pkg_version = '0'
    version = '{}-{}'.format(lib_version, pkg_version)
    license = "MIT (https://github.com/pmp-library/pmp-library/blob/master/LICENSE.txt)"
    url = "https://github.com/pmp-library/pmp-library"
    description = "Recipe for the pmp library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    short_paths = True

    scm = {
        "type" : "git",
        "url"  : "https://github.com/pmp-library/pmp-library.git",
        "revision" : '{}'.format(lib_version),
        "submodule" : "recursive"
    }

    def _configure(self):
        cmake = CMake(self)
        if self.settings.os == 'Macos':
            cmake.definitions['CMAKE_MACOSX_RPATH'] = "TRUE"
        cmake.configure()
        return cmake


    def build(self):
        cmake = self._configure()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = self._configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

