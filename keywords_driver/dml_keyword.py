import jsonpath
import json
import os.path
from db_connect.db import DB
import pandas as pd
from logs.log import Logger


class DmlKeywords:
    """支持DML测试用例的关键字驱动类,封装主要的测试动作"""
    def __init__(self):
        """初始化实例"""
        if os.getcwd().__contains__('keywords_driver'):
            self.db = DB('../config/db_config.conf', 'TESTDB')
            print('../config/db_config.conf')
        else:
            self.db = DB(os.getcwd() + '/config/db_config.conf', 'TESTDB')
            print(os.getcwd() + '/config/db_config.conf')
        self.db_engine = self.db.engine
        self.log = Logger(logger='test')

    def function(self, sql=None, func_type=None):
        """执行常用聚合函数的方法"""
        try:
            self.log.debug('sql: {}'.format(sql))
            with self.db_engine.connect() as conn:
                trans = conn.begin()
                result = conn.execute(sql)
                row = result.fetchone()
                trans.commit()
        except Exception as e:
            self.log.error('run error info: {}'.format(e))
        else:
            return row[0]
        finally:
            self.db_engine.dispose()
            self.log.info("dispose db connection in function() method")

    def select(self, sql=None):
        """执行select语句的方法"""
        try:
            result = pd.read_sql(sql=sql, con=self.db_engine)
        except Exception as e:
            self.log.error('run error info: {}'.format(e))
        else:
            return len(result)
        finally:
            self.db_engine.dispose()
            self.log.info("dispose db connection in select() method")

    def explain(self, sql=None):
        """执行explain语句的方法"""
        try:
            result = pd.read_sql(sql=sql, con=self.db_engine)
            result_dict = {'id': result['id'][0],
                           'select_type': result['select_type'][0],
                           'table': result['table'][0],
                           'partitions': result['partitions'][0],
                           'type': result['type'][0],
                           'possible_keys': result['possible_keys'][0],
                           'key': result['key'][0],
                           'key_len': result['key_len'][0],
                           'ref': result['ref'][0],
                           'rows': result['rows'][0],
                           'filtered': result['filtered'][0],
                           'extra': result['Extra'][0]}
        except Exception as e:
            self.log.error('run error info: {}'.format(e))
        else:
            return result_dict
        finally:
            self.db_engine.dispose()
            self.log.info("dispose db connection in explain() method")

    def insert(self, sql=None):
        """执行insert语句的方法"""
        try:
            with self.db_engine.connect() as conn:
                # connection.execution_options(isolation_level="AUTOCOMMIT")
                trans = conn.begin()
                result = conn.execute(sql)
                trans.commit()
        except Exception as e:
            trans.rollback()
            self.log.error('run error info: {}'.format(e))
        else:
            return result.rowcount
        finally:
            self.db_engine.dispose()
            self.log.info("dispose db connection in insert() method")

    def get_text(self, res, key):
        """校验字段获取的方法"""
        if res is not None:
            try:
                text = json.loads(res)
                value = jsonpath.jsonpath(text, '$..{}'.format(key))
                if value:
                    if len(value) == 1:
                        return value[0]
                return value
            except Exception as e:
                self.log.error('run error info: {}'.format(e))
        else:
            return None
