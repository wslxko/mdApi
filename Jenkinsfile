pipeline{
    agent any
    stages{
        stage("check out"){
            steps{
                git credentialsId: '30857ba1-cf29-4f9f-9609-bdf99e85d52d', url: 'https://github.com/wslxko/mdApi'
            }
        }
        stage("run"){bfc84e3fe897
            steps{
                sh label: '', script: 'python3 runner.py'
                echo '自动化代码执行完毕'
            }
        }
    }
}
