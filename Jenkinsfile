pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                 git branch: 'main', url: 'https://github.com/KARTHIKEYAN-20/my-jenkins-project.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
            }
        }
    }
}
