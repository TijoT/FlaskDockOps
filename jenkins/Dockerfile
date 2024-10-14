# Customize official Jenkins Docker image with plugin blueocean
FROM jenkins/jenkins:lts-jdk17

USER root

# installs latest stable release of docker and dependent packages
RUN curl -fsSL https://get.docker.com | sh

USER jenkins

RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"