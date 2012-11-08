#-*- coding: utf-8 -*-
import datetime,codecs

dict = {}

for i in xrange(0,150):
    dict.setdefault("name"+str(i))
    dict["name"+str(i)]="name"

s=codecs.open(r'c:\\dict.txt','a', 'utf-8')
s.write(unicode("测试条数:".decode("utf-8")))
s.write(str(len(dict))+"\r\n")
s.write("带括号开始时间:".decode("utf-8"))
a=datetime.datetime.now()
s.write(str(a)+"\r\n")

for (d,x) in dict.items():
    print "key:"+d+",value:"+str(x)
s.write("带括号结束时间:".decode("utf-8"))
b=datetime.datetime.now()
s.write(str(b)+"\r\n")
s.write("时间间隔:".decode("utf-8"))
s.write(str(b-a)+"\r\n")

s.write("不带括号开始时间:".decode("utf-8"))
c=datetime.datetime.now()
s.write(str(c)+"\r\n")
for d,x in dict.items():
    print "key:"+d+",value:"+str(x)
s.write("不带括号结束时间:".decode("utf-8"))
d=datetime.datetime.now()
s.write(str(d)+"\r\n")
s.write("时间间隔:".decode("utf-8"))
s.write(str(d-c)+"\r\n")
s.write("\r\n")
s.close()


