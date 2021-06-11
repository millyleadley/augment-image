# augment-image

Welcome to `augment-image`! This packages uses a simple Flask app to display some exciting image augmentations.

## Instructions for use

Clone the repo ([instructions](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)) and move to `augment-image/app`. Build the image:
```
docker image build -t app .
```

Create the docker container and start it. NB: `-d` indicates we detatch from the container in the terminal. `-p` indicates "publish" and maps a port on the Docker host to a container port.
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

## Features

* Introduced a default image and some text for the webpage
* Created an (equally exciting) image transformation for cropping
* Included tests for the cropping function and the flask app response
* Created a CI workflow that runs the tests and builds an image for every push, and pushes the image to [Docker hub](https://hub.docker.com/repository/docker/millyleadley/augmentate) for master branches

## Future work

I gave more attention to the github actions and docker part of this package as these were relatively new to me, but other stuff I thought would be cool to add:
* Create a html form for accepting the url, along with buttons for each type of transformation or "randomise"
* Lots more transformations, this ones in this package are fun: https://github.com/aleju/imgaug
* Adding a small database to track the images that have been transformed