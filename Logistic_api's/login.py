import requests
import json

test_cases_email = ['','     ','joeljustin@gmail.','joeljustin@gmail','joeljustin@.com','joeljustingmail.com','joel','joel#$%^@gamil.com','joel#justin@gmail.com',
                    'joeljustin@gmailcom','joel @gmail.com','joeljustin@ gmail.com','joeljustin@gmail com','joeljustin@gmail .com','joel justin@gmail.com','joeljustin@gmail.com    ',
                    'joeljustin@ .com','joeljustin@gmail.d','    joeljustin@gmail.com','@gmail.com','joeljustin@gmail\'com','joeljsutin@gmail@com','joeljustin@gmail)com',1234564]

test_cases_email_commands = ['null value for email','full of empty values','email without com','email without .com','email without gmail','email without @','without @gmail.com',
                             'with special characters','with one special char','email without dot','space before @gmail.com','space after @','space after gmail & no dot',
                             'space after gmail','space in between first name & last name','trailing spaces after email','space at the place of gmail','single char at the com place',
                             'starting spaces','only @gmail.com','single quotes at the place of dot','@ symbole at the place of dot','round bracket at the place of dot','integer data type']

print('-----------------------Passed Cases----------------------')
print('-------------------Checking Email-----------------------')

# print(len(test_cases_email),len(test_cases_email_commands))

for i in range(len(test_cases_email)):
    print(f'------------TestCase-{i+1}------------')
    print(f'Error : {test_cases_email_commands[i]}')
    try:
        val = {'data':{'email':test_cases_email[i],'pass':'123456'}}
        header = {'Content-type':'application/json','Accept':'text/plain'}
        r = requests.post('http://localhost:8888/login',data=json.dumps(val),headers=header)

        res = r.json().keys()

        if('error' in res):
            print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
        else:
            print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
        print('----------------------------------\n')

    except Exception as error:
        print('Exception Error',error)


print(f'------------TestCase-{len(test_cases_email)+1}-----------')
print(f'Error : without the email key')
try:
    val = {'data':{'pass':'123456'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/login',data=json.dumps(val),headers=header)

    res = r.json().keys()

    if('error' in res):
        print(f'password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
    print('Exception Error',error)


test_cases_password = ['','    ','12345']
test_cases_password_commands = ['null values of password','full of spaces','wrong length of password']

print('-------------------Checking Password-----------------------')

for i in range(len(test_cases_email),len(test_cases_email)+len(test_cases_password)):
    print(f'------------TestCase-{i+2}------------')
    print(f'Error : {test_cases_password_commands[i-len(test_cases_email)]}')
    try:
        val = {'data':{'email':'joeljustin@gmail.com','pass':test_cases_password[i-len(test_cases_email)]}}
        header = {'Content-type':'application/json','Accept':'text/plain'}
        r = requests.post('http://localhost:8888/login',data=json.dumps(val),headers=header)

        res = r.json().keys()

        if('error' in res):
            print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
        else:
            print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
        print('----------------------------------\n')

    except Exception as error:
        print('Exception Error',error)
    

print(f'------------TestCase-{(len(test_cases_email)+2) + (len(test_cases_password))}------------')
print(f'Error : without the password value')
try:
    val = {'data':{'email':'joeljustin@gmail.com'}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/login',data=json.dumps(val),headers=header)

    res = r.json().keys()

    if('error' in res):
        print(f'email : \'{val["data"]["email"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["data"]["email"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
    print('Exception Error',error)

print(f'------------TestCase-{(len(test_cases_email)+3) + (len(test_cases_password))}------------')
print(f'Error : both null value')
try:
    val = {'data':{'email':'','pass':''}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/login',data=json.dumps(val),headers=header)

    res = r.json().keys()

    if('error' in res):
        print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
    print('Exception Error',error)

print(f'------------TestCase-{(len(test_cases_email)+4) + (len(test_cases_password))}------------')
print(f'Error : both values full of spaces')
try:
    val = {'data':{'email':'     ','pass':'     '}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/login',data=json.dumps(val),headers=header)

    res = r.json().keys()

    if('error' in res):
        print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
    else:
        print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
    print('Exception Error',error)

print(f'------------TestCase-{(len(test_cases_email)+5) + (len(test_cases_password))}------------')
print(f'Error : without the whole object')
try:
    val = {'data':{}}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/login',data=json.dumps(val),headers=header)

    res = r.json().keys()

    if('error' in res):
        print('{data:{}} \nStatus : passed')
    else:
        print('{data:{}} \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
    print('Exception Error',error)

print(f'------------TestCase-{(len(test_cases_email)+6) + (len(test_cases_password))}------------')
print(f'Error : without the whole object')
try:
    val = {}
    header = {'Content-type':'application/json','Accept':'text/plain'}
    r = requests.post('http://localhost:8888/login',data=json.dumps(val),headers=header)

    res = r.json().keys()

    if('error' in res):
        print('{} \nStatus : passed')
    else:
        print('{} \nStatus : failed')
    print('----------------------------------\n')

except Exception as error:
    print('Exception Error',error)


test_cases_email_failed = ['12joel@gmail.com','joel1234@gmail.com','joel@gmail.com','joel@hotmail.in','joeljustin@yahoo.org','joeljustin@yahoo.in','joel.justin@gmail.com',
                           'joeljustin@renambl.com','joeljustin@gmail.com',]

test_cases_email_failed_commands = ['start value is number','inbetween value in number','four char value','hotmail.in extension','yahoo.org extension','yahoo.in extension',
                                    'including dot','renambl.com extension','normal email formate']

print('-----------------------Failed Cases----------------------')
print('-------------------Checking Email-----------------------')
# print(len(test_cases_email)+len(test_cases_password),len(test_cases_email_failed))
for i in range(len(test_cases_email)+len(test_cases_password),len(test_cases_email_failed)+len(test_cases_email)+len(test_cases_password)):
    print(f'------------TestCase-{i+7}------------')
    print(f'Success : {test_cases_email_failed_commands[i-(len(test_cases_email)+len(test_cases_password))]}')
    try:
        val = {'data':{'email':test_cases_email_failed[i-(len(test_cases_email)+len(test_cases_password))],'pass':'123456'}}
        header = {'Content-type':'application/json','Accept':'text/plain'}
        r = requests.post('http://localhost:8888/login',data=json.dumps(val),headers=header)

        res = r.json().keys()

        if('success' in res):
            print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
        else:
            print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
        print('----------------------------------\n')

    except Exception as error:
        print('Exception Error',error)


test_cases_pass_failed = ['123456','12345joel','!@#$%^&*()_+=-','123joel!@#$','123456  ',]

test_cases_pass_failed_commands = ['correct length','integer plus string','full of special character','number,string,special char','accept spaces as a password']

print('-------------------Checking password-----------------------')

for i in range(42,42+len(test_cases_pass_failed)):
    print(f'------------TestCase-{i+1}------------')
    print(f'Success : {test_cases_pass_failed_commands[i-42]}')
    try:
        val = {'data':{'email':'joeljustin@gmail.com','pass':test_cases_pass_failed[i-42]}}
        header = {'Content-type':'application/json','Accept':'text/plain'}
        r = requests.post('http://localhost:8888/login',data=json.dumps(val),headers=header)

        res = r.json().keys()

        if('success' in res):
            print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : failed')
        else:
            print(f'email : \'{val["data"]["email"]}\' password : \'{val["data"]["pass"]}\' \nStatus : passed')
        print('----------------------------------\n')

    except Exception as error:
        print('Exception Error',error)