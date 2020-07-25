if ("x${CMAKE_SOURCE_DIR}" STREQUAL "x${CMAKE_BINARY_DIR}")
  message(FATAL_ERROR
          "In-source build is not a good practice. Please use:
            mkdir build
            cd build
            cmake ..
          to build this project")
endif ()

cmake_minimum_required(VERSION 3.12 FATAL_ERROR)

project(sequeender
        LANGUAGES CXX
        VERSION 0.1.0
        HOMEPAGE_URL "https://github.com/songmeixu/sequeender"
        DESCRIPTION "one day, SEQuence problems got the qUEen's END ordER, \
        the codename is SEQUEENDER.")

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

option(BUILD_SHARED_LIBS "Whether to build shared or static lib" ON)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")

enable_testing()

#
# prepend header directories instead of append
#
set(CMAKE_INCLUDE_DIRECTORIES_BEFORE ON)

#
# Add our project's cmake dir the the module path. This gives us:
# cpplint, glog, googletest, pybind11,
# Cppyy commands and targets.
#
list(INSERT CMAKE_MODULE_PATH 0 ${CMAKE_SOURCE_DIR}/cmake)
message("${CMAKE_MODULE_PATH}")
find_package(Cppyy)

#
# Make the default build us c++11 and "RELEASE" (-O3)
#
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
if (NOT CMAKE_BUILD_TYPE)
  message(STATUS "No CMAKE_BUILD_TYPE given, default to Release")
  set(CMAKE_BUILD_TYPE Release CACHE STRING
      "Set the build type. Available values are: Debug Release RelWithDebInfo MinSizeRel"
      FORCE)
endif ()

if (WIN32 AND BUILD_SHARED_LIBS)
  message(STATUS "Set BUILD_SHARED_LIBS to OFF for Windows")
  set(BUILD_SHARED_LIBS OFF CACHE BOOL "" FORCE)
endif ()

include(cpplint)
include(glog)
include(googletest)
#include(pybind11)
include(GNUInstallDirs)

#
# Set up the target shared lib
#
add_subdirectory(sequeender)
