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
          sh 'python3 main.py'
        }
      }
      stage('Run test') {
        steps {
          container('python') {
            sh 'curl http://127.0.0.1:5000/?expr=5%2A(200%2B50)%2F10'
          }
        }
      }
    }
  }
}
