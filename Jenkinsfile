pipeline {
    agent any 
    stages {
        stage('Pull Images') { 
            steps {
                sleep time: 10, unit: 'MINUTES'
                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/pull_images.sh'
            }
        }
    }
}