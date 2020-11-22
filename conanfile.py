from conans import ConanFile, CMake, tools


class K2DepsConan(ConanFile):
    name                              = "K2Deps"
    version                           = "0.1"
    settings                          = "os", "compiler", "arch"
    requires                          = "cub/1.10.0@os/release",        \
                                        "moderngpu/2b39855@os/release", \
                                        "pybind11/2.6.1@"
    build_requires                    = "gtest/1.10.0@"
    default_options                   = {"gtest:shared": True}
    generators                        = "cmake_find_package"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
