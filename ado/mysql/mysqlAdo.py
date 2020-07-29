# -*- encoding: utf-8 -*-
"""
@File    : mysqlAdo.py
@Time    : 2020/6/25 19:58
@Author  : MordeKs
@Email   : Gjay@163.com
@Software: PyCharm
@Description:
"""

import contextlib

import pymysql


class DBHelper:
    def __init__(self, host='127.0.0.1', port=3306, user=None, passwd='', database=None, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset

    @contextlib.contextmanager
    def mysql(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.database,
                               charset=self.charset)
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            yield cursor
        finally:
            conn.commit()
            cursor.close()
            conn.close()

    def execute(self, sql, args=None):
        with self.mysql() as cursor:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            lastid = cursor.lastrowid
            return result

    def executemany(self, sql, args):
        if not args:
            return
        with self.mysql()as cursor:
            row_count = cursor.executemany(sql, args)
            result = cursor.fetchall()
            return result

    def insert(self,sql):
        with self.mysql()as cursor:
            cursor.execute(sql)
            last_id = cursor.lastrowid
            return last_id

    def update(self,sql,args):
        if not args:
            return
        with self.mysql()as cursor:
            count = cursor.execute(sql,args)
            return count