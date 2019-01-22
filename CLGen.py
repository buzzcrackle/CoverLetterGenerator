import pyperclip
import sys

error = "Um... that's wrong. Something like:\npython CLGen.py Dropbox Intern"

f = open("coverletter.txt", "r")
body = f.read()

if len(sys.argv) == 3:
    body = body.replace("COMPANY_NAME", str(sys.argv[1]))
    body = body.replace("JOB_TITLE", str(sys.argv[2]))
    pyperclip.copy(body)
    print(body)
else:
    print(error)
