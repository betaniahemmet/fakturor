from PIL import Image
from config import images_path
import os


def affirm_image_size():
    """Make sure that images are the right size"""
    image_paths = [f"{images_path}\\{i}" for i in os.listdir(images_path)]
    resize_count = 0
    for image_path in image_paths:
        image = Image.open(image_path)
        if image.size[0] > 200 or image.size[1] > 100:
            resize_count += 1
            image.thumbnail((200, 100))
            image.save(image_path)

    print(f"resized {resize_count} images")


def affirm_image_type():
    """Make sure that images are PNG"""
    image_paths = [f"{images_path}\\{i}" for i in os.listdir(images_path)]
    type_change_count = 0
    for image_path in image_paths:
        image = Image.open(image_path)
        if image.format != "PNG":
            type_change_count += 1
            split_path = image_path.split(".")
            image.save(f"{split_path[0]}.png")
            os.remove(image_path)

    print(f"Turned {type_change_count} images into PNG:s")
