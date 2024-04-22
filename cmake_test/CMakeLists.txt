cmake_minimum_required(VERSION 3.10)  # Set the minimum version of CMake required

# Set your project name and version
project(MinimalCMakeProject VERSION 1.0)

# Specify C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add an executable
add_executable(MinimalCMake src/main.cpp)
