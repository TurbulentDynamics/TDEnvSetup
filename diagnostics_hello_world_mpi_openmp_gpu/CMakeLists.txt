cmake_minimum_required(VERSION 3.12.3)
project (mpi_hello_world)


set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ".")

include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-std=c++14" COMPILER_SUPPORTS_CXX14)
set(CMAKE_CXX_STANDARD 14)

set(CMAKE_NO_SYSTEM_FROM_IMPORTED OFF)

find_package(MPI REQUIRED)
include_directories(SYSTEM ${MPI_INCLUDE_PATH})

#Must follow MPI...
find_package(OpenMP)
if (OPENMP_FOUND)
    message("Building with OpenMPI")
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
    set (CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
endif()



#set(CUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-10.0)
#find_package(CUDA 10 REQUIRED)
#include_directories(${CUDA_INCLUDE_DIRS})
#include_directories(${CUDA_LIBRARY_DIRS})
#set(CUDA_NVCC_FLAGS ${CUDA_NVCC_FLAGS} -std=c++11)


include_directories("${CMAKE_SOURCE_DIR}")



#-------------------------------


# ngxyz must = 1
add_executable(td_hello main_mpi_openmp_gpu_hello_world.cpp)
target_compile_definitions(td_hello PRIVATE -DWITH_MPI=0)

#add_executable(td_hello_gpu main_mpi_openmp_gpu_hello_world.cpp)
#target_compile_definitions(td_hello_gpu PRIVATE -DWITH_MPI=0 -DWITH_GPU=1)


add_executable(td_hello_mpi main_mpi_openmp_gpu_hello_world.cpp)
target_link_libraries(td_hello_mpi ${MPI_LIBRARIES})
target_compile_definitions(td_hello_mpi PRIVATE -DWITH_MPI=1)

add_executable(td_hello_mpi_cart main_mpi_openmp_gpu_hello_world.cpp)
target_link_libraries(td_hello_mpi_cart ${MPI_LIBRARIES})
target_compile_definitions(td_hello_mpi_cart PRIVATE -DWITH_MPI=1 -DWITH_MPI_CART=1)

#add_executable(td_hello_mpi_gpu main_mpi_openmp_gpu_hello_world.cpp)
#target_link_libraries(td_hello_mpi_gpu ${MPI_LIBRARIES})
#target_compile_definitions(td_hello_mpi_cart_gpu PRIVATE -DWITH_MPI=1 -DWITH_MPI_CART=1 -DWITH_GPU=1)


#-------------------------------
