import requests

name = 'dinosaur'
api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'SKDWNkk5OmzCCjkkIk9qNw==kHPaSVtQHBC8o5RO'})
if response.status_code == requests.codes.ok:
    print(response.json())
else:
    print("Error:", response.status_code, response.json())

