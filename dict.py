# -*- coding:utf-8 -*-
#��������û�кõĽ������
#python dict ��ϰ dict��json��ʽ������ ��javascript �еķ��ʻ���һ��
"""
dict.clear()	 ɾ���ֵ�������Ԫ��
dict.copy()	 �����ֵ�(ǳ����)��һ������
dict.fromkeysc(seq,val=None)	 ����������һ�����ֵ䣬��seq �е�Ԫ�������ֵ�ļ���val �����ֵ������м���Ӧ�ĳ�ʼֵ(������ṩ��ֵ����Ĭ��ΪNone)
dict.get(key,default=None)	 ���ֵ�dict �еļ�key,��������Ӧ��ֵvalue������ֵ��в����ڴ˼����򷵻�default ��ֵ(ע�⣬����default ��Ĭ��ֵΪNone)
dict.has_key(key)	 �����(key)���ֵ��д��ڣ�����True�����򷵻�False. ��Python2.2�汾����in ��not in �󣬴˷��������ѷ��������ˣ������ṩһ�� �ɹ����Ľӿڡ�
dict.items()	 ����һ�������ֵ���(��, ֵ)��Ԫ����б�
dict.keys()	 ����һ�������ֵ��м����б�
dict.values()	 ����һ�������ֵ�������ֵ���б�
dict.iter()	 ����iteritems(), iterkeys(), itervalues()�����Ƕ�Ӧ�ķǵ�������һ������ͬ�������Ƿ���һ�������ӣ�������һ���б�
dict.pop(key[, default])	 �ͷ���get()���ƣ�����ֵ���key �����ڣ�ɾ��������dict[key]�����key �������ڣ���û�и���default ��ֵ������KeyError �쳣��
dict.setdefault(key,default=None)	 �ͷ���set()���ƣ�����ֵ��в�����key ������dict[key]=default Ϊ����ֵ��
dict.setdefault(key,default=None)	 �ͷ���set()���ƣ�����ֵ��в�����key ������dict[key]=default Ϊ����ֵ��
"""

#dict �� key value����ʽ����
dict = {
    "name" : "����",
    "sex" : "��",
    "age" : 22,
    "address" : "������xx��xx·xx��˾"
    }

#���key��Ӧ��valueֵ
print dict["name"]
print dict.get("name")

#�������е�key �� valueֵ ��Ӧֵ
for d in dict:
    print "key:"+d+",value:"+str(dict[d])

#dict��keys ��values
print dict.keys() #���['age', 'address', 'name', 'sex']
print dict.values() 

#dict ��ɾ��
dict["phone"]="134xxxxxxxx" #���һ��ֵ
print dict["phone"] # 134xxxxxxxx

print dict.pop("phone") # ɾ�� ������ɾ����ֵ #134xxxxxxxx

del(dict["name"]) #ɾ��һ��ֵ ֱ��ɾ��
#print dict["name"] #����

dict["sex"]="Ů" #�޸�һ��keyֵ
print dict["sex"] #Ů

#dict.clear() #������е�ֵ
#print dict.keys() #��

#del dict #����ɾ�� ����dict�Ľṹ
#print dict.keys() #����

#�ж�key�Ƿ���� 
if "tel" in dict.keys():
    print "tel in dict"
else:
    print "tel not in dict"


#ֱ�Ӹ�ֵ����һ��dict
dict2 = dict.copy()
print dict2.keys()

#dict ��û�з���ֱ������ж���key�ĺ�����
