
# Jenkins

Project demonstrates CI with jenkins server

## Start server
Build and start jenkins server by using the following command:
`docker compose -f docker-compose.yaml up -d`

To rebuild the docker image and start jenkins server, run the following command:
`docker compose -f docker-compose.yaml up --build -d`

## Server initial admin password
Once jenkins server is up & running, fetch admin password by accessing the file in the docker container by using the following command
`docker exec DOCKER_CONTAINER_ID cat /var/jenkins_home/secrets/initialAdminPassword`

## Post installation setup 
https://www.jenkins.io/doc/book/installing/docker/#setup-wizard

