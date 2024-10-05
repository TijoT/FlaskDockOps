pipeline {
  agent any
  stages {
    
    stage('Checkout') {
      steps {
        git(credentialsId: 'Jenkins-Github-Pat', url: 'https://github.com/TijoT/FlaskCI', branch: 'main', poll: true)
      }
    }

    stage('Build docker') {
      steps{
        sh ("docker compose -f docker-compose_app.yaml up -d")
        sh ("docker-compose -f docker-compose_app.yaml up -d")
        echo "Docker-compose-build Build Image Completed"  
      }
    }

    stage('Test') {
      steps{
        sh ("cd src")
        sh ("pytest tests/")
      }
    }
  }

}