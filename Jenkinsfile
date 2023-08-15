podTemplate(yaml: '''
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
''') {
  node(POD_LABEL) {
    stage('Get calc project') {
      git url: 'https://github.com/BrazovskyVladimir/Web-calculator.git', branch: 'master'
      container('python') {
        stage('Build calc project') {
          sh '''
          echo pwd
          '''
        }
      }
    }

    stage('Build calc Image') {
      container('kaniko') {
        stage('Build calc project') {
          sh '''
            /kaniko/executor --context `pwd` --destination brazovsky/calc:1.0
          '''
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
}
