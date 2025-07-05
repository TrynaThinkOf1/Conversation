cmake_minimum_required(VERSION 4.0)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_VERBOSE_MAKEFILE ON) # to detect errors better
set(CMAKE_BUILD_TYPE Release)
project(
	Conversation
	VERSION 0.1.0
	DESCRIPTION "A small cross-platform GUI app written in C++ that universally converts media types"
	LANGUAGES CXX
	)

find_package(
	FreeImage REQUIRED
)
 

add_executable(convo
	src/main.cpp
)

target_link_libraries(convo
	PRIVATE
	 freeimage::FreeImage
)
