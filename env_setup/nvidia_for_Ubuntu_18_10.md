# To Install cuda-10.1 and Jetpack-4.2 on Ubuntu 18.10

```sudo apt-get install linux-headers-$(uname -r)```

Check https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1810&target_type=debnetwork

```
sudo dpkg -i cuda-repo-ubuntu1810_10.1.105-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1810/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda

export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH
export PATH=/usr/local/cuda-10.0/bin:$PATH
```


## The NVIDIA Persistence Daemon can be started as the root user by running:
```/usr/bin/nvidia-persistenced --verbose``` 
 
 
## Install Writable Samples
```cuda-install-samples-10.1.sh ~/nvidia-samples-10.1```
 
 
## Install some useful tools
```sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev```
 
 
 ## Install Jetpack SDK
Download https://developer.nvidia.com/embedded/dlc/nv-sdk-manager
```
sudo apt install ~/Downloads/sdkmanager-[version].[build#].deb 

#runwith sdkmanager
```
 
