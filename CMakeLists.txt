cmake_minimum_required(VERSION 3.22)
project(gdbviz1)

set(SOURCES viz.cpp)
set(TARGET gdbviz1)

add_executable(${TARGET} ${SOURCES})

SET_TARGET_PROPERTIES(${TARGET} PROPERTIES PREFIX "")
set_target_properties(${TARGET} PROPERTIES
    WINDOWS_EXPORT_ALL_SYMBOLS TRUE
)


set(SOURCES deque.cpp)
set(TARGET deque)

add_executable(${TARGET} ${SOURCES})

set(SOURCES mandelbrot.cpp)
set(TARGET mandelbrot)

add_executable(${TARGET} ${SOURCES})
