cmake_minimum_required(VERSION 4.0)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_VERBOSE_MAKEFILE ON) # to detect errors better
project(
	Conversation
	VERSION 0.1.0
	DESCRIPTION "A small cross-platform GUI app written in C++ that universally converts media types"
	LANGUAGES CXX
	)

include_directories("${PROJECT_SOURCE_DIR}/linking/include") # for 3rd party headers

add_executable(convo
	src/main.cpp
)

# add 3rd party dynamic libraries for the linker | located inside "${PROJECT_SOURCE_DIR}/linking/lib"
target_link_libraries(convo

)
