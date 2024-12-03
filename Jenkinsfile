pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mjid6/fastapi-app" // Replace with your DockerHub username and image name
        DOCKER_TAG = "latest" // Docker image tag
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone your GitHub repository
                git 'https://github.com/elidrissi-abdelmajid/fastapi_model.git' // Replace with your repository URL
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after the pipeline completes
        }
    }
}
