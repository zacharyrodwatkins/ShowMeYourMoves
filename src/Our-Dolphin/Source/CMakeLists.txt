cmake_minimum_required(VERSION 3.5.0)
project(Our-Dolphin)

if(WIN32)
    set(DolphinProcessSrc DolphinProcess/Windows/WindowsDolphinProcess.cpp)
endif(WIN32)

if(UNIX)
   set(DolphinProcessSrc DolphinProcess/Linux/LinuxDolphinProcess.cpp)
endif(UNIX)

#set(PYDIR /usr/include/python3.6)
include(ExternalProject)

list(APPEND CMAKE_MODULE_PATH  "${CMAKE_SOURCE_DIR}/cmake/Modules/")
find_package(PythonInterp REQUIRED)
find_package(PythonLibs REQUIRED)
#include(BuildBoost) # Custom module





include_directories(${Boost_INCLUDE_DIR} ${PYTHON_INCLUDE_DIRS})
link_directories(${Boost_LIBRARY_DIR})


find_package(PythonLibs ${PY_VERSION} REQUIRED)
find_package(Boost 1.65.1 REQUIRED COMPONENTS system python)



set(SRCS ${DolphinProcessSrc}
         DolphinProcess/DolphinAccessor.cpp  
         Common/MemoryCommon.cpp
         MemoryWatch/MemWatchEntry.cpp   
         MemoryScanner/MemoryScanner.cpp
         Dolphin-Watcher/DolphinWatcher.cpp
         DolphinProcess/Linux/LinuxDolphinProcess.cpp
         DolphinProcess/IDolphinProcess.h
         )

set(CMAKE_INCLUE_CURRENT_DIR ON)


set(CMAKE_AUTOMOC ON)

add_executable(Dolphin-Watch main.cpp ${SRCS})

#add_library(DolphinMemoryEngine SHARED ${SRCS})

add_library(DolphinMemoryEngine SHARED bindings.cpp ${SRCS})
target_link_libraries(DolphinMemoryEngine ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
add_dependencies(DolphinMemoryEngine Boost)

set_target_properties(DolphinMemoryEngine PROPERTIES SUFFIX .so)
set_target_properties(DolphinMemoryEngine PROPERTIES PREFIX "")