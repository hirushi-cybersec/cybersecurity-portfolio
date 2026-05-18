import hashlib
import requests
def check_pwned(password):
 try:
        sha1=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix, suffix = sha1[:5], sha1[5:]
        url=f"https://api.pwnedpasswords.com/range/{prefix}"
        res=requests.get(url, timeout=10)
        res.raise_for_status()
        hashes=(line.split(':')for line in res.text.splitlines())
        for h,count in hashes:
           if h==suffix:
              return int(count)

        return 0
 except requests.exceptions.Timeout:
    print("Request timed out. Check your internet connection")
    return 0
 except requests.exceptions.RequestException as error:
    print(f"other error:{error}")
    return 0
password=input("enter a password").strip()
count=check_pwned(password)
if count>0:
    print(f"\033[91mstrength:very weak\033[0m")
    print(f"This password was found {count} times in data breaches!")
else:
    print("not found in breaches")
exit()
