pipeline {
  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        spec:
          containers:
          - name: python
            image: python:alpine
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
          sh 'python main.py'
        }
      }
    }
  }
}
