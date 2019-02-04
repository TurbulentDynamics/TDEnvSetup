# To Install cuda-10.0 and Jetpack-3.3 on Ubuntu 16.04

```sudo apt-get install linux-headers-$(uname -r)```

Check https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=debnetwork

```
sudo dpkg -i cuda-repo-ubuntu1604_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda

export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH
export PATH=/usr/local/cuda-10.0/bin:$PATH
```

## The NVIDIA Persistence Daemon can be started as the root user by running:
```/usr/bin/nvidia-persistenced --verbose``` 
 
 
## Install Writable Samples
```cuda-install-samples-10.0.sh ~/nvidia-samples-10.0```
 
 
## Install some usefull tools
```sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev```
 
 
# Machine Learning Tools
Machine Learning work should be done in a container. To install ["nvidia-docker2"](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)#prerequisites)

```
#For Ubuntu 16.04
sudo apt-get install nvidia-docker2
sudo pkill -SIGHUP dockerd
#Test
docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
```
 
