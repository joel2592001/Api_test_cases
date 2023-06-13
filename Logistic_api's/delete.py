import requests
import json

email = ['','     ','joeljustin@gmail.','joeljustin@gmail','joeljustin@.com','joeljustingmail.com','joel','joel#$%^@gamil.com','joel#justin@gmail.com',
                    'joeljustin@gmailcom','joel @gmail.com','joeljustin@ gmail.com','joeljustin@gmail com','joeljustin@gmail .com','joel justin@gmail.com','joeljustin@gmail.com    ',
                    'joeljustin@ .com','joeljustin@gmail.d','    joeljustin@gmail.com','@gmail.com','joeljustin@gmail\'com','joeljsutin@gmail@com','joeljustin@gmail)com',1234564]

email_commands = ['null value for email','full of empty values','email without com','email without .com','email without gmail','email without @','without @gmail.com',
                             'with special characters','with one special char','email without dot','space before @gmail.com','space after @','space after gmail & no dot',
                             'space after gmail','space in between first name & last name','trailing spaces after email','space at the place of gmail','single char at the com place',
                             'starting spaces','only @gmail.com','single quotes at the place of dot','@ symbole at the place of dot','round bracket at the place of dot','integer data type']

print('-----------------------------------Passed Cases----------------------------')

print('-----------------------------------testing Edit Name----------------------------')


for i in range(len(email)):
    print(f'--------------Test Case - {i+1}-------------')
    print(f'Error Type : {email_commands[i]}')
    try:
        val = {'id':email[i],'delete':'tomato'}
        header = {'Content-type':'application/json','Accept':'text/plain'}
        r = requests.post('http://localhost:8888/delete',data=json.dumps(val),headers=header)
        # print(list(r.json().keys())[0])
        res = r.json().keys()
        
        if('error' in res):
            print(f'Email : \'{val["id"]}\', Delete_name : \'{val["delete"]}\' \nStatus : passed')
        else:
            print(f'Email : \'{val["id"]}\', Delete_name : \'{val["delete"]}\' \nStatus : failed')
        print('-----------------------------------------\n')
    
    except Exception as error:
        print('Exception Error :',error)
        print('-----------------------------------------\n')

print(f'--------------Test Case - {len(email)+1}-------------')
print(f'Error Type : without email data')
try:
    val = {'delete':'tomato'}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/delete',data=json.dumps(val),headers=header)
    # print(list(r.json().keys())[0])
    res = r.json().keys()
    
    if('error' in res):
        print(f'Delete_name : \'{val["delete"]}\' \nStatus : passed')
    else:
        print(f'Delete_name : \'{val["delete"]}\' \nStatus : failed')
    print('-----------------------------------------\n')

except Exception as error:
    print('Exception Error :',error)
    print('-----------------------------------------\n')


delete = ['','    ','   tomato','tomato   ','12345','!@#$%^&*()-','tomato12345',123456,'to','sweet potato ']

delete_commands = ['null value for name','full of empty spaces','spaces before value','spaces after value','given number instead of string',
                   'full of special characters','number in name','integer data type','minimum length','space after the first name and last name']



print('-----------------------------------testing Edit Delete name----------------------------')

for i in range(len(email),len(email)+len(delete)):
    print(f'--------------Test Case - {i+2}-------------')
    print(f'Error Type : {delete_commands[i-len(email)]}')
    try:
        val = {'id':'joeljustin@gmail.com','delete':delete[i-len(email)]}
        header = {'Content-type':'application/json','Accept':'text/plain'}
        r = requests.post('http://localhost:8888/delete',data=json.dumps(val),headers=header)
        # print(list(r.json().keys())[0])
        res = r.json().keys()
        
        if('error' in res):
            print(f'Email : \'{val["id"]}\', Delete_name : \'{val["delete"]}\' \nStatus : passed')
        else:
            print(f'Email : \'{val["id"]}\', Delete_name : \'{val["delete"]}\' \nStatus : failed')
        print('-----------------------------------------\n')
    
    except Exception as error:
        print('Exception Error :',error)
        print('-----------------------------------------\n')