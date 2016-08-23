#!/usr/bin/env python
# coding=utf8

import sys
import json
import urllib
import urllib2
import argparse
import webbrowser
import sqlite3

reload(sys)
sys.setdefaultencoding('utf8')

"""
dict - Chinese/English Translation
@author Feei(wufeifei@wufeifei.com)
@date   2013.12.09
"""


class Dict:
    key = '716426270'
    keyFrom = 'wufeifei'
    api = 'http://fanyi.youdao.com/openapi.do?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='
    dbname = '/home/linwei/workspace/dict/yimudict.db'

    def __init__(self):
        args = self.parse_args()
        if args['debug']:
            print args
        if args['list']:
            dbhandler = DBHandler(self.dbname)
            word_list = dbhandler.query('')
            for item in word_list:
                self.parse_print(item[1], args['detail'])
            return
        if not args['words'] or len(args['words']) < 0:
            print 'ERROR! -h for help'
            return
        for word in args['words']:
            if args['open']:
                self.open_in_browser(word)
            elif args['delete']:
                dbhandler = DBHandler(self.dbname)
                print dbhandler.delete(word)
            else:  # needs translate
                url = self.api + urllib.quote(word)
                raw_content = urllib2.urlopen(url).read()
                if args['add']:
                    dbhandler = DBHandler(self.dbname)
                    print dbhandler.save(word, raw_content)
                else:
                    self.parse_print(raw_content, args['detail'])

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Command line dictionary, for words query, add, delete. Use sqlite3 for store.')
        parser.add_argument('-a', '--add', action='store_true', help='save to database')
        parser.add_argument('-d', '--delete', action='store_true', help='delete from database')
        parser.add_argument('-l', '--list', action='store_true', help='list all words in database')
        parser.add_argument('-o', '--open', action='store_true', help='open query in browser')
        parser.add_argument('-i', '--detail', action='store_true', help='show word detail')
        parser.add_argument('-e', '--debug', action='store_true', help='debug info')
        parser.add_argument('words', metavar='WORDS', type=str, nargs='*')
        return vars(parser.parse_args())

    def open_in_browser(self, word):
        site = 'http://dict.youdao.com/w/' + word
        webbrowser.open(site)
        return

    def parse_print(self, raw_content, show_detail):
        content = json.loads(raw_content)
        code = content['errorCode']
        if code == 0:  # Success
            try:
                u = content['basic']['us-phonetic']  # English
                e = content['basic']['uk-phonetic']
            except KeyError:
                try:
                    c = content['basic']['phonetic']  # Chinese
                except KeyError:
                    c = 'None'
                u = 'None'
                e = 'None'

            try:
                explains = content['basic']['explains']
            except KeyError:
                explains = 'None'

            print '\033[1;32m->', content['query'], '\033[0m'
            print '\033[1;31m------------------------------------- \033[0m'
            print '\033[1;31m#\033[0m', '\033[1;33m', content['translation'][0],
            if u != 'None':
                print '(U:', u, 'E:', e, ')',
            elif c != 'None':
                print '(Pinyin:', c, ')',
            print '\033[0m'

            if explains != 'None':
                for i in range(0, len(explains)):
                    print '\033[1;31m# \033[0m', explains[i]
            else:
                print '\033[1;31m# \033[0m Explains None'
            # Phrase
            if show_detail and 'web' in content:
                print '\033[1;31m#  Phrase\033[0m'
                for i in range(0, len(content['web'])):
                    print '\033[1;31m# \033[0m', content['web'][i]['key'], ':', ' '.join(content['web'][i]['value'])
            # print '\033[1;31m################################### \033[0m'
            print

        elif code == 20:  # Text to long
            print 'WORD TO LONG'
        elif code == 30:  # Trans error
            print 'TRANSLATE ERROR'
        elif code == 40:  # Don't support this language
            print 'CAN\'T SUPPORT THIS LANGUAGE'
        elif code == 50:  # Key failed
            print 'KEY FAILED'
        elif code == 60:  # Don't have this word
            print 'DO\'T HAVE THIS WORD'


class DBHandler:

    db = None

    def __init__(self, name):
        self.db = sqlite3.connect(name)
        self.db.execute('''CREATE TABLE IF NOT EXISTS tbl_words
                           (word VARCHAR(64) PRIMARY KEY NOT NULL ,
                           explain TEXT NULL,
                           update_time DATETIME DEFAULT CURRENT_TIMESTAMP)
                        ''')

    def __del__(self):
        self.db.close()

    def save(self, word, explain):
        cur = self.db.cursor()
        cur.execute('INSERT OR IGNORE INTO tbl_words(word, explain) VALUES(?, ?)', (word, unicode(explain)))
        rs = cur.rowcount
        cur.close()
        self.db.commit()
        return rs

    def delete(self, word):
        cur = self.db.cursor()
        cur.execute('DELETE FROM tbl_words WHERE word=?', (word,))
        rs = cur.rowcount
        cur.close()
        self.db.commit()
        return rs

    def query(self, cond):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM tbl_words' + cond)
        rs = cur.fetchall()
        cur.close()
        return rs


if __name__ == '__main__':
    Dict()
