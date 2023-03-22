# Include environment from the '.env' file in each rule
include .env
export

build:
	docker buildx create --use && \
	docker buildx build \
	-t open-sourdough \
	--platform linux/amd64,linux/arm \
	.
run:
	docker run \
		-v /mnt/open-sourdough/images/:/data \
		--device=/dev/video0:/dev/video0 \
		-it \
		-e OPEN_SOURDOUGH_ROOT_IMAGE_DIR=${OPEN_SOURDOUGH_ROOT_IMAGE_DIR} \
		-e OPEN_SOURDOUGH_DB_HOST=${OPEN_SOURDOUGH_DB_HOST} \
		-e OPEN_SOURDOUGH_DB_NAME=${OPEN_SOURDOUGH_DB_NAME} \
		-e OPEN_SOURDOUGH_DB_USER=${OPEN_SOURDOUGH_DB_USER} \
		-e OPEN_SOURDOUGH_DB_PASSWORD=${OPEN_SOURDOUGH_DB_PASSWORD} \
		-e OPEN_SOURDOUGH_DB_PORT=${OPEN_SOURDOUGH_DB_PORT} \
		--rm \
		open-sourdough 
