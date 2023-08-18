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
          sh 'apt update'
          sh 'apt install sshpass'
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
    stage('gzip') {
        steps {
            sh "tar -zcvf calc.build-${env.BUILD_NUMBER}.gz ./*.py"
            archiveArtifacts artifacts: "calc.build-${env.BUILD_NUMBER}.gz"
        }
    }
    stage('ssh') {
        steps {
              withCredentials([usernamePassword(credentialsId: 'diplom1', usernameVariable: 'NUSER', passwordVariable: 'NPASS')]) {
                  script {
                     sh "apt install -y sshpass"
                     sh "sshpass -p ${NPASS} scp -o StrictHostKeyChecking=no calc.build-${env.BUILD_NUMBER}.gz ${NUSER}@192.168.218.114:/home/acd/Desktop/"
                  }
               }
        }
        }
    }
    
  
   post {
     success {
        withCredentials([string(credentialsId: 'botSecret', variable: 'TOKEN'), string(credentialsId: 'chatId', variable: 'CHAT_ID')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC *Branch*: ${env.GIT_BRANCH} *Test* : OK '
        """)
        }
     }

     aborted {
        withCredentials([string(credentialsId: 'botSecret', variable: 'TOKEN'), string(credentialsId: 'chatId', variable: 'CHAT_ID')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC *Branch*: ${env.GIT_BRANCH} *Test* : `Aborted` '
        """)
        }

     }
     failure {
        withCredentials([string(credentialsId: 'botSecret', variable: 'TOKEN'), string(credentialsId: 'chatId', variable: 'CHAT_ID')]) {
        sh  ("""
            curl -s -X POST https://api.telegram.org/bot${TOKEN}/sendMessage -d chat_id=${CHAT_ID} -d parse_mode=markdown -d text='*${env.JOB_NAME}* : POC  *Branch*: ${env.GIT_BRANCH} *Test* : `Failure` '
        """)
        }
     }

 }
}
