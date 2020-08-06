pipeline {

    agent any

    stages {

        stage('Build Images') {

                steps {
                    sh 'chmod +x ./scripts/*.sh'
                    sh './scripts/build_images.sh'
                }
        }

        stage('Run Playbook') {

                steps {
                    sh './scripts/ansible.sh'
                }
        }

        // stage('Start Swarm') {
        //         steps {
        //             sh './scripts/swarm_setup.sh'
        //         }
        // }

        stage('Deploy Stack') {
                steps {
                    sh './scripts/deploy_stack.sh'
                }
        }

        stage('Cleanup'){
                steps {
                    sh './scripts/cleanup.sh'
                }
        }
    }
}