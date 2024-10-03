# Build image 
`docker build -t TAG_NAME .`

# Analyze files in the built image 
`docker run --rm -it --entrypoint=/bin/bash TAG_NAME`

# Run image in a detached mode. Container is removed when it exits i.e logs are no longer available
`docker run -d --rm TAG_NAME`

# Analyze stdout from a detached container
`docker run -d TAG_NAME`
`docker logs CONTAINER_ID`
