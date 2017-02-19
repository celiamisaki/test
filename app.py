
import ch
import random
import sys
import os
import re
import time
import json
import urllib
import traceback
import __future__
import shelve
from time import localtime, strftime
from urllib.request import urlopen
import urllib.request as urlreq
from urllib.request import urlopen
from xml.etree import cElementTree as ET
from urllib.request import unquote
from random import choice
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq
import re

################################
lockdown = False
activated = True
################################

def getUptime():
  """
 Returns the number of seconds since the programs started.
 """
  #do return startTime if you want the process start time

  return time.time() - startTime

################################
##File Stuff##

startTime = time.time()

pd = dict()
wordtodaytime = dict()
wife = dict()
ping = dict()
oco = dict()
family = dict()
pdf = dict()
waifu = dict()


########################################
########## BLACKLIST ###################

dictionary = dict()
f = open("definitions.txt", "r") # read-only
for line in f.readlines():
  try:
    if len(line.strip())>0:
      word, definition, name = json.loads(line.strip())
      dictionary[word] = json.dumps([definition, name])
  except:
    print("[ERROR]Cant load definition: %s" % line)
f.close()

########################################
########## BLACKLIST ###################

blacklist = dict()
try:
  f = open("blacklist.txt", "r")
  blacklist = eval(f.read())
  f.close()
except:pass

########################################
########## RANK ########################

developer = []
file = open("developer.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    developer.append(name.strip())
print("[INF]Loading Developer...")
file.close()

########################################

admin = []
file = open("admin.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    admin.append(name.strip())
print("[INF]Loading Admin...")
file.close()

########################################

mod = []
file = open("mod.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    mod.append(name.strip())
print("[INF]Loading Mod...")
file.close()

#######################################

assistant = []
file = open("assistant.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    assistant.append(name.strip())
print("[INF]Loading Assistant...")
file.close()

########################################


registered = []
file = open("registered.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    registered.append(name.strip())
print("[INF]Loading Registered...")
file.close()

########################################

blacklist = []
file = open("blacklist.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    blacklist.append(name.strip())
print("[INF]Loading Blacklist...")
file.close()

########################################

whitelist = []
file = open("whitelist.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    whitelist.append(name.strip())
print("[INF]Loading Whitelist...")
file.close()

########################################
############# STATUS ROOM ##############

rooms = []
file = open("rooms.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    rooms.append(name.strip())
print("[INF]Loading Rooms...")
file.close()

#########################################


lock = []
file = open("locks.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    lock.append(name.strip())
print("[INF]Loading lock...")
file.close()


unlock = []
file = open("unlock.txt", 'r')
for name in file.readlines():
  if len(name.strip()) > 0 :
    unlock.append(name.strip())
print("[INF]Loading unlock...")
file.close()

#########################################
########### SN Notifs ###################

sasaran = dict()
f = open ("notes.txt", "r") #read-only
print("[INF]Loading Notes...")
time.sleep(1)
for line in f.readlines():
  try:
    if len(line.strip())>0:
      to, body, sender = json.loads(line.strip())
      sasaran[to] = json.dumps([body, sender])
  except:
    print("[Error] Notes load fails : %s" % line)
f.close()

notif = []
f = open("notif.txt", "r")
print("[INF]Loading Notifs...")
for name in f.readlines():
  if len(name.strip())>0: notif.append(name.strip())
f.close

#########################################
################# NICK ##################

nicks=dict()
f=open ("nicks.txt","r")#r=read w=right
for line in f.readlines():#loop through eachlinimporte and read each line
    try:#try code
        if len(line.strip())>0:#strip the whitespace checkgreater than 0
            user , nick = json.loads(line.strip())
            nicks[user] = json.dumps(nick)
    except:
        print("[Error]Can't load nick %s" % line)
f.close()

def myanimelistanime(args):
  try:
    s = args.split(" ", 1)
    args = s[1]
    val = s[0]
    try:
      val = int(val)
    except:
      args = " ".join(s)
      val = 1
  except:
      args = args
      val = 1
  val = val - 1
  if val < 0:
    val = 0
    anime = mal.anime(args, 0, val)
  else: return "Anime: %s" % anime


def myanimelistanime(args):
  try:
    s = args.split(" ", 1)
    args = s[1]
    val = s[0]
    try:
      val = int(val)
    except:
      args = " ".join(s)
      val = 1
  except:
      args = args
      val = 1
  val = val - 1
  if val < 0:
    val = 0
  anime = mal.anime(args, 0, val)
  return anime

def sntonick(username):
    user = username.lower()
    if user in nicks:
        nick = json.loads(nicks[user])
        return nick
    else:
        return user

def pars(args):
  args=args.lower()
  if args in name:return name

def roompars(args):
  args = args.lower()
  if args in name:return name

########################################
############# GOOGLE ###################

def gis(cari):
  argss = cari
  args = argss.split()
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (x12; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("https://www.google.com.br/search?hl=en&authuser=0&site=imghp&tbm=isch&source=hp&biw=1366&bih=623&q=" + "+".join(args), headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','').replace('http://','gis:').replace('https://','gis:').replace('.jpg','.jpg:end').replace('.gif','.gif:end').replace('.png','.png:end')
  anjay = re.findall('<div class="rg_meta">(.*?)</div>', resp)
  setter = list()
  la = "".join(anjay)
  a = re.findall('"ou":"gis:(.*?):end","ow"', la)
  q = 1
  for result in a:
    if ".jpg" in result or ".gif" in result or ".png" in result:
     if "vignette" not in result and "mhcdn.net" not in result and "alicdn.com" not in result and "gambardanfoto.com" not in result and "squarespace.com" not in result and "polyvore.com" not in result and "wikia.nocookie" not in result and "blogspot.com" not in result and "wordpress.com" not in result and "minionnation.co.uk" not in result and "twimg.com" not in result and "ohmymag.com" not in result and "waterfrontcinema.co.uk" not in result and "funmobility.netdna-ssl.com" not in result and "images-amazon.com" not in result and "upload.wikimedia.org" not in result:
      setter.append('(%s) http://%s' % (q, result))
      q += 1
  return "<br/>"+"<br/>".join(setter[0:4])

def tube(args):
  search = args.split()
  url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&key=AIzaSyBSnh-sIjd97_FmQVzlyGbcaYXuSt_oh84" % "+".join(search))
  udict = url.read().decode('utf-8')
  data = json.loads(udict)
  rest = []
  for f in data["items"]:
    rest.append(f)

  d = random.choice(rest)
  link = "http://www.youtube.com/watch?v=" + d["id"]["videoId"]
  videoid = d["id"]["videoId"]
  title = d["snippet"]["title"]
  uploader = d["snippet"]["channelTitle"]
  descript = d["snippet"]['description']
  count    = d["snippet"]["publishedAt"]
  return "Resultado: %s <br/><br/><br/><br/><br/><br/><br/><br/><font color='#ffcc00'> %s </font><br/><font color='#ff0000'> Canal </font>:  %s <br/><font color='#ff0000'> Publicado em </font>: %s<br/><font color='#ff0000'> Descrição </font>:<i> %s ...</i><br/> " % (link, title, uploader, count, descript[:200])

def gs(args):
  args = args.split()
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (x12; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("https://www.google.com.br/search?q=" + "+".join(args), headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','').replace('http://','gs:').replace('https://','gs:')
  anjay = re.findall('<h3 class="r">(.*?)</h3>', resp)
  setter = list()
  la = "".join(anjay)
  a = re.findall('<a href="gs:(.*?)" onmousedown="(.*?)">(.*?)</a>', la)
  q = 1
  for link, fak, title in a:
      setter.append("<br/>(%s) %s : http://%s" % (q, title.capitalize(), link))
      q += 1
  return "".join(setter[0:4])

def rainbow(word):
    length = len(word)
    #set rgb values
    r = 255 #rgb value set to red by default
    g = 0
    b = 0
    sub = int(765/length)
    counter = 0
    string = ""
    for x in range(0, length):
        letter = word[counter]
        s = "<f x12%02X%02X%02X='0'>%s" % (r, g, b, letter)
        string = string+s
        counter+=1
        if (r == 255) and (g >= 0) and (b == 0): #if all red
            g = g+sub
            if g > 255: g = 255
        if (r > 0) and (g == 255) and (b == 0): #if some red and all green
            r = r-sub #reduce red to fade from yellow to green
            if r<0: r = 0 #if red gets lower than 0, set it back to 0
        if (r == 0) and (g == 255) and (b >= 0):
            b = b+sub
            if b>255:
                b = 255
                trans = True
        if (r == 0) and (g > 0) and (b == 255):
            g = g-sub
            if g<0: g = 0
        if (r >= 0) and (g == 0) and (b == 255):
            r = r+sub
            if r>255: r = 255
    return string


##End##
########################################

def serMaiden(args):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://animemaiden.net/?s="+"+".join(args.split())+"&post_type=anime", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  reichan = re.findall('<h3 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h3>', resp)
  setter = list()
  q = 1
  for link, title in reichan:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:5])

def lateMaiden():
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://animemaiden.net/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  reichan = re.findall('<h4 class="carousel-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h4>', resp)
  setter = list()
  q = 1
  for link, title in reichan:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:5])

def newMaiden(args):
  headers = {}
  headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
  req = urllib.request.Request("http://animemaiden.net/", headers = headers)
  resp = urllib.request.urlopen(req).read().decode("utf-8").replace('\n','').replace('\r','').replace('\t','')
  reichan = re.findall('<h3 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h3>', resp)
  setter = list()
  q = 1
  for link, title in reichan:
    setter.append('(<b>%s</b>). <b>%s</b>: %s' % (q, title, link))
    q += 1
  return "<br/>".join(setter[0:5])

#############################################################
##========================Variables========================##

botname = "RestiaBot" #Put your bot name here

botpassword = "bayu1997!" #Put your bot password here

cek_mods = dict() #Don't mess with this variable. This one is related with *mods command.

error = ("Expectation failed.")    #Error message

command_list = ['help','wl/register','uwl/unregister','bl/blacklist','chain','ubl/unblacklist','unchain','rank','setrank','pm','broadcast','say','reverse/rsay','find','multichat','ban','unban','join','leave','lock','unlock','rooms','save','mods','activate','restrict','lockdown','wake']

prefix = "-" ##You set the prefix here

##===========================End===========================##
#############################################################

#setting colors

class TestBot(ch.RoomManager):
  def onInit(self):
    self.setNameColor("808080")
    self.setFontColor("606060")
    self.setFontFace("Comic")
    self.setFontSize(12)
    self.enableBg()
    self.enableRecording()

  def saveAll(self):
    room = self._Room
    f = open("blacklist.txt", "w")
    f.write("\n".join(blacklist))
    f.close()
    f = open("developer.txt", "w")
    f.write("\n".join(developer))
    f.close()
    f = open("admin.txt", "w")
    f.write("\n".join(admin))
    f.close()
    f = open("mod.txt", "w")
    f.write("\n".join(mod))
    f.close()
    f = open("assistant.txt", "w")
    f.write("\n".join(assistant))
    f.close()
    f = open("registered.txt", "w")
    f.write("\n".join(registered))
    f.close()
    f = open("whitelist.txt", "w")
    f.close()
    f = open("rooms.txt", "w")
    f.write("\n".join(self.roomnames))
    f.close()


  def findUser(self, args):
          stuff = urllib.request.urlopen("http://" + args + ".chatango.com/").read().decode()
          if "buyer" in stuff:
                  return "<f x12FF0000='1'>%s <f x12='1'>é um Username." % args.title()
          elif "group" in stuff:
                  return "<f x12FF0000='1'> %s <f x1233FFFF='1'>é um chat, é o seu link interno é: <f x12FF0000='1'>%s" % (args.title(), ch.getServer(args))
          elif not "buyer" in stuff or not "group" in stuff:
                  return "%s isso existe?" % args.title()

  def getAccess(self, room, user):
    vroom = room
    if user.name in developer and not user.name in blacklist: return 6
    elif user.name in admin and not user.name in blacklist: return 5
    elif user.name in mod and not user.name in blacklist: return 4
    elif user.name in assistant and not user.name in blacklist: return 3
    elif user.name in registered and not user.name in blacklist and not room.name in lock : return 2
    elif user.name not in whitelist and not user.name in blacklist and not room.name in lock : return 1
    elif user.name in blacklist: return -1
    else: return 0

  def roomUsers():
      usrs = []
      gay = []
      prop = 0
      prop = prop + len(room._userlist) - 1
      for i in room._userlist:
        i = str(i)
        usrs.append(i)
      while prop >= 0:
        j = usrs[prop].replace("<User: ", "")
        i = j.replace(">", "")
        gay.append(i)
        prop = prop - 1
      return gay

  def getParticipant(arg):
      rname = self.getRoom(arg)
      usrs = []
      gay = []
      finale = []
      prop = 0
      prop = prop + len(rname._userlist) - 1
      for i in rname._userlist:
        i = str(i)
        usrs.append(i)
      while prop >= 0:
        j = usrs[prop].replace("<User: ", "")
        i = j.replace(">", "")
        gay.append(i)
        prop = prop - 1
      for j in gay:
        if j not in finale:
          finale.append(j)
      return finale

  def pars(args):
    args=args.lower()
    for name in room.usernames:
      if args in name:return name

  def roompars(args):
    args = args.lower()
    for name in self.roomnames:
      if args in name:return name
#############################################
##connecting and disconnecting crap##

  def onConnect(self, room):
    print("[+] Mad Hatter Connected to "+room.name)
    for i in cek_mods: #Di onJoin
      if len(cek_mods[i]) > 1:
        rmm, rmd = json.loads(cek_mods[i])
        self.getRoom(rmm).message("<br/>||<font color='#87ceeb'>OWNER</font>: "+ (self.getRoom(rmd).ownername) +" <br/>||Mods: "+", ".join(self.getRoom(rmd).modnames), True)
        self.leaveRoom(rmd)
        cek_mods.pop(i)
      return

  def onReconnect(self, room):
    print("[+] Mad Hatter Reconnected to "+room.name)

  def onDisconnect(self, room):
    print("[+] Mad Hatter Disconnected from "+room.name)

  def onBan(self, room, user, target):
    print(user.name+" got banned in "+room.name)


  def onConnectFail(self, room):
    print("[ERR] Room Not Found")
    for i in cek_mods: #Di onJoin
      if len(cek_mods[i]) > 1:
        rmm, rmd = json.loads(cek_mods[i])
        self.getRoom(rmm).message("room tidak tersedia")
        cek_mods.pop(i)
      return



##End##
#############################################

#############################################
##setting up commands##

  def onMessage(self, room, user, message):
   try:
    if user == self.user:
        return
    global activated
    global lockdown
    global lock
    global developer
    global admin
    global mod
    global assistant
    try:
      if room.getLevel(self.user) > 0:
        print("[%s]- [MSG] - [Rank %s] - [%s] - [%s] - [%s: %s]" % (time.strftime("%d/%m/%y- %H:%M:%S", time.localtime(time.time())), self.getAccess(room, user), room.name, message.ip, user.name.title(), message.body))
      else:
        print("[%s]- [MSG] - [Rank %s] - [%s] - [User_IP: Null] %s: %s" % (time.strftime("%d/%m/%y- %H:%M:%S", time.localtime(time.time())), self.getAccess(room, user), room.name, user.name.title(), message.body))
    except:
      pass

########################################################################### MSG NOTIFICAÇÃO #####################################################################################

    if user.name in notif and user.name in sasaran:
      room.message("<br/>Olá <f x12FF0000='1'> "+user.name+"   <f x1233FFFF='1'> você possui uma mensagem não lida em minha [<f x12FF0000='0'>C<f x12FF2F00='0'>A<f x12FF5E00='0'>I<f x12FF8D00='0'>X<f x12FFBC00='0'>A<f x12FFEB00='0'> <f x12D0FF00='0'>D<f x12A1FF00='0'>E<f x1272FF00='0'> <f x1243FF00='0'>E<f x1214FF00='0'>N<f x1200FF2F='0'>T<f x1200FF5E='0'>R<f x1200FF8D='0'>A<f x1200FFBC='0'>D<f x1200FFEB='0'>A <f x1233FFFF='1'>] para ler sua mensagem digite -rn", True)
      notif.remove(user.name)

##################################################################################################################################################################################

    if "test" in message.body:
      room.message (random.choice(["ya, test diterima oleh Restiabot! "+"@"+sntonick(user.name)+ " :D "]),True)
    if "konichiwa" in message.body:
      room.message (random.choice(["Konnichiwa "+sntonick(user.name)+ " -sama ^o^"]),True)
    if "konbanwa" in message.body:
      room.message (random.choice(["konbanwa"+sntonick(user.name)+ " -sama ^o^"]),True)
    if "bye" in message.body:
            room.message (random.choice(["Sayonara Matta Ashitee! "+"@"+sntonick(user.name)+ ""]),True)
    if "back" in message.body:
      if user.name in "0zx":
        room.message("%s" % " Tadaima anata <3 :*")
      else:
        room.message("Tadaima "+sntonick(user.name)+" ! :)", True)
    if "laper" in message.body or "Laper" in message.body:
      room.message(random.choice(["*Lempar soyjoy ke <b>%s</b>*" % sntonick(user.name),"*Lempar Snickers ke <b>%s</b>*" % sntonick(user.name)]), True)
    if "oppai" in message.body:
        room.message("*Boing - Boing*")
    if message.body.startswith("ngantuk") or "ngantuk" in message.body:
        room.message("Tidur lah !! >_>")
    if "tadaima" in message.body:
        room.message(random.choice(["Wellcome home ! :)","Okaerinasai ! ^o^","Wokaerinasai !!!!"]))
    if "oyasumi" in message.body or "oyasuminasai" in message.body:
        if user.name in "0zx":
         room.message("Oyasuminasai Anata :* ^o^ ")
    if "ohayo" in message.body or "ohayou" in message.body:
        room.message(random.choice(["ohayou minasan :D","oha senpai :x","ohayou"+sntonick(user.name)+ " ^o^"]))
        if user.name in "0zx":
         room.message("Ohayo Anata <3 ^o^")
    if "sepi" in message.body:
      room.message("Restia Disini untukmu :x :x ")
    if "cium" in message.body or "kiss" in message.body:
      room.message("nih :x , http://media.giphy.com/media/X3ndlrK6rOCt2/giphy.gif")
    if "tsundere" in message.body:
      room.message("Nani??, http://i173.photobucket.com/albums/w77/omghaet/Index/Biri-Biri.png  @"+ user.name+".")
    if "yandere" in message.body:
      room.message("Yes!, I'm here, http://vignette2.wikia.nocookie.net/futurediary/images/a/a5/YunoYandereFace.jpg/revision/latest?cb=20120128011750  @"+ user.name+".")
    if "kata bijak" in message.body:
      room.message(random.choice(["jangan lah berhenti bermimpi karena mimpi bisa itu suatu saat akan menjadi nyata.",
          "berani ambil resiko, kita tidak akan pernah tau apa yang akan terjadi.",
          "jangan pernah lupa dengan orang yang selalu mendukung mu dari belakang.",
          "jangan pernah sekali-kali sombong, karena di atas langit masih ada langit.",
          "To true friendship, how long you've known each other means nothing.",
          "You want weapons? We??re in a library! Books! The best weapons in the world!",
          "mulut lebih tajam dari benda apapun kalu kita salah menggunakan nya.",
          "Dividing an impossibly large task into smaller solvable problems is a programmer??s job.",
          "dunia ini penuh dengan melodi dan harmoni, jangan sekali2 merusak nya dengan keluhan anda :)",
          "Hold hands. That's what you're meant to do. Keep doing that... and don't let go.",
          "cintailah orang yang mencintai anda juga?",
          "jangan pernah malah olahraga",
          "Don't worry if plan A fails, there are 25 more letters in the alphabet.",
          "Life doesn't have any hands, but it can sure give you a slap sometimes.",
          "lihat ke belakang, sewaktu2 jika anda tidak sedang sibuk",
          "Belajar ketika orang lain tidur, bekerja ketika orang lain bermalasan, dan bermimpi ketika orang lain berharap.",
          "Pain has deep roots. The only way to dig it out is to forgive...",
          "Love,after all,always said more about those who felt it then it did about the ones they love.",
          "Memories are funny things.Sometimes they're real ,but other times they change into what we went them to be.",
          "The moment of impact. The moment of impact proves potential for change. Has ripples effects far beyond what we can predict."]))
    if "quotes" in message.body:
      room.message(random.choice(["jangan lah berhenti bermimpi karena mimpi bisa itu suatu saat akan menjadi nyata.",
          "berani ambil resiko, kita tidak akan pernah tau apa yang akan terjadi.",
          "jangan pernah lupa dengan orang yang selalu mendukung mu dari belakang.",
          "jangan pernah sekali-kali sombong, karena di atas langit masih ada langit.",
          "To true friendship, how long you've known each other means nothing.",
          "You want weapons? We??re in a library! Books! The best weapons in the world!",
          "mulut lebih tajam dari benda apapun kalu kita salah menggunakan nya.",
          "Dividing an impossibly large task into smaller solvable problems is a programmer??s job.",
          "dunia ini penuh dengan melodi dan harmoni, jangan sekali2 merusak nya dengan keluhan anda :)",
          "Hold hands. That's what you're meant to do. Keep doing that... and don't let go.",
          "cintailah orang yang mencintai anda juga?",
          "jangan pernah malah olahraga",
          "Don't worry if plan A fails, there are 25 more letters in the alphabet.",
          "Life doesn't have any hands, but it can sure give you a slap sometimes.",
          "lihat ke belakang, sewaktu2 jika anda tidak sedang sibuk",
          "Belajar ketika orang lain tidur, bekerja ketika orang lain bermalasan, dan bermimpi ketika orang lain berharap.",
          "Pain has deep roots. The only way to dig it out is to forgive...",
          "Love,after all,always said more about those who felt it then it did about the ones they love.",
          "Memories are funny things.Sometimes they're real ,but other times they change into what we went them to be.",
          "The moment of impact. The moment of impact proves potential for change. Has ripples effects far beyond what we can predict."]))

    if user.name.startswith("#") or user.name.startswith("!"):return
    if self.user == user: return
    if user.name in blacklist: return
    if self.getAccess(room, user) > 0:
      if not activated and self.getAccess(room, user) > 1: return #return, if not activated and user rank is less than 4.
      if "restia" == message.body.lower() or  "restia" in message.body.lower() :
        rank = self.getAccess(room, user)
        if rank == 1:
           room.message(random.choice(["%s" % "Watashi wa koko ni imasu? "+sntonick(user.name) ,"Restia disini:D "+sntonick(user.name),"Mōshiwakearimasenga, watashi wa isogashī ndesu "+sntonick(user.name)]), True)
        if rank == 2:
           room.message(random.choice(["%s" % "Watashi wa koko ni imasu? "+sntonick(user.name) ,"Restia disini:D "+sntonick(user.name),"Mōshiwakearimasenga, watashi wa isogashī ndesu "+sntonick(user.name)]), True)
        if rank == 3:
           room.message(random.choice(["%s" % "Watashi wa koko ni imasu? "+sntonick(user.name) ,"Restia disini:D "+sntonick(user.name),"Mōshiwakearimasenga, watashi wa isogashī ndesu "+sntonick(user.name)]), True)
        if rank == 4:
           room.message(random.choice(["%s" % "Watashi wa koko ni imasu? "+sntonick(user.name) ,"Restia disini:D "+sntonick(user.name),"Mōshiwakearimasenga, watashi wa isogashī ndesu "+sntonick(user.name)]), True)
        if rank == 5:
           room.message(random.choice(["%s" % "Watashi wa koko ni imasu? "+sntonick(user.name) ,"Restia disini:D "+sntonick(user.name),"Mōshiwakearimasenga, watashi wa isogashī ndesu "+sntonick(user.name)]), True)
        if rank == 6:
          room.message("Nani mo shien suru koto ga dekimasendeshita ?? "+sntonick(user.name)+"-sama", True)
      if "afk" in message.body.lower() or "Afk"== message.body.lower():
        rank = self.getAccess(room, user)
        if rank == 1:
           room.message(random.choice(["%s" % "Mata ashitane :D "+sntonick(user.name) ,"Sayonara >< "+sntonick(user.name)+"@","Balik lagi ya :( "+sntonick(user.name)+"?"]), True)
        if rank == 2:
           room.message(random.choice(["%s" % "Mata ashitane :D "+sntonick(user.name) ,"Sayonara >< "+sntonick(user.name)+"@","Balik lagi ya :( "+sntonick(user.name)+"?"]), True)
        if rank == 3:
           room.message(random.choice(["%s" % "Mata ashitane :D "+sntonick(user.name) ,"Sayonara >< "+sntonick(user.name)+"@","Balik lagi ya :( "+sntonick(user.name)+"?"]), True)
        if rank == 4:
           room.message(random.choice(["%s" % "Mata ashitane :D "+sntonick(user.name) ,"Sayonara >< "+sntonick(user.name)+"@","Balik lagi ya :( "+sntonick(user.name)+"?"]), True)
        if rank == 5:
           room.message(random.choice(["%s" % "Mata ashitane :D "+sntonick(user.name) ,"Sayonara >< "+sntonick(user.name)+"@","Balik lagi ya :( "+sntonick(user.name)+"?"]), True)
        if rank == 6:
          room.message("Sayōnara :D ,Mata ashitane "+sntonick(user.name)+"-sama Ōku o yaburimasu :* ", True)
      if "offline" == message.body.lower() or "off" in message.body or "Off" == message.body.lower():
        rank = self.getAccess(room, user)
        if rank == 2:
           room.message(random.choice(["%s" % "Sampai nanti lagi "+sntonick(user.name) ,"See you "+sntonick(user.name)+"?","Sayonara "+sntonick(user.name)+"@"]), True)
        if rank == 3:
           room.message(random.choice(["%s" % "Sampai nanti lagi "+sntonick(user.name) ,"See you "+sntonick(user.name)+"?","Sayonara "+sntonick(user.name)+"@"]), True)
        if rank == 4:
           room.message(random.choice(["%s" % "Sampai nanti lagi "+sntonick(user.name) ,"See you "+sntonick(user.name)+"?","Sayonara "+sntonick(user.name)+"@"]), True)
        if rank == 5:
           room.message(random.choice(["%s" % "Sampai nanti lagi "+sntonick(user.name) ,"See you "+sntonick(user.name)+"?","Sayonara "+sntonick(user.name)+"@"]), True)
        if rank == 6:
          room.message("Atode mōichido suru made <3 "+sntonick(user.name)+"-sama", True)
         
    ##Commands | You design great commands for your bot in this part
    if message.body[0] == "." or message.body[0] == "" or message.body[0] == "" : #prefix usage in this line (for this case I use "*" as prefix)
        data = message.body[1:].split(" ", 1) #This part splits message body into [0]prefix and [1:]data ([1:] <- this means the message body's second character and after) and data will be split into 2 (cmd(data[0]), args(data[1])) which is very usefull. (Many thanks to TryHardHusky)
        if len(data) == 2: #If there are more than 1 data (This is where we will get args)
          cmd, args = data[0], data[1] #the first data (data[0]) will be the cmd (specified command) and the next data will be args (it doesn't matter how many word next to the cmd, It'd eventually be args)
        else: #If there is only 1 data (No args)
          cmd, args = data[0], "" #the arg will simply be "" (Empty)
        cmd == cmd.lower()

######################################################################################################################################################
#################################################################### SN/RN MESSAGE ######################################################################


        if cmd == "sn" and len(args)  and self.getAccess(room, user) >= 2:
          try:
            to, body = args.split(" ", 1)
            sender = user.name
            if to in developer or to in admin or to in assistant or to in whitelist or to in registered:
              sasaran[to] = json.dumps([body, sender])
              room.message("[MSG]terkirim send of 1 second ago")
              notif.append(to)
            else: room.message("sumimasen <f x11FF0000='1'>"+to+"<f x1133FFFF='1'> anata bukan  ,user terdaftar.", True)
            #if user.name : room.message( kamu dapat sn dari .... silahkan gunakan cmd 'sn read ) kek gitu aja
          except: room.message("error !!")

        if cmd == "rn" and self.getAccess(room, user) >= 2:
          try:
            if user.name in sasaran:
              body, sender = json.loads(sasaran[user.name])
              room.message(" <br/><br/><br/>[<f x12FF0000='0'>C<f x12FF2F00='0'>A<f x12FF5E00='0'>I<f x12FF8D00='0'>X<f x12FFBC00='0'>A<f x12FFEB00='0'> <f x12D0FF00='0'>D<f x12A1FF00='0'>E<f x1272FF00='0'> <f x1243FF00='0'>E<f x1214FF00='0'>N<f x1200FF2F='0'>T<f x1200FF5E='0'>R<f x1200FF8D='0'>A<f x1200FFBC='0'>D<f x1200FFEB='0'>A <f x1233FFFF='1'>] <br/> <f x1233FFFF='1'>Username : <f x12FF0000='1'>"+user.name+"<br/>  <f x1233FFFF='1'>Remetente : <f x12FF0000='1'>"+sender+"<br/>  <f x1233FFFF='1'>Mensagem : <f x12FFCC00='1'>"+body, True)
              del sasaran[user.name]
              notif.remove(to)
          except: return
          else: room.message("<f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'> tidak ada pesan masuk :|", True)

######################################################################################################################################################
############################################################### UNLOCK/LOCK BOT ######################################################################

        if cmd == "lock"and self.getAccess(room, user) >= 4:
          self.getRoom("tanpaid-chat")
          if args in lock:
            room.message("Rooms is <f x11FF0000='1'> [locked] ", True)
            return
          if args in self.roomnames:
            if self.getAccess(room, user) > 0: 
              lock.append(args)
              room.message("tidak bisa chat <f x11FF0000='1'> %s   <f x1133FFFF='1'> karena <f x11FF0000='1'> room [locked] " % args, True)
            else:room.message("sumimasen kamu bukan moderator di sini :|")
          if args == "":
            if room.name in lock:
              room.message("Este chat já está <f x11FF0000='1'> [TRANCADO] ", True)
              return
            lock.append(room.name)
            room.message("done Rooms  <f x11FF0000='1'> %s   <f x1133FFFF='1'> is <f x11FF0000='1'> [LOCKED] " % room.name, True)
          if args not in self.roomnames:
            if args == "": return
            room.message("sumimasen kamu bukan moderator di sini :| <f x11FF0000='1'> %s ."% args, True)
            return


        if cmd == "unlock" and self.getAccess(room, user) >= 4:
          self.getRoom("tanpaid-chat")
          if args in self.roomnames:
            if args in lock:
              if self.getAccess(room, user) > 0:
                lock.remove(args)
                room.message("room chat <f x11FF0000='1'> %s   <f x1133FFFF='1'> is <f x1133FF33='1'> [unlock] " % args, True)
              else: room.message("*warning*  Anda tidak diizinkan untuk melakukan akses ini. *warning* ")
            else:
              room.message("chatting ini sudah <f x1133FF33='1'> [inlock] ", True)
              return
          if args == "":
            if room.name in lock:
              lock.remove(room.name)
              self.getRoom("tanpaid-chat").message("<f x1133FFFF='1'><br/><br/>[<f x11FF0000='0'>S<f x11FF4C00='0'>T<f x11FF9800='0'>A<f x11FFE400='0'>T<f x11B3FF00='0'>U<f x1167FF00='0'>S<f x11BFF00='0'> <f x1100FF4C='0'>C<f x1100FF98='0'>M<f x1100FFE4='0'>D<f x1133FFFF='1'>]<f x1133FFFF='1'><br/><br/><br/><b>Username</b>: <f x11FF0000='1'>%s <f x1133FFFF='1'><br/><b>Chat</b>: <f x11FF0000='1'>%s  <f x1133FFFF='1'><br/><b>Comando</b>: <f x11FF0000='1'>%s <f x1133FFFF='1'><br/><b>IP</b>: <f x11FF0000='1'>%s" % (user.name, room.name, cmd, message.ip), True)    
            else:
              room.message("done Rooms <f x11FF0000='1'> %s   <f x1133FFFF='1'> is <f x1133FF33='1'> [UNLOCK] " % args, True)
              return
          if args not in self.roomnames:
            if args == "": return
            room.message("maaf kamu bukan mod :) <f x11FF0000='1'> %s ."% args, True)
            return

######################################################################################################################################################
########################################################### BOT HABILITADO / DESABILITADO ############################################################

        if cmd == "sleep" and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 0:
          if lockdown: return
          room.message(" <f x1133FFFF='1'> Restia Mau <f x11FF0000='1'> [Tidur]  ", True)
          self.getRoom("tanpaid-chat").message("<f x1233FFFF='1'><br/><br/>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>S<f x12FFA200='0'>T<f x12FFD800='0'>A<f x12C9FF00='0'>T<f x1293FF00='0'>U<f x125DFF00='0'>S<f x1227FF00='0'> <f x1200FF36='0'>C<f x1200FF6C='0'>M<f x1200FFA2='0'>D<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>]<f x1233FFFF='1'><br/><br/><br/>Username: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>Chat: <f x12FF0000='1'>%s  <f x1233FFFF='1'><br/>Comando: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>IP: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, message.ip), True)
          lockdown = True

        if cmd == "wakeup" and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 0:
           if not lockdown: return
           room.message("<f x1133FFFF='1'> Restia sudah <f x1133FF33='1'> [Bangun] ", True)
           self.getRoom("tanpaid-chat").message("<f x1233FFFF='1'><br/><br/>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>S<f x12FFA200='0'>T<f x12FFD800='0'>A<f x12C9FF00='0'>T<f x1293FF00='0'>U<f x125DFF00='0'>S<f x1227FF00='0'> <f x1200FF36='0'>C<f x1200FF6C='0'>M<f x1200FFA2='0'>D<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>]<f x1233FFFF='1'><br/><br/><br/>Username: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>Chat: <f x12FF0000='1'>%s  <f x1233FFFF='1'><br/>Comando: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>IP: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, message.ip), True)
           lockdown = False

######################################################################################################################################################
############################################### DELISGAR BOT #########################################################################################

        if cmd == "shutdown" and self.getAccess(room, user) >= 6:
            self.saveAll()
            room.message("Bye *waves*")
            self.setTimeout(3, self.stop, )

        if cmd == "sma": room.message(serMaiden(args), True)

        if cmd == "lma": room.message(lateMaiden(), True)

        if cmd == "nma": room.message(newMaiden(args), True)

######################################################################################################################################################
######################################################### REGISTRO  BOT ##############################################################################


        elif cmd == "wl":
          if args == "":
             rank = self.getAccess(room, user)
             if rank == 1:
                registered.append(user.name)
                self.getRoom("tanpaid-chat").message("<f x1233FFFF='1'><br/><br/>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>S<f x12FFA200='0'>T<f x12FFD800='0'>A<f x12C9FF00='0'>T<f x1293FF00='0'>U<f x125DFF00='0'>S<f x1227FF00='0'> <f x1200FF36='0'>C<f x1200FF6C='0'>M<f x1200FFA2='0'>D<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>]<f x1233FFFF='1'><br/><br/><br/>Username: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>Chat: <f x12FF0000='1'>%s  <f x1233FFFF='1'><br/>Comando: <f x12FF0000='1'>%s - %s  <f x1233FFFF='1'><br/>IP: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, user.name, message.ip), True)
                room.message(user.name+" selamat anda sudah terdaftar gunakan *cmds ", True)
             if rank == 2:
                room.message(user.name+" anda sudah terdaftar gunakan *cmds ", True)
          else:
              rank = self.getAccess(room, ch.User(args))
              if rank == 1:
                 registered.append(args)
                 self.getRoom("tanpaid-chat").message("<f x1233FFFF='1'><br/><br/>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>S<f x12FFA200='0'>T<f x12FFD800='0'>A<f x12C9FF00='0'>T<f x1293FF00='0'>U<f x125DFF00='0'>S<f x1227FF00='0'> <f x1200FF36='0'>C<f x1200FF6C='0'>M<f x1200FFA2='0'>D<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>]<f x1233FFFF='1'><br/><br/><br/>Username: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>Chat: <f x12FF0000='1'>%s  <f x1233FFFF='1'><br/>Comando: <f x12FF0000='1'>%s - %s  <f x1233FFFF='1'><br/>IP: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, args, message.ip), True)
                 room.message(args+" Selamat anda sudah terdaftar gunakan *cmds ", True)
              if rank == 2:
                 room.message(args+" Anda sudah terdaftar gunakan *cmds ", True)

        elif cmd == "uwl":
          if args == "":
             rank = self.getAccess(room, user)
             if rank == 2:
                registered.remove(user.name)
                self.getRoom("tanpaid-chat").message("<f x1233FFFF='1'><br/><br/>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>S<f x12FFA200='0'>T<f x12FFD800='0'>A<f x12C9FF00='0'>T<f x1293FF00='0'>U<f x125DFF00='0'>S<f x1227FF00='0'> <f x1200FF36='0'>C<f x1200FF6C='0'>M<f x1200FFA2='0'>D<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>]<f x1233FFFF='1'><br/><br/><br/>Username: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>Chat: <f x12FF0000='1'>%s  <f x1233FFFF='1'><br/>Comando: <f x12FF0000='1'>%s - %s  <f x1233FFFF='1'><br/>IP: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, user.name, message.ip), True)
                room.message(user.name+" Anda telah dihapus dari daftar pengguna terdaftar.", True)
             if rank == 1:
                room.message(user.name+" Anda telah dihapus dari daftar pengguna.", True)
          else:
              rank = self.getAccess(room, ch.User(args))
              if rank == 2:
                 registered.remove(args)
                 self.getRoom("tanpaid-chat").message("<f x1233FFFF='1'><br/><br/>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>S<f x12FFA200='0'>T<f x12FFD800='0'>A<f x12C9FF00='0'>T<f x1293FF00='0'>U<f x125DFF00='0'>S<f x1227FF00='0'> <f x1200FF36='0'>C<f x1200FF6C='0'>M<f x1200FFA2='0'>D<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>]<f x1233FFFF='1'><br/><br/><br/>Username: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>Chat: <f x12FF0000='1'>%s  <f x1233FFFF='1'><br/>Comando: <f x12FF0000='1'>%s - %s  <f x1233FFFF='1'><br/>IP: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, args, message.ip), True)
                 room.message(args+" dihapus dari daftar pengguna terdaftar.", True)
              if rank == 1:
                 room.message(args+" dihapus dari daftar pengguna.", True)

  
######################################################################################################################################################
########################################################## DEFINITION ######################################################################################

        elif cmd == "define" or cmd == "df" and len(args) and self.getAccess(room, user) >= 2:
           try:
             try:
               word, definition = args.split(" as ",1)
               word = word.lower()
             except:
               word = args
               definition = ""
             if len(word.split()) > 4:
               room.message("Gagal")
               return
             elif len(definition) > 0:
               if word in dictionary:
                 room.message("%s defined already" % user.name.capitalize())
               else:
                 dictionary[word] = json.dumps([definition, user.name])
                 f =open("definitions.txt", "w")
                 for word in dictionary:
                   definition, name = json.loads(dictionary[word])
                   f.write(json.dumps([word, definition, name])+"\n")
                 f.close
                 room.message("Defination error :|")
             else:
              if word in dictionary:
                 definition, name = json.loads(dictionary[word])
                 room.message("<br/><br/><br/> ID :  <f x12FF0000='1'>  %s  <br/> <f x1233FFFF='1'>   kata kunci :   <f x12990099='1'>  %s  <br/> <f x1233FFFF='1'> definitions : <f x12FF6600='1'>  %s " % (name, word, definition),True)
              else:
                 room.message("<f x12FF0000='1'>"+args+" <f x1233FFFF='1'> Hal ini tidak diatur.", True)
           except:
             room.message("Ada yang salah :|")

        if (cmd == "undefine" or cmd == "undef" or cmd == "udf") and len(args) and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 0:
          try:
            word = args
            if word in dictionary:
              definition, name = json.loads(dictionary[word])
              if self.getAccess(room, user) > 0:
                del dictionary[word]
                room.message(" <f x1233FFFF='1'>Defination <f x12FF0000='1'>"+word+" <f x1233FFFF='1'> Itu dihapus dari database.", True)
                return
              else:
                room.message("<f x12FF0000='1'>User  %s   <f x1233FFFF='1'> Anda tidak diizinkan untuk menghapus Defination :| " % user.name, True)
                return
            else:
              room.message(" %s  is not yet defined you can define it by typing  define %s: meaning " % args, True)
          except:
            room.message("  Anda tidak diizinkan untuk melakukan tindakan ini.  ")
            return

        elif cmd == "mydf" and self.getAccess(room, user) >= 2:
          arr = []
          for i in dictionary:
            if user.name in dictionary[i]:
              arr.append(i)
          if len(arr) > 0:
            room.message("<f x12FF0000='1'> "+user.name+"    <f x1233FFFF='1'> Anda memiliki <f x12FF0000='1'>  "+str(len(arr))+"   <f x1233FFFF='1'> Dafinition ditambahkan  di Database saya:  <f x12FF0000='1'>  %s  "% (', '.join(sorted(arr))), True)
          else:
            room.message("Tidak ada Definition yang disimpan dalam Database.")

######################################################################################################################################################
########################################################## MESSAGENS TIME ############################################################################

        if cmd =="wordtoday" or cmd=="wt" and self.getAccess(room, user) >= 2:
            if self.getAccess(room, user) > 0:
              if user.name in wordtodaytime:
                w = json.loads(wordtodaytime[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and " <f x1133FFFF='1'>days" or " <f x1133FFFF='1'>hari" ) + "<f x11FF0000='1'> "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and " <f x1133FFFF='1'>hours" or " <f x1133FFFF='1'>jam" ) + "<f x11FF0000='1'> "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and " <f x1133FFFF='1'>minutes" or " <f x1133FFFF='1'>menit" ) + " <f x1133FFFF='1'><f x11FF0000='1'> "
                  string += str(seconds) + " " + (seconds == 1 and " <f x1133FFFF='1'>seconds" or " <f x1133FFFF='1'>detik" )
                  room.message("Untuk menggunakan perintah menunggu :  <f x11FF0000='1'>%s (~^o^)~ "% string,True)
                  return
              if self.getAccess(room, user) > 0:
                x=(random.choice(["hujan","embun","dingin","yuri","trap","gg","mal","idiot","jailson","yuri","waifu","rico","lindo","feio","gostoso","bom","gay","keep calm","arrogante","doçe","special","oppai","morte","anjo","caralho","nub","sol","amor","nude","velho","carinho","Sex",'rei',"impotent","cancêr"]))
                room.message("anda sedang <f x11FF0000='1'>"+sntonick(user.name)+" <f x1133FFFF='1'> merasakan! : <f x11FF0000='1'> "+str(x), True)
                wordtodaytime[user.name] = json.dumps(time.time()+1200)



        if cmd =="waifu" and self.getAccess(room, user) >= 2:
            if self.getAccess(room, user) > 0:
              if user.name in waifu:
                w = json.loads(waifu[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and " <f x1133FFFF='1'>days" or " <f x1133FFFF='1'>hari" ) + "<f x11FF0000='1'> "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and " <f x1133FFFF='1'>hours" or " <f x1133FFFF='1'>jam" ) + "<f x11FF0000='1'> "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and " <f x1133FFFF='1'>minutes" or " <f x1133FFFF='1'>menit" ) + " <f x1133FFFF='1'><f x11FF0000='1'> "
                  string += str(seconds) + " " + (seconds == 1 and " <f x1133FFFF='1'>seconds" or " <f x1133FFFF='1'>detik" )
                  room.message("Tunggu beberapa saat untuk menggunakan cmd ini lagi :  <f x11FF0000='1'>%s          (~^o^)~ "% string,True)
                  return
              if self.getAccess(room, user) > 0:
                x=(random.choice(["<br/>https://s17.postimg.org/smzu6nxjj/a1b88fa72ca2c930b5aa9ceacae5c95e.jpg<br/><f x1133FFFF='1'>Nama waifu: <f x11FF0000='1'>Inori <br/><f x1133FFFF='1'>Anime: <f x11FF0000='1'>Guilty Crown","<br/>https://s11.postimg.org/5ixcfjkzn/images.jpg<br/><f x1133FFFF='1'>Nama waifu: <f x11FF0000='1'>Kaga Koko <br/><f x1133FFFF='1'>Anime: <f x11FF0000='1'>Golden Time","<br/>http://i.imgur.com/fNsVi39.png<br/><f x1133FFFF='1'>Nama WAIFU: <f x11FF0000='1'>vert neptunia <br/><f x1133FFFF='1'>Anime: <f x11FF0000='1'>(?)","<br/>http://i.imgur.com/Xv5gHYv.jpg<br/><f x1133FFFF='1'>Nama WAIFU: <f x11FF0000='1'>Kou Yagami <br/><f x1133FFFF='1'>Anime: <f x11FF0000='1'>New game","<br/>https://66.media.tumblr.com/fff138cc0081579f0b3c1520f314b5d0/tumblr_nnw5j4ZxCk1tydz8to1_500.gif<br/><f x1133FFFF='1'>Nama WAIFU: <f x11FF0000='1'>Hestia <br/><f x1133FFFF='1'>Anime: <f x11FF0000='1'>Dungeon","<br/>http://i.imgur.com/xRiELxE.jpg<br/><f x1133FFFF='1'>Nama WAIFU: <f x11FF0000='1'>Shinobu <br/><f x1133FFFF='1'>Anime: <f x11FF0000='1'>Monogatari Series","<brhttp://i.imgur.com/VtFeG4H.jpg<br/><f x1133FFFF='1'>Nama WAIFU: <f x11FF0000='1'>Hare <br/><f x1133FFFF='1'>Anime: <f x11FF0000='1'>Guity crown","<br/>http://i.imgur.com/ZA7NP3N.jpg <br/><f x1133FFFF='1'>Nama WAIFU: <f x11FF0000='1'>Excell <br/><f x1133FFFF='1'>Anime: <f x11FF0000='1'>Kuro kami","<br/>http://i.imgur.com/3SiSIKp.jpg<br/><f x1133FFFF='1'>Nama WAIFU: <f x11FF0000='1'>Kuro <br/><f x1133FFFF='1'>Anime: <f x11FF0000='1'>Kuro kami","<br/>http://i.imgur.com/5L8Giys.png<br/><f x1133FFFF='1'>Nama WAIFU: <f x11FF0000='1'>Kirino <br/><f x1133FFFF='1'>Anime: <f x11FF0000='1'>Oreimo","<br/>http://i.imgur.com/kMiYfKu.jpg<br/><f x1133FFFF='1'>Nama WAIFU: <f x11FF0000='1'>Yuno <br/><f x1133FFFF='1'>Anime: <f x11FF0000='1'>Mirai nikki"]))
                room.message("selingkuhan"+sntonick(user.name)+"<f x1133FFFF='1'> :( :'( : <f x11FF0000='1'>  "+str(x)+"</font> ",True)
                waifu[user.name] = json.dumps(time.time()+1800)


        if cmd =="pdf" and self.getAccess(room, user) >= 2:
            if self.getAccess(room, user) > 0:
              if user.name in pdf:
                w = json.loads(pdf[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and " <f x1233FFFF='1'>day" or " <f x1233FFFF='1'>days" ) + "<f x12FF0000='1'> "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and " <f x1233FFFF='1'>hora" or " <f x1233FFFF='1'>horas" ) + "<f x12FF0000='1'> "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and " <f x1233FFFF='1'>minuto" or " <f x1233FFFF='1'>minutos" ) + " <f x1233FFFF='1'><f x12FF0000='1'> "
                  string += str(seconds) + " " + (seconds == 1 and " <f x1233FFFF='1'>segundo" or " <f x1233FFFF='1'>segundos" )
                  room.message("Para usar o comando novamente aguarde :  <f x12FF0000='1'>%s (~^o^)~ "% string,True)
                  return
              if self.getAccess(room, user) > 0:
                x=(random.choice(["Aiiii que delicia cara! http://i2.ytimg.com/vi/QBPgWoOpS5Q/mqdefault.jpg",
"O problema era na mangueira. http://i2.kym-cdn.com/photos/images/original/000/424/243/792.jpg",
"Não cara, No salame pode não. http://i.ytimg.com/vi/DHc9lnBHhME/mqdefault.jpg",
"Trabalhando e relaxando. http://lh3.googleusercontent.com/-9Kp9lq9fhls/Vwr1CYowkqI/AAAAAAAAFwI/eDG0okXfNqQiZHl7NPUj2RLALSn8LZFDw/w250-h167/zw7tlrG.gif",
"Arrochando os parafusos, queimando uma rosquinha, que delicia. http://i0.kym-cdn.com/photos/images/original/000/525/317/4c8.jpg",
"Senti firmeza demacol. http://i.ytimg.com/vi/JA0w7_Tjyas/hqdefault.jpg",
"Era essa peça q vc queria? http://i.ytimg.com/vi/qu8hJFF9DXw/hqdefault.jpg",
"Nossa assim você me mata. http://i.makeagif.com/media/6-21-2015/oiaVvf.gif"]))
                room.message("Caro Username "+sntonick(user.name)+"<f x1233FFFF='1'> sua frase é : <f x12FF0000='1'>  "+str(x)+"</font> ",True)
                pdf[user.name] = json.dumps(time.time()+1800)

        if cmd =="family" and self.getAccess(room, user) >= 2:
            if self.getAccess(room, user) > 0:
              if user.name in family:
                w = json.loads(family[user.name])
                if time.time() < w:
                  w = int(w) - int(time.time())
                  minute = 60
                  hour = minute * 60
                  day = hour * 24
                  days =  int(w / day)
                  hours = int((w % day) / hour)
                  minutes = int((w % hour) / minute)
                  seconds = int(w % minute)
                  string = ""
                  if days > 0:
                    string += str(days) + " " + (days == 1 and " <f x1133FFFF='1'>days" or " <f x1133FFFF='1'>hari" ) + "<f x11FF0000='1'> "
                  if len(string) > 0 or hours > 0:
                    string += str(hours) + " " + (hours == 1 and " <f x1133FFFF='1'>hours" or " <f x1133FFFF='1'>jam" ) + "<f x11FF0000='1'> "
                  if len(string) > 0 or minutes > 0:
                    string += str(minutes) + " " + (minutes == 1 and " <f x1133FFFF='1'>minutes" or " <f x1133FFFF='1'>menit" ) + " <f x1133FFFF='1'><f x11FF0000='1'> "
                  string += str(seconds) + " " + (seconds == 1 and " <f x1133FFFF='1'>seconds" or " <f x1133FFFF='1'>detik" )
                  room.message("maaf comand tidak bisa :  <f x11FF0000='1'>%s (~^o^)~ "% string,True)
                  return
              if self.getAccess(room, user) > 0:
                day= random.choice(room.usernames)
                dia= random.choice(room.usernames)
                room.message("Keluarga dari <f x11FF0000='1'>  ["+user.name+"]  <f x1133FFFF='1'> :D: <br/> ayah dari : <f x11FF0000='1'>"+user.name+"  <f x1133FFFF='1'> istrinya : <f x11FF0000='1'>"+day+" <f x1133FFFF='1'> anak Anda : <f x11FF0000='1'> "+dia, True)
                family[user.name] = json.dumps(time.time()+1800)

######################################################################################################################################################
########################################################## BLACKLIST #################################################################################


        if cmd.lower() == "bl" and self.getAccess(room, user) >= 5:
              if len(args) > 0:
                if "!anon" in args:
                    room.message("Anons are unable to be blacklisted.")
                    return
                else:
                      if args not in blacklist:
                        admin.remove(args)
                        mod.remove(args)
                        assistant.remove(args)
                        registered.remove(args)
                        whitelist.remove(args)
                        blacklist.append(args)
                        self.getRoom("tanpaid-chat").message("<f x12A498AC='1'><br/><br/>[<f x12FF0000='0'>S<f x12FF4C00='0'>T<f x12FF9800='0'>A<f x12FFE400='0'>T<f x12B3FF00='0'>U<f x1267FF00='0'>S<f x12BFF00='0'> <f x1200FF4C='0'>C<f x1200FF98='0'>M<f x1200FFE4='0'>D<f x12A498AC='1'>]<f x12A498AC='1'><br/><br/><br/><b>Username</b>: <f x12FF0000='1'>%s <f x12A498AC='1'><br/><b>Chat</b>: <f x12FF0000='1'>%s  <f x12A498AC='1'><br/><b>Comando</b>: <f x12FF0000='1'>%s - %s  <f x12A498AC='1'><br/><b>IP</b>: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, args, message.ip), True)    
                        rank = self.getAccess(room, user)
                        if rank == 5:
                          room.message("<br/><br/> <f x12FE9A2E='1'> [5 - Admin]  : <f x12FF0000='1'>  "+user.name+"  <br/> <f x12FF0000='1'>  "+args+"   <f x12A498AC='1'> Anda berada di <f x12FF0000='1'> [BLACKLIST]    <f x12A498AC='1'>sekarang", True)
                        if rank == 6:
                          room.message("<br/><br/> <f x12FE2EF7='1'> [6 - Developer]  : <f x12FF0000='1'>  "+user.name+"  <br/> <f x12FF0000='1'>  "+args+"   <f x12A498AC='1'> Anda berada di <f x12FF0000='1'> [BLACKLIST]    <f x12A498AC='1'>sekarang", True)
                      else:
                        rank = self.getAccess(room, user)
                        if rank == 5:
                          room.message("<br/><br/> <f x12FE9A2E='1'> [5 - Admin]   : <f x12FF0000='1'>  "+user.name+"  <br/>  <f x12A498AC='1'>pengguna <f x12FF0000='1'>  "+args+"   <f x12A498AC='1'> sudah di <f x12FF0000='1'> [BLACKLIST] ", True)
                        if rank == 6:
                          room.message("<br/><br/> <f x12FE2EF7='1'> [6 - Developer]  : <f x12FF0000='1'>  "+user.name+"  <br/>  <f x12A498AC='1'>pengguna <f x12FF0000='1'>  "+args+"   <f x12A498AC='1'> sudah di <f x12FF0000='1'> [BLACKLIST] ", True)
              else:
                rank = self.getAccess(room, user)
                if rank == 5:
                  room.message("<br/><br/> <f x12FE9A2E='1'> [5 - Admin] : <f x12FF0000='1'>  "+user.name+"  <br/> <f x12A498AC='1'>Restia membutuhkan <f x12FF0000='1'>[NICK]", True)
                if rank == 6:
                  room.message("<br/><br/> <f x12FE2EF7='1'> [6 - Developer]  : <f x12FF0000='1'>  "+user.name+"  <br/> <f x12A498AC='1'>Restia membutuhkan <f x12FF0000='1'>[NICK]", True)

        if cmd.lower() == "ubl" and self.getAccess(room, user) >= 5:
              self.getRoom("tanpaid-chat").message("<f x1133FFFF='1'><br/><br/>[<f x11FF0000='0'>S<f x11FF4C00='0'>T<f x11FF9800='0'>A<f x11FFE400='0'>T<f x11B3FF00='0'>U<f x1167FF00='0'>S<f x11BFF00='0'> <f x1100FF4C='0'>C<f x1100FF98='0'>M<f x1100FFE4='0'>D<f x1133FFFF='1'>]<f x1133FFFF='1'><br/><br/><br/><b>Username</b>: <f x11FF0000='1'>%s <f x1133FFFF='1'><br/><b>Chat</b>: <f x11FF0000='1'>%s  <f x1133FFFF='1'><br/><b>Comando</b>: <f x11FF0000='1'>%s <f x1133FFFF='1'><br/><b>IP</b>: <f x11FF0000='1'>%s" % (user.name, room.name, cmd, message.ip), True)    
              if self.getAccess(room, user) >0 : return
              if len(args) > 0:
                if "!anon" in args:
                    room.message("Anons tidak bisa di blacklisted.")
                    return
                else:
                      if args in blacklist:
                        blacklist.remove(args)
                        room.message("<br/><br/> <f x116666CC='1'> [Desenvolvedor]  : <f x11FF0000='1'>  "+user.name+"  <br/> <f x11FF0000='1'>  "+args+"   <f x1133FFFF='1'> Anda telah dihapus dari <f x11FF0000='1'> [BLACKLIST] ", True)
                      else:
                        room.message("<br/><br/> <f x116666CC='1'> [Desenvolvedor]  : <f x11FF0000='1'>  "+user.name+"  <br/>  <f x1133FFFF='1'>User name <f x11FF0000='1'>  "+args+"   <f x1133FFFF='1'> tidak <f x11FF0000='1'> [BLACKLIST] ", True)
              else:
                  room.message("<br/><br/> <f x116666CC='1'> [Desenvolvedor]  : <f x11FF0000='1'>  "+user.name+"  <br/> <f x1133FFFF='1'>Aku butuh <f x11FF0000='1'>[NICK]", True)

        if cmd == "blist":
         if self.getAccess(room, user) > 4:
            room.message("<br/><br/><f x11FF0000='1'> [BLACKLIST] :   <f x1133FFFF='1'><br/> [%s] " % (", ".join(blacklist)), True)

######################################################################################################################################################
########################################################## BAN USER ######################################################################################
        if cmd == "delete" or cmd == "del":
          if room.getLevel(self.user) > 0:
            if self.getAccess(room, user) >= 3 or room.getLevel(user) > 0:
              name = args.split()[0].lower()
              room.clearUser(ch.User(name))
            else:room.message("Maaf Restia tidak memiliki (mod) di sini :(")
          else:
            room.message("Restia Bukan mod disini :|")


        if cmd == "banlist":
          if self.getAccess(room, user) >= 3:
            room.message("Banned list Saat ini: "+str(room.banlist))

        if cmd == "ban" or cmd == "banned" and self.getAccess(room, user) >= 4:
          if self.getAccess(room, user) > 0:
            if self.getAccess(room, user) > 0:
              room.banUser(ch.User(args))
              room.message(" User   <f x11FF0000='1'>  "+args.title()+"   <f x1133FFFF='1'>  Banned Done.", True)
            else:
              room.message("Maaf Restia tidak memiliki (mod) di sini :(")
          else:
            room.message(" *warning* Anda tidak diizinkan untuk melakukan akses ini. *warning* ")

        if cmd == "unban" or cmd == "unbanned" and self.getAccess(room, user) >= 4:
          if args == "": return
          args = args.lower()
          if self.getAccess(room, user) > 0:
            if self.getAccess(room, user) > 0:
              if ch.User(args) not in room._getBanlist():
                room.message(" user   <f x11FF0000='1'>  "+args.title()+"   <f x1133FFFF='1'>  Hal ini tidak bisa di akses   ", True)
                return
              room.unban(ch.User(args))
              room.message(" anda sudah di unban   <f x11FF0000='1'>  "+args.title()+"   <f x1100000='1'>  , tidak menyalahgunakan aturan lagi, <f x1133FFFF='1'> spam , sara ,link share.  ", True)
            else:
              room.message("Maaf Restia tidak memiliki (mod) di sini :(")
          else:
            room.message("*warning*  Anda tidak diizinkan untuk melakukan tindakan ini. *warning* ", True)

      	
##########################################################################################################################################
################################################## ROOMS #################################################################################

        if cmd == "join" and self.getAccess(room, user) >= 3:
           if args == "": return
           if args in self.roomnames:
            room.message("<f x1133FFFF='1'> Restia sudah di room dan <f x1133FF33='1'>Sedang Online sekarang", True)
            self.getRoom("tanpaid-chat").message("<f x1233FFFF='1'><br/><br/>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>S<f x12FFA200='0'>T<f x12FFD800='0'>A<f x12C9FF00='0'>T<f x1293FF00='0'>U<f x125DFF00='0'>S<f x1227FF00='0'> <f x1200FF36='0'>C<f x1200FF6C='0'>M<f x1200FFA2='0'>D<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>]<f x1233FFFF='1'><br/><br/><br/>Username: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>Chat: <f x12FF0000='1'>%s  <f x1233FFFF='1'><br/>Comando: <f x12FF0000='1'>%s - %s  <f x1233FFFF='1'><br/>IP: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, args, message.ip), True)
           else:
             unlock.append(args)
             self.joinRoom(args)
             self.getRoom("tanpaid-chat").message("<f x1233FFFF='1'><br/><br/>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>S<f x12FFA200='0'>T<f x12FFD800='0'>A<f x12C9FF00='0'>T<f x1293FF00='0'>U<f x125DFF00='0'>S<f x1227FF00='0'> <f x1200FF36='0'>C<f x1200FF6C='0'>M<f x1200FFA2='0'>D<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>]<f x1233FFFF='1'><br/><br/><br/>Username: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>Chat: <f x12FF0000='1'>%s  <f x1233FFFF='1'><br/>Comando: <f x12FF0000='1'>%s - %s  <f x1233FFFF='1'><br/>IP: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, args, message.ip), True)
             room.message("  aku masuk room :  <f x12FF0000='1'>  "+args.title(),True)

        if cmd == "leave" and self.getAccess(room, user) >= 5:
            if args == "":
              room.message("<f x1133FF33='1'> Restia sudah keluar dari rooms . *waves*")
              self.getRoom("tanpaid-chat").message("<f x1233FFFF='1'><br/><br/>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>S<f x12FFA200='0'>T<f x12FFD800='0'>A<f x12C9FF00='0'>T<f x1293FF00='0'>U<f x125DFF00='0'>S<f x1227FF00='0'> <f x1200FF36='0'>C<f x1200FF6C='0'>M<f x1200FFA2='0'>D<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>]<f x1233FFFF='1'><br/><br/><br/>Username: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>Chat: <f x12FF0000='1'>%s  <f x1233FFFF='1'><br/>Comando: <f x12FF0000='1'>%s - %s  <f x1233FFFF='1'><br/>IP: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, room.name, message.ip), True)
              self.setTimeout(2, self.leaveRoom, room.name)
            else:
              self.leaveRoom(args)
              self.getRoom("tanpaid-chat").message("<f x1233FFFF='1'><br/><br/>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>S<f x12FFA200='0'>T<f x12FFD800='0'>A<f x12C9FF00='0'>T<f x1293FF00='0'>U<f x125DFF00='0'>S<f x1227FF00='0'> <f x1200FF36='0'>C<f x1200FF6C='0'>M<f x1200FFA2='0'>D<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>]<f x1233FFFF='1'><br/><br/><br/>Username: <f x12FF0000='1'>%s <f x1233FFFF='1'><br/>Chat: <f x12FF0000='1'>%s  <f x1233FFFF='1'><br/>Comando: <f x12FF0000='1'>%s - %s  <f x1233FFFF='1'><br/>IP: <f x12FF0000='1'>%s" % (user.name, room.name, cmd, args, message.ip), True)
              room.message("Restia sudah keluar dari rooms :  <f x12FF0000='1'>  "+args.title(),True)

        elif cmd == "rooms" and self.getAccess(room, user) >= 2: 
          j = [] 
          for i in self.roomnames: 
            j.append(i+"<f x12FF0000='1'> (%s)" % str(self.getRoom(i).usercount)) 
            j.sort() 
          room.message("[ <f x1233FFFF='1'> Restia wa, on raindearimasu (<f x12FF0000='1'>%s<f x1233FFFF='1'>)  <f x1233FFFF='1'> Chattorūmu] : <f x12FF0000='1'>  "%(len(self.roomnames))+", ".join(j), True)

        elif cmd == "lockstatus":
          if  args == "":
             if room.name not in lock:
                roomlock = "<f x1233FF33='1'>[LOCKED]"
                room.message("<br/><br/><br/><f x1233FFFF='1'>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>L<f x12FFA200='0'>O<f x12FFD800='0'>C<f x12C9FF00='0'>K<f x1293FF00='0'>S<f x125DFF00='0'>T<f x1227FF00='0'>A<f x1200FF36='0'>T<f x1200FF6C='0'>U<f x1200FFA2='0'>S<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>] <br/><f x1233FFFF='1'>[Chat]: "+room.name+"<br/> <f x1233FFFF='1'>[Status]: <f x1233FF33='1'>[UNLOCK] <br/><f x1233FFFF='1'>[SimSimi]: <f x12FF0000='1'>[LOCKED] ", True)
             if room.name in lock :
                roomlock = "<f x12FF0000='1'>[UNLOCK]"
                room.message("<br/><br/><br/><f x1233FFFF='1'>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>L<f x12FFA200='0'>O<f x12FFD800='0'>C<f x12C9FF00='0'>K<f x1293FF00='0'>S<f x125DFF00='0'>T<f x1227FF00='0'>A<f x1200FF36='0'>T<f x1200FF6C='0'>U<f x1200FFA2='0'>S<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>] <br/><f x1233FFFF='1'>[Chat]: "+room.name+"<br/> <f x1233FFFF='1'>[Status]: <f x12FF0000='1'>[UNLOCK] <br/><f x1233FFFF='1'>[SimSimi]: <f x12FF0000='1'>[LOCKED] ", True)
          else:
             if args not in lock:
                roomlock = "<f x1233FF33='1'>[LOCKED]"
                room.message("<br/><br/><br/><f x1233FFFF='1'>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>L<f x12FFA200='0'>O<f x12FFD800='0'>C<f x12C9FF00='0'>K<f x1293FF00='0'>S<f x125DFF00='0'>T<f x1227FF00='0'>A<f x1200FF36='0'>T<f x1200FF6C='0'>U<f x1200FFA2='0'>S<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>] <br/><f x1233FFFF='1'>[Chat]: "+args+"<br/> <f x1233FFFF='1'>[Status]: <f x1233FF33='1'>[UNLOCK] <br/><f x1233FFFF='1'>[SimSimi]: <f x12FF0000='1'>[LOCKED] ", True)
             if args  in lock :
                roomlock = "<f x12FF0000='1'>[UNLOCK]"
                room.message("<br/><br/><br/><f x1233FFFF='1'>[<f x12FF0000='0'>★<f x12FF3600='0'> <f x12FF6C00='0'>L<f x12FFA200='0'>O<f x12FFD800='0'>C<f x12C9FF00='0'>K<f x1293FF00='0'>S<f x125DFF00='0'>T<f x1227FF00='0'>A<f x1200FF36='0'>T<f x1200FF6C='0'>U<f x1200FFA2='0'>S<f x1200FFD8='0'> <f x1200C9FF='0'>★<f x1233FFFF='1'>] <br/><f x1233FFFF='1'>[Chat]: "+args+"<br/> <f x1233FFFF='1'>[Status]: <f x12FF0000='1'>[UNLOCK]<br/><f x1233FFFF='1'>[SimSimi]: <f x12FF0000='1'>[LOCKED] ", True)


        elif cmd == "locklist":
            room.message("<br/><br/><br/><f x1233FFFF='1'>[  <f x12FF0000='0'>★<f x12FF3F00='0'> <f x12FF7E00='0'>L<f x12FFBD00='0'>O<f x12FFFC00='0'>C<f x12C0FF00='0'>K<f x1281FF00='0'>L<f x1242FF00='0'>I<f x1203FF00='0'>S<f x1200FF3F='0'>T<f x1200FF7E='0'> <f x1200FFBD='0'>★<f x1233FFFF='1'>] <br/><f x1233FFFF='1'>[Status]: <f x1233FF33='1'>[LOCKED] <br/> <f x1233FFFF='1'>[Status]: <f x12FF0000='1'>[UNLOCK] <br/><f x1233FFFF='0'>[List of Chat] : <f x1233FFFF='0'>[<f x12FF0000='0'>%s" % ("<f x1233FFFF='0'>,<f x12FF0000='0'>".join(lock))+"<f x1233FFFF='0'>,<f x1233FF33='0'>%s<f x1233FFFF='0'>] " % ("<f x1233FFFF='0'>,<f x1233FF33='0'>".join(unlock)), True)

     

##########################################################################################################################################
################################################## SYSTEN ################################################################################

        if cmd == "save" and self.getAccess(room, user) >= 5:
          self.saveAll()
          room.message("Dētabēsu ga hozon sa remashita... *blush*")

        if cmd == "shutdown":
         if self.getAccess(room, user) >= 6:
          self.saveAll()
          room.message("shutdown *waves*")
          self.setTimeout(3, self.stop, )

        if cmd == "restart":
         if self.getAccess(room, user) >= 5:
            for room in self.rooms:
                time.sleep(2)
                room.reconnect()

        if cmd == "e"and self.getAccess(room, user) >= 6: #DO NOT MESS WITH THIS COMMAND IF YOU DON'T KNOW WHAT YOU'RE DOING (This is a vital command)
         if user.name == "0zx":
          ret = eval(args)
          if ret == None:
           room.message("Done.")
           return
          room.message(str(ret))
         else:
              room.message(" *warning*  Anda tidak diizinkan untuk melakukan akses ini. *warning* ")


##########################################################################################################################################
################################################## SAY #################################################################################

        if cmd == "say" and self.getAccess(room, user) >= 2:
            if args:
              room.message(args, True)
            else:
              room.message("ingin mengucapkan apa ?")

        if cmd == "reverse" or cmd == "rsay" and self.getAccess(room, user) >= 2: #Reversed arguments
          if args:
            room.message(args[::-1])
          else:
            room.message("Fook off"[::-1])

##########################################################################################################################################
################################################## CMDS/RANK #############################################################################

        elif cmd == "cmds":
          if args == "":
            rank = self.getAccess(room, user)
            if rank == 1:
              room.message("<br/><br/><br/><br/>★CMDS★<br/>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'> <br/> rank:  <f x1133FFFF='1'> [1 - Whitelist] <f x11FF0040='1'>"+"<br/> ★  [List Command] ★ "+"<br/><f x11FA5882='1'> [invite,invitegroup(ig),new,nma,lma,check,suck,eat,kill,hug,kisses,waifu2,rb,rb2,sn,rn,df,mydf,wt,waifu,pdf,family,blist,rooms,say,rsay,rank,ranker,mynick,nick,seenick,gs,gis,yt,yt2,pm,level,profile,about,find,bgtime,cso,find,cs,dice,people,users,myip,isdown,pg,barry,mc,relaxar,fuder,sut]", True)
            if rank == 2:
              room.message("<br/><br/><br/><br/>★CMDS★<br/>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'> <br/> rank:  <f x1100A3EF='1'> [2 - Registered] <f x11FF0040='1'>"+"<br/> ★  [List Command] ★ "+"<br/><f x11FA5882='1'>  [invite,invitegroup(ig),new,nma,lma,check,suck,eat,kill,hug,kisses,waifu2,rb,rb2,sn,rn,df,mydf,wt,waifu,pdf,family,blist,rooms,say,rsay,rank,ranker,mynick,nick,seenick,gs,gis,yt,yt2,pm,level,profile,about,find,bgtime,cso,find,cs,dice,people,users,myip,isdown,pg,barry,mc,relaxar,fuder,sut]", True)
            if rank == 3:
              room.message("<br/><br/><br/><br/>★CMDS★<br/>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'> <br/> rank:  <f x1133FFFF='1'> [3 - Assistant] <f x11FF0040='1'>"+"<br/> ★  [LList Command] ★ "+"<br/><f x11FA5882='1'>  [invite,invitegroup(ig),new,nma,lma,check,suck,eat,kill,hug,kisses,waifu2,rb,rb2,sn,rn,df,mydf,wt,waifu,pdf,family,blist,join,rooms,say,rsay,rank,ranker,mynick,nick,seenick,gs,gis,yt,yt2,pm,level,profile,about,find,bgtime,cso,find,cs,dice,people,users,myip,isdown,pg,barry,mc,relaxar,fuder,sut]", True)
            if rank == 4:
              room.message("<br/><br/><br/><br/>★CMDS★<br/>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'> <br/> rank:  <f x119F81F7='1'> [4 - Mod] <f x11FF0040='1'>"+"<br/> ★  →[List Command]←   ★ "+"<br/><f x11FA5882='1'>  [invite,invitegroup(ig),new,nma,lma,check,suck,eat,kill,hug,kisses,waifu2,rb,rb2,sn,rn,lock,unlock,df,mydf,wt,waifu,pdf,family,blist,ban,uban,join,rooms,say,rsay,rank,ranker,mynick,nick,seenick,gs,gis,yt,yt2,pm,modslevel,profile,about,find,bgtime,cso,find,cs,dice,people,users,myip,isdown,pg,barry,mc,relaxar,fuder,sut]", True)
            if rank == 5:
              room.message("<br/><br/><br/><br/>★CMDS★<br/>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'> <br/> rank:  <f x11FE9A2E='1'> [5 - Admin] <f x11FF0040='1'>"+"<br/> ★  →[List Command]←   ★ "+"<br/><f x11FA5882='1'> [invite,invitegroup(ig),new,nma,lma,check,suck,eat,kill,hug,kisses,waifu2,rb,rb2,sn,rn,lock,unlock,sleep,wakeup,df,mydf,udf,wt,waifu,pdf,family,bl,ubl,blist,ban,uban,join,leave,rooms,restart,say,rsay,ranker,mynick,nick,ping,seenick,gs,gis,yt,yt2,pm,msg,fax,bc,pm,mods,bg,level,profile,about,find,bgtime,cso,find,cs,dice,people,users,myip,isdown,pg,barry,mc,relaxar,fuder,sut]", True)
            if rank == 6:
              room.message("<br/><br/><br/><br/>★CMDS★<br/>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'> <br/> rank:  <f x11FE2EF7='1'> [6 - Developer] <f x11FF0040='1'>"+"<br/> ★  →[List Command]←   ★ "+"<br/><f x11FA5882='1'>[invite,invitegroup(ig),new,nma,lma,check,suck,eat,kill,hug,kisses,waifu2,rb,rb2,sn,rn,lock,unlock,sleep,wakeup,shutdown,df,mydf,udf,wt,waifu,pdf,family,bl,ubl,blist,ban,uban,join,leave,rooms,shutdown,restart,e,save,say,rsay,ping,rank,ranker,setrank,mynick,nick,seenick,gs,gis,yt,yt2,msg,fax,bc,pm,mods,bg,level,profile,about,find,bgtime,cso,find,cs,dice,people,users,myip,isdown,pg,barry,mc,relaxar,fuder,sut]", True)
        elif cmd == "rank":
          if args == "":
            rank = self.getAccess(room, user)
            if rank == 1:
              room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'><br/>rank: <f x1133FFFF='1'> [1 - Whitelist] <f x11FF0040='1'>", True)
            if rank == 2:
              room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'><br/>rank: <f x1100A3EF='1'> [2 - Registered] <f x11FF0040='1'>", True)
            if rank == 3:
              room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'><br/>rank: <f x1133FFFF='1'> [3 - Assistant] <f x11FF0040='1'>", True)
            if rank == 4:
              room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'><br/>rank: <f x119F81F7='1'> [4 - Mod] <f x11FF0040='1'>", True)
            if rank == 5:
              room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'><br/>rank: <f x11FE9A2E='1'> [5 - Admin] <f x11FF0040='1'>", True)
            if rank == 6:
              room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'><br/>rank: <f x11FE2EF7='1'> [6 - Developer] <f x11FF0040='1'>", True)
        
          else:
              rank = self.getAccess(room, ch.User(args))
              if rank == 0:
                room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+args+" <f x1133FFFF='1'><br/>rank: <f x1181BEF7='1'> [0 - Unranked] <f x11FF0040='1'>", True)
              if rank == 1:
                room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+args+" <f x1133FFFF='1'><br/>rank: <f x1133FFFF='1'> [1 - Whitelist] <f x11FF0040='1'>", True)
              if rank == 2:
                room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+args+" <f x1133FFFF='1'><br/>rank: <f x1100A3EF='1'> [2 - Registered] <f x11FF0040='1'>", True)
              if rank == 3:
                room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+args+" <f x1133FFFF='1'><br/>rank: <f x1133FFFF='1'> [3 - Assistant] <f x11FF0040='1'>", True)
              if rank == 4:
                room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+args+" <f x1133FFFF='1'><br/>rank: <f x119F81F7='1'> [4 - Mod] <f x11FF0040='1'>", True)
              if rank == 5:
                room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+args+" <f x1133FFFF='1'><br/>rank: <f x11FE9A2E='1'> [5 - Admin] <f x11FF0040='1'>", True)
              if rank == 6:
                room.message("<br/><br/>★ RANK ★<br/> <f x1133FFFF='1'>User Name: <f x11FF0000='1'>"+args+" <f x1133FFFF='1'><br/>rank: <f x11FE2EF7='1'> [6 - Developer] <f x11FF0040='1'>", True)

        if cmd == "ranker":
            room.message("<br/><br/><f x11FF0000='1'>            [ ★★★ RANK ALLY ★★★] "+"<br/><f x11FE2EF7='1'> [Developer]♤♤♤♤♤♤ :   <f x1133FFFF='1'> %s " % (", ".join(developer))+"<br/><f x11FE9A2E='1'> [Admin]♤♤♤♤♤ :   <f x119F81F7='1'> %s " % (", ".join(admin))+"<br/><f x11FE9A2E='1'> [Mod]♤♤♤♤ :   <f x119F81F7='1'> %s " % (", ".join(mod))+"<br/><f x1133FFFF='1'> [Assistant]♤♤♤ :   <f x11FE2EF7='1'> %s " % (", ".join(assistant))+"<br/><f x1133FFFF='1'> [Registered]♤♤ :   <f x11FE2EF7='1'> %s " % (", ".join(registered)), True)


        if cmd == "setrank" and self.getAccess(room, user) >= 6:
          if args != "":
#           try:
            args = args.lower()
            target, rank = args.split(" ", 1)
            target = str(target)
            rank = int(rank)
            available_rank = [-1,1,2,3,4,5,6]
            if not rank in available_rank:
              room.message("Masukkan peringkat yang sesuai")
              return
            if rank == 1:
              if target in whitelist:
                room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke    <f x1133FFFF='1'> [1 - Whitelist]    <f x1133FFFF='1'>  Sekarang :D. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in developer:
                developer.remove(target)
              if target in mod:
                mod.remove(target)
              if target in assistant:
                assistant.remove(target)
              if target in admin:
                admin.remove(target)
              if target in registered:
                registered.remove(target)
              whitelist.append(target)
              room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke    <f x1133FFFF='1'> [1 - Whitelist]    <f x1133FFFF='1'>  Sekarang :D. ", True)
            if rank == 2:
              if target in registered:
                room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke <f x1100A3EF='1'> [Registered]    <f x1133FFFF='1'>  Sekarang :D. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in developer:
                developer.remove(target)
              if target in mod:
                mod.remove(target)
              if target in assistant:
                assistant.remove(target)
              if target in admin:
                admin.remove(target)
              if target in whitelist:
                whitelist.remove(target)
              registered.append(target)
              room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke <f x1100A3EF='1'> [2 - Registered]    <f x1133FFFF='1'>  Sekarang :D. ", True)
            if rank == 3:
              if target in assistant:
                room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke    <f x1133FFFF='1'> [3 - Assistant]    <f x1133FFFF='1'>  Sekarang :D. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in developer:
                developer.remove(target)
              if target in mod:
                mod.remove(target)
              if target in registered:
                registered.remove(target)
              if target in admin:
                admin.remove(target)
              if target in whitelist:
                whitelist.remove(target)
              assistant.append(target)
              room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke    <f x1133FFFF='1'> [3 - Assistant]    <f x1133FFFF='1'>  Sekarang :D. ", True)
            if rank == 4:
              if target in mod:
                room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke    <f x119F81F7='1'> [4 - Mod]    <f x1133FFFF='1'>  Sekarang :D. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in developer:
                developer.remove(target)
              if target in assistant:
                assistant.remove(target)
              if target in registered:
                registered.remove(target)
              if target in admin:
                admin.remove(target)
              if target in whitelist:
                whitelist.remove(target)
              mod.append(target)
              room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke    <f x119F81F7='1'> [4 - Mod]    <f x1133FFFF='1'>  Sekarang :D. ", True)
            if rank == 5:
              if target in admin:
                room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke    <f x11FE9A2E='1'> [5 - Admin]   <f x1133FFFF='1'>  Sekarang :D. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in developer:
                developer.remove(target)
              if target in assistant:
                assistant.remove(target)
              if target in registered:
                registered.remove(target)
              if target in mod:
                mod.remove(target)
              if target in whitelist:
                whitelist.remove(target)
              admin.append(target)
              room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke    <f x11FE9A2E='1'> [5 - Admin]    <f x1133FFFF='1'>  Sekarang :D. ", True)
            if rank == 6:
              if not user.name == "0zx": return #put your name there (if user.name == "yourname" and user.name == "anothername":) To prevent other Owners(in this case is Co-Owners) to set user's rank to Co-Owner.
              if target in developer:
                room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke    <f x11FE2EF7='1'> [6 - Developer]   <f x1133FFFF='1'>  Sekarang :D. ",True)
                return
              if target in blacklist:
                blacklist.pop(target)
              if target in admin:
                admin.remove(target)
              if target in admin:
                admin.remove(target)
              if target in assistant:
                assistant.remove(target)
              if target in registered:
                registered.remove(target)
              if target in mod:
                mod.remove(target)
              if target in whitelist:
                whitelist.remove(target)
              developer.append(target)
              room.message("<f x11FF0000='1'>  "+target.title()+"   <f x1133FFFF='1'> Selamat anda dipromosikan ke   <f x11FE2EF7='1'> [6 - Developer]    <f x1133FFFF='1'>  Sekarang :D. ", True)
            if rank == -1:
              if target in blacklist:
                room.message(target.title()+" is already blacklisted.<br/>Reason: %s"% blacklist[target])
                return
              blacklist.update({target:"Annoying reason."})
              room.message(" <f x12FF0000='1'>  "+target.title()+"   <f x1233FFFF='1'> ,User anda berada di   <f x12FF0000='1'> [-1 - BLACKLIST]    <f x1233FFFF='1'>  agora. ", True)

##########################################################################################################################################
################################################################# NICKS ##################################################################

        elif cmd == "nick":
            if args:
                nick = args 
                user = user.name 
                nicks[user] = json.dumps(nick)
                room.message("<f x11FF0000='1'> "+user+"   <f x1133FFFF='1'> Ima kara Restia o yobidashimasu <f x11FF0000='1'> "+str(args)+" ", True)
                try: 
                    print("[SAVING] NICKS...")
                    f = open("nicks.txt", "w")
                    for user in nicks:
                        nick = json.loads(nicks[user])
                        f.write(json.dumps([user,nick]) + "\n")
                except:
                       room.message("Error untuk save nick.");return
            else:
              room.message("<f x11FF0000='1'>"+user.name+" <f x1133FFFF='1'> untuk menggunakan ini jenis perintah .nick + nama yang ingin Anda pake.", True)

        elif cmd == "mynick":
          user=user.name.lower()
          if user in nicks :
            nick = json.loads(nicks[user])
            room.message("<f x11FF0000='1'> "+user+" <f x1133FFFF='1'> nickname Anda saat ini :<f x11FF0000='1'> "+nick,True)
          else:
            room.message("<f x11FF0000='1'>"+user+" <f x1133FFFF='1'> Anda tidak memiliki nick. :D ", True)

        elif cmd == "seenick":
          try:
            if args in nicks:
              room.message("nick dari <f x11FF0000='1'>"+args+" <f x1133FFFF='1'> é :<f x11FF0000='1'>"+sntonick(args), True)
            else:
              room.message("pemakai <f x11FF0000='1'>"+args+" <f x1133FFFF='1'> tidak menemukan nick :|", True)
          except:
            return

##########################################################################################################################################
######################################################## GOOGLE ##########################################################################

        if cmd == "gs" and self.getAccess(room, user) >= 2:
            room.message("Search Google for : ( <f x12FF0000='1'>"+args+"  <f x1233FFFF='1'> ) <br/><br/>"+gs(args),True)

        if cmd == "gis" and self.getAccess(room, user) >= 2:
            room.message("Search Google image for : ( <f x12FF0000='1'>"+args+" <f x1233FFFF='1'> ) <br/><br/>"+gis(args),True)

        if cmd == "youtube" or cmd == "yt2" and self.getAccess(room, user) >= 2:
          if args:
               room.message(tube(args),True)

        if cmd == "yt" and self.getAccess(room, user) >= 2:
         len(args) > 0
         s_result = "";
         sarr = args;
         for i in range(0, len(sarr)):
           if(ord(sarr[i]) < 128):
                 s_result += sarr[i]
         site= "https://www.googleapis.com/youtube/v3/search?part=id&q=" + s_result.replace(" ", "%20")  + "&type=video&key=AIzaSyAA_MhpqTqMG3su4BSt4k7_AyozaEkG_p4"
         response = urlopen(site).read()
         json_response = json.loads(response.decode())
         if(len(json_response["items"]) > 0):
             vId = json_response["items"][0]["id"]["videoId"]
             room.message("https://www.youtube.com/watch?v=" + vId)

##########################################################################################################################################
######################################################## MSG #############################################################################

        if cmd == "msg" and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 0:
            name, body = args.split(" ", 1)
            self.getRoom(name).message(body)
            room.message("[MSG]send on 1 second ago.")

        if cmd == "bc" or cmd == "broadcast" and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 0:
           r = room.name
           l = "http://tanpaid-chat.chatango.com/"+r+"!"
           for room in self.rooms:
               room.message(" <br/><br/><br/><f x1133FFFF='1'>[<f x11FF0000='0'>B<f x11FF5500='0'>R<f x11FFAA00='0'>O<f x11AAFF00='0'>A<f x1155FF00='0'>D<f x1100FF55='0'>C<f x1100FFAA='0'>A<f x1100AAFF='0'>S<f x110055FF='0'>T<f x1133FFFF='1'>] <br/> <f x1133FFFF='1'>Username : <f x11FF0000='1'>"+user.name+"<br/>  <f x1133FFFF='1'>Chat : <f x11FF0000='1'>"+r+"<br/>  <f x1133FFFF='1'>Mensagem : <f x11FFCC00='1'>"+args+"<br/>  <f x1133FFFF='1'>Link : <f x11CC66CC='1'>"+l, True)
         else:
               room.message("*warning* Anda bkn siapa2 dan tidak diizinkan untuk melakukan tindakan ini. *warning* ")
        if cmd == "fax" or cmd == "Fax" and self.getAccess(room, user) >= 5:
         if self.getAccess(room, user) > 2:
           try:
             name, body = args.split(" ", 1)
             l = "http://.chatango.com/"+room.name+"!"
             if name in self.roomnames :
               self.getRoom(name).message("<br/><br/><br/><f x1133FFFF='1'>[<f x11FF0000='0'>M<f x11FF6D00='0'>S<f x11FFDA00='0'>G<f x1192FF00='0'> <f x1125FF00='0'>F<f x1100FF6D='0'>A<f x1100FFDA='0'>X<f x1133FFFF='1'>] <br/> <f x1133FFFF='1'>Username : <f x11FF0000='1'> %s <br/>  <f x1133FFFF='1'>Chat : <f x11FF0000='1'> %s <br/>  <f x1133FFFF='1'>Mensagem : <f x11FFCC00='1'> %s <br/>  <f x1133FFFF='1'>Link : <f x11CC66CC='1'> %s " % (user.name, room.name, body, l),True)
               room.message("[FAX]send on 1 second ago")
             else:
               room.message("Aku tidak online chat :|")
           except:room.message("error")
         else:
               room.message("*warning* Anda bkn siapa2 dan tidak diizinkan untuk melakukan tindakan ini. *warning* ")

        if cmd == "pm" and len(args) > 1 and self.getAccess(room, user) >= 2:
            name, msg = args.split(" ", 1)
            self.pm.message(ch.User(name.lower()), msg+" - from "+user.name)
            room.message('Sent to <font size="15"><font color="#FF9966"><b>%s</b></font></font>' % name, True)

        if cmd == "invite" or cmd == "Invite":
         if len (args) > 0:
            self.pm.message(ch.RoomManager(args),"%s kamu mendapat undangan dari ! http://%s.chatango.com ." %(room.ownername[0],room.name))
            room.message("invite terkirim!! kepada %s :)" % args)
         else:
            room.message("gak mau ah nginvite dia. :3")
        if cmd == "invitegroup" or cmd == "ig":
         if len (args) > 0:
            self.pm.message(ch.RoomManager(args),"%s kamu mendapat undangan group ! check di link http://%s.chatango.com ." %(room.ownername[0],room.name))
            room.message("invitegroup terkirim!! kepada %s :)" % args)
         else:
             room.message("gak mau ah nginvite dia")
##########################################################################################################################################
################################################## ROOMS RANK ############################################################################

        elif cmd == "level" and self.getAccess(room, user) >= 2 :
          if args == "":
            level = room.getLevel(user)
            if level == 1:
              title = "Moderator"
            if level == 2:
              title = "OWNER"
            if level == 0:
              title = "Slave"
            room.message("Your room level is: %s [%s]" %(level,title))
          else:
            level = room.getLevel(ch.User(args))
            if level == 1:
              title = "Moderator"
            if level == 2:
              title = "OWNER"
            if level == 0:
              title = "Slave"
            room.message("%s's room level is: %s [%s]" %(args.title(), level, title))

        elif cmd == "mods" and self.getAccess(room, user) >= 4:
          args = args.lower()
          if args == "":
            room.message("<br/>||<font color='#87ceeb'>OWNER</font>: <u>"+ (room.ownername) +"</u> <br/>||Mods: "+", ".join(room.modnames), True)
            return
          if args in self.roomnames:
              modask = self.getRoom(args).modnames
              owner = self.getRoom(args).ownername
              room.message("<br/>||<font color='#87ceeb'>OWNER</font>: <u>"+ (owner) +"</u> <br/>||Mods: "+", ".join(modask), True)
          else:
             self.joinRoom(args)
             cek_mods[user.name] = json.dumps([room.name,args])


##########################################################################################################################################
################################################## CHATANGO SPECIAL ######################################################################



        elif cmd=="about" and self.getAccess(room, user) >= 2:
           try:
             args=args.lower()
             stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
             crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
             mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
             mini=mini.replace("<img","<!")
             prodata = '<br/>'+mini
             room.message(prodata,True)
           except:
             room.message(""+args+" tidak tersedia di database ")

        elif cmd=="cso" and args != "" and self.getAccess(room, user) >= 2:
          offline = None
          url = urlreq.urlopen("http://"+args+".chatango.com").read().decode()
          if not "buyer" in url:
            room.message(args+" does not exist on chatango.")
          else:
            url2 = urlreq.urlopen("http://"+args+".chatango.com").readlines()
            for line in url2:
              line = line.decode('utf-8')
              if "leave a message for" in line.lower():
                print(line)
                offline = True
            if offline:
              room.message(random.choice([" %s " % args+" Tekidona <f x12FF0000='1'> [OFFLINE] "]), True)
            if not offline:
              room.message(random.choice([" %s " % args+" Tekidona <f x1233CC00='1'> [ONLINE] "]), True)


        elif cmd=="profile" or cmd=="prof" and args != "":
          try:
            args=args.lower()
            stuff=str(urlreq.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
            crap, age = stuff.split('<span class="profile_text"><strong>Age:</strong></span></td><td><span class="profile_text">', 1)
            age, crap = age.split('<br /></span>', 1)
            crap, gender = stuff.split('<span class="profile_text"><strong>Gender:</strong></span></td><td><span class="profile_text">', 1)
            gender, crap = gender.split(' <br /></span>', 1)
            if gender == 'M':
                gender = 'Male'
            elif gender == 'F':
                gender = 'Female'
            else:
                gender = '?'
            crap, location = stuff.split('<span class="profile_text"><strong>Location:</strong></span></td><td><span class="profile_text">', 1)
            location, crap = location.split(' <br /></span>', 1)
            crap,mini=stuff.split("<span class=\"profile_text\"><!-- google_ad_section_start -->",1)
            mini,crap=mini.split("<!-- google_ad_section_end --></span>",1)
            mini=mini.replace("<img","<!")
            picture = '<a href="http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg</a>'
            rank = self.getAccess(room, ch.User(args))
          except:
            df = ' não existe. :|'
          offline = None
          url = urlreq.urlopen("http://"+args+".chatango.com").read().decode()
          if not "buyer" in url:
            room.message(args+df)
          else:
            url2 = urlreq.urlopen("http://"+args+".chatango.com").readlines()
            for line in url2:
              line = line.decode('utf-8')
              if "leave a message for" in line.lower():
                offline = True
            rank = self.getAccess(room, ch.User(args))
            if offline:
             if rank == 0:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x1381BEF7='1'> [0 - Unranked] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 1:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x1333FFFF='1'> [1 - Whitelist] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 2:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x1300A3EF='1'> [2 - Registered] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 3:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x1333FFFF='1'> [3 - Assistant] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 4:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x139F81F7='1'> [4 - Mod] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 5:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x13FE9A2E='1'> [5 - Admin] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 6:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x13FE2EF7='1'> [6 - Developer] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x13FF0000='1'> Offline"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
            rank = self.getAccess(room, ch.User(args))
            if not offline:
             if rank == 0:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x1381BEF7='1'> [0 - Unranked] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 1:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x1333FFFF='1'> [1 - Whitelist] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 2:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x1300A3EF='1'> [2 - Registered] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 3:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x1333FFFF='1'> [3 - Assistant] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 4:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x139F81F7='1'> [4 - Mod] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 5:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x13FE9A2E='1'> [5 - Admin] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)
             if rank == 6:
                 room.message("<br/><br/>[<f x13FF0000='0'>P<f x13FF6D00='0'>R<f x13FFDA00='0'>O<f x1392FF00='0'>F<f x1325FF00='0'>I<f x1300FF6D='0'>L<f x1300FFDA='0'>E<f x1333FFFF='1'>]<br/>"+picture+"<br/> <f x1333FFFF='1'>Username: <f x13FF0000='1'>"+args+"<br/><f x1333FFFF='1'>Sex: <f x13FF0000='1'>"+gender+"<br/><f x1333FFFF='1'>Age: <f x13FF0000='1'>"+age+"<br/><f x1333FFFF='1'> Country: <f x13FF0000='1'>"+location+" <f x1333FFFF='1'><br/>Rank: <f x13FE2EF7='1'> [6 - Developer] <f x13FF0040='1'>"+"<br/><f x1333FFFF='1'> Status:<f x1333FF33='1'> Online"+"<br/> <f x1333FFFF='1'> Profile Complete: <f x136666CC='1'> http://barrykun.com/?"+args+"<f x1333FFFF='1'> ou <f x136666CC='1'> http://"+args+".chatango.com", True)


        if cmd == ("find") and len(args) > 0 and self.getAccess(room, user) >= 2:
          name = args.split()[0].lower()
          if not ch.User(name).roomnames:
            room.message("Yūzā wa, heya ya AFK de wa arimasen! ")
          else:
            room.message("Yūzā wa %s Genzai, ika no chattorūmu :  %s  " % (args, ", ".join(ch.User(name).roomnames)), True)

        if cmd == "seen":
          try:
            nama = args
            if nama in hist:
              waktu, ruang, body = json.loads(hist[nama])
              room.message("Message Terakhir dari User : "+nama+" - "+waktu+" - "+ruang+" - "+body)
            else:
              room.message("Res tidak melihatnya " + nama + " hampir disemua rooms :|")
          except:
              room.message("gagal")

        if cmd== "bg" or cmd == "background"and self.getAccess(room, user) >= 5:
         if args == "on":
             room.setBgMode(1)
             room.message("BG On", True)
         if args == "off":
            room.setBgMode(0)
            room.message("BG Off" ,True)

        if cmd=="bgtime" and len(args) > 0 and self.getAccess(room, user) >= 2:
            try:
                args=args.lower()
                bgimg = "http://fp.chatango.com/profileimg/%s/%s/%s/msgbg.jpg" % (args[0], args[1], args)
                pic = "http://fp.chatango.com/profileimg/%s/%s/%s/full.jpg" % (args[0], args[1], args)
                if len(args.split(" ", -1)) != 1:
                    return
                if len(args) == 1:
                    f_args, s_args = args, args
                elif len(args) > 1:
                    f_args, s_args = args[0], args[1]

                def getBgtime(args):
                    expired = True
                    url = ("http://st.chatango.com/profileimg/" + f_args + "/" + s_args + "/" + args + "/mod1.xml")
                    f = urllib.request.urlopen(url)
                    data = f.read().decode("utf-8")
                    e = ET.XML(data)
                    bg = e.findtext("d")
                    bg = int(urllib.request.unquote(bg))
                    if bg - int(time.time()) < 0:
                      total_seconds = int(time.time())-bg
                    else:
                      total_seconds = bg-int(time.time())
                      expired = False

                    # Helper vars:
                    MINUTE  = 60
                    HOUR    = MINUTE * 60
                    DAY     = HOUR * 24

                   # Get the days, hours, etc:
                    days    = int( total_seconds / DAY )
                    hours   = int( ( total_seconds % DAY ) / HOUR )
                    minutes = int( ( total_seconds % HOUR ) / MINUTE )
                    seconds = int( total_seconds % MINUTE )

                    # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
                    string = ""
                    if days > 0 or days < 0:
                        string += str(days) + " " + (days == 1 and " <f x1133FFFF='1'>days" or " <f x1133FFFF='1'>hari" ) + "<f x11FF0000='1'> "
                    if len(string) > 0 or hours > 0:
                        string += str(hours) + " " + (hours == 1 and " <f x1133FFFF='1'>hours" or " <f x1133FFFF='1'>jam" ) + "<f x11FF0000='1'> "
                    if len(string) > 0 or minutes > 0:
                        string += str(minutes) + " " + (minutes == 1 and " <f x1133FFFF='1'>minutes" or " <f x1133FFFF='1'>menit" ) + "<f x11FF0000='1'> "
                    string += str(seconds) + " " + (seconds == 1 and " <f x1133FFFF='1'>seconds" or " <f x1133FFFF='1'>detik" )
                    if expired == True:
                      return "<f x11FF0000='1'>Expired now"
                    elif expired == False:
                      return " "+string
                room.message("<br/><br/><f x1133FFFF='1'>[<f x11FF0000='0'>B<f x11FF5500='0'>G<f x11FFAA00='0'> <f x11AAFF00='0'>S<f x1155FF00='0'>T<f x1100FF55='0'>A<f x1100FFAA='0'>T<f x1100AAFF='0'>U<f x110055FF='0'>S<f x1133FFFF='1'>] <br/>Username:<f x11FF0000='1'> " + args.title() +"<br/><f x1133FFFF='1'>Imagem background: <br/>"+bgimg+"<br/><f x1133FFFF='1'> Tempo restante:  <f x11FF0000='1'>" + getBgtime(args), True)
            except:
                room.message("<br/><br/><f x1133FFFF='1'>[<f x11FF0000='0'>B<f x11FF5500='0'>G<f x11FFAA00='0'> <f x11AAFF00='0'>S<f x1155FF00='0'>T<f x1100FF55='0'>A<f x1100FFAA='0'>T<f x1100AAFF='0'>U<f x110055FF='0'>S<f x1133FFFF='1'>] <br/>Username:<f x11FF0000='1'> " + args.title() +"<br/><f x1133FFFF='1'>Imagem background: <br/>"+bgimg+"<br/><f x1133FFFF='1'> Tempo restante: <f x11FF0000='1'>Expirada", True)

##########################################################################################################################################
################################################## CMD NORMAIS ###########################################################################

        if cmd == "cs" or cmd =="currentstats" and self.getAccess(room, user) >= 2:
          a = len(self.roomnames)
          b = len(developer)
          c = len(admin)
          d = len(mod)
          e = len(assistant)
          f = len(registered)
          g = len(nicks)
          h = len(blacklist)
          rank = self.getAccess(room, user)
          if rank == 2:
             room.message("<br/><br/><br/>  <f x1233FFFF='1'> ★ Current stats Database ★"+"<br/>  <f x1233FFFF='1'> Developer: <f x12FF0000='1'> "+str(b)+" <br/>  <f x1233FFFF='1'> Admin: <f x12FF0000='1'> "+str(c)+"<br/>  <f x1233FFFF='1'> Mod: <f x12FF0000='1'> "+str(d)+"<br/>  <f x1233FFFF='1'> Assistant: <f x12FF0000='1'> "+str(e)+"<br/>  <f x1233FFFF='1'> Registered: <f x12FF0000='1'> "+str(f)+"<f x1233FFFF='1'> (Incluíndo você) <br/>  <f x1233FFFF='1'> Blacklist: <f x12FF0000='1'> "+str(h)+"<br/>  <f x1233FFFF='1'> Chat: <f x12FF0000='1'>"+str(a)+"<br/>  <f x1233FFFF='1'> Nick: <f x12FF0000='1'>"+str(g) ,True)
          if rank == 3:
             room.message("<br/><br/><br/>  <f x1233FFFF='1'> ★ Current stats Database ★"+"<br/>  <f x1233FFFF='1'> Developer: <f x12FF0000='1'> "+str(b)+" <br/>  <f x1233FFFF='1'> Admin: <f x12FF0000='1'> "+str(c)+"<br/>  <f x1233FFFF='1'> Mod: <f x12FF0000='1'> "+str(d)+"<br/>  <f x1233FFFF='1'> Assistant: <f x12FF0000='1'> "+str(e)+"<f x1233FFFF='1'> (Incluíndo você)<br/>  <f x1233FFFF='1'> Registered: <f x12FF0000='1'> "+str(f)+"<br/>  <f x1233FFFF='1'> Blacklist: <f x12FF0000='1'> "+str(h)+"<br/>  <f x1233FFFF='1'> Chat: <f x12FF0000='1'>"+str(a)+"<br/>  <f x1233FFFF='1'> Nick: <f x12FF0000='1'>"+str(g) ,True)
          if rank == 4:
             room.message("<br/><br/><br/>  <f x1233FFFF='1'> ★ Current stats Database ★"+"<br/>  <f x1233FFFF='1'> Developer: <f x12FF0000='1'> "+str(b)+" <br/>  <f x1233FFFF='1'> Admin: <f x12FF0000='1'> "+str(c)+"<br/>  <f x1233FFFF='1'> Mod: <f x12FF0000='1'> "+str(d)+"<f x1233FFFF='1'> (Incluíndo você)<br/>  <f x1233FFFF='1'> Assistant: <f x12FF0000='1'> "+str(e)+"<br/>  <f x1233FFFF='1'> Registered: <f x12FF0000='1'> "+str(f)+"<br/>  <f x1233FFFF='1'> Blacklist: <f x12FF0000='1'> "+str(h)+"<br/>  <f x1233FFFF='1'> Chat: <f x12FF0000='1'>"+str(a)+"<br/>  <f x1233FFFF='1'> Nick: <f x12FF0000='1'>"+str(g) ,True)
          if rank == 5:
             room.message("<br/><br/><br/>  <f x1233FFFF='1'> ★ Current stats Database ★"+"<br/>  <f x1233FFFF='1'> Developer: <f x12FF0000='1'> "+str(b)+" <br/>  <f x1233FFFF='1'> Admin: <f x12FF0000='1'> "+str(c)+"<f x1233FFFF='1'> (Incluíndo você)<br/>  <f x1233FFFF='1'> Mod: <f x12FF0000='1'> "+str(d)+"<br/>  <f x1233FFFF='1'> Assistant: <f x12FF0000='1'> "+str(e)+"<br/>  <f x1233FFFF='1'> Registered: <f x12FF0000='1'> "+str(f)+"<br/>  <f x1233FFFF='1'> Blacklist: <f x12FF0000='1'> "+str(h)+"<br/>  <f x1233FFFF='1'> Chat: <f x12FF0000='1'>"+str(a)+"<br/>  <f x1233FFFF='1'> Nick: <f x12FF0000='1'>"+str(g) ,True)
          if rank == 6:
             room.message("<br/><br/><br/>  <f x1233FFFF='1'> ★ Current stats Database ★"+"<br/>  <f x1233FFFF='1'> Developer: <f x12FF0000='1'> "+str(b)+"<f x1233FFFF='1'> (Incluíndo você) <br/>  <f x1233FFFF='1'> Admin: <f x12FF0000='1'> "+str(c)+"<br/>  <f x1233FFFF='1'> Mod: <f x12FF0000='1'> "+str(d)+"<br/>  <f x1233FFFF='1'> Assistant: <f x12FF0000='1'> "+str(e)+"<br/>  <f x1233FFFF='1'> Registered: <f x12FF0000='1'> "+str(f)+"<br/>  <f x1233FFFF='1'> Blacklist: <f x12FF0000='1'> "+str(h)+"<br/>  <f x1233FFFF='1'> Chat: <f x12FF0000='1'>"+str(a)+"<br/>  <f x1233FFFF='1'> Nick: <f x12FF0000='1'>"+str(g) ,True)

        if cmd == "dice" and self.getAccess(room, user) >= 2:
          die1=random.randint(1,6)
          die2=random.randint(1,6)
          room.message("Saikoro o furu to na~tsu : "+str(die1)+" , "+str(die2))

        if cmd =="users":
           d=str(room.usercount)
           room.message("<f x1133FFFF='1'>done. <f x11FF0000='1'> <b>"+d+"</b> <f x1133FFFF='1'> pengguna <f x1133FF33='1'>online<f x1133FFFF='1'>, saat ini adalah pengguna terdaftar yang : <f x11FF0000='1'><b>%s</b>" % ", ".join(room.usernames),True)

        if cmd == "ping" and self.getAccess(room, user) >= 4:
           if args == "":
            usrs = []
            gay = []
            finale = []
            prop = 0
            prop = prop + len(room._userlist) - 1
            for i in room._userlist:
              i = str(i)
              usrs.append(i)
            while prop >= 0:
              j = usrs[prop].replace("<User: ", "")
              i = j.replace(">", "")
              gay.append(i)
              prop = prop - 1
            for i in gay:
              if i not in finale:
                finale.append(i)
            if len(finale) > 40:
              room.message("@%s"% (" @".join(finale[:41])), True)
            if len(finale) <=40 :
              room.message("@%s"% (" @".join(finale)), True)
           if args != "":
             if args not in self.roomnames:
               room.message("restia tidak disana.")
               self.getRoom("tanpaid-chat").message("<br/><br/><b>Nama</b>: %s <br/><b>Rooms</b>: %s  <br/><b>Commmand</b>: %s <br/><b>IP</b>: %s" % (user.name, room.name, cmd, message.ip), True)    
               return

        elif cmd == "people" and self.getAccess(room, user) >= 2:
         if args == "":
          usrs = []
          gay = []
          finale = []
          prop = 0
          prop = prop + len(room._userlist) - 1
          for i in room._userlist:
            i = str(i)
            usrs.append(i)
          while prop >= 0:
            j = usrs[prop].replace("<User: ", "")
            i = j.replace(">", "")
            gay.append(i)
            prop = prop - 1
          for i in gay:
            if i not in finale:
              finale.append(i)
          if len(finale) > 40:
            room.message("<f x11FF0000='1'>saat ini ada  %s <f x11000099='1'> user yang sudah terdaftar di room chat : <f x113366FF='1'>%s"% (len(finale),", ".join(finale)), True)
          if len(finale) <=40 :
            room.message("<f x1133FFFF='1'>saat ini ada <f x11FF0000='1'>  %s   <f x1133FFFF='1'>user yang sudah terdaftar di room chat : <f x11FF0000='1'>%s"% (len(finale),", ".join(finale)), True)
         if args != "":
           if args not in self.roomnames:
             room.message("Restia tidak disana.")
             return
           users = getParticipant(str(args))
           if len(users) > 40:
             room.message("<font color='#9999FF'> 40 </font> of  %s   current users in  %s : %s"% (len(users), args.title(), ", ".join(users[:41])), True)
           if len(users) <=40:
             room.message("<f xFF0000='1'>Há <f xFF0000='1'> %s  <f x000099='1'>pengguna di chat ini <f x3366FF='1'> %s : %s"% (len(users), args.title(), ", ".join(users)), True)

        if cmd == "rr":
            room.message(random.choice(["%s" % "<f x11FF0000='1'>  BANNG!!  <f x11FF0000='1'> "+user.name+" , <f x1133FFFF='1'>  anda  <f x11FF0000='1'> meninggal!! ","<f x11FF0000='1'> *click*  <f x11FF0000='1'> "+user.name+" ,  <f x1133FFFF='1'> anda  <f x1133FF33='1'> selamat!! "]), True)

        elif cmd == "sut":
          minute = 60
          hour = minute * 60
          day = hour * 24
          days =  int(getUptime() / day)
          hours = int((getUptime() % day) / hour)
          minutes = int((getUptime() % hour) / minute)
          seconds = int(getUptime() % minute)
          string = ""
 
          if days > 0:
 
            string += str(days) + " " + (days == 1 and " <f x1133FFFF='1'>days" or " <f x1133FFFF='1'>hari" ) + "<f x11FF0000='1'> "
 
          if len(string) > 0 or hours > 0:
 
            string += str(hours) + " " + (hours == 1 and " <f x1133FFFF='1'>hours" or " <f x1133FFFF='1'>jam" ) + "<f x11FF0000='1'> "
 
          if len(string) > 0 or minutes > 0:
 
            string += str(minutes) + " " + (minutes == 1 and " <f x1133FFFF='1'>minutes" or " <f x1133FFFF='1'>menit" ) + "<f x11FF0000='1'> "
 
          string += str(seconds) + " " + (seconds == 1 and " <f x1133FFFF='1'>seconds" or " <f x1133FFFF='1'>detik" )
          room.message("<f x1133FF33='1'> [ONLINE]  <f x1133FFFF='1'> on : <f x11FF0000='1'>%s" % string, True)

        elif cmd == "server" and self.getAccess(room, user) >= 2:
          minute = 60
          hour = minute * 60
          day = hour * 24
          days =  int(getUptime() / day)
          hours = int((getUptime() % day) / hour)
          minutes = int((getUptime() % hour) / minute)
          seconds = int(getUptime() % minute)
          string = ""

          if days > 0:

            string += str(days) + " " + (days == 1 and " <f x1233FFFF='1'>days" or " <f x1233FFFF='1'>hari" ) + "<f x12FF0000='1'> "

          if len(string) > 0 or hours > 0:

            string += str(hours) + " " + (hours == 1 and " <f x1233FFFF='1'>hours" or " <f x1233FFFF='1'>jam" ) + "<f x12FF0000='1'> "

          if len(string) > 0 or minutes > 0:

            string += str(minutes) + " " + (minutes == 1 and " <f x1233FFFF='1'>minutes" or " <f x1233FFFF='1'>menit" ) + "<f x12FF0000='1'> "

          string += str(seconds) + " " + (seconds == 1 and " <f x1233FFFF='1'>seconds" or " <f x1233FFFF='1'>detik" )
          z=(random.choice(["701","721","710","701","781","761","731","733","732","782",]))
          x=(random.choice(["1","2","3","4","5"]))
          room.message("<br/><br/><br/><f x1233FFFF='1'>[<f x12FF0000='0'>I<f x12FF2800='0'>N<f x12FF5000='0'>F<f x12FF7800='0'>O<f x12FFA000='0'>R<f x12FFC800='0'>M<f x12FFF000='0'>A<f x12D7FF00='0'>S<f x12AFFF00='0'>I<f x1287FF00='0'> <f x1237FF00='0'>S<f x120FFF00='0'>E<f x1200FF28='0'>R<f x1200FF50='0'>V<f x1200FF78='0'>I<f x1200FFA0='0'>S<f x1200FFC8='0'>]<br/><f x1233FFFF='1'>Version bot: <f x12FF0000='1'>2.0.1  <br/><f x1233FFFF='1'>Versi sistem : <f x12FF0000='1'>Python 3.5.2 <br/><f x1233FFFF='1'>Memori: <f x12FF0000='1'>"+str(z)+"<f x1233FFFF='1'>MB/<f x12FF0000='1'>32<f x1233FFFF='1'>GB (Free: <f x12FF0000='1'>31<f x1233FFFF='1'>GB) [<f x12FF0000='1'>1<f x1233FFFF='1'>% ] <br/>Ping: <f x12FF0000='1'>"+str(x)+"<f x1233FFFF='1'>ms <br/>Servis online: <f x12FF0000='1'>24<f x1233FFFF='1'> Hari<br/> Bot online: <f x12FF0000='1'>%s" % string, True)

        if cmd == "ms" or cmd == "lag":
            room.message(random.choice(["%s" % "42ms","32ms","41ms","62ms","85ms","42ms","10ms","25ms","95ms"]), True)

        elif cmd=="timelocal":
             room.message(strftime("jam sekarang é : "+"%H:%M:%S", localtime()))     

        if cmd == "myip":
            room.message("<f x11FF0000='1'>  "+user.name+"    <f x1133FFFF='1'>   tidak menumakan ip   <f x11FF0000='1'>  "+message.ip+" ", True)
        elif cmd=="isdown"and self.getAccess(room, user) >= 2:
          if len(args)>0:
            for line in urlreq.urlopen("http://www.downforeveryoneorjustme.com/"+args):
              decoder=line.decode("UTF-8")
              if "It's just you." in decoder:
                room.message("Site <f x11FF0000='1'>"+args+"<f x1133FFFF='1'> now <f x1133FF33='1'>[ONLINE]", True)
                break
              if "It's not just you!" in decoder:
                room.message("site <f x11FF0000='1'>"+args+"<f x1133FFFF='1'> now <f x11FF0000='1'>[OFFLINE]", True)
                break
              if "doesn't look like a site on the interwho." in decoder:
                room.message("lik dari site: <f x11FF0000='1'>"+args+"<f x1133FFFF='1'> sekarang <f x116633FF='1'>tidak valid", True)
                break
              else:
                 continue
          else:
            room.message("command (isdown) user gunakaan command <isdown + [O url site tsb]")

##########################################################################################################################################
################################################## CMD ARGS ##############################################################################

        if cmd == "pg" and self.getAccess(room, user) >= 2:
             if not args == "":
                              room.message(random.choice(["Sim","Não","De jeito nenhum","Mais do que provável","Nunca","Descubra você mesmo","Sem duvida","Como eu vou saber?","Eu me recuso a comentar sobre isso.","Isso é meio óbvio."]))
             else:
                              room.message("Este é o comando (pergunta) Para usá-lo, digite .pg+[Sua pergunta aqui]")
        if cmd == "barry" and self.getAccess(room, user) >= 2:
             if not args == "":
                               room.message(random.choice(["http://barrykun.com/?"+args]))
             else:
                               room.message("Este é o comando (barry) Para usá-lo, digite .barry+[O nick do profile]")
        if cmd == "mc" and self.getAccess(room, user) >= 2:
            if not args == "":
                            room.message(random.choice(["http://ch.besaba.com/chat/html5/?"+args]))
            else:
                            room.message("Este é o comando (mc) Para usá-lo, digite .mc+[O nome do chat]")
        if cmd == "relaxar" :
            if not args == "":
                            room.message(random.choice(["%s" % "Iai vamos relaxar? https://pbs.twimg.com/media/CDrx3lQW0AAEJ4o.jpg @"+args]), True)
            else:
                            room.message(random.choice(["%s" % "Iai vamos relaxar? https://pbs.twimg.com/media/CDrx3lQW0AAEJ4o.jpg @"+user.name]), True)

        if cmd == "fuder" and self.getAccess(room, user) >= 2:
            if not args == "":
                            room.message(random.choice(["%s" % "Oi amor, vamos fuder? ( ͡° ͜ʖ ͡°) @"+args]), True)
            else:
                            room.message(random.choice(["%s" % "Oi amor, vamos fuder? ( ͡° ͜ʖ ͡°) @"+user.name]), True)
        if cmd == "kiss" and self.getAccess(room, user) >= 2:
            if not args == "":
                            room.message(random.choice(["%s" % "https://i.imgur.com/eyJifvl.gif  @"+args]), True)
            else:
                            room.message(random.choice(["%s" % "https://i.imgur.com/eyJifvl.gif @"+user.name]), True)

        elif cmd == "check" and self.getAccess(room, user) >= 2:
                  room.message(self.findUser(args), True)

##suck
        if cmd == "suck" and self.getAccess(room, user) >= 2:
            room.message(" <f x12FF0000='1'>"+user.name+"<f x1233FFFF='1'>-anda menghisap <f x12FF0000='1'>"+random.choice(room.usernames)+"<f x1233FFFF='1'>-enak kan :o", True)

###eat
        if cmd == "eat":
            room.message("oke!!! "+user.name+" aku akan memakan "+random.choice(room.usernames)+" haha")
         
##kills
        if cmd == "kill":
            room.message(" <f x11FF0000='1'>"+user.name+"<f x1133FFFF='1'> Telah membunuh <f x11FF0000='1'>"+random.choice(room.usernames)+" i kill you haha", True)
 
        if cmd == "hug":
            if args:
              room.message("*Tertawa lah sebelum di tertawakan:D <f x11FF0000='1'>" + args+"*")
            else:
              room.message("*gamau mahal <f x11FF0000='1'>"+random.choice(room.usernames)+"*",True)
##kiss
        if cmd == "kisses":
            if args:
              room.message("*kiss :* <f x11FF0000='1'>" + args+"*", True)
            else:
              room.message("*kiss :* <f x11FF0000='1'>"+random.choice(room.usernames)+"*", True)##########################################################################################################################################
        if cmd == "waifu2":
            die1=random.randint(1,100)
            die2=random.randint(1,100)
            die3=random.randint(1,100)
            die4=random.randint(1,100)
            room.message("<f x11FF0000='1'>"+user.name+"<f x1133FFFF='1'> sua waifu vai ser <f x11FF0000='1'>"+random.choice(room.usernames)+"<f x1133FFFF='1'> vocês vão se beijar <f x11FF0000='1'>"+str(die1)+"<f x1133FFFF='1'> vezes ao dia e vai levar <f x11FF0000='1'>"+str(die2)+"<f x1133FFFF='1'> chute em um mês e tem <f x11FF0000='1'>"+str(die3)+"% <f x1133FFFF='1'> de chance pra ficar com sua waifu e <f x11FF0000='1'>"+str(die4)+"% <f x1133FFFF='1'>chance de <f x11FF0000='1'>"+random.choice(room.usernames)+"<f x1133FFFF='1'> ser amante.", True)



##########################################################################################################################################
################################################## CMD RB ################################################################################

        elif cmd == "rb" and self.getAccess(room, user) >= 2:
              if args == "":
                rain = rainbow('Rainbow!')
                room.message(rain,True)
              else:
                rain = rainbow(args)
                room.message(rain,True)

        elif cmd == "rb2" and self.getAccess(room, user) >= 2:
              if args == "":
                rain = rainbow('Rainbow!')
                room.message(rain)
              else:
                rain = rainbow(args)
                room.message(rain)

################################################## FINAL #################################################################################


   except Exception as e:
         try:
          et, ev, tb = sys.exc_info()
          lineno = tb.tb_lineno
          fn = tb.tb_frame.f_code.co_filename
          room.message("[Error] %s Line %i - %s"% (fn, lineno, str(e)))
          return
         except:
          room.message("Undescribeable error detected !!")
          return





  def onFloodWarning(self, room):
    time.sleep(2)
    room.reconnect()



def hexc(e):
  et, ev, tb = sys.exc_info()
  if not tb: print(str(e))
  while tb:
    lineno = tb.tb_lineno
    fn = tb.tb_frame.f_code.co_filename
    tb = tb.tb_next
  print("(%s:%i) %s" % (fn, lineno, str(e)))

if __name__ == "__main__":
   try:
     TestBot.easy_start(rooms, botname, botpassword)
   except KeyboardInterrupt:
     print("Console initiated a kill.")
   except Exception as e:
     hexc(e)
