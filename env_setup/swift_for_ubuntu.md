# To install swift on Ubuntu 16
Need to create a spack spec file for this

```sudo apt-get install libicu-dev unzip```

[Goto swift download page and copy link](https://swift.org/download/)
```
cd ~
wget https://swift.org/builds/swift-4.2.1-release/ubuntu1604/swift-4.2.1-RELEASE/swift-4.2.1-RELEASE-ubuntu16.04.tar.gz
tar zxf swift-*.tar.gz --directory ~/swift-4.2
echo "export PATH=~/swift-4.2/usr/bin:\"\${PATH}\"" >> ~/.bashrc
source ~/.bashrc
```





