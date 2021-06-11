from app import DEFAULT_PATH
from image_augmentations import crop
from PIL import Image


def test_crop():
    original = Image.open(DEFAULT_PATH)
    original_width, original_height = original.size

    pixels = 50
    cropped_width, cropped_height = crop(original, pixels=pixels).size

    assert original_width == cropped_width
    assert (original_height - pixels * 2) == cropped_height

