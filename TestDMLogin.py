# Logging In
# Import the library files.
import requests

# The json library parses JSON into a Python dictionary or list.
# It can also convert Python dictionaries or lists into JSON strings.
# Requests is an Apache2 Licensed HTTP library, written in Python.
# It allows you to send HTTP/1.1 requests.

# A Python 'dictionary' can represent a JSON object, which is used as
# a payload to pass the user ID and password.
payload_dictionary = {'user_id': 'SEC_Filer', 'password': '5azIKxKyx2NmtRvv53', 'persona': 'admin'}

# Send the PUT request to the server and save the response in a variable.
response = requests.put('https://UDMWSPEK301.kingandwood.com/api/v1/session/login', json=payload_dictionary, verify=False)

# Retrieve the response in JSON format.
json_response = response.json()
print(json_response)
# Successful.
if response.status_code == 200:
    print(response.status_code)

    # The authorization token is present.
    # This token is required to be passed in future API requests.
    x_auth_token = json_response['X-Auth-Token']
    customer_id = json_response['customer_id']
    print(x_auth_token)
    print(customer_id)

# Invalid user id or password
elif response.status_code == 401:
    print('Login failed')
    print(json_response['error']['message'])

else:
    print('Login failed')
    print(json_response['error']['message'])