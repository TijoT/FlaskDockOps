pipeline {
  agent any
  stages {
    
    stage('Checkout') {
      steps {
        git(credentialsId: 'Jenkins-Github-Pat', url: 'https://github.com/TijoT/FlaskCI', branch: 'main', poll: true)
      }
    }

    stage('Test') {
      steps {
        echo 'Print test '
      }
    }

    stage('Deploy') {
      steps {
        echo 'Print deploym'
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
  options {
    skipDefaultCheckout(true)
  }
}