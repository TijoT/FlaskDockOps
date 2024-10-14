
# Jenkins CI/CD with Docker

Project demonstrates CI/CD pipeline of a Flask app using Jenkins and Docker. 
The official Jenkins (LTS) docker image is customized to include docker application, enabling 
the building of Docker images within the Jenkins container.

## Start Jenkins server
The `docker_compose_jenkins.yaml` defines two services: 
1. `jenkins-docker`: service to run Docker within Docker
2. `jenkins-blueocean`: customized Jenkins image with blueocean plugin

To build and start jenkins server, run the following command:  
    `docker compose -f docker_compose_jenkins.yaml up -d`

To rebuild the docker image and start Jenkins server fresh, run the following commands:  
    `docker network remove NETWORKID`   -- remove obsolete networks  
    `docker volume remove VOLUMENAME`   -- remove obsolete volumes  
    `docker compose -f docker_compose_jenkins.yaml build --no-cache`

References:  
    https://www.jenkins.io/doc/book/installing/docker/  
    https://www.jenkins.io/doc/book/installing/docker/#setup-wizard

## Retrieve initial admin password
Once Jenkins server is up and running, you need the initial admin password to setup Jenkins. 
To retrieve it from the docker container, run the following command  
    `docker exec DOCKER_CONTAINER_ID cat /var/jenkins_home/secrets/initialAdminPassword`

Create login details and install relevant plugins to continue working with Jenkins.

## Flask app
The Flask app is a simple web application that runs in debug mode, listening on port `3000`. When the app is accessed,
it displays a message `Congrats!!`. 

Pytest is used to run tests and verify the flask app.

## CI pipeline in Jenkins
Create a multi-stage pipeline that includes the following steps:
* Build: Build a Docker image that packages the Flask app. Once built, launch the Flask app by starting Docker container.
* Test: Execute `pytest` to validate flask app running inside the container
* Teardown: After testing, stop and remove the Docker container to clean up resources
* Deploy: If tests are passed, push Docker image to docker repo for further use.

