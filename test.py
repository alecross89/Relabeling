import os
print(os.getcwd())

src = './images/'
image_names = []
# need to have an array for image path, to use for the Image.open
images = []
for folder in os.listdir(src):
    if folder[0] != '.':
        image_names.append(folder)
        images.append(os.listdir(src+folder))
        
print(image_names)
print(images[0][0])
# print(os.listdir('./images/'))