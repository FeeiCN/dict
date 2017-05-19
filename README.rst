dict
====

|status| |github-release| |pypi-release| |pyversion| |license| |star|

.. |status| image:: https://img.shields.io/pypi/status/dict-cli.svg
    :alt: Status
    :target: https://pypi.python.org/pypi/dict-cli

.. |github-release| image:: https://img.shields.io/github/release/wufeifei/dict.svg
    :alt: GitHub Release
    :target: https://github.com/wufeifei/dict/releases

.. |pypi-release| image:: https://img.shields.io/pypi/v/dict-cli.svg
    :alt: PyPI Release
    :target: https://pypi.python.org/pypi/dict-cli

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/dict-cli.svg
    :alt: PYVersion
    :target: https://pypi.python.org/pypi/dict-cli

.. |license| image:: https://img.shields.io/github/license/wufeifei/dict.svg
    :alt: License
    :target: https://github.com/wufeifei/dict/blob/master/LICENSE

.. |star| image:: https://img.shields.io/github/stars/wufeifei/dict.svg?style=social&label=Star
    :alt: Star
    :target: https://github.com/wufeifei/dict/stargazers


命令行下中英文翻译工具（Chinese and English translation tools in the command line）

安装(Install)
============

        [sudo] pip install dict-cli

用法(Usage)
===========

英译中(English To Chinese)
-------------------------

::

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

中译英(Chinese To English)
-------------------------

::

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

