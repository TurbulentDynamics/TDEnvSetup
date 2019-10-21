# Install Python Packages

```
module purge
echo "spack load python-3.8.0">>~/.zshrc
source ~/.zshrc
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip3 install --upgrade pip

pip3 install --trusted-host pep8 coverage nose pylint sphinx sphinx_rtd_theme recommonmark tqdm
pip3 install pandas numpy scipy matplotlib dask
pip3 install jupyterlab

#Make your python life easier: https://github.com/prompt-toolkit/ptpython
pip3 install --trusted-host ptpython
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
