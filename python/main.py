import sys,re
import base64,binascii
import json

args = sys.argv
str = args[1].split('.')



header = base64.b64decode(str[0]).decode("UTF-8")
payload = base64.b64decode(str[1]).decode("UTF-8")

print(header)
print(payload)
