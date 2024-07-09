from PIL import Image, ImageEnhance, ImageFilter
import os
path = './imgs'
pathOut = '/editedImgs'


def upgrade_contrast(path, pathOut):
    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")
        edit = img.filter(ImageFilter.SHARPEN) 
        clean_name = os.path.splitext(filename)[0]
        edit.save(f'.{pathOut}/{clean_name}_sharpened.jpg')

def input_factor():
    while True:
        value =  input("Entor the factor for the enhancer.")
        if value.isnumeric():
            print(value)
            print("integer")
            value = int(value)
            break

    return value


def enhance_photo(path, pathOut):
    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")
        edit = img.filter(ImageFilter.SHARPEN)
        enhancer = ImageEnhance.Contrast(edit)
        factor = input_factor()
        edit = enhancer.enhance(factor)
        clean_name = os.path.splitext(filename)[0]
        edit.save(f'.{pathOut}/{clean_name}_enhanced.jpg')


if __name__ == "__main__":
    upgrade_contrast(path, pathOut)
    enhance_photo(path, pathOut)