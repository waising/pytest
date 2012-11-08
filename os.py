# -*- coding:utf-8 -*-
import os

#os.listdir('c:\\') 显示目录下的所有文件和文件夹信息

if not os.path.exists('c:\\zzz'): #目录不存在则创建目录
    os.mkdir('c:\\zzz')

os.rmdir('c:\\zzz')#删除一个文件夹不能删除多级

if not os.path.exists('c:\\zz1z'):#目录存在则创建 可以创建多级目录
    os.makedirs('c:\\zz1z\\zzz')

os.removedirs('c:\\zz1z\\zzz') #删除多级文件夹

if os.path.exists('c:\\z'):
    os.rename('c:\\z','c:\\zzz')#更改文件夹名称

f=file('c:\\aa.txt','w')#创建一个空文件
f.close()

os.remove('c:\\aa.txt') #移除一个文件

for txt in os.walk('c:\\zz'):
    print txt
#('c:\\zz', ['dd'], ['aa.txt']) 输出此目录下的所有文件
#('c:\\zz\\dd', [], []) 子目录下的文件

#os.system('calc')#调用计算器


print os.path.abspath('dd')#返回文件夹的绝对路径
print os.path.basename('c:\\zz\\dd')#返回path中的文件名 最后一个\后的字符
print os.path.dirname('c:\\zz\\dd')#返回path中的文件夹 返回c:\zz \前面的字符
print os.path.getatime('c:\\zz') #文件或文件夹的最后访问时间 单位秒
print os.path.getmtime('c:\\zz')#文件或文件夹的最后修改时间
print os.path.getctime('c:\\zz')#文件或文件夹的创建时间
print os.path.getsize('c:\\zz\\aa.txt')#文件或文件夹的大小，若是文件夹返回0

if os.path.isabs('c:\\zz'):#返回是否是绝对路径
    print 'yes'
else:
    print 'no'

if os.path.isfile('c:\\zz\\aa.txt'):#返回是否是文件路径
    print 'yes'

if os.path.isdir('c:\\zz'):#返回是否是文件夹路径
    print 'yes'

if os.path.islink('c:\\zz\\aa.txt'):#是否为快捷方式 但是好像都是 NO
    print 'yes'
else:
    print 'no'

print os.path.join('c:\\zz\\dd','11')#拼接path print c:\zz\dd\11

print os.path.normcase('c:/zz/aa.txt')#转换路径中的间隔符 print c:\zz\aa.txt
print os.path.normpath('c:/.zzaa.txt')#转换路径为系统可识别的路径 print c:\.zzaa.txt
print os.path.realpath('zz')#转换路径为绝对路径

print os.path.split('c:\\zz\\aa.txt')#将路径分解为(文件夹,文件名)print ('c:\\zz', 'aa.txt')

print os.path.splitext('c:\\zz\\aa.txt')#将路径分解为(其余部分,.扩展名)，若文件名中没有扩展名，扩展名部分为空字符串print ('c:\\zz\\aa.txt')

print os.linesep#用于在文件中分隔行的字符串 print 空行
print os.sep#分隔文件路径名的字符串 print \
print os.pathsep#分隔文件路径的字符串 print ;
print os.curdir #当前工作目录的字符串名称 print .
print os.pardir #当前工作目录的 父目录的字符串名称..


