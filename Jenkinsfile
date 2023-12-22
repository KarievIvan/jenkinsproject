pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('hello') {
      steps {
        bat 'python hello.py'
      }
    }
    stage('test_Lab2') {
      steps {
        bat 'python test_Lab2.py'
      }
    }
  }
}