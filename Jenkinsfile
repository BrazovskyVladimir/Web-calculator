pipeline {
  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        spec:
          containers:
          - name: python
            image: python
            command:
            - cat
            tty: true
        '''
    }
  }
  stages {
    stage('Run calc') {
      steps {
        container('python') {
          sh 'pip3 install flask'
          sh 'pip3 install flake8'
        }
      }
    }
    stage('Test code') {
      steps {
        container('python') {
          sh 'flake8 --extend-ignore E501,F401,F403 ./'
        }
      }
    }
    stage('Start server') {
      steps {
        container('python') {
          sh 'nohup python3 main.py &'
        }
      }
    }
    stage('Test calc and server') {
      steps {
        container('python') {
          sh '$result = 'curl "http://127.0.0.1:5000/?expr=5%2A%28200%2B50%29%2F10"' '
          sh '$result'
        }
      }
    }
    
  }
}
