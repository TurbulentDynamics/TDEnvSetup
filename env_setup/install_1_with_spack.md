# Installing applications with spack
#### [spack](https://spack.readthedocs.io/en/latest/) allows multiple versions of each app, and uses [environment modules](http://modules.sourceforge.net) to "load" them.  It is very usefull for hpc environments, and can be used to install apps into home directory on 'clusters.'



## Installing spack
```
cd ~
git clone https://github.com/spack/spack.git --single-branch

echo 'export SPACK_ROOT=~/spack'>>~/.zshrc
echo 'export PATH=$SPACK_ROOT/bin:$PATH'>>~/.zshrc
echo '. $SPACK_ROOT/share/spack/setup-env.sh'>>~/.zshrc
. ~/.zshrc
#spack bootstrap
```

## Installing applications with spack
```
#Cuda 11.5 works with gcc 10
#https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#title-new-cuda-tools
spack install gcc@10.3.0 
spack compiler find

CC=%gcc@10.3.0

spack install cmake@3.21.4${CC}
spack install openmpi@4.1.1${CC} openmpi@3.1.6${CC} openmpi@2.1.6${CC} mpich@3.4.2${CC}
spack install gcc@9.4.0${CC} gcc@8.5.0${CC} gcc@7.5.0${CC} gcc@6.5.0${CC} gcc@5.5.0${CC} 
spack insall rust@1.51.0${CC}
spack install llvm@13.0.0${CC}

#spack install octave@4.2.1

#Interesting HPC tools
spack install likwid

#Download pgi from pgroup.com and from the download directory
#spack install pgi

#To update all available compilers
#spack compiler find
```






