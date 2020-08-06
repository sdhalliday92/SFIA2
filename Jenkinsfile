pipeline {
    agent any
    stages {
        stage('Build Images') {
            steps {
                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_images.sh'
            }
        }
        stage('Deploy Stack') {
            steps {
                sh './scripts/deploy_stack.sh'
            }
        }
        stage('Cleanup') {
            steps {
                sh './scripts/cleanup.sh'
            }
        }
    }
}