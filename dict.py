#!/usr/bin/env python

import sys
import json
import urllib
import urllib2


"""
dict - Chinese/English Translation
@author Feei(wufeifei@wufeifei.com)
@date   2013.12.09
"""


class Dict:
    key = '716426270'
    keyFrom = 'wufeifei'
    api = 'http://fanyi.youdao.com/openapi.do?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='
    content = None

    def __init__(self, argv):
        if len(argv) == 1:
            self.api = self.api + urllib.quote(argv[0])
            self.translate()
        else:
            print 'ERROR'

    def translate(self):
        content = urllib2.urlopen(self.api).read()
        self.content = json.loads(content)
        self.parse()

    def parse(self):
        code = self.content['errorCode']
        if code == 0:  # Success
            try:
                u = self.content['basic']['us-phonetic'] # English
                e = self.content['basic']['uk-phonetic']
            except KeyError:
                try:
                    c = self.content['basic']['phonetic'] # Chinese
                except KeyError:
                    c = 'None'
                u = 'None'
                e = 'None'

            try:
                explains = self.content['basic']['explains']
            except KeyError:
                explains = 'None'

            print '\033[1;31m################################### \033[0m'
            print '\033[1;31m# \033[0m', self.content['query'], self.content['translation'][0],
            if u != 'None':
                print '(U:', u, 'E:', e, ')'
            elif c != 'None':
                print '(Pinyin:', c, ')'
            else:
                print

            if explains != 'None':
                for i in range(0, len(explains)):
                    print '\033[1;31m# \033[0m', explains[i]
            else:
                print '\033[1;31m# \033[0m Explains None'
            print '\033[1;31m################################### \033[0m'
            # Phrase
            # for i in range(0, len(self.content['web'])):
            #     print self.content['web'][i]['key'], ':'
            #     for j in range(0, len(self.content['web'][i]['value'])):
            #         print self.content['web'][i]['value'][j]
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

if __name__ == '__main__':
    Dict(sys.argv[1:])
