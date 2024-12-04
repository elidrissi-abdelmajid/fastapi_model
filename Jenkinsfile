pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mjid6/fastapi-app" // Replace with your DockerHub username and image name
        DOCKER_TAG = "latest" // Docker image tag
    }

     stages {
            stage('Clone Repository') {
                steps {
                    git branch: 'master', url: 'https://github.com/elidrissi-abdelmajid/fastapi_model.git'
                }
            }
            stage('Build Docker Image') {
                steps {
                    script {
                        docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                    }
                }
            }
            stage('Push Docker Image') {
                steps {
                    script {
                        docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                            docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                        }
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
