#!/bin/bash

# 以下目录 请替换成部署服务器上的目录
cd /home/guanli/DmlTestFramework

python -m venv dml_test_venv
source ./dml_test_venv/bin/activate
pip install -r ./requirements/lib.txt

/home/guanli/DmlTestFramework/dml_test_venv/bin/python3 /home/guanli/DmlTestFramework/cases/run_unittest.py


