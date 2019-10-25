#!/usr/bin/env python
#def str2int(s):
#    def fn(x, y):
#        return x*10 + y
#    def char2num(s):
#        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
#    return reduce(fn, map(char2num, s))
#
#i = str2int('567')
#print '%10d'%i
#import functools
#def log(func):

class A(object):
    def __init__(self):
        self.a = 100
    def show(self):
        print "A.a = %d" % self.a


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print "B.a = %d" %self.a
        self.show()
        self.a = 1000
        print "B.a = %d" % self.a
        self.show()

if __name__ == "__main__":
    bb = B()
