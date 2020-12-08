pipeline{
    agent any
    stages{
        stage("check out"){
            steps{
                git credentialsId: '30857ba1-cf29-4f9f-9609-bdf99e85d52d', url: 'https://github.com/wslxko/mdApi'
            }
        }
        stage("run"){
            steps{
                sh label: '', script: '/usr/local/bin/python3 runner.py -p idaas -e sit'
                echo '自动化代码执行完毕'
            }
        }
        stage("send email"){
            steps{
                emailext(
                    attachmentsPattern: 'report/latest/测试报告.html,report/latest/测试运行日志.log',
                    from: 'lxksg@qq.com',
                    mimeType: 'text/plain',
                    subject: '自动化测试报告',
                    to: '${DEFAULT_RECIPIENTS},382558359@qq.com',
                    body: '自动化测试结果，详细见附件。
                            ${PROJECT_NAME}'
                )
            }
        }
    }
}
