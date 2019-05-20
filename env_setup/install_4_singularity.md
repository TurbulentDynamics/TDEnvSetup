# Singularity



## Install


###  Ubuntu
```
VERSION=2.5.2
wget https://github.com/singularityware/singularity/releases/download/$VERSION/singularity-$VERSION.tar.gz
tar xvf singularity-$VERSION.tar.gz
cd singularity-$VERSION
./configure --prefix=/usr/local
make
sudo make install
```

### macOS
```brew cask install virtualbox
brew cask install vagrant
brew cask install vagrant-manager
mkdir singularity-vm
cd singularity-vm
vagrant init singularityware/singularity-2.5
vagrant up
vagrant ssh
```

```
sudo singularity build td_base_ml.simg Singularity.td_base_ml
```


```
sudo singularity build --sandbox td_base_ml.sandbox Singularity.td_base_ml
sudo singularity shell --nv td_base_ml.sandbox/
```



