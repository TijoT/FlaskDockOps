pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Test build message'
      }
    }

    stage('Test') {
      steps {
        echo 'Execute pytest from source code'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploy when test is successful'
      }
    }

    stage('Finish') {
      steps {
        echo 'Pipeline completed'
      }
    }

  }
}