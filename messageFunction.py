import base64


def get_message_part(msg):
    msg_part = msg['payload']
    return msg_part


def get_message_body(msg_part):
    msg_body = msg_part['body']['data']
    return msg_body


def get_message(service, message):
    message_rslt = service.users().messages().get(userId='me', id=message['id']).execute()
    message_part = get_message_part(message_rslt)
    message_body = get_message_body(message_part)
    return message_rslt, message_body


def get_decoded_message(encoded_msg):
    decoded_msg = base64.urlsafe_b64decode(encoded_msg).decode()
    return decoded_msg
