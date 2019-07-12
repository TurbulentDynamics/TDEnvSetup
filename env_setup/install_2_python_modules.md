# Install Python Packages

```
module purge 
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip3 install --upgrade pip

pip3 install --trusted-host pep8 coverage nose pylint sphinx sphinx_rtd_theme recommonmark
pip3 install pandas numpy scipy matplotlib dask
pip3 install jupyterlab
```

## for specific projects use virtualenv
```
#On MacOS
spack load python@3.7.4%clang

#On linux
module load python-3.7.4


python -m venv dirToNewVenv
source dirToNewVenv/bin/activate
pip3 install --upgrade pip
pip3 install matplitlib==3.1.1
#or use requirements.txt
pip3 install -r requirements.txt

#deactivate when needed
```
