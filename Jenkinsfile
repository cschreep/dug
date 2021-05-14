pipeline {

    agent none
    stages {
        stage('Test') {
            agent {
                dockerfile true
            }
            steps {
                sh '''
                make test
                '''
            }
        }
        stage('Build docker') {
//             when {
//                 tag "release-*"
//             }
            agent {
                dockerfile {
                    filename 'Dockerfile.build'
                }
            }
            steps {
                sh '''
                make build
                '''
            }
        }
    }
}