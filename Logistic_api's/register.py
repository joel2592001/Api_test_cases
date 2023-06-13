import requests
import json

print('-----------------------Passed Cases----------------------')
print('-------------------Checking Name-----------------------')
try:
    val = {'data':{'name':'','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-1----------')
    print('Error : name is a null value')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 1')

try:
    val = {'data':{'name':'     ','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-2----------')
    print('Error : name is a undefined value')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 2')

try:
    val = {'data':{'name':'   joel','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-3----------')
    print('Error : spaces before value')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 3')

try:
    val = {'data':{'name':'joel    ','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-4----------')
    print('Error : spaces after value')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 4')

try:
    val = {'data':{'name':'joel1234','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-5----------')
    print('Error : name cant contain numbers')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 5')

try:
    val = {'data':{'name':'jo','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-6----------')
    print('Error : minimu characters of name')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 6')

try:
    val = {'data':{'name':'joel@*#*','email':'joeljustin@gmail.com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-7----------')
    print('Error : cant contain special char')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 7')

try:
    val = {'data':{'email':'joeljustin@gmail.com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-8----------')
    print('Error : giving without name value')
    if('error' in res):
        print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 8')

try:
    val = {'data':{'name':'joel justin ','email':'joeljustin@gmail.com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-9----------')
    print('Error : giving space after first name and end of value')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 9')

print('--------------------------Checking Email---------------------------')

try:
    val = {'data':{'name':'joeljustin','email':'','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-10----------')
    print('Error : email is a null value')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 10')

try:
    val = {'data':{'name':'joeljustin','email':'     ','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-11----------')
    print('Error : full of empty spaces')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 11')

try:
    val = {'data':{'name':'joeljustin','email':'joeljusting@gmail.com     ','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-12----------')
    print('Error : empty spaces after value')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 12')

try:
    val = {'data':{'name':'joeljustin','email':'    joeljusting@gmail.com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-13----------')
    print('Error : empty spaces before value')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 13')

try:
    val = {'data':{'name':'joeljustin','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-14----------')
    print('Error : without email value')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 14')

try:
    val = {'data':{'name':'joeljustin','email':'joel@gmail.','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-15----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 15')

try:
    val = {'data':{'name':'joeljustin','email':'joel@gmail','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-16----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 16')

try:
    val = {'data':{'name':'joeljustin','email':'joel@.com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-17----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 17')

try:
    val = {'data':{'name':'joeljustin','email':'joeljustingmail.com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-18----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 18')

try:
    val = {'data':{'name':'joeljustin','email':'joeljustin','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-19----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 19')

try:
    val = {'data':{'name':'joeljustin','email':'joeljustin!#$%^&@gmail.com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-20----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 20')

try:
    val = {'data':{'name':'joeljustin','email':'joel#justin@gmail.com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-21----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 21')

try:
    val = {'data':{'name':'joeljustin','email':'joeljustin@gmailcom','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-22----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 22')

try:
    val = {'data':{'name':'joeljustin','email':'joel @gmail.com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-23----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 23')

try:
    val = {'data':{'name':'joeljustin','email':'joel@ gmail.com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-24----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 24')

try:
    val = {'data':{'name':'joeljustin','email':'joel@gmail .com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-25----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 25')

try:
    val = {'data':{'name':'joeljustin','email':'joeljustin@gmail com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-26----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 26')

try:
    val = {'data':{'name':'joeljustin','email':'joel justin@gmail com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-27----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 27')

try:
    val = {'data':{'name':'joeljustin','email':'joeljustin@gmail.c','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-28----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 28')

try:
    val = {'data':{'name':'joeljustin','email':'@gmail.com','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-29----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 29')

try:
    val = {'data':{'name':'joeljustin','email':'joeljustin@','pass':'1234567'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-30----------')
    print('Error : wrong email formate')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 30')

print('-----------------------------Testing password----------------------------')

try:
    val = {'data':{'name':'joeljustin','email':'joeljustin@gmail.com','pass':''}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-31----------')
    print('Error : null password')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 31')

try:
    val = {'data':{'name':'joeljustin','email':'joeljustin@gmail.com','pass':'      '}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-32----------')
    print('Error : full of spaces')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 32')

try:
    val = {'data':{'name':'joeljustin','email':'joeljustin@gmail.com'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-33----------')
    print('Error : without password value')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 33')


print('------------------------Failed Cases---------------------------')

print('-------------------Testing Name------------------')

try:
    val = {'data':{'name':'joeljustin','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-34----------')
    print('Success : correct name formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 34')

try:
    val = {'data':{'name':'joel justin','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-35----------')
    print('Success : correct name formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 35')

try:
    val = {'data':{'name':'JOEL','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-36----------')
    print('Success : correct name formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 36')

try:
    val = {'data':{'name':'JOE','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-37----------')
    print('Success : correct name formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 37')

try:
    val = {'data':{'name':'Joel Justin','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-38----------')
    print('Success : correct name formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 38')

  print('------------------------Testing Email-------------------------')

try:
    val = {'data':{'name':'joel','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-39----------')
    print('Success : correct email formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 39')

try:
    val = {'data':{'name':'joel','email':'123joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-40----------')
    print('Success : correct email formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 40')

try:
    val = {'data':{'name':'joel','email':'joeljustin1234@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-41----------')
    print('Success : correct email formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 41')

try:
    val = {'data':{'name':'joel','email':'joeljustin@hotmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-42----------')
    print('Success : correct email formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 42')

try:
    val = {'data':{'name':'joel','email':'joeljustin@hotmail.in','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-43----------')
    print('Success : correct email formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 43')

try:
    val = {'data':{'name':'joel','email':'joeljustin@yahoo.org','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-44----------')
    print('Success : correct email formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 44')

try:
    val = {'data':{'name':'joel','email':'joel.justin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-45----------')
    print('Success : correct email formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 45')

try:
    val = {'data':{'name':'joel','email':'joel-justin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-46----------')
    print('Success : correct email formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 46')

try:
    val = {'data':{'name':'joel','email':'joel-justin@renambl.in','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-47----------')
    print('Success : correct email formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 47')


print('--------------------------Testing password----------------------')

try:
    val = {'data':{'name':'joel','email':'joeljustin@gmail.com','pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-48----------')
    print('Success : correct password formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 48')

try:
    val = {'data':{'name':'joel','email':'joeljustin@gmail.com','pass':'123456joel'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-49----------')
    print('Success : correct password formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 49')

try:
    val = {'data':{'name':'joel','email':'joeljustin@gmail.com','pass':'!@#$%^&*()_+='}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-50----------')
    print('Success : correct password formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 50')

try:
    val = {'data':{'name':'joel','email':'joeljustin@gmail.com','pass':'123456!@#$joel'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-51----------')
    print('Success : correct password formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 51')

try:
    val = {'data':{'name':'joel','email':'joeljustin@gmail.com','pass':'123456   '}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-52----------')
    print('Success : correct password formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 52')

try:
    val = {'data':{'name':'joel','email':'joeljustin@gmail.com','pass':'123456   joel'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-53----------')
    print('Success : correct password formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 53')

try:
    val = {'data':{'name':'joel','email':'joeljustin@gmail.com','pass':'joelju'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-54----------')
    print('Success : correct password formate')
    if('success' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 54')


print('-----------------Added extra passed test cases---------------')

try:
    val = {'data':{'name':'','email':'','pass':''}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('---------TestCase-55----------')
    print('Error : All null value')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 55')

try:
    val = {'data':{'name':'     ','email':'     ','pass':'    '}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('---------TestCase-56----------')
    print('Error : all empty spaces')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 56')

try:
    val = {'data':{}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('---------TestCase-57----------')
    print('Error : without the whole object')
    if('error' in res):
        print('{data:{}} \nStatus : passed')
    else:
        print('{data:{}} \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 57')

try:
    val = {}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    req = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    re = req.json().keys()

    # print(req.json())
    print('---------TestCase-58----------')
    print('Error : without the whole body')
    if('error' in re):
        print('{} \nStatus : passed')
    else:
        print('{} \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 58')

try:
    val = {'data':{'name':'joel'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    req = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    re = req.json().keys()

    # print(req.json())
    print('---------TestCase-59----------')
    print('Error : without the whole body')
    if('error' in re):
        print(f'name : \'{val["data"]["name"]}\' \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 59')

try:
    val = {'data':{'name':'joel','email':'joel@gmail.com','pass':1234567}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/register',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('---------TestCase-60----------')
    print('Error : integer datatype password')
    if('error' in res):
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : {val["data"]["pass"]} \nStatus : passed')
    else:
        print(f'name : \'{val["data"]["name"]}\' email : \'{val["data"]["email"]}\' password : {val["data"]["pass"]} \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 60')