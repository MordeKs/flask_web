# -*- encoding: utf-8 -*-
"""
@File    : mongoAdo.py
@Time    : 2020/6/25 9:58
@Author  : MordeKs
@Email   : Gjay@163.com
@Software: PyCharm
@Description:
"""
import pymongo

class MongoDBHelper:

    def __init__(self,
                 db='db',
                 username=None,
                 password=None,
                 host='127.0.0.1',
                 port=27017,
                 table=None):
        """
        :param db:
        :param username:
        :param password:
        :param host:
        :param port:
        :param table:
        """
        self.db = db
        self.client = pymongo.MongoClient(f'mongodb://{host}:{port}')
        self.username = username
        self.password = password
        self.host=host
        self.port=port
        self.table=table
        if self.username and self.password:
            self.db1 = self.client[self.db][self.table].authenticate(self.username, self.password)
        else:
            self.db1 = self.client[self.db][self.table]

    def db_find(self,sentence):
        result = self.db1.find(sentence)
        return result

    def db_update(self,sentence):
        result = self.db1.update_one(sentence)
        return result

    def db_update_many(self,sentence):
        result = self.db1.update_many(sentence)
        return result


if __name__ == '__main__':
    db = MongoDBHelper(
        db='credit_negative',
        username='pszx',
        password='ps#123456',
        host='10.2.1.64',
        port=27019,
        table='psds-ycyj-fljf-sxbzxr'
    )
    sentence = {}
    print(db.db_find(sentence=sentence).limit(10))


