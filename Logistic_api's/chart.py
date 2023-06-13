import requests
import json

try:
    val = {'id':''}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-1----------')
    print('Error : email is a null value')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 1')

try:
    val = {'id':'     '}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-2----------')
    print('error : only empty spaces')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed ')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 2')

try:
    val = {'id':'joeljusting@gmail.com     '}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-3----------')
    print('error : trailing spaces after the value')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 3')

try:
    val = {'id':'     joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-4----------')
    print('error : starting spaces before value')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 4')

try:
    val = {}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-5----------')
    print('error : totall empty data')
    if('error' in res):
        print('email : {} \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
  print('Exception Error : 5')

try:
    val = {'id':'joel@gmail.'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-6----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 6')

try:
    val = {'id':'joel@gmail'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-7----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 7')

try:
    val = {'id':'joel@.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-8----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 8')

try:
    val = {'id':'joeljustingmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-9----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 9')

try:
    val = {'id':'joeljustin'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-10----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 10')

try:
    val = {'id':'joeljustin!#$%^&@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-11----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 11')

try:
    val = {'id':'joel#justin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-12----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 12')

try:
    val = {'id':'joeljustin@gmailcom'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-13----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 13')

try:
    val = {'id':'joel @gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-14----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 14')

try:
    val = {'id':'joel@ gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-15----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 15')

try:
    val = {'id':'joel@gmail .com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-16----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 16')

try:
    val = {'id':'joeljustin@gmail com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-17----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 17')

try:
    val = {'id':'joel justin@gmail com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-18----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 18')

try:
    val = {'id':'joeljustin@gmail.c'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-19----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 19')

try:
    val = {'id':'@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-20----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 20')

try:
    val = {'id':'joeljustin@'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-21----------')
    print('error : wrong email formate')
    if('error' in res):
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 21')

print('---------------------failed_cases----------------------')
try:
    val = {'id':'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-22----------')
    print('success : Correct email formate')
    if('success' in res):
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 22')

try:
    val = {'id':'123joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-23----------')
    print('success : Correct email formate')
    if('success' in res):
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 23')

try:
    val = {'id':'joel1234@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-24----------')
    print('success : Correct email formate')
    if('success' in res):
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 24')

try:
    val = {'id':'j@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-25----------')
    print('success : Correct email formate')
    if('success' in res):
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 25')

try:
    val = {'id':'joel@hotmail.in'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-26----------')
    print('success : Correct email formate')
    if('success' in res):
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 26')

try:
    val = {'id':'joel.justin@hotmail.in'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-27----------')
    print('success : Correct email formate')
    if('success' in res):
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 27')

try:
    val = {'id':'joeljustin@renambl.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/chart',data=json.dumps(val),headers=header)

    res = r.json().keys()

    print('----------TestCase-28----------')
    print('success : Correct email formate')
    if('success' in res):
        print(f'email : \'{val["id"]}\' \nStatus : failed')
    else:
        print(f'email : \'{val["id"]}\' \nStatus : passed')
    print('--------------------------------\n')

except Exception as error:
  print('Exception Error : 28')



