#!/bin/sh -l
## Requests 2 Nodes, and starts 4 mpi processes per node
#SBATCH -N 2
#SBATCH --ntasks-per-node=4
#SBATCH -t 01:00:00
#SBATCH -A <account>
#SBATCH -p ProdQ
#SBATCH -o hello-world-n8.out
#SBATCH --mail-user=<email_address>

export LC_ALL=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8

export WORKSPACE=$SLURM_SUBMIT_DIR
echo $WORKSPACE
cd $WORKSPACE


module load intel/2018u
export CC=icc
export CXX=icpc


mpirun -n 4 -ppn 4 ./td_hello_mpi_cart
