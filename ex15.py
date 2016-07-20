#!/usr/bin/env 
# -- coding: utf-8 --

from sys import argv
#载入模块
script, filename = argv
#引入filename参数
txt = open(filename)
#打开文件并且赋值给txt函数
print "Here's your file %r:" % filename
#打印要读取的文件名称参数
print txt.read()
#打印txt函数内容
print "Type the filename again:"
#打印文字
file_again = raw_input("> ")
#是否继续打印，输入文件名称
txt_again = open(file_again)
#打开文件并赋值给txt_again
print txt_again.read()
#打印txt_again的内容