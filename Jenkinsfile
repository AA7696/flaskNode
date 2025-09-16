pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_PATH = '/usr/local/bin/docker-compose'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/AA7696/flaskNode.git'
            }
        }

        stage('Build and Deploy') {
            steps {
                sh '''
                echo "Stopping existing containers..."
                ${DOCKER_COMPOSE_PATH} down

                echo "Building and starting containers..."
                ${DOCKER_COMPOSE_PATH} up --build -d
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
            echo '✅ Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed!'
        }
    }
}
