import io
import requests
from flask import Flask, request, render_template
from PIL import Image
from image_augmentations import random_augmentation

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["MAX_CONTENT_LENGTH"] = 4 * 1024 * 1024

DEFAULT_PATH = "static/default.jpg"
AUGMENTATED_PATH = "static/augmented_image.jpg"


@app.route("/", methods=["GET"])
def index():
    image_url = request.args.get("url")
    if image_url:
        image_response = requests.get(image_url)
        image = Image.open(io.BytesIO(image_response.content))
    else:
        image = Image.open(DEFAULT_PATH)
    augmented, augmentation = random_augmentation(image)
    augmented.convert("RGB").save(AUGMENTATED_PATH)
    return render_template(
        "index.html", augmentation=augmentation, object="image" if image_url else "milhouse"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

