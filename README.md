# Relabeling

### Setup
It is probably best to create a venv with `python3` (I used `python 3.6`).  If you're using `conda` then create a venv:
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

### Running
To run the program, you must include the path to the image folder w.r.t `relabel.py`, for example: 
```
$ python relabel.py './image_folder_name/'
```
Once you start classifying images, they will be put into empty or not_empty folders (those folders will be created when the program starts if they don't already exist).  

To mark image as **Empty** - **Left Arrow**

To mark image as **Not Empty** - **Right Arrow**
 
