
# Jenkins CI/CD with Docker

Project demonstrates CI with Jenkins server. 
Jenkins server started as a container in debian based environment.

## Start Jenkins server
Docker compose file contains two services - DockerInDocker, Custom built Jenkins image.
Reference: https://www.jenkins.io/doc/book/installing/docker/
Build and start jenkins server by using the following command:  
`docker compose -f docker_compose_jenkins.yaml up -d`

To rebuild the docker image and start Jenkins server fresh, run the following commands:
`docker network remove NETWORKID`   -- remove obsolete networks
`docker volume remove VOLUMENAME`   -- remove obsolete volumes
`docker compose -f docker_compose_jenkins.yaml build --no-cache`

## Server initial admin password
Once jenkins server is up & running, fetch admin password by accessing the file 
in the docker container by using the following command  
`docker exec DOCKER_CONTAINER_ID cat /var/jenkins_home/secrets/initialAdminPassword`

## Post installation setup 
https://www.jenkins.io/doc/book/installing/docker/#setup-wizard

# CI pipeline in Jenkins
Create a multi-stage pipeline that includes the following steps
    * Build: build a docker image to start flask app
    * Test: Run pytest to check flask app
    * Deploy: Push docker image to docker repo when tests are successfull

