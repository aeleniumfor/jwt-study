import sys,re
import base64

args = sys.argv
str = args[1].split('.')

print(base64.b64decode(str[0]))
print(base64.b64decode(str[1]))
