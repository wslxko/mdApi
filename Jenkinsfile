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
                    attachmentsPattern: './report/latest/测试报告.html',
                    from: 'lxksg@qq.com',
                    mimeType: 'text/plain',
                    subject: 'auto test report',
                    to: 'lxksg@qq.com',
                    body: """
                        <body>
                          <table width='95%' cellpadding='0' cellspacing='0'>
                            <tr>
                              <td>
                                <h2>构建结果:<span color='#0000FF'>${currentBuild.currentResult}</span></h2>
                              </td>
                            </tr>
                            <!-- git信息 -->
                            <tr>
                              <td><br/>
                                <b>
                                  <font color="#0B610B">git信息</font>
                                </b>
                                <hr size="2" width="100%" align="center" />
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <ul>
                                  <li>项目名称: idaas</li>
                                  <li>项目分支: sit</li>
                                  <li>提交人: lxk</li>
                                  <li>提交时间: lxk</li>
                                  <li>提交信息: lxk</li>
                                  <li>提交hash: lxk</li>
                                </ul>
                              </td>
                            </tr>
                            <!-- 构建信息 -->
                            <tr>
                              <td><br/>
                                <b>
                                  <font color="#0B610B">构建信息</font>
                                </b>
                                <hr size="2" width="100%" align="center" />
                              </td>
                            </tr>
                            <tr>
                              <td>
                                <ul>
                                  <li>构建编号: 1次构建</li>
                                  <li>当前下载地址: 1</a></li>
                                  <li>最后下载地址: 1</a></li>
                                  <li>构建日志: <a href="1console">1console</a></li>
                                </ul>
                              </td>
                            </tr>
                          </table>
                        </body>
                        """,
                )
            }
        }
    }
}
