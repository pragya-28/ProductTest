pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('setup') {
            steps {
                browserstack(credentialsId: '78e87401-8946-4e7e-9d5c-b9dccfbb8e52'){
                    sh 'python JenkinsTest.py'
                    echo 'Hello....'}
            }
        }
    }
}
