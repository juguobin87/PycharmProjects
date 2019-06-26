# Upload a new document along with its metadata

import os
import requests
import json
from mimetypes import MimeTypes
import urllib

g_mime_type_ = MimeTypes()

user_id = 'SEC_Filer'
password = '5azIKxKyx2NmtRvv53'
server = 'UDMWSPEK301.kingandwood.com'

#  Retrieve X-Auth-Token
payload_dictionary = { 'user_id': user_id, 'password': password }

# We are ready to send the request as an HTTP 'PUT' request.
response = requests.put('https://' + server + '/api/v1/session/login',json=payload_dictionary, verify = False)

json_response = response.json()

if 'X-Auth-Token' in json_response:
    x_auth_token = json_response['X-Auth-Token']
    print('Succeeded.')
    print('')

else:
    print('The login was unsuccessful.')
    print(json_response['error']['message'])

#### TASK STARTS HERE #####

# To authorize our request, we send the X-Auth-Token that we retrieved when
# logging in.
headers = { 'X-Auth-Token': x_auth_token }

# Retrieve the document type and class
def get_ws_type(filename):
    url = urllib.request.pathname2url(filename)
    content_type, encoding = g_mime_type_.guess_type(url)
    if content_type in ['application/pdf', 'application/x-pdf']:
        return 'DOC', 'ACROBAT'
    if content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return 'DOC', 'WORDX'
    if content_type == 'application/msword':
        return 'DOC', 'WORD'
    if content_type == 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
        return 'DOC', 'PPTX'
    if filename.endswith('.MSG'):
        return 'E-MAIL', 'MIME'


# Set the parameters
user_name = 'SEC_Filer'
doc_name = 'dmTest'
folder_id = 'SEC!723882'
database_name = 'SEC'
file_path = 'C://git-cheatsheet.pdf'
base_url ='https://'+ server +'/api/v1'

# Get file size
file_size = os.path.getsize(file_path)

# Get class and type of the documents
doc_class, doc_type = get_ws_type(file_path)

# Set the document metadata
profile = {'doc_profile': {'name': 'TestDocument',
                           'size': file_size,
                           'type': doc_type,
                           'class': doc_class,
                           'author': user_name,
                           'operator': user_name,
                           'database': database_name},
                           'user_trustees': [{'name': user_name,
                                              'id': user_name,
                                              'access': 'full_access'}]}

files_ = {'json': (None, json.dumps(profile), 'application/json'),
          'file': open(file_path, 'rb')}
# print(files_)
# Check if the operation is allowed
operations_url = base_url + '/folders/' + folder_id + '/operations'
check_operations = requests.get(operations_url,headers=headers, verify = False)
json_response = check_operations.json()['data']

# If the user has permission then proceed
if json_response['add_content'] == True:

    print('Upload document operation is allowed.')

    # Define the upload url
    upload_url = base_url +'/folders/' + folder_id + '/documents'
    print(upload_url)

    # Send the POST request and retrieve the response
    response = requests.post(upload_url, files=files_, headers=headers, verify = False)

    print(response.headers)
    doc_profile = response.json()['data']

    # Retrieve the document ID
    doc_id = database_name + '!' + str(doc_profile['document_number']) + '.' \
         + str(doc_profile['version'])

    print('Created ' + doc_id + ' successfully')

    # Successful
    if response.status_code ==201:
       print('Document uploaded successfully')

    # Invalid user id or password
    elif response.status_code ==401:
       json_response = response.json()
       print(json_response['error']['message'])

    else:
       print('Task failed.')
       print(json_response['error']['message'])

# If the user is not allowed to perform this task then print
# a message and exit
else:
    print('Uploading document is NOT allowed.')