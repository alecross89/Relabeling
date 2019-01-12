# Relabeling

### Setup
It is probably best to create a venv with `python3` (I used python 3.6).  If you're using `conda` then create a venv:
``` 
$ conda create -n my_venv_name python=3.6
```
Then clone the repo:
```
git clone https://github.com/alecross89/Relabeling.git
```

Next, switch into the `Relabeling` folder, and install the requirements:
```
pip install -r requirements.txt 
```
Then load the images you would like to label in this directory.  The file structure should be like this:
```
    ├── Relabeling                    
    │   ├── relabel.py       
    │   ├── requirements.txt      
    │   └── image_folder_name
            ├── image id folder (ex. d2c7e807-0d75-48ce-980e-36666939f131)         
            │   ├── rgb.png        
            ├── ...
```
As of right now you need to go into `relabel.py` and change `src='./test_folder/'` to `src='./image_folder_name/'`.  Once you start
classifying images, they will be put into empty or not_empty folders (that will be created when the program starts).  

To mark image as **Empty** - **Left Arrow**

To mark image as **Not Empty** - **Right Arrow**

To run the program: 
```
python relabel.py
```
 
