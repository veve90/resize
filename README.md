# Install


## Install pip 
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install Pillow
```

## Create exe 

### pyinstaller
```
pip install pyinstaller
pyinstaller --onefile --log-level=DEBUG --name resize cli.py
```

# Run
You have to have an "input" and "output" folder near the exe. 
You just have to double click the exe


