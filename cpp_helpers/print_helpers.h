#ifndef COMMON_PRINT_HELPERS_H
#define COMMON_PRINT_HELPERS_H

#include <iostream>
#include <type_traits>

// General template for printing containers
template<typename T>
void print(const T& container, typename T::const_iterator* = nullptr) {
    std::cout << "{ ";
    for (const auto& element : container) {
        std::cout << element << " ";
    }
    std::cout << "}" << std::endl;
}

// Specialization for printing maps
template<typename K, typename V>
void print(const std::map<K, V>& m) {
    std::cout << "{ ";
    for (const auto& pair : m) {
        std::cout << pair.first << ": " << pair.second << ", ";
    }
    std::cout << "}" << std::endl;
}

template<typename K, typename V>
void print(const std::unordered_map<K, V>& um) {
    std::cout << "{ ";
    for (const auto& pair : um) {
        std::cout << pair.first << ": " << pair.second << ", ";
    }
    std::cout << "}" << std::endl;
}

// Specialization for printing pairs
template<typename T1, typename T2>
void print(const std::pair<T1, T2>& p) {
    std::cout << "{(" << p.first << ", " << p.second << ")}" << std::endl;
}

// Specialization for printing strings
void print(const std::string& str) {
    std::cout << "\"" << str << "\"" << std::endl;
}

// Specialization for printing arrays
template<typename T, size_t N>
void print(const T (&arr)[N]) {
    std::cout << "{ ";
    for (const auto& element : arr) {
        std::cout << element << " ";
    }
    std::cout << "}" << std::endl;
}

// Fallback for single elements
template<typename T>
typename std::enable_if<!std::is_container<T>::value>::type print(const T& element) {
    std::cout << element << std::endl;
}

#endif // COMMON_PRINT_HELPERS_H
