cmake_minimum_required(VERSION 3.11)
project(PackageTest CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_MODULE_PATH ${CMAKE_BINARY_PATH})

if(APPLE)
   set(basePoint @loader_path)
else()
    set(basePoint $ORIGIN)
endif()

include(GNUInstallDirs)
file(RELATIVE_PATH relDir
     ${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_INSTALL_BINDIR}
     ${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR})

set(CMAKE_INSTALL_RPATH ${basePoint} ${basePoint}/${relDir})

find_package(pmp REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example pmp::pmp)

install(TARGETS example
        DESTINATION ${CMAKE_INSTALL_BINDIRs})
