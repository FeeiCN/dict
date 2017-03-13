## dict
> Linux命令行下翻译工具

## Install

```
wget https://raw.githubusercontent.com/wufeifei/dict/master/dict.py
sudo mv ./dict.py /usr/local/bin/dict
sudo chmod +x /usr/local/bin/dict
```

## Usage

#### English To Chinese

```
$ dict test
###################################
#  test 测试 (U: tɛst E: test )
#  n. 试验；检验
#  vt. 试验；测试
#  vi. 试验；测试
#  n. (Test)人名；(英)特斯特
###################################
```

```
$ dict I love you
################################### 
#  I love you 我爱你
# 
#  我爱你。
# 
#  I love you :  我爱你
#                ILOVEYOU蠕虫
#                寻找伴郎
#  I really love you :  真的爱你
#                       其实很爱你
#                       我是真的爱你
#  I Do love you :  我是爱你的
#                   真的爱你
#                   爱你我该怎么办
################################### 
```

#### Chinese To English
```
$ dict 测试
###################################
#  测试 test (Pinyin: cè shì )
#  [试验] test
#  measurement
###################################
```

```bash
$ dict 我爱你
################################### 
#  我爱你 I love you (Pinyin: wǒ ài nǐ )
# 
#  I love you
# 
#  我爱你 :  I love you
#            Ich liebe dich
#            Wuh that I love you
#  我也爱你 :  I Love You Too
#              And I Love You So
#              Ik ook van jou
#  我就爱你 :  The Arrangement
#              gou couh gyaez mwngz muengh
#              I'll just be love you
################################### 
```
