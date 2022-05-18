from faker import Faker
from random import random
import time
from pymysql import TIMESTAMP
from pysqler import Insert
from datetime import datetime, timedelta


fake = Faker()


class DataType:
    Enum = 'enum'
    INT = 'int'
    DOUBLE = 'double'
    EMAIL = 'email'
    STR = 'str'
    TEXT = 'text'
    CITY = 'city'
    DATETIME = 'datetime'
    TIMESTAMP = 'timestamp'
    DATE = 'date'


def _get_data(columns_dict):
    item = dict()
    for column in columns_dict:

        column_data_option = columns_dict[column]
        column_data_type = column_data_option[0]

        if column_data_type == DataType.Enum:
            column_data_items = column_data_option[1]
            item[column] = fake.random_choices(
                elements=column_data_items, length=1)[0]
            continue

        if column_data_type == DataType.STR:
            item[column] = fake.pystr()
            continue

        if column_data_type == DataType.TEXT:
            text_l = column_data_option[1]
            u = fake.texts(nb_texts=text_l,
                           max_nb_chars=500,
                           ext_word_list=None)
            item[column] = " ".join(u)
            continue

        if column_data_type == DataType.EMAIL:
            item[column] = fake.company_email()
            continue

        if column_data_type == DataType.TIMESTAMP:
            timestamp = int(datetime.now().timestamp()*1000)
            item[column] = timestamp
            continue

        if column_data_type == DataType.CITY:
            item[column] = fake.city()
            continue
        if column_data_type == DataType.DATETIME:
            if len(column_data_option) == 2:
                dt_op = column_data_option[1]
                if dt_op == 'random':
                    item[column] = str(fake.date_time())
                    continue
            now = datetime.now()
            now_str = now.strftime("%Y-%m-%d %H:%M:%S")
            item[column] = now_str
            continue

        if column_data_type == DataType.DOUBLE:
            if len(column_data_option) == 2:
                column_data_arrange = column_data_option[1]

                min_d = column_data_arrange[0]
                max_d = column_data_arrange[1]
                bound = max_d - min_d
                item[column] = min_d + \
                    fake.pyfloat(0, 2, positive=True) * bound
            else:
                item[column] = fake.pyfloat(positive=True)
            continue

        if column_data_type == DataType.INT:
            if len(column_data_option) == 2:
                column_data_arrange = column_data_option[1]

                min_d = column_data_arrange[0]
                max_d = column_data_arrange[1]
                item[column] = fake.random_int(min=min_d, max=max_d)
            else:
                item[column] = fake.random_int()
            continue
    return item


def gen(columns: dict, interval_min=1000, interval_max=3000, increment_id=''):
    """
    间隔随机毫秒数生成模拟订单数据
    :param columns: 数据包含的字段机器数据类型
    :param interval_min: 最小毫秒数
    :param interval_max: 最大毫秒数
    :return:
    """

    while True:
        # item["user_mail"] = fake.safe_email()
        item = _get_data(columns)
        if increment_id:
            now = datetime.now()
            item[increment_id] = int(now.timestamp() * 1000)

        yield item
        interval = fake.random_int(min=interval_min, max=interval_max) * 0.001
        time.sleep(interval)
