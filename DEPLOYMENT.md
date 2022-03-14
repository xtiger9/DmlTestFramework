## DmlTestFramework 部署手册

---

### 使用方式一

在IDE(例如：Pycharm)中运行

---

#### 步骤

- 1.在IDE中打开项目
- 2.在Pycharm中配置好python interpreter
- 3.修改以下文档为你的测试数据库信息
  ```
  DmlTestFramework/config/db_config.conf
  ```
- 4.修改以下文档中的目录为你的程序运行主机的目录
  ```
  DmlTestFramework/shell/auto_run.sh
  ```
- 5.打开IDE中的terminal, 执行以下命令安装依赖包
    ```shell
    # 请留意是否需要替换成程序运行主机的实际路径
    pip install -r .\requirements\lib.txt
    ```
- 6.打开cases目录下的run_unittest.py
- 7.点击运行按钮即可运行测试用例
- 8.查看`DmlTestFramework/report/`下的测试报告

### 使用方式二

在Linux服务器（例如：CentOS 7）上运行

---

#### 步骤

- 1.将DmlTestFramework整个项目文件放置在服务器目录下
- 2.修改以下文档为你的测试数据库信息
  ```
  DmlTestFramework/config/db_config.conf
  ```
- 3.修改以下文档中的目录为你的程序运行主机的目录
  ```
  DmlTestFramework/shell/auto_run.sh
  ```
- 4.运行shell目录下的auto_run.sh文件 或 设置crontab任务定时运行
  ```shell
  # 请留意auto_run.sh中的路径是否需要替换成程序运行主机的实际路径
  bash DmlTestFramework/shell/auto_run.sh
  ```
- 5.查看`DmlTestFramework/report/`下的测试报告

### 注意事项

---

程序使用的是Python3.9；
以上两种使用方式，作者均测试成功无报错；
若挪至其他机器后有报错，建议可从以下三方面排查：
- 程序运行环境
- 程序运行路径
- 配置文件路径







