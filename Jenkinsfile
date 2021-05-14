pipeline {

    agent none
    stages {
//         stage('Install') {
//             steps {
//                 sh '''
//                 make install
//                 '''
//             }
//         }
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
        stage('Publish') {
            when {
                tag "release-*"
            }
            agent {
                dockerfile {
                    filename 'Dockerfile.build'
                }
            }
            steps {
                sh '''
                make build
                make publish
                '''
            }
        }
    }
}