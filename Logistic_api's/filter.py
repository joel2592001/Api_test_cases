import requests
import json

print('-----------------------------------Passed Cases----------------------------')

print('-----------------------------------testing date----------------------------')

print('--------------Test Case - 1-------------')
print('Error Type : null value for date')
try:
    val = {"date":'','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 2-------------')
print('Error Type : full of empty spaces')
try:
    val = {"date":'       ','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)

print('--------------Test Case - 3-------------')
print('Error Type : wrong length for year in date')
try:
    val = {"date":'201/05/25','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 4-------------')
print('Error Type : string for date')
try:
    val = {"date":'joel','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 5-------------')
print('Error Type : integer datatype')
try:
    val = {"date":1234567,'id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 6-------------')
print('Error Type : wrong length for month in date')
try:
    val = {"date":'2001/1/25','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 7-------------')
print('Error Type : wrong length for day in date')
try:
    val = {"date":'2001/01/5','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 8-------------')
print('Error Type : dd/mm/yyyy formate')
try:
    val = {"date":'25/09/2001','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 9-------------')
print('Error Type : starting spaces in date')
try:
    val = {"date":'   2001/03/25','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 10-------------')
print('Error Type : ending spaces in date')
try:
    val = {"date":'2001/03/25    ','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 11-------------')
print('Error Type : without the date data')
try:
    val = {'id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')


print('-----------------------------------Passed Cases----------------------------')

print('-----------------------------------testing date----------------------------')

print('--------------Test Case - 12-------------')
print('Error Type : null value for date')
try:
    val = {"date":'','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 13-------------')
print('Error Type : full of empty spaces')
try:
    val = {"date":'       ','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)

print('--------------Test Case - 14-------------')
print('Error Type : wrong length for year in date')
try:
    val = {"date":'201/05/25','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 15-------------')
print('Error Type : string for date')
try:
    val = {"date":'joel','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 16-------------')
print('Error Type : integer datatype')
try:
    val = {"date":1234567,'id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 17-------------')
print('Error Type : wrong length for month in date')
try:
    val = {"date":'2001/1/25','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 18-------------')
print('Error Type : wrong length for day in date')
try:
    val = {"date":'2001/01/5','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 19-------------')
print('Error Type : dd/mm/yyyy formate')
try:
    val = {"date":'25/09/2001','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 20-------------')
print('Error Type : starting spaces in date')
try:
    val = {"date":'   2001/03/25','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 21-------------')
print('Error Type : trailing spaces in date')
try:
    val = {"date":'2001/03/25    ','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 22-------------')
print('Error Type : without the date data')
try:
    val = {'id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('---------------------------------------------testing email-----------------------------------------')

print('--------------Test Case - 23-------------')
print('Error Type : null value for email')
try:
    val = {"date":'2001/03/25','id':'','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 24-------------')
print('Error Type : full of empty spaces')
try:
    val = {"date":'2001/03/25','id':'      ','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 25-------------')
print('Error Type : without com extension')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail.','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 26-------------')
print('Error Type : without .com extension')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 27-------------')
print('Error Type : without @ extension')
try:
    val = {"date":'2001/03/25','id':'joeljustingmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 28-------------')
print('Error Type : without @gmail.com extension')
try:
    val = {"date":'2001/03/25','id':'joel','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 29-------------')
print('Error Type : including special characters')
try:
    val = {"date":'2001/03/25','id':'joel#$%^@gamil.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 30-------------')
print('Error Type : including single special characters')
try:
    val = {"date":'2001/03/25','id':'joel#justin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 31-------------')
print('Error Type : without dot before com')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmailcom','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 32-------------')
print('Error Type : space before @gmail.com')
try:
    val = {"date":'2001/03/25','id':'joel @gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 33-------------')
print('Error Type : space after @')
try:
    val = {"date":'2001/03/25','id':'joeljustin@ gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 34-------------')
print('Error Type : space after @gmai instead of dot')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 35-------------')
print('Error Type : space after @gmai')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail .com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 36-------------')
print('Error Type : space inbetween firstname and last name')
try:
    val = {"date":'2001/03/25','id':'joel justin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 37-------------')
print('Error Type : starting spaces before email')
try:
    val = {"date":'2001/03/25','id':'     joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 38-------------')
print('Error Type : ending spaces after email')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail.com    ','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 39-------------')
print('Error Type : spaces at the place of gmail')
try:
    val = {"date":'2001/03/25','id':'joeljustin@ .com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 40-------------')
print('Error Type : without name before @gmail.com')
try:
    val = {"date":'2001/03/25','id':'@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \'{val["id"]}\', Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 41-------------')
print('Error Type : single quotes at the place of dot')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail\'com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 42-------------')
print('Error Type : special character at the place dot')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail)com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 43-------------')
print('Error Type : @ symbole at the place dot')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail@com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 44-------------')
print('Error Type : spaces at the place of email name')
try:
    val = {"date":'2001/03/25','id':'   @gmail@com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')


print('-----------------------------------testing filter type----------------------------')

print('--------------Test Case - 45-------------')
print('Error Type : null value for type')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail.com','filter_type':''}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 46-------------')
print('Error Type : apace values for type')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail.com','filter_type':'    '}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 47-------------')
print('Error Type : starting spaces before type')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail.com','filter_type':'    added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 48-------------')
print('Error Type : ending spaces after type')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail.com','filter_type':'added    '}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 49-------------')
print('Error Type : special characters in type')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail.com','filter_type':'!@#$%^&*()'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 50-------------')
print('Error Type : integer data type')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail.com','filter_type':1234567}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 51-------------')
print('Error Type : without the filter data')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail.com'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\" \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\" \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')


print('--------------Test Case - 52-------------')
print('Error Type : integer data type')
try:
    val = {"date":'2001/03/25','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 53-------------')
print('Error Type : all data empty values')
try:
    val = {"date":'','id':'','filter_type':''}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 54-------------')
print('Error Type : all data empty spaces')
try:
    val = {"date":'    ','id':'    ','filter_type':'    '}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 55-------------')
print('Error Type : without the whole data')
try:
    val = {}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
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


print('-----------------------------------Failed Cases----------------------------')

print('-----------------------------------testing date----------------------------')


print('--------------Test Case - 56-------------')
print('Success Type : hyphen inbetween date')
try:
    val = {"date":'2001-09-25','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')


print('-----------------------------------testing email----------------------------')

print('--------------Test Case - 57-------------')
print('Success Type : hyphen inbetween date')
try:
    val = {"date":'2001-09-25','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 58-------------')
print('Success Type : starting with number')
try:
    val = {"date":'2001-09-25','id':'123joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 59-------------')
print('Success Type : inbetween numbers')
try:
    val = {"date":'2001-09-25','id':'joeljustin1234@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 60-------------')
print('Success Type : minimum char in email name')
try:
    val = {"date":'2001-09-25','id':'j@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 61-------------')
print('Success Type : hotmail.in extension email formate')
try:
    val = {"date":'2001-09-25','id':'joeljustin@hotmail.in','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 62-------------')
print('Success Type : yahoo.org extension email formate')
try:
    val = {"date":'2001-09-25','id':'joeljustin@yahoo.org','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 63-------------')
print('Success Type : yahoo.in extension email formate')
try:
    val = {"date":'2001-09-25','id':'joeljustin@yahoo.in','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 64-------------')
print('Success Type : dot inbetween firstname and last name')
try:
    val = {"date":'2001-09-25','id':'joel.justin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 65-------------')
print('Success Type : @renamble.com extension')
try:
    val = {"date":'2001-09-25','id':'joeljustin@renambl.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 66-------------')
print('Success Type : @renamble.com extension')
try:
    val = {"date":'2001-09-25','id':'joeljustin@renambl.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('-----------------------------------testing filter type----------------------------')

print('--------------Test Case - 67-------------')
print('Success Type : name added')
try:
    val = {"date":'2001-09-25','id':'joeljustin@gmail.com','filter_type':'added'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

print('--------------Test Case - 68-------------')
print('Success Type : name delivery')
try:
    val = {"date":'2001-09-25','id':'joeljustin@gmail.com','filter_type':'delivery'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/filter',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('success' in res):
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : failed')
    else:
       print(f'Date : \'{val["date"]}\', Email : \"{val["id"]}\", Filter_type : \'{val["filter_type"]}\' \nStatus : passed')
    print('-----------------------------------------\n')
   
except Exception as error:
  print('Exception Error :',error)
  print('-----------------------------------------\n')

