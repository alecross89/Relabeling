import os
print(os.getcwd())

src = './images/'
image_names = []
# need to have an array for image path, to use for the Image.open
images = []
image_folder = []
counter=0
for folder in os.listdir(src):
    if folder[0] != '.':
        image_folder.append(src+folder)
        image_names.append(folder)
        images.append(os.listdir(src+folder))
        
print(image_names)
print(images[0][0])
print(image_folder)
# print(os.listdir('./images/'))