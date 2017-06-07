# dict

[![status](https://img.shields.io/pypi/status/dict-cli.svg)](https://pypi.python.org/pypi/dict-cli)
[![Build](https://img.shields.io/travis/wufeifei/dict.svg)](https://pypi.python.org/pypi/dict-cli)
[![Coverage](https://img.shields.io/coveralls/wufeifei/dict.svg)](https://coveralls.io/github/wufeifei/dict)
[![PyPi-Relase](https://img.shields.io/pypi/v/dict-cli.svg)](https://pypi.python.org/pypi/dict-cli)
[![GitHub-Relase](https://img.shields.io/github/release/wufeifei/dict.svg)](https://github.com/wufeifei/dict/releases)
[![Python-Versions](https://img.shields.io/pypi/pyversions/dict-cli.svg)](https://pypi.python.org/pypi/dict-cli)
[![License](https://img.shields.io/github/license/wufeifei/dict.svg)](https://github.com/wufeifei/dict/blob/master/LICENSE)

命令行下中英文翻译工具（Chinese and English translation tools in the command line）

[![asciicast](http://asciinema.org/a/123670.png?v=2)](http://asciinema.org/a/123670)


## 安装(Install)

```bash
sudo pip install dict-cli
```

## 用法(Usage)

#### 英译中(English To Chinese)
```bash
$ dict test
###################################
#  test 测试
#  (U: tɛst E: test)
#
#  n. 试验；检验
#  vt. 试验；测试
#  vi. 试验；测试
#  n. (Test)人名；(英)特斯特
#
#  Test : 测试
#          测验
#          检验
#  Test Drive : Test Drive
#                Test Drive
#                无限狂飙
#  Test Engineer : 测试员
#                   测试工程师
#                   软件测试工程师
###################################

$ dict I love you
###################################
#  I love you 我爱你
#
#
#  我爱你。
#
#  I love you : 我爱你
#                ILOVEYOU蠕虫
#                寻找伴郎
#  I really love you : 真的爱你
#                       其实很爱你
#                       我是真的爱你
#  I Do love you : 我是爱你的
#                   真的爱你
#                   爱你我该怎么办
###################################
```

#### 中译英(Chinese To English)

```bash
$ dict 测试
###################################
#  测试 test
#  (Pinyin: cè shì)
#
#  [试验] test
#  measurement
#
#  测试 : Test
#          test
#          TST test
#  集成测试 : Integration testing
#              Test d'intégration
#              통합 시험
#  ANOVA测试 : Gage R&amp;R
#             ANOVA gauge R&amp;R
###################################

$ dict 我爱你
###################################
#  我爱你 I love you
#  (Pinyin: wǒ ài nǐ)
#
#  I love you
#
#  我爱你 : I love you
#            Ich liebe dich
#            Wuh that I love you
#  我也爱你 : I Love You Too
#              And I Love You So
#              Ik ook van jou
#  我就爱你 : The Arrangement
#              gou couh gyaez mwngz muengh
#              I'll just be love you
###################################
```
