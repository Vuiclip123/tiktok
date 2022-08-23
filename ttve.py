#!/usr/local/bin/python 
# -*- coding: utf-8 -*-
from time import sleep
import requests,os
import os, requests, io, time, random, bs4, sys, datetime, re, base64, urllib.parse, json, threading, cursor
lmkvip="\033[1;31m[\033[1;33mLMK-TOOL\033[1;31m]\033[1;35m❯\033[1;36m❯\033[1;37m❯\033[1;32m "
os.system("clear") 
def logo():
  logo = """
                    
\t\t\033[1;33m          〚 𝕋𝕆𝕆𝕃 𝔹𝕐 〛            

\033[1;36m\t██╗   ██╗██╗   ██╗██╗ ██████╗██╗     ██╗██████╗ 
\033[0;35m\t██║   ██║██║   ██║██║██╔════╝██║     ██║██╔══██╗
\033[1;93m\t██║   ██║██║   ██║██║██║     ██║     ██║██████╔╝
\033[1;92m\t╚██╗ ██╔╝██║   ██║██║██║     ██║     ██║██╔═══╝ 
\033[1;36m\t ╚████╔╝ ╚██████╔╝██║╚██████╗███████╗██║██║     
\033[1;34m\t  ╚═══╝   ╚═════╝ ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝     

\033[1;33m\t╔♫════════════════════════════════════════♫═╗
\t\033[1;36m        ☞ 𝕐𝕆𝕌𝕋𝕌𝔹𝔼: VUICLIP.CF
\t\033[1;33m        ☞ ℤ𝔸𝕃𝕆: 0948399159
\t\033[1;35m        ☞ Tsr: TYPRO
\t\033[1;32m        ☞ Facebook: typro102
\t\033[1;31m        ☞ Tool Tăng View TikTok
\033[1;33m\t╚═♫════════════════════════════════════════♫╝";

          
"""
  for pr in logo:sys.stdout.write(pr);sys.stdout.flush();time.sleep(0.001)



  
logo() 

VIDEO = input("\033[1;34m➻❥ Nhập ID ViDeo : ")

###VIDEO = "7132337880457858331" #video id


os.system("clear") 
logo() 


class Main:
    def __init__(self):

        self.url = "https://zefoy.com/"
        self.session = requests.session()

    def solve_captcha(self, sessid):
        try:
            # -- get captcha image --
            response = self.session.get(
                self.url + "a1ef290e2636bf553f39817628b6ca49.php",
                headers={
                    "origin": "https://zefoy.com",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest",
                    "cookie": f"PHPSESSID={sessid}",
                },
                params={
                    "_CAPTCHA": "",
                    "t": f"{round(random.random(), 8)} {int(time.time())}",
                },
            )

            json_data =  {
                "requests": [{
                    "image": {
                        "content": str(base64.b64encode(response.content).decode())
                    },
                    "features": [{"type": "TEXT_DETECTION"}]
                }]
            }

            req = requests.post(
                url = 'https://content-vision.googleapis.com/v1/images:annotate',
                headers = {
                    'x-origin': 'https://explorer.apis.google.com',
                },
                params = {
                    'alt': 'json',
                    'key': 'AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM',
                },
                json = json_data
            )

            captcha_answer = req.json()['responses'][0]["textAnnotations"][0]["description"]

            if captcha_answer == "" or captcha_answer is None:
                self.solve_captcha(sessid)
            
            captcha_answer = re.compile('[^a-zA-Z]').sub('', captcha_answer).lower()

            # submit response
            _response = self.session.post(
                self.url,
                data={
                    "captcha_secure": captcha_answer,
                    "r75619cf53f5a5d7aa6af82edfec3bf0": "",
                },
                headers={
                    "cookie": f"PHPSESSID={sessid}",
                    "origin": "https://zefoy.com",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest",
                },
            )
            alpha_key = re.findall('(?<=")[a-z0-9]{16}', _response.text)[0]
            print(f"Solved captcha ! | {captcha_answer}")

            return alpha_key
        
        except Exception as e:
            print(f"Error: {e}")
            print("Captcha Invalid | Check access to Zefoy | xtekky.com may be down")
            self.solve_captcha(sessid)

    def get_sessid(self):
        sessid = self.session.get(
            self.url,
            headers={
                "origin": "https://zefoy.com",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
        ).cookies.values()[0]
        return sessid

    def decrypt(self, data):
        return base64.b64decode(urllib.parse.unquote(data[::-1])).decode()

    def decrypt_timer(self, data):
        # decrypted = base64.b64decode(urllib.parse.unquote(data[::-1])).decode()
        if len(re.findall(" \d{3}", data)) != 0:
            timer = re.findall(" \d{3}", data)[0]
        else:
            timer = data.split("= ")[1].split("\n")[0]

        return int(timer)

    def views_loop(self, sessid, alpha_key):
        while True:
            time.sleep(2)

            request = self.session.post(
                self.url + "c2VuZC9mb2xsb3dlcnNfdGlrdG9V",
                headers={
                    "cookie": f"PHPSESSID={sessid}",
                    "origin": "https://zefoy.com",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest",
                },
                data={alpha_key: f"https://www.tiktok.com/@onlp/video/{VIDEO}"},
            )
            decryped_answer = self.decrypt(request.text)

            if "This service is currently not working" in decryped_answer:
                print("Views not available in the moment")
                input()
                sys.exit()

            elif "Server too busy" in decryped_answer:
                print("Server busy ! (waiting 10s)")
                time.sleep(10)
                continue

            elif "function updatetimer()" in decryped_answer:
                print("\r", end="")
                timer = self.decrypt_timer(decryped_answer)

                print(f"Timer: {timer} (Vui Lòng Chờ)  ")
                time.sleep(timer)

                print("\033[1;33m"+"------------------------------------------------------------")
                    
                continue

            soup = bs4.BeautifulSoup(decryped_answer, "html.parser")
            try:
                beta_key = soup.find("input", {"type": "text"}).get("name")
            except:
                input(decryped_answer)
                sys.exit()

            time.sleep(1)

            start = time.time()
            send_views = requests.post(
                self.url + "c2VuZC9mb2xsb3dlcnNfdGlrdG9V",
                headers={
                    "cookie": f"PHPSESSID={sessid}",
                    "origin": "https://zefoy.com",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest",
                },
                data={beta_key: VIDEO},
            )
            latency = round(time.time() - start, 2)
            if latency > 3:
                
                print(f"Sent views [id={VIDEO}]")  
                
            decrypted_response = self.decrypt(send_views.text)

            if "Too many requests. Please slow down." in decrypted_response:
                print("Ratelimited")
                time.sleep(120)
                continue

            timer = self.decrypt_timer(decrypted_response)

            
            print(f"\033[1;36mTimer: {timer} (Vui Lòng Chờ)  ")
            time.sleep(timer)

            print(f"\033[1;33m"+"------------------------------------------------------------")
                
            

    def main(self):
        sessid = self.get_sessid()
        print(f"\033[1;31mSessid: {sessid}")
        alpha_key: str = self.solve_captcha(sessid)
        print("\n" + f"Alpha Key: {alpha_key.upper()}")
        
        self.views_loop(sessid, alpha_key)


if __name__ == "__main__":
    Main().main()
