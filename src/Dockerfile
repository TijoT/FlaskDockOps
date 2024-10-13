# Official python image based on debian 12
FROM python:3.12.6-slim-bookworm

# working directory in the container
WORKDIR /usr/app

COPY ./requirements.txt /usr/app/    

RUN pip install -r requirements.txt

# COPY all files except those defined in .dockerignore
COPY . /usr/app/ 

EXPOSE 3000 

# Execute python script
CMD [ "python3",  "main.py"]