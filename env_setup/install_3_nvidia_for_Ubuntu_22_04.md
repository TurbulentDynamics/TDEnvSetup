# To Install cuda-12 Ubuntu 22.04

```
sudo apt-get install linux-headers-(uname -r)

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get -y install nvidia-driver nvidia-dkms
sudo apt-get -y install cuda

set -Ux LD_LIBRARY_PATH /usr/local/cuda/lib64
echo set -Ux LD_LIBRARY_PATH /usr/local/cuda/lib64>>~/.config/fish/config.fish
fish_add_path /usr/local/cuda-12.0/bin
echo fish_add_path /usr/local/cuda-12.0/bin>>~/.config/fish/config.fish
```


## The NVIDIA Persistence Daemon can be started as the root user by running:
```/usr/bin/nvidia-persistenced --verbose``` 
 
 
## Install Writable Samples
```cuda-install-samples-12.0.sh ~/nvidia-samples-12.0```
 
 
## Install some useful tools
```sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev```
 
 
 ## Install (Jetpack) SDK Manager
Download https://developer.nvidia.com/embedded/dlc/nv-sdk-manager
```
sudo apt install ./sdkmanager-[version].[build#].deb 

#runwith sdkmanager
```
 
