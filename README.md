## DmlTestFramework

---

### 功能说明

---

DmlTestFramework是一个小的测试框架/工具；
其主要功能是：对MySQL数据库的DML系列操作进行功能测试；
目前为第一版，仅实现了DML中SELECT部分的测试用例的设计。


### 使用场景

---

1. 假设：新开发了一款类似MySQL的数据库，需要进行一系列测试，其中就包括对DML这块的测试工作；
2. 假设：对现有数据库涉及DML操作的模块进行了变更或二次开发，需要进行测试；
3. 假设：对MySQL数据库进行了二次开发，需要进行测试。

### 项目结构

---

```
DmlTestFramework 
    .
    ├── case # 测试用例-代码部分
          ├── test_dml.py # SELECT测试用例-代码部分 所在文件
    |     └── run_unittest.py # 运行所有测试用例集 并 生成测试报告的文件
    ├── cases_data # 测试用例-数据部分
    |     └── select.yaml # SELECT测试用例-数据部分 所在文件
    ├── config # 数据库配置文件
    ├── db_connect # 获取数据库连接的文件
    ├── keywords_driver # 测试用例-关键字驱动文件
    ├── import_data # 需要导入数据库的测试数据
    |     └── IMPORT.md # 建表语句 和 导入测试数据的脚本 所在文件
    ├── logs # 彩色日志文件
    ├── report # 测试报告所在文件
    ├── requirements # 需要安装的依赖包
    ├── shell # 自动运行的脚本
    ├── DEPLOYMENT.md # 程序部署文件
    └── README.md # 程序说明文件
```

### 测试用表

---

>  表名: `test_table` 
> 
>  获取 `建表语句`和`导入测试数据的脚本`: `../import_data/IMPORT.md` 

|  字段名  |     数据类型     | 是否为空 | Key | 默认值 | 备注  |
|:-----:|:------------:|:---:|----|:----:|:----:|
|  id   |   int(11)    | NO  | PRI | NULL |  主键  | 
| key1  | varchar(100) | YES | MUL | NULL | 普通二级索引 |
| key2  |   int(11)    | YES | UNI | NULL | 唯一二级索引 | 
| key3  | varchar(100) | YES | MUL | NULL | 普通二级索引 |  
| key_part1 | varchar(100) | YES | MUL | NULL | 联合索引 | 
| key_part2 | varchar(100) | YES |    | NULL |      | 
| key_part3 | varchar(100) | YES |    | NULL |      |  
| common_field | varchar(100) | YES |    | NULL |      | 







