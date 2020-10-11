# Install

## Install pip 
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install Pillow
```

# Create exe 

## py2exe does not work with python 3.7.7
```
pip install py2exe
python setup.py install
python setup.py py2exe
```
# pyinstaller
```
pip install pyinstaller
pyinstaller cli.py --name resize
```
