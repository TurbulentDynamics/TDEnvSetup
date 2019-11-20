# Turbulent Dynamics Environment setup
Turbulent Dynamics developes Maching Learning and MPI applications for both High Performance Computing (Supercomputing) and edge devices (Xavier, Raspberry PI, MyriadX) and MacOS.  Minimising system admin workload is not easy, as lots of the devices require a different stack, especially edge devices, and sometimes sudo is not available (on HPC systems).  Therefore our hierarchy of goals are:

1. Avoid sudo installs (sudo not available on HPC systems)
2. Use containers where possible (Edge devices usually struggle/cant)
3. Use Python Venv, for ML Tensorflow and tools

| Device                         | Use Case                                    |            OS            |         Container |
|--------------------------------|---------------------------------------------|:------------------------:|------------------:|
| HPC System                     | Training ML Large Scale MPI apps 100s nodes |           Linux          | Maybe Singularity |
| Workstations (with AMD GPU)    | Training ML                                 | Ubuntu 18.04 (Cuda 10.0) |   Nvidia-docker 2 |
| Workstations (with Nvidia GPU) | Training ML MPI app testing                 | Ubuntu 18.04 (Cuda 10.0) | Nvidia-docker 2   |
| MacOS (AMD GPU)                | Visualisations in Metal iOS apps            |                          | Docker            |
| NVIDIA Xavier/Nano             | ML Inferencing                              |                          | Not Available     |
| MyriadX (Intel Compute Stick)  | ML Inferencing                              | Ubuntu 16.04 + OpenVINO  | Not Available     |
| Raspberry Pi                   | ML Inferencing                              |                          | Not Available     |
|                                |                                             |                          |                   |


* [Install brew on both MacOS and Linux](env_setup/install_0_brew.md)
* [Install spack and some applications](env_setup/install_1_with_spack.md)
* [Install python modules](env_setup/install_2_python_modules.md)

* [Install Nvidia CUDA and tools on Ubuntu 16.04](env_setup/install_3_nvidia_for_Ubuntu_16_04.md)
* [Install Nvidia CUDA and tools on Ubuntu 18.04](env_setup/install_3_nvidia_for_Ubuntu_18_04.md)
* [Install docker, nvidia-docker2 and run TD_Base_ML container](env_setup/install_4_nvidia_docker2_base_ml_container.md)
* [Install singularity and run TD_Base_ML container](env_setup/install_5_singularity.md.md)
* [Optional Apps](env_setup/install_6_optional_apps.md)

* [(WIP) Use Spack to install Swift](env_setup/spack_swift_package.py)
* [(WIP) Install Swift on Ubuntu](env_setup/swift_for_ubuntu.md)




# Turbulent Dynamics Coding Guidelines

[View this on turbulentdynamics.github.io/dev_info/](https://turbulentdynamics.github.io/tdEnvSetup/)

### Some Visualisations
 * [Vector Identifiers](https://turbulentdynamics.github.io/tdEnvSetup/graphics/arrows.html) The vectors are numbered differently than usual LBM implementations
 * [Item Identifiers](https://turbulentdynamics.github.io/tdEnvSetup/graphics/cube.html) The cells in the outer shell of the lattice grid has been given an identification
 * [Visualisation 1000 cubes](https://turbulentdynamics.github.io/tdEnvSetup/graphics/1000.html)


