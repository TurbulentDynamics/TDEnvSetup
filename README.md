# Turbulent Dynamics

Turbulent Dynamics developes Maching Learning, MPI and iOS applications for both High Performance Computing (Supercomputing), edge devices (Xavier, Raspberry PI, MyriadX) and MacOS.  Minimising system admin workload is not trivial so this guide was created to try setup a common dominator for all projects.


1. [Environment setup](#Environment-setup)
2. [Simple Cluster Diagnostics](#Simple-Cluster-Diagnostics)
3. [Coding Guidelines](#Coding-Guidelines)


# Environment setup
Turbulent Dynamics developes Maching Learning, MPI and iOS applications for both High Performance Computing (Supercomputing) edge devices (Xavier, Raspberry PI, MyriadX) and MacOS.  Minimising system admin workload is not trivial, as different devices require a different stack, especially edge devices, and sometimes sudo is not available (on HPC systems).  This drives out environment and app choices.

1. Avoid sudo installs by using Brew for basic tools.
2. Avoid sudo and allow multiple versions of apps using Spack (also compiles all dependencies giving performance advantages).
3. Use containers where possible (Edge devices struggle or are unable).
4. Use Python Venv, for ML Tensorflow and tools.


| Device                         | Use Case                                                | Notes                             |
|--------------------------------|---------------------------------------------------------|-----------------------------------|
| HPC System                     | Training ML and Large Scale MPI apps 100s nodes         | Sudo not available                |
| Workstations (with AMD GPU)    | Training ML                                             |                                   |
| Workstations (with Nvidia GPU) | Training ML, rebuilding Xavier/Nano and MPI app testing | Nvidia SDK limits to Ubuntu 18.04 |
| MacOS (AMD GPU)                | Visualisations in Metal and iOS apps                    | Develop in Swift                  |
| NVIDIA Xavier/Nano             | ML Inferencing                                          | Limited to Cuda 10.0, Tensorflow 1.14         |
| MyriadX (Intel Compute Stick)  | ML Inferencing                                          | OpenVINO limits to Ubuntu 16      |
| Raspberry Pi                   | ML Inferencing                                          |                                   |



* [Install brew on both MacOS and Linux](env_setup/install_0_brew.md)
* [Install spack and some applications](env_setup/install_1_with_spack.md)
* [Install python modules](env_setup/install_2_python_modules.md)

* [Install OpenVINO on Ubuntu 16.04](env_setup/install_3_OpenVINO_on_Ubuntu_16_04.md)
* [Install Nvidia CUDA and tools on Ubuntu 18.04](env_setup/install_3_nvidia_for_Ubuntu_18_04.md)
* [Install docker, nvidia-docker2 and run TD_Base_ML container](env_setup/install_4_nvidia_docker2_base_ml_container.md)
* [Install singularity and run TD_Base_ML container](env_setup/install_5_singularity.md.md)
* [Optional Apps](env_setup/install_6_optional_apps.md)

* [(WIP) Use Spack to install Swift](env_setup/spack_swift_package.py)
* [(WIP) Install Swift on Ubuntu](env_setup/swift_for_ubuntu.md)


# Simple Cluster Diagnostics
Simple utility to check if OpenMP, MPI and cuda are working as expected.
[Diagnostics OpenMP, MPI, GPU](diagnostics_hello_world_mpi_openmp_gpu/README.md)




# Coding Guidelines

[View this on turbulentdynamics.github.io/dev_info/](https://turbulentdynamics.github.io/tdEnvSetup/)

### Some Visualisations
 * [Vector Identifiers](https://turbulentdynamics.github.io/tdEnvSetup/graphics/arrows.html) The vectors are numbered differently than usual LBM implementations
 * [Item Identifiers](https://turbulentdynamics.github.io/tdEnvSetup/graphics/cube.html) The cells in the outer shell of the lattice grid has been given an identification
 * [Visualisation 1000 cubes](https://turbulentdynamics.github.io/tdEnvSetup/graphics/1000.html)


