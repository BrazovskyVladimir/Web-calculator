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
          sh 'python3 main.py'
        }
      }
    }
  }
}
