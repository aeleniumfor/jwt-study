import sys,re
import base64
import json
import hashlib,hmac
import urllib.request

args = sys.argv
str = args[1].split('.')

print(args[1])
header = base64.b64decode(str[0])
payload = base64.b64decode(str[1])
print(header)
print(payload)

hp = base64.urlsafe_b64encode(header)+b'.'+base64.urlsafe_b64encode(payload)
print(hp)

secret = b'secret'
signature = hmac.new(secret,hp, hashlib.sha256)
signature = signature.digest()
signature = base64.urlsafe_b64encode(signature)


jwt = (hp+b"."+signature).decode("UTF-8").strip("=")
print(jwt)