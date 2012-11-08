import urllib2,urllib,cookielib

def LoginMop(user,pwd):
    cookie = cookielib.CookieJar()
    cookieProc = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookieProc)
    urllib2.install_opener(opener)
    
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.5(KHTML, like Gecko) Chrome/19.0.1084.56 Safari/536.5',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
            'Origin': 'http://www.mop.com',
            'Referer': 'http://www.mop.com/',
            'Content-Type': 'application/x-www-form-urlencoded'
            }

    post = {
        'user_name':user,
        'password':pwd
        }

    post = urllib.urlencode(post)

    req = urllib2.Request(
            url='http://passport.mop.com/Login?',
            data=post,
            headers=header
            )

    res = urllib2.urlopen(req).read();

    #print res.decode('utf-8')

    if 'waising' in res:
        print 'ok'
    else:
        print 'err'

    
if __name__=='__main__':
    LoginMop('waising','wangweixing')



