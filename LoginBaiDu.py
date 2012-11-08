import urllib2,urllib,cookielib,webbrowser

def LoginBaiDu(user,pwd):
    cookie = cookielib.CookieJar()
    cookieProc = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookieProc)
    urllib2.install_opener(opener)
    print 'sss'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2'}

    post = {
        'username':user,
        'password':pwd,
        'tpl':'mn',
        'u':'http://www.baidu.com/',
        'psp_tt':0,
        'mem_pass':'on'
        }

    post = urllib.urlencode(post)

    req = urllib2.Request(
            url='https://passport.baidu.com/?login',
            data=post,
            headers=header
            )

    res = urllib2.urlopen(req).read(500);

    if 'passCookie' in res:
        print 'ok'
    else:
        print 'err'

    #webbrowser.open(res)
    
if __name__=='__main__':
    LoginBaiDu('waising0204','')



