cmake_minimum_required(VERSION 3.10)
project(ConsumerRepo)

# Find the Qt5 package
find_package(Qt5 REQUIRED COMPONENTS Widgets)

# Find the installed library
find_package(my_library REQUIRED)

# Add the executable
add_executable(consumer src/main.cpp)

# Link the library and Qt5 to the executable
target_link_libraries(consumer PRIVATE my_library Qt5::Widgets)

# Ensure proper include directories
target_include_directories(consumer PRIVATE ${Qt5Widgets_INCLUDE_DIRS})
