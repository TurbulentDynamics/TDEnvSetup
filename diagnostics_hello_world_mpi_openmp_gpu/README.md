# Turbulent Dynamics Cluster Hello World

See (https://github.com/TurbulentDynamics/TD_env_setup_dev_info)[https://github.com/TurbulentDynamics/TD_env_setup_dev_info] for help to install and setup.

# Get Started
```
cmake .
make

#Some MPI implementations need slots defined
echo localhost slots=64 >> hostfile

./hello
mpirun -np 8  --hostfile hostfile ./td_hello_mpi
mpirun -np 8  --hostfile hostfile ./td_hello_mpi_cart
```