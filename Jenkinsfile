pipeline {
    agent any 
    stages {
        stage('clone repo') { 
            steps {
                sh "rm -rf REGEX"
                sh "git clone https://github.com/padhideepak89/REGEX.git"
                sh "mvn clean -f ./REGEX"
            }
        }
        stage('Test') { 
            steps {
                sh "mvn test -f ./REGEX"
            }
        }
        stage('Deploy') { 
            steps {
                sh "mvn package -f REGEX" 
            }
        }
    }
}
