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
  environment {
        // Customize these environment variables as needed
        DOCKER_REGISTRY_CREDENTIALS = credentials('docker-registry-credentials')
        KUBE_CONFIG_CREDENTIALS = credentials('kube-config-credentials')
        IMAGE_NAME = 'my-python-app'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        KUBE_NAMESPACE = 'jenkins-ns'
        KUBE_DEPLOYMENT_NAME = 'my-webcalc'
  }

  stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("${IMAGE_NAME}:${IMAGE_TAG}", '.')
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', "${DOCKER_REGISTRY_CREDENTIALS}") {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withCredentials([kubeconfigFile(credentialsId: "${KUBE_CONFIG_CREDENTIALS}", variable: 'KUBECONFIG')]) {
                        sh "kubectl --kubeconfig=${KUBECONFIG} apply -f kubernetes/deployment.yaml -n ${KUBE_NAMESPACE}"
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
