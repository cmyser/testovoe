

from django.http import JsonResponse
# Create your views here.
import requests as r
import json 








fixtura_users = r.get('http://jsonplaceholder.typicode.com/users')
fixtura_posts = r.get('http://jsonplaceholder.typicode.com/posts')

fix_users = fixtura_users.json()
fix_posts = fixtura_posts.json()




fix_mass = []
count = 1


for i in fix_users:
    comp = {'model': 'data_show.company'}
    comp['pk'] = count
    comp['fields'] = i['company']
    fix_mass.append(comp)
    

    geo = {'model': 'data_show.geo'}
    geo['pk'] = count
    geo['fields'] = i['address']['geo']
    fix_mass.append(geo)
    

    addr = {'model': 'data_show.address'}
    addr['pk'] = count
    del i['address']['geo']
    addr['fields'] = i['address']
    addr['fields']['geo'] = count
    fix_mass.append(addr)



  

    user = {'model': 'data_show.user'}
    d = {}
    user['pk'] = count
    d['name'] = i['name']
    d['username'] = i['username']
    d['email'] = i['email']
    d['address'] = count
    d['phone'] = i['phone']
    d['website'] = i['website']
    d['company'] = count

    user['fields'] = d
    fix_mass.append(user)
    
    count += 1
    comp = {}
    geo = {}
    addr = {}
    
    

cot = 1
fi = []
for i in fix_posts:
    fix = {'model': 'data_show.post'}
    del i['id']
    fix['pk'] = cot
    fix['fields'] = i
    fi.append(fix)


    fix = {}
    cot += 1
    
    





with open(r"fixtures/users.json", "w") as write_file:
    json.dump(fix_mass, write_file)

with open(r"fixtures/posts.json", "w") as write_file:
    json.dump(fi, write_file)