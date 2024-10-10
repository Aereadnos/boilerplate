cmake_minimum_required(VERSION 3.10)
project(LibraryRepo)

# Add your source files here
add_library(my_library STATIC src/library.cpp)

# Install include directories into the installation path
target_include_directories(my_library PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>  # This is the relative path used after installation
)

# Set the C++ standard
set_target_properties(my_library PROPERTIES CXX_STANDARD 17 CXX_STANDARD_REQUIRED YES)

# Install the library and the header files
install(TARGETS my_library
    EXPORT my_libraryConfig
    DESTINATION lib
)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/ DESTINATION include)

# Create and install CMake package configuration files
install(EXPORT my_libraryConfig
    FILE my_libraryConfig.cmake
    DESTINATION lib/cmake/my_library
)

# Specify where to find the include directories for this package
include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/my_libraryConfigVersion.cmake"
    VERSION 1.0
    COMPATIBILITY AnyNewerVersion
)

install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/my_libraryConfigVersion.cmake"
    DESTINATION lib/cmake/my_library
)
