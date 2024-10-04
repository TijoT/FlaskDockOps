pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        echo 'Test build message'
        git(url: 'https://github.com/TijoT/FlaskCI', branch: 'main')
      }
    }

  }
}