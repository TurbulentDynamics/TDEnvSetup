# To Install cuda-10.0 and Jetpack-4.2 on Ubuntu 18.04
# (Nvidia SDK and Xavier use cuda 10.0)

```
sudo apt-get install linux-headers-$(uname -r)
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda

export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH
export PATH=/usr/local/cuda-10.0/bin:$PATH
```


## The NVIDIA Persistence Daemon can be started as the root user by running:
```/usr/bin/nvidia-persistenced --verbose``` 
 
 
## Install Writable Samples
```cuda-install-samples-10.0.sh ~/nvidia-samples-10.0```
 
 
## Install some useful tools
```sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev```
 
 
 ## Install Jetpack SDK
Download https://developer.nvidia.com/embedded/dlc/nv-sdk-manager
```
sudo apt install ~/Downloads/sdkmanager-[version].[build#].deb 

#runwith sdkmanager
```
 
