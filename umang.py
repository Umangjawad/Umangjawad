#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To balochhacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
print "\x1b[1;91mExit"
os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
for e in z + '\n':
sys.stdout.write(e)
sys.stdout.flush()
time.sleep(0.01)

#Dev:baloch_hacker
##### LOGO #####
logo = """
\033[1;96m  UU          UU   MMM                  MMM  AAAAAAAAA  NNN                  NN         GGGGGG
\033[1;96m  UU          UU   MM   M            M   MM  AA             AA  NN   NN            NN      GG               GG
\033[1;96m  UU          UU   MM      M      M      MM  AA             AA  NN       NN        NN    GG
\033[1;96m  UU          UU   MM         MM         MM  AAAAAAAAA  NN           NN     NN   GG           GGGGGG
\033[1;96m  UU          UU   MM                         MM  AA             AA  NN              NN NN   GG           GG     GG
\033[1;96m  UUUUUUUU   MM                         MM  AA             AA  NN                    NN    GGGGGGGG     GG
\033[1;96m  MMM             M MM   UU           UU          SSSSSSSS  IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII   RRRRRRRRR            AAAAAAAAA
\033[1;96m  MM    M      M    MM   UU           UU        SS                                IIIII                RR              RR         AA              AA
\033[1;96m  MM       MM       MM   UU           UU        SSSSSSSSS                IIIII                RR             RR          AA              AA
\033[1;96m  MM                     MM   UU           UU                        SS                IIIII                RR RR R RR            AAAAAAAAAA
\033[1;96m  MM                     MM   UU           UU                        SS                IIIII                RR          RR            AA                AA
                      MM                     MM   UUUUUUUU        SSSSSSSS     IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII   RR             RR         AA                AA
                      ;' ·,       ,         GANOOK98         •98•   
         ;     '·, ,'·,  ' ·, 
         ',       ,'   ' ·,    ' ·, 
  , · " " ·,     :',       '·,      ' · ,          ,   ·  ' ; 
,"::' ·,::   ", ,':::' ,       ' · ,   ,  ,' ·  '            ; 
¦::                 ' ··,:::::':·,......  , ' 
",:::      ,":::::          ' ··,::,::,'_._._._._._._._._._', 
         ,"::::::          ´   , "      „ „",  ,"      „ „', 
        ,"::::                 ;     „"   ,"   ;     „"  ," 
        ;::::                   "„    ", "     ",  „ "„ " ; 
        ;:::       , "  "   "   "   "     „"·::::::::::::::"„- , 
        ;::      ,"                         "„·:::::::::::::·„" 
        ;::      ;                             "„·:::::::„" 
        ",::    ;         ,·'                       ", " 
          ",::   ",       '·,         ˆ ·,         ,·'    ,ˆ 
            ",::   ",                     ˆ · , ,' , · ˆ    ," 
            _",:::   ",_._._._._._._.      _._._ ," 
          ,'                             ,":::",          ', 
        ,'                            ,"::::::::",          ', 
       ,'                           ,' ",::::::::,",          ', 
      ,',.,. ,.,.,.,.,.,.,.,.,.,.,.,"   "::::"    ", 
         ,":::::                       ,":::",        º² "UMANG"
       ,":::                          ,"::::::",            ", 
      ,"::                          ,":::::::::",            ", 
     ,"::                          ,":::::::::::",            "
   |___'|.·´—    Umanghacker UmangJawad     -«•š
\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mUmangJawad\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•
\033[1;96m:•◈•╔╗─────────╔╗───────╔╗
\033[1;96m:•◈•║║─────────║║───────║║
\033[1;96m:•◈•║║╔══╦╗╔╦══╣╚═╦══╦══╣║╔╦══╦═╗
\033[1;96m:•◈•║║║╔╗║╚╝║║═╣╔╗║╔╗║╔═╣╚╝╣║═╣╔╝   
\033[1;96m:•◈•║╚╣╚╝╠╗╔╣║═╣║║║╔╗║╚═╣╔╗╣║═╣║    OF NOWSHERA PAKISTAN UMANG JAWAD HACKER
\033[1;96m:•◈•╚═╩══╝╚╝╚══╩╝╚╩╝╚╩══╩╝╚╩══╩╝
\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;94mUmangJawad\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"""

def tik():
titik = ['.   ','..  ','... ']
for o in titik:
print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;96m╔══╗╔╗──────╔╗─╔═╗╔═╗───╔═╗
\033[1;96m║╔╗║║║──────║║─║║╚╝║║───║╔╝
\033[1;96m║╚╝╚╣║╔══╦══╣║╔╣╔╗╔╗╠══╦╝╚╦╦══╗
\033[1;96m║╔═╗║║║╔╗║╔═╣╚╝╣║║║║║╔╗╠╗╔╬╣╔╗║ FROM NOWSHERA PAKISTAN
\033[1;96m║╚═╝║╚╣╔╗║╚═╣╔╗╣║║║║║╔╗║║║║║╔╗║
\033[1;96m╚═══╩═╩╝╚╩══╩╝╚╩╝╚╝╚╩╝╚╝╚╝╚╩╝╚╝
\033[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;93mUmangJawad\033[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"""
jalan("\033[1;96m----------------------//\\")
jalan("\033[1;96m---------------------// ¤ \\")
jalan("\033[1;96m---------------------\\ ¤ //")
jalan("\033[1;96m---------------------- \\//")
jalan("\033[1;96m-------------------- (___)")
jalan("\033[1;96m---------------------(___)")
jalan("\033[1;96m---------------------(___)")
jalan("\033[1;96m---------------------(___)_________")
jalan("\033[1;96m--------\_____/\__/----\__/\_____/")
jalan("\033[1;96m------------\ _°_[------------]_ _° /")
jalan("\033[1;96m----------------\_°_¤ ---- ¤_°_/")
jalan("\033[1;96m--------------------\ __°__ /")
jalan("\033[1;96m---------------------|\_°_/|")
jalan("\033[1;96m---------------------[|\_/|]")
jalan("\033[1;96m---------------------[|[¤]|]")
jalan("\033[1;96m---------------------[|;¤;|]")
jalan("\033[1;96m---------------------[;;¤;[]")
jalan("\033[1;96m--------------------;;;;¤][]\ ")
jalan("\033[1;96m-------------------;;;;;¤][]-\ ")
jalan("\033[1;96m------------------;;;;;[¤][]--\ ")
jalan("\033[1;96m-----------------;;;;;|[¤][]---\ ")
jalan("\033[1;96m----------------;;;;;[|[¤][]|---| ")
jalan("\033[1;96m---------------;;;;;[|[¤]|]|---| ")
jalan("\033[1;96m----------------;;;;[|[¤]|/---/ ")
jalan("\033[1;96m-----------------;;;[|[¤]/---/ ")
jalan("\033[1;96m------------------;;[|[¤/---/ ")
jalan("\033[1;96m-------------------;[|[/---/ ")
jalan("\033[1;96m--------------------[|/---/ ")
jalan("\033[1;96m---------------------/---/ ")
jalan("\033[1;96m--------------------/---/|] ")
jalan("\033[1;96m-------------------/---/]|];")
jalan("\033[1;96m------------------/---/¤]|];;")
jalan("\033[1;96m-----------------|---|[¤]|];;;")
jalan("\033[1;96m-----------------|---|[¤]|];;;")
jalan("\033[1;96m------------------\--|[¤]|];;")
jalan("\033[1;96m-------------------\-|[¤]|]; ")
jalan("\033[1;96m---------------------\|[¤]|] ")
jalan("\033[1;96m----------------------\\¤// ")
jalan("\033[1;96m-----------------------\|/ ")
jalan("\033[1;96m------------------------V ")                                     
jalan("\033[1;96m------------------------------------")
jalan("\033[1;96m╭━━━╮╱╱╱╱╱╭╮╱╱╱╱╭━╮╭━╮")
jalan("\033[1;96m┃╭━╮┃╱╱╱╱╱┃┃╱╱╱╱┃┃╰╯┃┃")
jalan("\033[1;96m┃╰━━┳━━┳┳━╯┣━━┳━┫╭╮╭╮┣━━┳━╮")
jalan("\033[1;96m╰━━╮┃╭╮┣┫╭╮┃┃━┫╭┫┃┃┃┃┃╭╮┃╭╮╮")
jalan("\033[1;96m┃╰━╯┃╰╯┃┃╰╯┃┃━┫┃┃┃┃┃┃┃╭╮┃┃┃┃")
jalan("\033[1;96m╰━━━┫╭━┻┻━━┻━━┻╯╰╯╰╯╰┻╯╰┻╯╰╯")
jalan("\033[1;96m╱╱╱╱┃┃")
jalan("\033[1;96m╱╱╱╱╰╯")
jalan('\033[1;93m              Welcome to UMANGJAWADHACKER')
print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;96mShabirBaloch\033[1;97m•◈•▬ ▬ ▬ ▬ ▬
