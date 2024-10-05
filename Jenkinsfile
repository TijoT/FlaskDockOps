pipeline {
    options {
        skipDefaultCheckout true
    }

  agent any
  stages {
    
    stage('Checkout') {
      steps {
        git(credentialsId: 'Jenkins-Github-Pat', url: 'https://github.com/TijoT/FlaskCI', branch: 'main')
      }
    }

    stage('Build docker') {
      steps{
        sh ("tree")
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