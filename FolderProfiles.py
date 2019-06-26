# Retrieve the name of the workspace for a given workspace_id and the profile information of its child folders

import requests

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


# TASK STARTS HERE

# Set the parameter
workspace_id = 'SEC!723881'

# To authorize our request, we send the X-Auth-Token that we retrieved when
# logging in.
headers = { 'X-Auth-Token': x_auth_token}

# Get the name of the workspace associated with the workspace_id.
# This will be used while displaying the output. The response is a string.
response = requests.get('https://' + server + '/api/v1/workspaces/' + workspace_id, headers=headers, verify=False)

# Check if the API request was successful.
if response.status_code == 200:

    # Retrieve the response in JSON format.
    json_response = response.json()
    print(json_response)
    # Get the name of the workspace.
    workspace_name = json_response['data']['name']

    # Get the child folders of this workspace.
    response = requests.get('https://' + server + '/api/v1/workspaces/SEC!723882/children', headers=headers, verify=False)

    if response.status_code == 200:
        # Retrieve the response in JSON format.
        json_response = response.json()

        # Now that the response has been converted to a dictionary,
        # the different parts of the response can be easily accessed.
        # Print the child folder IDs and their names found under the workspace.
        print('The folder IDs and names of folders within workspace "' + workspace_name + '":')
        for folder in json_response['data']:
            print(folder)

else:

    # API request failed. Print the error message.
    print('Task failed.')
    json_response = response.json()
    print(json_response)
# TASK ENDS HERE
