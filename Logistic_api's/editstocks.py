import requests
import json

print('-----------------------------------Passed Cases----------------------------')

print('-----------------------------------testing Edit Name----------------------------')


print('--------------Test Case - 1-------------')
print('Error Type : null value for name')
try:
    val = {'id':'joeljustin@gmail.com','edit':'','quantity':'20'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 2-------------')
print('Error Type : empty spaces for name')
try:
    val = {'id':'joeljustin@gmail.com','edit':'     ','quantity':'20'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 3-------------')
print('Error Type : space before value')
try:
    val = {'id':'joeljustin@gmail.com','edit':'     tomato','quantity':'20'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 4-------------')
print('Error Type : space after value')
try:
    val = {'id':'joeljustin@gmail.com','edit':'tomato    ','quantity':'20'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 5-------------')
print('Error Type : name contain numbers')
try:
    val = {'id':'joeljustin@gmail.com','edit':'tomato12345','quantity':'20'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 6-------------')
print('Error Type : minimum length for name')
try:
    val = {'id':'joeljustin@gmail.com','edit':'to','quantity':'20'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 7-------------')
print('Error Type : with special char')
try:
    val = {'id':'joeljustin@gmail.com','edit':'tomato!@#$%^&*()','quantity':'20'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 8-------------')
print('Error Type : without name data')
try:
    val = {'id':'joeljustin@gmail.com','quantity':'20'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 10-------------')
print('Error Type : giving space after end of value')
try:
    val = {'id':'joeljustin@gmail.com','edit':'sweet potato ','quantity':'20'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')


print('-----------------------------------testing Quantity----------------------------')

print('--------------Test Case - 11-------------')
print('Error Type : null spaces for quantity')
try:
    val = {'id':'joeljustin@gmail.com','edit':'sweet potato','quantity':''}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 12-------------')
print('Error Type : full of empty space value')
try:
    val = {'id':'joeljustin@gmail.com','edit':'sweet potato','quantity':'      '}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 13-------------')
print('Error Type : given letter instead of number')
try:
    val = {'id':'joeljustin@gmail.com','edit':'sweet potato','quantity':'joel'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 14-------------')
print('Error Type : given special char instead of number')
try:
    val = {'id':'joeljustin@gmail.com','edit':'sweet potato','quantity':'!@#$'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 15-------------')
print('Error Type : given space before value')
try:
    val = {'id':'joeljustin@gmail.com','edit':'sweet potato','quantity':' 20'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 16-------------')
print('Error Type : given space after value')
try:
    val = {'id':'joeljustin@gmail.com','edit':'sweet potato','quantity':'20 '}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 17-------------')
print('Error Type : without quantity data')
try:
    val = {'id':'joeljustin@gmail.com','edit':'sweet potato'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 18-------------')
print('Error Type : value less than one')
try:
    val = {'id':'joeljustin@gmail.com','edit':'sweet potato','quantity':'0'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 19-------------')
print('Error Type : maximum value for quantity')
try:
    val = {'id':'joeljustin@gmail.com','edit':'sweet potato','quantity':'10000000'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 20-------------')
print('Error Type : all null values')
try:
    val = {'id':'','edit':'','quantity':''}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 21-------------')
print('Error Type : all values filled with empty spaces')
try:
    val = {'id':'      ','edit':'      ','quantity':'      '}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 22-------------')
print('Error Type : all values filled with empty spaces')
try:
    val = {}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
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


print('---------------------------------------Failed Test Cases--------------------------------------')

print('-----------------------------------Testing Email------------------------------------')

print('--------------Test Case - 23-------------')
print('Error Type : ')
try:
    val = {'id':'joeljustin@gmail.com','edit':'tomato','quantity':'20'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/editstock',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Edit : \'{val["edit"]}\', Quantity : \'{val["quantity"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')