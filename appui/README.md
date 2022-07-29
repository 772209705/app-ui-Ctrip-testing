### 项目介绍
    携程旅行 APP UI 自动化测试，基于Python3.x、pytest 6.2.5 、allure2.x  可生成好看报告allure、 pytest基础用法、显示等待

### 配置环境
    pip install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple

### allure 用法
    1、启动项目并生成allure
    pytest --alluredir=reports/allure --clean-alluredir
    
    2、将allure生成 html格式查看
    allure generate reports/allure -o allure_html --clean