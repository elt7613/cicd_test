pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    
    stage('Env setup') {
      steps {
        sh 'python3 -m venv .venv'
      }
    }

    stage('Install requirements') {
      steps {
        sh '.venv/bin/pip install -r requirements.txt'
      }
    }

    stage('Make migrations') {
      steps {
        sh '.venv/bin/python manage.py makemigrations'
      }
    }

    stage('Migrate') {
      steps {
        sh '.venv/bin/python manage.py migrate'
      }
    }

    stage('Test') {
      steps {
        sh '.venv/bin/python test.py'
      }
    }

    stage('Run') {
      steps {
        sh '.venv/bin/python manage.py runserver 0.0.0.0:8457'
      }
    }
  }
}
