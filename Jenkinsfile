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
        - sleep
        args:
        - 99d
      - name: kaniko
        image: gcr.io/kaniko-project/executor:debug
        command:
        - sleep
        args:
        - 9999999
        volumeMounts:
        - name: kaniko-secret
          mountPath: /kaniko/.docker
      restartPolicy: Never
      volumes:
      - name: kaniko-secret
        secret:
            secretName: dockercred
            items:
            - key: .dockerconfigjson
              path: config.json
        '''
        }
        }
   
  stages {
        stage('Run calc') {
      steps {
        container('python') {
          sh 'pip3 install flask'
          sh 'pip3 install flake8'
          sh 'pip3 install prometheus-flask-exporter'
        }
      }
    }
    stage('Test code') {
      steps {
        container('python') {
          sh 'flake8 --extend-ignore E501,F401,F403,W293,F841 ./'
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
            script {
                def result = sh(returnStdout: true, script: 'curl "http://127.0.0.1:5000/?expr=5%2A%28200%2B50%29%2F10"').trim()
                echo "Result: ${result}"
                if (result != '125.0') {
                    error "Result is not equal to 125. Stopping the job."
                }
            }
        }
      }
    }
        stage('Build') {
            steps {
              container('python') {
                script {
                 
          sh 'echo pwd'
          
        }
      }
    }
}
        stage('Push') {
            steps {
              container('kaniko') {
                script {
          sh '/kaniko/executor --context `pwd` --destination brazovsky/calc:1.0'
        }
      }
    }
  }
  }
    post {
     success {
        withCredentials([string(credentialsId: 'botSecret', variable: 'TOKEN'), string(credentialsId: 'chatId', variable: 'CHAT_ID')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC *Branch*: ${env.GIT_BRANCH} *Test* : OK *Image push* = YES'
        """)
        }
     }

     aborted {
        withCredentials([string(credentialsId: 'botSecret', variable: 'TOKEN'), string(credentialsId: 'chatId', variable: 'CHAT_ID')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC *Branch*: ${env.GIT_BRANCH} *Test* : `Aborted` *Image push* = `Aborted`'
        """)
        }

     }
     failure {
        withCredentials([string(credentialsId: 'botSecret', variable: 'TOKEN'), string(credentialsId: 'chatId', variable: 'CHAT_ID')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC  *Branch*: ${env.GIT_BRANCH} *Test* : `Failure` *Image push* = `no`'
        """)
        }
     }

     }
  
}
