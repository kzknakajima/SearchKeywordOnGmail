from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import base64
from bs4 import BeautifulSoup


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_message_list(service,query,max_Results):
    msg_list = service.users().messages().list(userId='me',q=query,maxResults=max_Results).execute()
    return msg_list

def get_message_part(msg):
    msg_part = msg['payload']
    return msg_part

def get_message_body(msg_part):
    msg_body = msg_part['body']['data']
    return msg_body

def get_decoded_message(encoded_msg):
    decoded_msg = base64.urlsafe_b64decode(encoded_msg).decode()
    return decoded_msg

def connect_gmail_service():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return service


def main():
    query = 'from:mailmag@mag2premium.com'
    max_Results = 1

    service = connect_gmail_service()
    results = get_message_list(service,query,max_Results)
    messages = results.get('messages',[])

    if not messages:
        print('No messages found.')
    else:
        print('Messages:')
        for message in messages:
            message = service.users().messages().get(userId='me', id=message['id']).execute()
            message_part = get_message_part(message)
            message_body = get_message_body(message_part)
            decoded_msg = get_decoded_message(message_body)
            # text = BeautifulSoup(decoded_msg,'html.parser')
            print(decoded_msg)

if __name__ == '__main__':
    main()
