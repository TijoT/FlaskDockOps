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

  }
  options {
    skipDefaultCheckout(true)
  }
}