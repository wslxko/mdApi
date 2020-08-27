pipeline{
    agent any
    stages{
        stage("run"){
            steps{
                sh label: '', script: '/usr/local/bin/python3 runner.py -p idaas -e uat'
                echo '自动化代码执行完毕'
            }
        }
    }
}
