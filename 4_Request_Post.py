import requests

# To create a new emp record
res = requests.post('http://127.0.0.1:5000/create', json = {"Branch":"kadiri"})
res_data = res.json()
Branch = res_data['Branch']
assert Branch == 'kadiri', 'HTTP Post method is not working'
print(' \n post is :', res_data)