pipeline{
    agent any
    stages{
        stage("check out"){
            steps{
                git credentialsId: 'cc20d591-cf24-4226-91e6-bfc84e3fe897', url: 'https://github.com/wslxko/mdApi'
            }
        }
        stage("run"){
            steps{
                sh 'python3 runner.py'
            }
        }
    }
}