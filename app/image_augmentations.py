from PIL import Image
import random


def random_augmentation(image: Image):
    augmentations = {"rotated": rotate, "flipped": fliplr, "plain": do_nothing, "cropped": crop}
    augmentation, func = random.choice(list(augmentations.items()))
    return func(image), augmentation


def do_nothing(image: Image):
    return image


def fliplr(image: Image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)


def rotate(image: Image):
    return image.rotate(random.randint(0, 365))


def crop(image: Image, pixels=50):
    """
    Crops the top and bottom of an image.
    """
    w, h = image.size
    return image.crop((0, pixels, w, h - pixels))

