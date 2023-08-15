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
      - name: kubectl
        image: bitnami/kubectl
        command:
        - sleep
        args:
        - 99d
        volumeMounts:
        - name: kubectl-secret
          mountPath: /home/jenkins/.kube
      restartPolicy: Never
      volumes:
      - name: kubectl-secret
        secret:
            secretName: admin-conf-secret 
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
    stage('Deploy calc Image') {
      container('kubectl') {
        stage('Deploy calc project') {
          sh '''
            kubectl apply -f /home/jenkins/agent/workspace/calcdeploy/deployment.yaml
          '''
        }
      }
    }
  }
}
