# Open Sourdough
Continously take pictures of your starter!

## How to run it
```bash
# build the docker image
docker build -t open-sourdough .

# create the directory where the data ends up
mkdir -p /home/$USER/data/

# run the image. notice the video device is mounted
docker run \
    -v /home/$USER/data/:/data \
    --device=/dev/video0:/dev/video0 \
    -it \
    -e OPEN_SOURDOUGH_ROOT_IMAGE_DIR=/data/ \
    -e OPEN_SOURDOUGH_DB_HOST=192.168.0.140 \
    -e OPEN_SOURDOUGH_DB_NAME=open-sourdough \
    -e OPEN_SOURDOUGH_DB_USER=postgres \
    -e OPEN_SOURDOUGH_DB_PASSWORD=postgres \
    -e OPEN_SOURDOUGH_DB_PORT=5438 \
    --rm \
    open-sourdough 
```