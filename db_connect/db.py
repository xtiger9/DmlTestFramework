from sqlalchemy import create_engine
import configparser


class DB:
    """获取数据库连接"""
    def __init__(self, config_file, db_environment):
        # 实例化db配置文件
        conf = configparser.ConfigParser()
        conf.read(config_file)
        # 获取db连接参数
        connector = conf[db_environment]['CONNECTOR']
        host = conf[db_environment]['HOST']
        port = conf[db_environment]['PORT']
        user = conf[db_environment]['USER']
        passwd = conf[db_environment]['PASSWD']
        db_name = conf[db_environment]['DB_NAME']
        charset = conf[db_environment]['CHARSET']

        try:
            self.engine = create_engine(f'{connector}://{user}:{passwd}@{host}:{port}/{db_name}?charset={charset}')
        except Exception as e:
            print('init db connect failed: {}'.format(e))
