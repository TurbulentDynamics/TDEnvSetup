# To install swift on Ubuntu 18
Need to create a spack spec file for this

```sudo apt-get install -y clang libicu-dev```

[Goto swift download page and copy link](https://swift.org/download/)
```
cd ~
wget https://swift.org/builds/swift-5.0-release/ubuntu1804/swift-5.0-RELEASE/swift-5.0-RELEASE-ubuntu18.04.tar.gz
tar zxf swift-*.tar.gz --directory ~
echo "export PATH=~/swift-5.0-RELEASE-ubuntu18.04/usr/bin:\"\${PATH}\"" >> ~/.zshrc
source ~/.zshrc
```





