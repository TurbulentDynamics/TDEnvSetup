# Install Python Packages

```
pip install --upgrade pip

pip install --trusted-host pep8 coverage nose pylint sphinx sphinx_rtd_theme recommonmark tqdm --user
pip install pandas numpy scipy matplotlib dask --user
pip install jupyterlab --user

#Make your python life easier: https://github.com/prompt-toolkit/ptpython
#pip install --trusted-host ptpython ptpython --user
```

## for specific projects use virtualenv
```

python3 -m venv dirToNewVenv #current python exec linked by default
source dirToNewVenv/bin/activate.fish
pip install --upgrade pip
pip install matplitlib==3.6.2
#or use requirements.txt
pip install -r requirements.txt

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
