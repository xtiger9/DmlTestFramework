创建表test_table的语句：
```sql
create table test_table(
 id int not null auto_increment,
 key1 varchar(100),
 key2 int,
 key3 varchar(100),
 key_part1 varchar(100),
 key_part2 varchar(100),
 key_part3 varchar(100),
 common_field varchar(100),
 primary key(id),
 key idx_key1(key1),
 unique key uk_key2(key2),
 key idx_key3(key3),
 key idx_key_part(key_part1, key_part2, key_part3)
) Engine=InnoDB CHARSET=utf8;
```


往表test_table中导入数据的语句：
```sql
LOAD DATA INFILE '/tmp/test_table_data.csv' 
INTO TABLE test_table
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
 (key1,key2,key3,key_part1,key_part2,key_part3,common_field);
```

导入后查询表test_table中数据如下：
```sql
mysql> select count(*) from test_table;                                         
+----------+
| count(*) |
+----------+
|    29990 |
+----------+
1 row in set (0.01 sec)
```
