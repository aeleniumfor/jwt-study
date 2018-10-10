import sys,re
import base64
import json
import hashlib,hmac
import codecs

args = sys.argv
str = args[1].split('.')
print("----------------------------")
print(args[1])
header = base64.b64decode(str[0])
payload = base64.b64decode(str[1])
print("----------------------------")
print(header)
print(payload)
print("----------------------------")

signature = base64.b64encode(header)+b'.'+base64.b64encode(payload)
print(signature)
base64.urlsafe_b64encode

secret = b'secret'

signature = hmac.new(secret,signature, hashlib.sha256)
print(str[2])
signature = signature.hexdigest()
print(signature.decode('hex'))
##signature = [(i+j) for (i,j) in zip(signature[::2],signature[1::2])]
