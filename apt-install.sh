

apt install vim git 







cd ~
git clone https://github.com/spack/spack.git


echo "export SPACK_ROOT=~/spack">>~/.bashrc
echo "export PATH=$SPACK_ROOT/bin:$PATH">>~/.bashrc

