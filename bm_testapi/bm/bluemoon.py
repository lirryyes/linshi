from hashlib import md5
import requests
import execjs

class BluemoonWeb:
    def __init__(self, user, password):
        self.login(user, password)
    
    
    def login(self, user, password):
        password = password.encode(encoding='UTF-8')
        password = md5(password).hexdigest()
        plaintext = '{"account":"%s","password":"%s","rand":"8888"}' % (
            user, password)
        data = execjs.compile(
            open("bm/generateUrl.js", encoding='utf-8').read()).call('run', plaintext)
        valicode = requests.get(
            "http://angelapi.bluemoon.com.cn/portal-admin/js/valiCodeImg.jsp?0.1482404016800165"

        )
        res = requests.post(data['url'],

                            data=data['params'],

                            cookies=valicode.cookies,

                            headers={"Content-Type": "application/json"})
        self.res_data = res.json()
        self.cookies = dict(res.request._cookies)
        self.res_data['cookies'] = self.cookies 
        return self.res_data

    def getHttpsCookies(self):
        url = "https://angelapi.bluemoon.com.cn/bluemoonMana/mallcrm/hrOrg/org/hrOrgManage.jsp?token="
        cookies = self.getCookies(url,self.token)
        return cookies
    
    @classmethod
    def getCookies(cls,url,token):
        url = url + token
        headers = {'Cookie': 'JSESSIONID=C4B5D952FA5E44E76CE569CD4604747B'}
        cookie_res = requests.get(url)
        
        cookies = dict(cookie_res.cookies)
        return cookies
    
    @classmethod
    def getDict(cls):
        data = {
            "bluemoonMana": "https://angelapi.bluemoon.com.cn/bluemoonMana/mallcrm/hrOrg/org/hrOrgManage.jsp?token=",
            "bmcrm-crmbp": "https://tmallapi.bluemoon.com.cn/bmcrm-crmbp/crmbp/relation/businessRelation/relationIntegrate.jsp?token=",
            "portal-admin": "https://angelapi.bluemoon.com.cn/portal-admin//admin/user/userManager.jsp?token="
        }
        return data
