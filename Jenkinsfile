pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mjid6/fastapi-app" // Replace with your DockerHub username and image name
        DOCKER_TAG = "latest" // Docker image tag
    }

     stages {
            stage('Clone Repository') {
                steps {
                    git branch: 'main', url: 'https://github.com/elidrissi-abdelmajid/fastapi_model.git'
                }
            }
            stage('Build Docker Image') {
                steps {
                    script {
                        docker.build('fastapi_model_image:latest')
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
