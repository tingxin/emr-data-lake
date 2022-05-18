import pymysql.cursors
import setting


def get_conn(db: str = setting.DB):
    connection = pymysql.connect(host=setting.HOST,
                                 port=setting.PORT,
                                 user=setting.USER,
                                 password=setting.PWD,
                                 database=db,
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def get_binlog_info():
    conn = get_conn()

    with conn.cursor() as cursor:
        sql = 'show master status;'
        cursor.execute(sql)
        conn.commit()
        t = cursor.fetchone()
        return t['File'], t['Position']


def fetch_one(sql: str):
    conn = get_conn()

    with conn.cursor() as cursor:
        cursor.execute(sql)
        conn.commit()
        t = cursor.fetchone()
        return t


def fetch(sql: str):
    conn = get_conn()

    with conn.cursor() as cursor:
        cursor.execute(sql)
        conn.commit()
        t = cursor.fetch_all()
        return t
