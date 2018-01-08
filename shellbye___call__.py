# -*- coding:utf-8 -*-
# Created by shellbye on 2018/1/8.(

class MyClass(object):
    def __call__(self, *args, **kwargs):
        print("been called!")


if __name__ == '__main__':
    my = MyClass()
    my()
    pass
