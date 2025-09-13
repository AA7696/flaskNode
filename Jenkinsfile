pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_PATH = '/usr/local/bin/docker-compose'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/AA7696/flaskNode.git'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh '''
                docker-compose down
                docker-compose up --build -d
                '''
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker system prune -f'
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Deployment Failed!'
        }
    }
}
