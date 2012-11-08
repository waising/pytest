# -*- coding:utf-8 -*-
#中文问题没有好的解决方法
#python dict 练习 dict是json格式的数据 和javascript 中的访问基本一样
"""
dict.clear()	 删除字典中所有元素
dict.copy()	 返回字典(浅复制)的一个副本
dict.fromkeysc(seq,val=None)	 创建并返回一个新字典，以seq 中的元素做该字典的键，val 做该字典中所有键对应的初始值(如果不提供此值，则默认为None)
dict.get(key,default=None)	 对字典dict 中的键key,返回它对应的值value，如果字典中不存在此键，则返回default 的值(注意，参数default 的默认值为None)
dict.has_key(key)	 如果键(key)在字典中存在，返回True，否则返回False. 在Python2.2版本引入in 和not in 后，此方法几乎已废弃不用了，但仍提供一个 可工作的接口。
dict.items()	 返回一个包含字典中(键, 值)对元组的列表
dict.keys()	 返回一个包含字典中键的列表
dict.values()	 返回一个包含字典中所有值的列表
dict.iter()	 方法iteritems(), iterkeys(), itervalues()与它们对应的非迭代方法一样，不同的是它们返回一个迭代子，而不是一个列表。
dict.pop(key[, default])	 和方法get()相似，如果字典中key 键存在，删除并返回dict[key]，如果key 键不存在，且没有给出default 的值，引发KeyError 异常。
dict.setdefault(key,default=None)	 和方法set()相似，如果字典中不存在key 键，由dict[key]=default 为它赋值。
dict.setdefault(key,default=None)	 和方法set()相似，如果字典中不存在key 键，由dict[key]=default 为它赋值。
"""

#dict 以 key value的形式存在
dict = {
    "name" : "张三",
    "sex" : "男",
    "age" : 22,
    "address" : "北京市xx区xx路xx公司"
    }

#输出key对应的value值
print dict["name"]
print dict.get("name")

#遍历所有的key 和 value值 对应值
for d in dict:
    print "key:"+d+",value:"+str(dict[d])

#dict的keys 和values
print dict.keys() #输出['age', 'address', 'name', 'sex']
print dict.values() 

#dict 增删改
dict["phone"]="134xxxxxxxx" #添加一个值
print dict["phone"] # 134xxxxxxxx

print dict.pop("phone") # 删除 并返回删除的值 #134xxxxxxxx

del(dict["name"]) #删除一个值 直接删除
#print dict["name"] #报错

dict["sex"]="女" #修改一个key值
print dict["sex"] #女

#dict.clear() #清空所有的值
#print dict.keys() #空

#del dict #彻底删除 不存dict的结构
#print dict.keys() #报错

#判断key是否存在 
if "tel" in dict.keys():
    print "tel in dict"
else:
    print "tel not in dict"


#直接赋值给另一个dict
dict2 = dict.copy()
print dict2.keys()

#dict 有没有方法直接输出有多少key的函数？
