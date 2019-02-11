# Install Docker and Nvidia 
Machine Learning work should be done in a container. To install ["nvidia-docker2"](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)#prerequisites)


## Install docker
```
#For Ubuntu 16.04
#https://docs.docker.com/install/linux/docker-ce/ubuntu/
apt-get install apt-transport-https ca-certificates gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

#sudo groupadd docker
sudo usermod -aG docker $USER

#Enable docker to run at startup
sudo systemctl enable docker

#Verify that Docker CE is installed correctly by running the hello-world image.
docker run hello-world
```


## Install nvidia-docker2
```
#https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)
sudo apt-get install nvidia-docker2
sudo pkill -SIGHUP dockerd

#Test
docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
```
 
 
 
