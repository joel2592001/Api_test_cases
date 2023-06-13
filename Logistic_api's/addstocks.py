import requests
import json

print('-----------------------------------Passed Cases-----------------------------------')

print('-----------------------------------testing email-----------------------------------')

print('--------------Test Case - 1-------------')
print('Error Type : empty email value')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":''}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 2-------------')
print('Error Type : empty email')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'    '}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 3-------------')
print('Error Type : empty email')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@ gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 4-------------')
print('Error Type : starting spaces in email')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'   joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 5-------------')
print('Error Type : trailing spaces in email')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@gmail.com   '}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 6-------------')
print('Error Type : without com')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@gmail.'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 7-------------')
print('Error Type : without .com')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@gmail'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 8-------------')
print('Error Type : without gmail')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 9-------------')
print('Error Type : without @')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustingmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 10-------------')
print('Error Type : without @gmail.com')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joel'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 11-------------')
print('Error Type : special characters')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joel#$%^@gamil.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 12-------------')
print('Error Type : single special characters')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joel#justin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 13-------------')
print('Error Type : without dot after gmail')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@gmailcom'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 14-------------')
print('Error Type : space before @gmail.com')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joel @gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 15-------------')
print('Error Type : space after gmail & not contain dot')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@gmail com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 16-------------')
print('Error Type : space after gmail')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@gmail .com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 17-------------')
print('Error Type : space inbetween firstname and lastname')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joel justin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 18-------------')
print('Error Type : space for gmail')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@ .com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')
  
print('--------------Test Case - 19-------------')
print('Error Type : single letter for com at the end')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@gmail.d'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 20-------------')
print('Error Type : only @gmail.com')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 21-------------')
print('Error Type : single quotes after gmail instead of dot')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@gmail\'com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 22-------------')
print('Error Type : @ symbole after gmail ,instead of dot')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljsutin@gmail@com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 23-------------')
print('Error Type :  round bracket after gmail ,instead of dot')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@gmail)com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 24-------------')
print('Error Type :  without the email data')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('-------------------------------------testing stock name-----------------------------------')

print('--------------Test Case - 25-------------')
print('Error Type :  empty value for name')
try:
    val = {"data":{"name":'','quantity':'10','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 26-------------')
print('Error Type : full of spaces')
try:
    val = {"data":{"name":'    ','quantity':'10','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 27-------------')
print('Error Type : empty value for name')
try:
    val = {"data":{"name":'      ','quantity':'10','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 28-------------')
print('Error Type : number values')
try:
    val = {"data":{"name":'1234567','quantity':'10','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 29-------------')
print('Error Type : integer data type')
try:
    val = {"data":{"name":123456,'quantity':'10','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 30-------------')
print('Error Type : wrong length of name')
try:
    val = {"data":{"name":'as','quantity':'10','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')


print('-------------------------------------testing stock quantity-----------------------------------')

print('--------------Test Case - 31-------------')
print('Error Type : string instead of integer')
try:
    val = {"data":{"name":'tomato','quantity':'joel','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 32-------------')
print('Error Type : special character instead of integer')
try:
    val = {"data":{"name":'tomato','quantity':'@#$%^','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 33-------------')
print('Error Type : empty value for quantity')
try:
    val = {"data":{"name":'tomato','quantity':'','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 34-------------')
print('Error Type : full of empty spaces')
try:
    val = {"data":{"name":'tomato','quantity':'    ','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')
  
print('--------------Test Case - 35-------------')
print('Error Type : starting spaces')
try:
    val = {"data":{"name":'tomato','quantity':'  12','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 36-------------')
print('Error Type : ending spaces')
try:
    val = {"data":{"name":'tomato','quantity':'12  ','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 37-------------')
print('Error Type : without quantity data')
try:
    val = {"data":{"name":'tomato','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 38-------------')
print('Error Type : lesser than one')
try:
    val = {"data":{"name":'tomato','quantity':'0','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 39-------------')
print('Error Type : Negattive value')
try:
    val = {"data":{"name":'tomato','quantity':'-1','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 40-------------')
print('Error Type : Maximum value for quantity')
try:
    val = {"data":{"name":'tomato','quantity':'10000000','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')


print('-------------------------------------testing stock id-----------------------------------')

print('--------------Test Case - 41-------------')
print('Error Type : string instead of integer')
try:
    val = {"data":{"name":'tomato','id':'joel','quantity':'20'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 42-------------')
print('Error Type : special character instead of integer')
try:
    val = {"data":{"name":'tomato','id':'@#$%^','quantity':'20'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 43-------------')
print('Error Type : empty value for id')
try:
    val = {"data":{"name":'tomato','id':'','quantity':'20'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 44-------------')
print('Error Type : full of empty spaces')
try:
    val = {"data":{"name":'tomato','id':'    ','quantity':'20'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')
  
print('--------------Test Case - 45-------------')
print('Error Type : starting spaces')
try:
    val = {"data":{"name":'tomato','id':'  12','quantity':'20'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 46-------------')
print('Error Type : ending spaces')
try:
    val = {"data":{"name":'tomato','id':'12  ','quantity':'20'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 47-------------')
print('Error Type : without id data')
try:
    val = {"data":{"name":'tomato','quantity':'20'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 48-------------')
print('Error Type : lesser than one')
try:
    val = {"data":{"name":'tomato','id':'0','quantity':'20'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 49-------------')
print('Error Type : Negattive value')
try:
    val = {"data":{"name":'tomato','id':'-1','quantity':'20'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 50-------------')
print('Error Type : Maximum length for id')
try:
    val = {"data":{"name":'tomato','id':'10000000','quantity':'20'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('------------------------------combain testing-----------------------------')

print('--------------Test Case - 51-------------')
print('Error Type : all null values')
try:
    val = {"data":{"name":'','id':'','quantity':''},"log_id":''}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 52-------------')
print('Error Type : all data filled with empty spaces ')
try:
    val = {"data":{"name":'     ','id':'     ','quantity':'      '},"log_id":'      '}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 53-------------')
print('Error Type : without data object ')
try:
    val = {"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 54-------------')
print('Error Type : without any data')
try:
    val = {}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print('{} \nStatus : passed')
    else:
       print('{} \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 55-------------')
print('Error Type : without name data')
try:
    val = {"data":{'quantity':'10','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    else:
       print(f'quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')


print('---------------------------------------Failed Test Cases--------------------------------------')

print('-----------------------------------Testing Email------------------------------------')

print('--------------Test Case - 56-------------')
print('Success Type : Actual email formate')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 57-------------')
print('Success Type : starting with number')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'12joel@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 58-------------')
print('Success Type : inbetween numbers')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joel1234@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 59-------------')
print('Success Type : only one letter for email')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'j@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 60-------------')
print('Success Type : hotmail.in extension')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joel@hotmail.in'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 61-------------')
print('Success Type : yahoo.org extension')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@yahoo.org'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 62-------------')
print('Success Type : yahoo.in extension')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@yahoo.in'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 63-------------')
print('Success Type : included dot in email name')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joel.justin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 64-------------')
print('Success Type : renambl.com extension')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@renambl.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')


print('-----------------------------------Testing Name------------------------------------')

print('--------------Test Case - 65-------------')
print('Success Type : normal name')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'123'},"log_id":'joeljustin@renambl.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 66-------------')
print('Success Type : space after first word')
try:
    val = {"data":{"name":'sweet potato','quantity':'10','id':'123'},"log_id":'joeljustin@renambl.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 67-------------')
print('Success Type : Minimum length of name')
try:
    val = {"data":{"name":'bun','quantity':'10','id':'123'},"log_id":'joeljustin@renambl.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')


print('-----------------------------------Testing Quantity------------------------------------')

print('--------------Test Case - 68-------------')
print('Success Type : minimum quantity')
try:
    val = {"data":{"name":'tomato','quantity':'1','id':'123'},"log_id":'joeljustin@renambl.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 69-------------')
print('Success Type : maximum quantity')
try:
    val = {"data":{"name":'tomato','quantity':'1000000','id':'123'},"log_id":'joeljustin@renambl.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('-----------------------------------Testing id------------------------------------')

print('--------------Test Case - 69-------------')
print('Success Type : minimum id no')
try:
    val = {"data":{"name":'tomato','quantity':'20','id':'1'},"log_id":'joeljustin@renambl.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 70-------------')
print('Success Type : maximum id no')
try:
    val = {"data":{"name":'tomato','quantity':'10','id':'100000'},"log_id":'joeljustin@renambl.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/addstocks',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : failed')
    else:
       print(f'stock_name : \'{val["data"]["name"]}\', quantity : \'{val["data"]["quantity"]}\', stock id : \'{val["data"]["id"]}\', email : \'{val["log_id"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')