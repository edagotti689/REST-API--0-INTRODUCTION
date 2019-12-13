import requests

## To get all emp details
res = requests.get('http://127.0.0.1:5000/get')
#print('\n response code is :', res.status_code)
#print('\n EMP details are :', res.json())


## To create new emp record
# r = requests.post('http://127.0.0.1:5000/create', json={"DID":555})
# r_data = r.json()
# did = r_data['DID']
# assert did == 555 , ' HTTP POST method is not working'
# print('\n POST is :', r_data)


## To Update emp 
#r = requests.put('http://127.0.0.1:5000/update', json={"EID":999})
#print('\n update is :', r.text)


## To Delete emp 
r = requests.delete('http://127.0.0.1:5000/delete', json={"DID":"50000"})
#print(dir(r))
print('\n response code is :', r.status_code)
assert r.status_code == 200 , ' Not able to process request'
print('\n Deleted is :', r.text)
