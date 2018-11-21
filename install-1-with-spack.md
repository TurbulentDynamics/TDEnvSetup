#Installing applications with spack
####[spack](https://spack.readthedocs.io/en/latest/) allows multiple versions of each app, and uses [environment modules](http://modules.sourceforge.net) to "load" them.  It is very usefull for hpc environments, adn can be used to install apps into home directory on 'clusters.'





## Installing spack
cd ~
git clone https://github.com/spack/spack.git

echo "export SPACK_ROOT=~/spack">>~/.bashrc
echo "export PATH=$SPACK_ROOT/bin:$PATH">>~/.bashrc
echo ". $SPACK_ROOT/share/spack/setup-env.sh">>~/.bashrc
spack bootstrap




## Installing applications with spack
spack install gcc@8.2.0 
module load gcc@8.2.0
spack compiler find

spack install cmake@3.12.3%gcc@8.2.0 openmpi@3.1.2%gcc@8.2.0 openmpi@2.1.5%gcc@8.2.0 


spack install octave@4.2.1


#For Linux
spack install python@3.7.0%gcc@8.2.0 

#For MacOS [python issue on mac](https://github.com/spack/spack/issues/2230)
spack install python@3.7.0%clang@10.0.0-apple






