#  Create a folder under a workspace

import requests
import json

user_id = 'SEC_Filer'
password = '5azIKxKyx2NmtRvv53'
server = 'UDMWSPEK301.kingandwood.com'

#  Retrieve X-Auth-Token
payload_dictionary = {'user_id': user_id, 'password': password}

# We are ready to send the request as an HTTP 'PUT' request.
response = requests.put('https://' + server + '/api/v1/session/login', json=payload_dictionary, verify=False)

json_response = response.json()

if 'X-Auth-Token' in json_response:
    x_auth_token = json_response['X-Auth-Token']
    print('Succeeded.')
    print('')

else:
    print('The login was unsuccessful.')
    print(json_response['error']['message'])

# Set the parameters.
workspace_id = 'SEC!723881'
folder_name = 'Test2'
database_name = 'SEC'
security = 'Private'
custom1 = 'SEC!723882'
custom2 = '215921'

# Define base URL.
base_url = 'https://' + server + '/api/v1'

# Define the header.
headers = {'Content-type': 'application/json', 'X-Auth-Token': x_auth_token}

# Check if operation is allowed.
operations_url = base_url + '/folders/' + workspace_id + '/operations'
check_operations = requests.get(operations_url, headers=headers, verify=False)
print(check_operations.json())
json_response = check_operations.json()['data']
# Check if the operation is allowed.
if json_response['add_folders'] == True:
    print('Adding folders operation is allowed.')

    payload = {"database": "SEC",
              "name": folder_name,
              "default_security": security,
              "parent_id": "SEC!723882"
               }

    # Define the url to create folder
    folder_create_url = base_url + '/workspaces/' + workspace_id + '/folders'

    # Send the POST request to create folder
    response = requests.post(folder_create_url, data=json.dumps(payload), headers=headers, verify=False)

    # Retrieve the response in JSON format
    json_response = response.json()

    # Successful.
    if response.status_code == 201:
        folder = json_response['data']
        print('Folder ' + folder_name + ' '+ folder['id'] +' created sucessfully.')

    # Invalid user id or password
    elif response.status_code == 401:
        print(json_response['code']['code_message'])

    else:
        print('Task failed.')
        print(json_response)
        print(json_response['code']['code_message'])

# User is not allowed to perform this task, print
# a message and exit
else:
    print('Adding folders operation is NOT allowed')