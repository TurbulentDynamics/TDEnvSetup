# Install Docker and Nvidia 
Machine Learning work should be done in a container. To install ["nvidia-containertoolkit"](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)

## Install docker
```
#For Ubuntu 22.04
#https://docs.docker.com/install/linux/docker-ce/ubuntu/
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo docker run hello-world

#sudo groupadd docker
sudo usermod -aG docker $USER
#log out (or sometimes even restart) needed to continue normally

#Enable docker to run at startup
sudo systemctl enable docker

#Verify that Docker CE is installed correctly by running the hello-world image.
docker run hello-world
```


## Install nvidia-docker2
```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo systemctl restart docker

```
 
## Working with Container
```
# Build container, this command will build container locally (note the ".")
 # The container will build tensorflow with native CPU flags to get all instructions working natively on the build machine.
 # NOTE: these containers occupy a lot of space, 10's of GBs (or even 100 GB), so ensure there is sufficient free space

nvidia-docker build -f Dockerfile.td_base -t td_base .
nvidia-docker build -f Dockerfile.td_base_nvidia_ml -t td_base_nvidia_ml .

#To run the new interactive container
 #Use --privileged if access needed to OTHER devices like USB drives.

 # NOTE: -v flag and the text that follows allows the user to mount the specified directory so it can be easily used by the docker container
nvidia-docker run --runtime=nvidia -it --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 -v /opt/path/to/fast/storage:/ml_data td_base_nvidia_ml


#Inside the container, run a few simple tests

import torch
torch.cuda.is_available()


#======
# This container is also built on dockerhub, but it may not have the same CPU instruction flags as the host machine.
# Pull container, this command will download pre built container from dockerhub.com 
nvidia-docker pull turbulentdynamics/td_base_ml #TODO: change this to td_base_nvidia_ml if that will be built and used, if not remove this part
nvidia-docker image ls

``` 
 
