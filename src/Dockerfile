# Official python image based on debian 12
FROM python:3.12.6-slim-bookworm

# working directory in the container
WORKDIR /usr/app

# Temporarily add requirements.txt file for pip install instruction
# Bind mounted files do not persist in the final image
RUN --mount=type=bind,source=./src/requirements.txt,target=/tmp/requirements.txt \
    pip install --requirement /tmp/requirements.txt

# Root level reference for copying    
# copy all files except those defined in .dockerignore
COPY docker_compose_app.yaml ./src/ /usr/app/ 

EXPOSE 3000 

# Execute python script
CMD [ "python3",  "main.py"]