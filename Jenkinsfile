pipeline {
    agent any 
    stages {
        stage('Build Images') { 
            steps {
                sh 'docker build -t sdhalliday92/service_1 ./Service_1'
                sh 'docker build -t sdhalliday92/service_2 ./Service_2'
                sh 'docker build -t sdhalliday92/service_3 ./Service_3'
                sh 'docker build -t sdhalliday92/service_4 ./Service_4'
            }
        }
    }
}