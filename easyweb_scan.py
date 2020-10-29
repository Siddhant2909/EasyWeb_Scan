import os
import json
import requests
import time

print('      _____              __        __   _       ____                      ')
print('     | ____|__ _ ___ _   \ \      / /__| |__   / ___|  ___ __ _ _ __      ')
print('     |  _| / _` / __| | | \ \ /\ / / _ \ |_ \  \___ \ / __/ _` | `_ \     ')
print('     | |__| (_| \__ \ |_| |\ V  V /  __/ |_) |  ___) | (_| (_| | | | |    ')
print('     |_____\__,_|___/\__, | \_/\_/ \___|_.__/  |____/ \___\__,_|_| |_|    ')
print('                     |___/                                                ')
print('                         #Created By Siddhant Sawalka#                 \n ')

print('Enter URL:')
url = input()

if 'www.' in url or 'api.' in url:
    if 'www.' in url:
        url1 = url.split('www.',1)[1]
    elif 'api.' in url:
        url1 = url.split('api.',1)[1]
elif 'www.' not in url:
    if 'http' in url or 'https' in url:
        url1 = url.split('://',1)[1]
    else:
        print('Invalid URL.Please Try Entering A Valid URL.')

def live(url1):
    if '/' in url1:
        url1 = url1.split('/',1)[0]
    r=(requests.head(url))
    if(r.status_code == 200):
        print("[+] Website is Live")
    else:
        print("[+] Website isn't not Live")

def subdomain(url1):

    if '/' in url1:
        url1 = url1.split('/',1)[0]
    
    os.system("start cmd /k python ../../../../../Windows/System32/Sublist3r/sublist3r.py -d {} -t 50 -o {}.txt".format(url1,url1))
    print("[+] Check the text file {}.txt for the subdomain list".format(url1))

def subdomain_takeover(url1):

    if '/' in url1:
        url1 = url1.split('/',1)[0]
    errors={"Web Site Not Found",
    "Sorry, this page is no longer available.",
    "If this is your website and you've just created it, try refreshing in a minute",
    "The specified bucket does not exist",
    "Repository not found",
    "Trying to access your account?",
    "404 Not Found",
    "Please try again or try Desk.com free for 14 days",
    "Domain uses DO name serves with no records in DO",
    "Fastly error: unknown domain:",
    "The feed has not been found.",
    "404: This page could not be found.",
    "The thing you were looking for is no longer here, or never was",
    "There isn't a Github Pages site here.",
    "NoSuchBucketThe specified bucket does not exist.",
    "404 Blog is not found",
    "We could not find what you're looking for.",
    "No settings were found for this company:",
    "No such app",
    "Uh oh. That page doesn't exist.",
    "is not a registered InCloud YouTrack",
    "No Site For Domain",
    "It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us.",
    "Unrecognized domain",
    "Tunnel *.ngrok.io not found",
    "404 error unknown site!",
    "This public report page has not been activated by the user",
    "Project doesnt exist... yet!",
    "Sorry, this shop is currently unavailable.",
    "This job board website is either expired or its domain name is invalid.",
    "page not found",
    "project not found",
    "Whatever you were looking for doesn't currently exist at this address",
    "Please renew your subscription",
    "Non-hub domain, The URL you've accessed does not provide a hub.",
    "The requested URL was not found on this server.",
    "This UserVoice subdomain is currently available!",
    "The page you are looking for doesn't exist or has been moved",
    "Do you want to register *.wordpress.com?",
    "Hello! Sorry, but the website you&rsquo;re looking for doesn&rsquo;t exist.",
    }
    readfile = open('{}.txt'.format(url1), 'r')
    list = readfile.read().split('\n')
    for target in list:
        if target == "":
            continue
        response = requests.get("https://"+url1)
        response.text
        targetresponse = response.text
        for err in errors:
            if err in targetresponse:
                print("[+]"+target+":"+"Vulnerable")
                break
            else:
                print("[+]"+target+":"+"Not Vulnerable")
                break       
    readfile.close()            

def dir(url):
    file = 'wordlist.txt'
    with open(file) as f:
        l = f.readline()
        while l:
            combine = url+"/"+l.strip()
            r=requests.get(combine)
            if r.status_code == 200:
                print("[+]"+combine+"---"+str(r.status_code))
            l = f.readline()

def clickjacking(url1):
    if '/' in url1:
        url1 = url1.split('/',1)[0]
    os.system("curl {} -I  > {}.txt ".format(url,url1))
    dic=jsonconvert(url1)
    if('x-Frame-Options' in dic.keys() or 'Content-Security-Policy' in dic.keys()):
        print("[+] The website is not vulnerable to clickjacking")
    else:
        print("[+] The website is vulnerable to clickjacking")

def cors():
    print('Enter Origin:')
    origin = input()
    def cors(url,url1,origin):
        url1 = url1.split('.')[0]
        os.system("curl {} -I -H origin:{} > {}.txt ".format(url,origin,url1))
        dic=jsonconvert(url1)
        status_code=int(dic.get('HTTP/1.1')[0])
        if status_code>=200 and status_code<300:
            if ('Access-Control-Allow-Origin:' in dic.keys() and 'Access-Control-Allow-Credentials:' in dic.keys()):
                if (dic.get('Access-Control-Allow-Origin:')[0] == origin and dic.get('Access-Control-Allow-Credentials:')[0] == 'true'):
                    print('[+] Case 1 Possible.The entered domain is subject to exploitation.')
                elif (dic.get('Access-Control-Allow-Origin:')[0] == 'null' and dic.get('Access-Control-Allow-Credentials:')[0] == 'true'):
                    print('[+] Case 2 Possible.The entered url might be subject to misconfigured CORS exploitation')
                elif (dic.get('Access-Control-Allow-Origin:')[0] == '*' and dic.get('Access-Control-Allow-Credentials:')[0] == 'true'):
                    print('[+]Case 3 Possible.The entered url is not subject to misconfigured CORS exploitation')
                else:
                    print('[+] The entered url is not subject is not subject to misconfigured CORS exploitation')
            else:
                print('[+] The entered URL is not subject to misconfigured CORS exploitation')
        elif status_code>=300:
            print('[+] Not Applicable becauce of {} status code.'.format(status_code))
        else:
            print('[+] The entered URL is not subject to misconfigured CORS exploitation')
    cors(url,url1,origin)


def jsonconvert(url1):
    dict1={}
    with open("{}.txt".format(url1)) as f:
        for line in f:
            if line.strip():  # non-empty line?
                key, value = line.split(None, 1)  # None means 'all whitespace', the default
                if 'Link:' in dict1.keys() and key == 'Link:':
                    key = 'Link1:'
                dict1[key] = value.split()
    out = open("{}_response.json".format(url1), "w") 
    json.dump(dict1, out, indent = 4, sort_keys = False) 
    out.close()
    f= open('{}_response.json'.format(url1))
    dic = json.load(f)
    f.close()
    return dic

print("To check whether website is live: 1")
print("To check for subdomains and subomain takeover: 2")
print("To list directories: 3")
print("Check whether vulnerable to Clickjacking: 4")
print("Check whether vulnerable to misconfigured CORS: 5")
print("Check for all the above in the entered url: 6")
print("---Enter your Choice---")
flag=int(input())
if(flag == 1):
    live(url1)
elif(flag ==2):
    subdomain(url1)
    time.sleep(15)
    subdomain_takeover(url1)
elif(flag ==3):
    dir(url)
elif(flag ==4):
    clickjacking(url1)
elif(flag ==5):
    cors()
elif(flag ==6):
    live(url1)
    subdomain(url1)
    time.sleep(15)
    subdomain_takeover(url1)
    clickjacking(url1)
    cors()