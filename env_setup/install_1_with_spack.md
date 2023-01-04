# Installing applications with spack
#### [spack](https://spack.readthedocs.io/en/latest/) allows multiple versions of each app, and uses [environment modules](http://modules.sourceforge.net) to "load" them.  It is very usefull for hpc environments, and can be used to install apps into home directory on 'clusters.'



## Installing spack
```
cd ~
git clone -c feature.manyFiles=true https://github.com/spack/spack.git ~/spack --single-branch --branch releases/latest

. ~/spack/share/spack/setup-env.fish

#spack bootstrap
```

## Installing applications with spack
```
#Cuda 11.8 works with gcc 11
#https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#title-new-cuda-tools
#spack install gcc@11.3.0
spack compiler find

set CC %gcc@11.3.0

spack install cmake@3.21.4{$CC}
spack install openmpi@4.1.1{$CC} mpich@4.0.2{$CC}
spack install rust@1.60.0{$CC}

#Older optional versions
#spack install openmpi@3.1.0{$CC} openmpi@2.1.6{$CC} mpich@3.4.3{$CC}
#spack install gcc@10.4.0{$CC} gcc@9.4.0{$CC} gcc@8.5.0{$CC} gcc@7.5.0{$CC}
#spack install llvm@15.0.3{$CC}

#spack install octave@4.2.1

#Interesting HPC tools
spack install likwid numactl hpctoolkit 

#Download pgi from pgroup.com and from the download directory
#spack install pgi

#To update all available compilers
#spack compiler find
```






