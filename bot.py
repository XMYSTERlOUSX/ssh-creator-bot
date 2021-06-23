import random
import string
import time
import os
try:
    import telepot
    from telepot.loop import MessageLoop
except:
    os.system('pip install telepot --user')
try:
    import requests
except:
    os.system('pip install requests --user')


class host:
    def __init__(self, host):
        h = host.replace('http://', '')
        h = host.replace('https://', '')
        self.host = host
        self.h = h
        x = requests.get(url='https://api.hackertarget.com/dnslookup/?q='+self.h) 
        dns = x.text.split("\n")[0].split(":")[1].strip()
        self.dns = dns
    def port(self, chat):
        x = requests.get(url='https://api.hackertarget.com/nmap/?q='+self.dns)
        bot.sendMessage(chat, x.text)
    def lookup(self, chat):
        bot.sendMessage(chat, self.dns)
    def header(self, chat):
        xx = requests.get(url='https://api.hackertarget.com/httpheaders/?q='+self.host)
        bot.sendMessage(chat, xx.text)
    def links(self, chat):
        zz = requests.get(url='https://api.hackertarget.com/pagelinks/?q='+self.h)
        bot.sendMessage(chat, zz.text)
    

#print(host('https://vodafone.com.eg').links('asd'))
class ssh:
    def __init__(self, ids_list):
        self.session = requests.Session()
        self.username = "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(10, 12)))
        self.password = "sshDieProfis"
        self.servers_id = ids_list
    def main(self, chat):
        current_id = random.choice(self.servers_id)
        url = "https://www.speedssh.com/"
        req = self.session.get(url)
        cookies = dict(req.cookies)
        url = "https://www.speedssh.com/create-account-ssh.php"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'www.speedssh.com',
            'Origin': 'https://www.speedssh.com',
            'Referer': 'https://www.speedssh.com/create-ssh-account-server/30/ssh-server-united-states-1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36 OPR/74.0.3911.75',
            'X-Requested-With': 'XMLHttpRequest',
        }
        data = f"serverid={current_id}&username={self.username}&password={self.password}"
        req = self.session.post(url, headers=headers, data=data)
        if "Your Account has been successfully created" in req.text:
            host_ip = req.text.split("<br>")[6].split(":")[1].strip()
            all_info = f"{host_ip}:443@speedssh.com-{self.username}:{self.password}"
            ex = req.text.split("<br>")[8]
            alls=f"host : {host_ip} \nusername : speedssh.com-{self.username}\npass : {self.password}\nhttp_custom : {host_ip}:443@speedssh.com-{self.username}:{self.password}\n{ex}"
            bot.sendMessage(chat, alls)
            return alls
        elif "has reached Account maximum" in req.text:
            self.servers_id.remove(current_id)
            self.main(chat)
        else:
            self.servers_id.remove(current_id)
            self.main(chat)

class ssl:
    def __init__(self, ids_list):
        self.session = requests.Session()
        self.username = "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(10, 12)))
        self.password = "sslDieProfis"
        self.servers_id = ids_list
    def main(self, chat):
        current_id = random.choice(self.servers_id)
        url = "https://www.speedssh.com/"
        req = self.session.get(url)
        cookies = dict(req.cookies)
        url = "https://www.speedssh.com/create-account-ssl.php"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'www.speedssh.com',
            'Origin': 'https://www.speedssh.com',
            'Referer': 'https://www.speedssh.com/create-ssl-account-server/230/server-us-ssl/tls-1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36 OPR/74.0.3911.75',
            'X-Requested-With': 'XMLHttpRequest',
        }
        data = f"serverid={current_id}&username={self.username}&password={self.password}"
        req = self.session.post(url, headers=headers, data=data)
        if "Your Account has been successfully created" in req.text:
            host_ip = req.text.split("<br>")[4].split(":")[1].strip()
            all_info = f"{host_ip}:443@speedssh.com-{self.username}:{self.password}"
            ex = req.text.split("<br>")[6]
            alls=f"host : {host_ip} \nusername : speedssh.com-{self.username}\npass : {self.password}\nhttp_custom : {host_ip}:443@speedssh.com-{self.username}:{self.password}\n{ex}"
            bot.sendMessage(chat, alls)
            return alls
        elif "has reached Account maximum" in req.text:
            self.servers_id.remove(current_id)
            self.main(chat)
        else:
            self.servers_id.remove(current_id)
            self.main(chat)


       

serope = ["44", "46", "48", "50"]
sasia = ["36", "38", "40", "42"]
samrica = ["30", "32", "34"]
lerope = ["256", "252", "254", "256", "252"]
lasia = ["244", "238", "240", "242", "246", "248"]
lamrica = ["230", "234", "236"]


def substr(string, start, length = None):
    if start < 0:
        start = start + len(string)
    if not length:
        return string[start:]
    elif length > 0:
        return string[start:start + length]
    else:
        return string[start:length]

 
def bot_msg(msg):

    chat_id = msg['chat']['id']

    command = msg['text']
    a=command
    if '0' in str(command.find('/ssl')):
        one = a.find('-num ')+5
        one2 = a.find('-plc') - one - 1
        one3 = substr(a, one, one2)
        two = a.find('-plc ')+5
        two2 = a.find(';') - two
        two3 = substr(a, two, two2)
        string = '/ssl -num '+one3+' -plc '+two3+';'

        if string in a:
            if two3 == 'er':
                bot.sendMessage(chat_id, 'wait 15s please')
                for i in range(int(one3)):
                    creator = ssl(lerope)
                    x = creator.main(chat_id)
            elif two3 == 'ar':
                bot.sendMessage(chat_id, 'wait 15s please')
                for i in range(int(one3)):
                    creator = ssl(lamrica)
                    x = creator.main(chat_id)
            elif two3 == 'as':
                bot.sendMessage(chat_id, 'wait 15s please')
                for i in range(int(one3)):
                    creator = ssl(lasia)
                    x = creator.main(chat_id)
            else:
                bot.sendMessage(chat_id, 'choose avaible place please')
        else:        
            bot.sendMessage(chat_id, 'wrong syntax')

    elif '0' in str(command.find('/ssh')):
        one = a.find('-num ')+5
        one2 = a.find('-plc') - one - 1
        one3 = substr(a, one, one2)
        two = a.find('-plc ')+5
        two2 = a.find(';') - two
        two3 = substr(a, two, two2)
        string = '/ssh -num '+one3+' -plc '+two3+';'

        if string in a:
            if two3 == 'er':
                bot.sendMessage(chat_id, 'wait 5s please')
                for i in range(int(one3)):
                    creator = ssh(serope)
                    x = creator.main(chat_id)
            elif two3 == 'ar':
                bot.sendMessage(chat_id, 'wait 5s please')
                for i in range(int(one3)):
                    creator = ssh(samrica)
                    x = creator.main(chat_id)
            elif two3 == 'as':
                bot.sendMessage(chat_id, 'wait 5s please')
                for i in range(int(one3)):
                    creator = ssh(sasia)
                    x = creator.main(chat_id)
            else:
                bot.sendMessage(chat_id, 'choose avaible place please')
        else:        
            bot.sendMessage(chat_id, 'wrong syntax')

    elif '0' in str(command.find('/host')):
        one = a.find('-t ')+3
        one2 = a.find('-h') - one - 1
        one3 = substr(a, one, one2)
        two = a.find('-h ')+3
        two2 = a.find(';') - two
        two3 = substr(a, two, two2)
        string = '/host -t '+one3+' -h '+two3+';'
        if string in a:
            if one3 == 'port':
                bot.sendMessage(chat_id, 'wait 5s please')
                host(two3).port(chat_id)
            elif one3 == 'lookup':
                bot.sendMessage(chat_id, 'wait 5s please')
                host(two3).lookup(chat_id)
            elif one3 == 'header':
                bot.sendMessage(chat_id, 'wait 5s please')
                host(two3).header(chat_id)
            elif one3 == 'links':
                bot.sendMessage(chat_id, 'wait 5s please')
                host(two3).links(chat_id)
            else:
                bot.sendMessage(chat_id, 'choose avaible type please')
        else:
            bot.sendMessage(chat_id, 'wrong syntax')
    elif '0' in str(command.find('/help')):
        helps = 'welcome to Die Profis bot\nlist of classes:\n    host\n    ssh\n    ssl\n    trojan (coming soon in new update 24/2/2021)\n    proxy (coming soon in new update 24/2/2021)\n    create dns server (coming soon in new update 24/2/2021)\nclass host:\n    syntax:\n        /host -t <select type> -h <host>;\n    list of options (types):\n        -port -> check open ports in host\n        -header -> get headers from host\n        -lookup -> get ip from host (dns)\n        -links -> show other links for host\n        -test -> for test inject       (coming soon in new update 24/2/2021)\n    test:\n        /host -t port -h vodafone.com.eg;\n\nclass ssh:\n    syntax:\n        /ssh -num <num of account> -plc <place>\n    list of places:\n        -er\n        -as\n        -am\n        -num -> number of accounts\n    test:\n        /ssl -num 5 -plc er;\n \nclass ssl:\n    syntax:\n        /ssl -num <num of account> -plc <place>\n    list of places:\n        -er\n        -as\n        -am\n        -num -> number of accounts\n    test:\n        /ssl -num 5 -plc er;\n\n        '
        bot.sendMessage(chat_id, helps)
    elif '0' in str(command.find('/start')):
        bot.sendMessage(chat_id, 'welcome mr:.... (what\'s your name )')



     
bot = telepot.Bot('1871071012:AAF4U-vLrGSitG_qJVBjyc6bPBes-gozMOc')

MessageLoop(bot, bot_msg).run_as_thread()

while 1:

    time.sleep(1)

