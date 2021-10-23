import base64
import re

from gmailService import connect_gmail_service

def results_of_search(plain_msg,keyword,sentence_vol):
    paragraphs = re.split(r'\r\n', plain_msg)
    list_of_some_paragraphs = []
    for i,paragraph in enumerate(paragraphs):
        if keyword in paragraph:
            list_of_some_paragraphs.append(paragraphs[i-sentence_vol : i+sentence_vol+1])
    return list_of_some_paragraphs

def replace_htmltxt_to_plaintxt(html_msg):
    pattern = r'<.*?>' # patterns of html tag
    plain_msg = re.sub(pattern,'',html_msg)
    return plain_msg

def get_message_list(service,query,max_Results):
    msg_list = service.users().messages().list(userId='me',q=query,maxResults=max_Results).execute()
    return msg_list

def get_count_of_keyword(plain_msg,keyword):
    result_of_count = plain_msg.count(keyword)
    return result_of_count

def get_message_date(messages,msg):
    headers = msg['payload']['headers']
    for h in headers:
        if h.get('name') == 'Date':
            msg_date = h.get('value')
    return msg_date

def get_message_part(msg):
    msg_part = msg['payload']
    return msg_part

def get_message_body(msg_part):
    msg_body = msg_part['body']['data']
    return msg_body

def get_decoded_message(encoded_msg):
    decoded_msg = base64.urlsafe_b64decode(encoded_msg).decode()
    return decoded_msg

# def connect_gmail_service():
#     creds = None
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())
#     service = build('gmail', 'v1', credentials=creds)
#     return service


def main():
    keyword = input("Please input keyword:")
    query = 'from:mailmag@mag2premium.com' #query for gmail API
    max_Results = 5 #the number of latest message
    sentence_volume = 2

    service = connect_gmail_service()
    results = get_message_list(service,query,max_Results)
    messages = results.get('messages',[])

    if not messages:
        print('No messages found.')
    else:
        for message in messages:
            message = service.users().messages().get(userId='me', id=message['id']).execute()
            message_part = get_message_part(message)
            message_body = get_message_body(message_part)
            decoded_msg = get_decoded_message(message_body)
            plain_msg = replace_htmltxt_to_plaintxt(decoded_msg)

            message_date = get_message_date(messages,message)
            print('Date:',message_date[:-20])#-20 means to remove time, leave just Date
            keyword_count = get_count_of_keyword(plain_msg,keyword)
            # print(f'Count: "{keyword}" : "{keyword_count}" ')

            if keyword in plain_msg:
                lst_of_paragraphs = results_of_search(plain_msg,keyword,sentence_volume)
                print('--------------------------')
                for para in lst_of_paragraphs:
                    for sentence in para:
                        print(sentence)
                    print('--------------------------')
                print('############################')
            else:
                # print('Your keyword is not found in Message.')
                print('############################')

if __name__ == '__main__':
    main()
