# C++ Project: Library and Consumer

This project consists of two repositories: 
- `library_repo`: A simple C++ library.
- `consumer_repo`: A C++ executable that uses the library.

## Directory Structure

```
/parent_directory
   ├── library_repo
   │    ├── CMakeLists.txt
   │    └── src
   │         └── library.cpp
   └── consumer_repo
        ├── CMakeLists.txt
        └── src
             └── main.cpp
```

## How to Use

### Prerequisites

- CMake 3.10+
- A C++ compiler (e.g., GCC, Clang)

### Steps to Build and Run

1. Clone or extract the project.
   ```bash
   tar -xvf project.tar.gz
   ```

2. Navigate to the `consumer_repo` directory.
   ```bash
   cd parent_directory/consumer_repo
   ```

3. Create a `build` directory and navigate into it.
   ```bash
   mkdir build && cd build
   ```

4. Run CMake to configure the project.
   ```bash
   cmake ..
   ```

5. Build the project.
   ```bash
   make
   ```

6. Run the resulting executable.
   ```bash
   ./consumer
   ```

This will build the `library_repo` as a static library and link it to the `consumer_repo` executable.
