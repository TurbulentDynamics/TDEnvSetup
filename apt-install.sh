

apt install -y vim git curl 







cd ~
git clone https://github.com/spack/spack.git

echo "export SPACK_ROOT=~/spack">>~/.bashrc
echo "export PATH=$SPACK_ROOT/bin:$PATH">>~/.bashrc
echo ". $SPACK_ROOT/share/spack/setup-env.sh">>~/.bashrc
spack bootstrap
