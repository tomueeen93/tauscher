# -*- coding: utf-8 -*-

import os
import config

class Tauscher(object):
    """
    This is main trader class.
    """
    def __init__(self, hoge='Hello', *args, **kwargs):
        self.hoge = hoge

    def say_hello(self):
        """
        test
        """
        print(self.hoge)
        return self.hoge

    def main(self):
        """
        this is main trader method
        """
        pass

if __name__ == '__main__':
    t = Tauscher()
    t.main()
