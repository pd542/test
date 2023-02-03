import requests
from bs4 import BeautifulSoup
from base64 import urlsafe_b64decode
import re
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

session = requests.session()
url="https://www.eahub.cn/member.php?mod=logging&action=login"
r=session.get(url)
print(r.text)
soup = BeautifulSoup(r.text, "html.parser")
formhash = soup.find_all('input')[1]['value']
loginhash = re.sub(r'loginhash=','',re.search(r'loginhash=[a-zA-Z0-9]+', r.text).group())
print(loginhash)

url="https://www.eahub.cn/member.php?mod=logging&action=login&loginsubmit=yes&loginhash="+loginhash+"&mobile=2&handlekey=loginform&inajax=1"
data={'formhash':formhash,
      'referer':'https://www.eahub.cn/?mobile=2',
      'fastloginfield':'username',
      'cookietime':'2592000',
      'username':'pd542',
      'password':'Pdl289020879',
      'questionid':0,
      'answer':''}
text_data="formhash="+formhash+"&referer=https%3A%2F%2Fwww.eahub.cn%2F%3Fmobile%3D2&fastloginfield=username&cookietime=2592000&username=pd542&password=Pdl289020879&questionid=0&answer="
requestJSONdata=str(data).replace("+", "%2B")
requestdata=requestJSONdata.encode("utf-8")
print(text_data)
head = {
'Host': 'www.eahub.cn',
'Connection': 'keep-alive',
'Accept': 'application/xml, text/xml, */*; q=0.01',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Mi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Origin': 'https://www.eahub.cn',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://www.eahub.cn/member.php?mod=logging&action=login',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

r=session.post(url,data=text_data,headers=head)
print(r.text)
