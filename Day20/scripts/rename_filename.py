# This script is run in order to convert the filenames into proper order under each directory/folder of traffic_light_images directory.

import os
from pathlib import Path

os.chdir(os.path.dirname(os.getcwd()))
img_dir = os.chdir(os.getcwd() + '\\traffic_light_images')
green_dir = os.listdir(os.getcwd() + '\\green')
red_dir = os.listdir(os.getcwd() + '\\red')
yellow_dir = os.listdir(os.getcwd() + '\\yellow')

# rename green imgs
def rename_green_imgs():
    i = 0
    try:
        for img in green_dir:
            data_file = Path(os.getcwd() + '\\green\\' + str(img))
            data_file.rename(os.getcwd() + '\\green\\green_' + str(i) + '.jpg')
            i = i + 1
    except:
        pass


# rename red imgs
def rename_red_imgs():
    i = 0
    try:
        for img in red_dir:
            data_file = Path(os.getcwd() + '\\red\\' + str(img))
            data_file.rename(os.getcwd() + '\\red\\red_' + str(i) + '.jpg')
            i = i + 1
    except:
        pass

# rename yellow images
def rename_yellow_imgs():
    i = 0
    try:
        for img in yellow_dir:
            data_file = Path(os.getcwd() + '\\yellow\\' + str(img))
            data_file.rename(os.getcwd() + '\\yellow\\yellow_' + str(i) + '.jpg')
            i = i + 1
    except:
        pass



if __name__ == '__main__':
    rename_green_imgs()
    rename_red_imgs()
    rename_yellow_imgs()
    print(os.getcwd())