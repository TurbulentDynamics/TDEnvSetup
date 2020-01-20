# Install Python Packages

```
#Ensure default python is python3
#update-alternatives --install /usr/bin/python python /usr/bin/python3 10

module purge
echo "spack load python@3.8.1">>~/.zshrc
source ~/.zshrc
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip3 install --upgrade pip

pip3 install --trusted-host pep8 coverage nose pylint sphinx sphinx_rtd_theme recommonmark tqdm --user
pip3 install pandas numpy scipy matplotlib dask --user
pip3 install jupyterlab --user

#Make your python life easier: https://github.com/prompt-toolkit/ptpython
pip3 install --trusted-host ptpython ptpython --user
```

## for specific projects use virtualenv
```
#On MacOS
spack load python@3.7.4%clang

#On linux
spack load python@3.8.0

python -m venv dirToNewVenv #current python exec linked by default
source dirToNewVenv/bin/activate
pip3 install --upgrade pip
pip3 install matplitlib==3.1.1
#or use requirements.txt
pip3 install -r requirements.txt

#To deactivate when needed
deactivate
```



## Conda testing (WIP)
```
brew cask install miniconda
conda config --set auto_activate_base false
conda deactivate 
conda env create -f tdCondaBase.yaml
```

#### Usage Examples
```
conda activate tdCondaBase
conda deactivate

# list all the conda environment available
conda info --envs  

# Remove environment and its dependencies
conda remove --name envname --all

# Clone an existing environment
conda create --name clone_envname --clone envname
```
