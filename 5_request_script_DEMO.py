import requests

#To get the emp details 
res = requests.get("http://127.0.0.1:5000/get")
print(" \n response code is :", res.status_code)
print(" \n EMP details are :", res.json())

# To create a new emp record
# res = requests.post('http://127.0.0.1:5000/create', json = {"Branch":"kadiri"})
# res_data = res.json()
# Branch = res_data['Branch']
# assert Branch == 'kadiri', 'HTTP Post method is not working'
# print(' \n post is :', res_data)

#To update emp 
# res = requests.put('http://127.0.0.1:5000/update', json = {"Branch":"Bangalore"})
# print('\n response code is :', res.status_code)
# print('\n update is :', res.text)

# To Delete emp 
# res = requests.delete('http://127.0.0.1:5000/delete', json = {"eid":"2336778"})
# print(dir(res))
# print('\n response code is :', res.status_code)
# assert res.status_code == 200 , 'Not able to process request'
# print('\n deleted is ', res.text)

