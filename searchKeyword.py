import re
from gmailService import connect_gmail_service
from messageFunction import get_message, get_decoded_message


def results_of_search(plain_msg, keyword, sentence_vol):
    prgrphs = re.split(r'\r\n', plain_msg)
    lst_of_prgrphs = []
    for i, prgrph in enumerate(prgrphs):
        if keyword in prgrph:
            lst_of_prgrphs.append(prgrphs[i-sentence_vol: i+sentence_vol+1])
    return lst_of_prgrphs


def replace_htmltxt_to_plaintxt(html_msg):
    pattern = r'<.*?>'  # patterns of html tag
    plain_msg = re.sub(pattern, '', html_msg)
    return plain_msg


def get_message_list(ser, query, max_R):
    msg_lst = ser.users().messages().list(userId='me', q=query, maxResults=max_R).execute()
    return msg_lst


def get_count_of_keyword(plain_msg, keyword):
    result_of_count = plain_msg.count(keyword)
    return result_of_count


def get_message_date(msg):
    headers = msg['payload']['headers']
    for h in headers:
        if h.get('name') == 'Date':
            msg_date = h.get('value')
    return msg_date


def main():
    keyword = input("Please input keyword:")
    query = 'from:mailmag@mag2premium.com'
    max_Results = 10  # the number of searched mails
    sentence_volume = 2  # the number of printed range, hitting keyword

    service = connect_gmail_service()
    results = get_message_list(service, query, max_Results)
    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')
    else:
        for message in messages:
            message_rslt, message_body = get_message(service, message)
            decoded_msg = get_decoded_message(message_body)
            plain_msg = replace_htmltxt_to_plaintxt(decoded_msg)

            # message_date = get_message_date(messages, message_rslt)
            message_date = get_message_date(message_rslt)
            keyword_count = get_count_of_keyword(plain_msg, keyword)
            print('Date:', message_date[:-20])  # :-20 remove time, leave just Date
            print(f'Count: {keyword_count}')

            if keyword in plain_msg:
                lst_of_prgrphs = results_of_search(plain_msg, keyword, sentence_volume)
                print('--------------------------')
                for para in lst_of_prgrphs:
                    for sentence in para:
                        print(sentence)
                    print('--------------------------')
                print('###################################')
            else:
                print('###################################')


if __name__ == '__main__':
    main()
