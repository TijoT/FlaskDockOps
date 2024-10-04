pipeline {
    options {
        skipDefaultCheckout true
    }

  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/TijoT/FlaskCI', branch: 'main')
      }
    }

  }
}