pipeline {
    agent any
    stages {
        stage('Clone Repository') {
    steps {
        git branch: 'main', url: 'https://github.com/KARTHIKEYAN-20/my-jenkins-project.git'
    }
}
        stage('Extract ZIP and Start Server') {
            steps {
                sh 'python3 step5_script.py'  // Change this to match your actual script name
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover tests/'  // Adjust if needed
            }
        }
        stage('Generate Report') {
            steps {
                sh 'cat report.txt'  // Adjust if needed
            }
        }
    }
}
