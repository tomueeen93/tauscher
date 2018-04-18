# -*- coding: utf-8 -*-

import unittest

import sys,os
sys.path.append(os.pardir)
sys.path.append(os.getcwd())

from tauscher.tauscher import Tauscher

class TestTauscher(unittest.TestCase):
    class_objects = None

    # テストクラスが初期化される際に一度だけ呼ばれる (python2.7以上)
    # @classmethod
    # def setUpClass(cls):
    #     if sys.flags.debug: print('> setUpClass method is called.')
    #     # テストの準備するための重い処理のメソッドを実行
    #     cls.CLS_VAL = '> setUpClass : initialized!'
    #     if sys.flags.debug: print(cls.CLS_VAL)

    def test_say_hello(self):
        t = Tauscher()
        self.assertEqual(t.say_hello(), 'Hello')


if __name__ == '__main__':
    unittest.main()
