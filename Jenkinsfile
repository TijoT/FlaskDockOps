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

  }
}