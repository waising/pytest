#-*- coding: utf-8 -*-
import datetime,codecs

dict = {}

for i in xrange(0,20000):
    dict.setdefault("name"+str(i))
    dict["name"+str(i)]="name"

s=codecs.open(r'c:\\dict.txt','a', 'utf-8')

def write(des):
    s.write(des.decode("utf-8"))

write("测试条数:")
write(str(len(dict))+"\r\n")
write("带括号开始时间:")
a=datetime.datetime.now()
s.write(str(a)+"\r\n")

for (d,x) in dict.items():
    print "key:"+d+",value:"+str(x)
write("带括号结束时间:")
b=datetime.datetime.now()
write(str(b)+"\r\n")
write("时间间隔:")
write(str(b-a)+"\r\n")

write("不带括号开始时间:")
c=datetime.datetime.now()
write(str(c)+"\r\n")
for d,x in dict.items():
    print "key:"+d+",value:"+str(x)
write("不带括号结束时间:")
d=datetime.datetime.now()
write(str(d)+"\r\n")
write("时间间隔:")
write(str(d-c)+"\r\n")
write("\r\n")
s.close()


