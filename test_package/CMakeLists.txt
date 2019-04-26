cmake_minimum_required (VERSION 3.5)
project (NanoSVGTest)

set (CMAKE_CXX_STANDARD 11)

include (${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable (nanosvgtest nanosvgtest.cpp)

target_compile_definitions(nanosvgtest PRIVATE NANOSVGRAST_CPLUSPLUS NANOSVGRAST_IMPLEMENTATION)

conan_target_link_libraries (nanosvgtest)
