# Search for workspaces of a particular client in the database.

import requests

user_id = 'USER_ID'
password = 'PASSWORD'
server = 'SERVER_NAME'

#  Retrieve X-Auth-Token
payload_dictionary = {'user_id': 'SEC_Filer', 'password': '5azIKxKyx2NmtRvv53' }

# We are ready to send the request as an HTTP 'PUT' request.
response = requests.put('https://UDMWSPEK301.kingandwood.com/api/v1/session/login', json=payload_dictionary, verify = False)

json_response = response.json()

if 'X-Auth-Token' in json_response:
    x_auth_token = json_response['X-Auth-Token']
    print('Succeeded.')
    print('')

else:
    print('The login was unsuccessful.')
    print(json_response['error']['message'])


# TASK STARTS HERE

# Authorize the API request by sending the X-Auth-Token,
# retrieved when logging in, as a header.
headers = {'X-Auth-Token': x_auth_token}

# Assign the parameters that are required to search the workspaces of a
# particular client
# For example :'1010' and '002' respectively.
parameters = {'custom1': 'K0119040001', 'custom2': '215921'}

# Send the 'GET' request to the server and store the response in a variable.
response = requests.get('https://UDMWSPEK301.kingandwood.com/api/v1/workspaces/search', headers=headers, params=parameters,  verify = False)

# Check if the API request was successful
if response.status_code == 200:

    # Retrieve the response in JSON format.
    json_response = response.json()

    # Print the ID and name of the retrieved workspaces.
    print('The names and folder ids of workspaces for client and matter:')
    for workspace in json_response['data']:
        print(workspace['id'] + ',' + workspace['name'])

else:
    # API request failed. Print the error message.
    print('Task failed.')
    json_response = response.json()
    print(json_response['error']['message'])

# TASK ENDS HERE
