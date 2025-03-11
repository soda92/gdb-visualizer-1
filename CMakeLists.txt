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

set(SOURCES windows-error.c)
set(TARGET windows-error)

add_executable(${TARGET} ${SOURCES})

set(SOURCES sync-thread.c)
set(TARGET sync-thread)

add_executable(${TARGET} ${SOURCES})

set(SOURCES event.c)
set(TARGET event)

add_executable(${TARGET} ${SOURCES})

set(SOURCES mutex.c)
set(TARGET mutex)

add_executable(${TARGET} ${SOURCES})

set(SOURCES dictionary.c)
set(TARGET dictionary)

add_executable(${TARGET} ${SOURCES})
