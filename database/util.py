from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from datetime import datetime
from time import strftime
import env

start_time = datetime.now()


def log(msg):
    elapsed_time = str(datetime.now() - start_time).split('.')[0]
    print('[{} ({})] {}'.format(strftime('%Y-%m-%d %H:%M:%S'), elapsed_time, msg))


def get_connection(db: str) -> Engine:
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'
    return create_engine(url)


def partition(seq, size):
    # from http://stackoverflow.com/a/434328
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def get_mysql_command():
    return f'mysql -u{env.user} -p{env.password} --host {env.host}'.split()

