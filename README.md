# deployment_interview

Peter (CTO) likes images but loves data augmentation more. He wants a way to see how typical image augmentation in our machine learning affects the images we input to the model. He codes a simple boiler-plate application for you and asks you to finish it off!

To complete the flask app you will need to do the following:

1. Download (Do not fork) the repo, upload to a new repo in your name/account.
2. Write a dockerfile for amd64 for the app.
3. Use github actions to build the dockerfile.
4. Add a image augmentation function image_augmentations.py
5. Add a test for your function
6. Improve the repo/python code/deployment in some imaginative way to show-off... Highlight this in the readme.
7. Send the recycleye team the link to your code.

Put the instructions here on how to set up/run the docker file. It should port-forward the application to run on http://127.0.0.1:8000/.




# augment-image

Welcome to `augment-image`! This packages uses a simple Flask app to return some exciting image augmentations.

## Instructions

Create a virtual environment (feel free to use your favourite installer instead of conda) and install the requirements:
```
conda create -n augment python=3.9.5
conda activate augment
conda install -f requirements.txt
```

Clone the repo ([instructions](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)) and move to `augment-image/app`. Build the image:
```
docker image build -t app .
```

Create the docker container and start it. Note that `-d` indicates we detatch from the container in the terminal. `-p` indicates publish and maps a port on the Docker host (to the outside world) to a container port.
```
docker run -d -p 8000:8000 app
```

To see a random augmentation of the default image (Milhouse from The Simpsons), head to:
```
http://0.0.0.0:8000/
```

To use your own image, append `?url=<image_url>`, for example:
```
http://0.0.0.0:8000/?url=https://imgs.xkcd.com/comics/bad_code.png
```


* Introduced a default image
* Described the augmentation