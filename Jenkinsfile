pipeline {
   agent any

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    
    stage('Env  setup') {
      steps {
        sh '''
          python3 -m venv .venv
          source .venv/bin/activate
        '''
      }
    }
    stage('Requirement install') {
      steps {
        sh '''
          source .venv/bin/activate
          pip install -r requirements.txt
        '''
      }
    }
    stage('Migrate') {
      steps {
        sh '''
          source .venv/bin/activate
          python manage.py migrate
        '''
      }
    }
    stage('Make migrations') {
      steps {
        sh '''
          source .venv/bin/activate
          python manage.py makemigrations
        '''
      }
    }
    stage('Test') {
      steps {
        sh '''
          source .venv/bin/activate
          python test.py
        '''
      }
    }
  }
}