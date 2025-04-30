pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                git url: "https://github.com/AMMUG143/hii.git", branch: "main"
            }
        }

        stage('install dependencies') {
            steps {
                bat '''
                    C:\\Users\\amrutha\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m venv venv
                    venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install pytest
                '''
            }
        }

        stage('testing') {
            steps {
                bat '''
                    venv\\Scripts\\activate
                    pytest test_bill.py
                '''
            }
        }

        stage('deploy') {
            steps {
                bat '''
                    venv\\Scripts\\activate
                    C:\\Users\\amrutha\\AppData\\Local\\Programs\\Python\\Python313\\python.exe getbill.py
                '''
            }
        }
    }
}
