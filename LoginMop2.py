# -*- coding:utf-8 -*-
import urllib2,urllib,cookielib

def LoginBaiDu(user,pwd):
    cookie = cookielib.CookieJar()
    cookieProc = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookieProc)
    urllib2.install_opener(opener)

    header = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5'}

    post = {
        'user_name':user,
        'password':pwd
        }

    post = urllib.urlencode(post)

    req = urllib2.Request(
            url='http://passport.mop.com/Login?url=http://www.mop.com',
            data=post,
            headers=header
            )
    try:
        res = urllib2.urlopen(req).read()
    except urllib2.HTTPError,error:
        res = error.read()
    
    print res.decode("utf-8")

    if 'waising' in res:
        print 'ok'
    else:
        print 'err'
    
if __name__=='__main__':
    LoginBaiDu('waising','wangweixing')



