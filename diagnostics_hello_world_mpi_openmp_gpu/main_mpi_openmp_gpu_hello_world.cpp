//
//  MPI OpenMP GPU Hello World
//  
//
//  Created by Niall P. O'Byrnes on 19/04/19.
//  Copyright © 2019 Niall P. O'Byrnes. All rights reserved.
//

#include <stdlib.h>
#include <iostream>

#if WITH_MPI == 1
#include <mpi.h>
#endif

#ifdef _OPENMP
#include <omp.h>
#endif


#if WITH_GPU == 1
#include <cuda.h>
#include <cuda_runtime.h>
#include "helper_cuda.h"
#include "helper_string.h"
#endif



int main(int argc, char* argv[]){

    int ngx = 2;
    int ngy = 2;
    int ngz = 2;
        
    //Setup MPI and OpenMP
    int numprocs = 1;
    int rank = 0;
    int nthreads_set = 1;
    int nthreads_avail = 1;
    int nthreads_requested = 2;


#ifdef _OPENMP
    nthreads_avail = omp_get_max_threads();
    omp_set_num_threads(nthreads_requested);
#endif

    
    
#if WITH_MPI == 1
    
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    
    
    MPI_Group comm_group;
    MPI_Comm_group(MPI_COMM_WORLD, &comm_group);
    

    MPI_Comm comm_cart;
    
    //MPI_Errhandler comm_errhandler;
    //MPI_Comm_create_errhandler((MPI_Comm_errhandler_function *)&my_comm_errhandler_test, &comm_errhandler);
    //MPI_Comm_set_errhandler(MPI_COMM_WORLD, comm_errhandler);
    
    printf("SETUP   rank/procs   %2i/%2i   ngxyz %i %i %i\n", rank, numprocs, ngx, ngy, ngz);
    
// #else
//     //Create Dummies
//     MPI_Comm comm_cart;
//     MPI_Group comm_group;
#endif
    
    
    int mpi_coords[3] = {0, 0, 0};
#if WITH_MPI_CART == 1

    int comm_ndims = 3;
    int dim_sizes[3] = {ngx, ngy, ngz};
    int wrap_around[3] = {0, 0, 0};
    
    //Allows the MPI topology to rearrange the ranks
    int reorder = 0;
    
    MPI_Dims_create(numprocs, 3, dim_sizes);
    MPI_Cart_create(MPI_COMM_WORLD, comm_ndims, dim_sizes, wrap_around, reorder, &comm_cart);
    MPI_Comm_group(comm_cart, &comm_group);

    MPI_Cart_coords(comm_cart, rank, 3, mpi_coords);

#endif




#pragma omp parallel for
    for (int t = 0; t < nthreads_requested; t++) {
        int tid = omp_get_thread_num();
        std::cout << "Hello Im Node " << rank << " with Coords " <<
        mpi_coords[0] << " " <<
        mpi_coords[1] << " " <<
        mpi_coords[2] << ".  This is thread " <<
        tid << " of (req:" << nthreads_requested << 
        "/machine:" << nthreads_avail << ")" << std::endl;

        //I have X GPU, (list gpus)
    }






#if WITH_MPI == 1
    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Group_free(&comm_group);
    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Finalize();
#endif

    std::cout << "Im finished now " << rank << std::endl;

    return 0;

}//end of main
