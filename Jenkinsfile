pipeline {
  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        spec:
        containers:
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
    stage('Build calc Image') {
      container('kaniko') {
        stage('Build calc project') {
          sh '''
            /kaniko/executor --context `pwd` --destination brazovsky/calc:1.0
          '''
        }
      }
    }
  }
}
