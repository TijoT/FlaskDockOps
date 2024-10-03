# Official python image based on debian 12
FROM python:3.12.6-slim-bookworm

# working directory in the container
WORKDIR /usr/app

# install apt packages required for speedtest
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get upgrade -y --no-install-recommends 

COPY requirements.txt /usr/app/    

RUN pip install -r requirements.txt

# COPY all files except those defined in .dockerignore
COPY . /usr/app/ 

# Execute python script
CMD [ "python3",  "main.py"]