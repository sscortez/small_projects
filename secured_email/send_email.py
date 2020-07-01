
import base64
import os
import pickle
from email.mime.text import MIMEText
from os.path import join

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build

SCOPE = ['https://www.googleapis.com/auth/gmail.compose']
_parent_path = os.path.dirname(__file__)


def get_credentials():
    pickle_path = join(_parent_path, 'token.pickle')
    with open(pickle_path, 'rb') as token:
        creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                join(_parent_path, 'credentials.json'),
                SCOPE)
            creds = flow.run_local_server(port=0)

        with open(pickle_path, 'wb') as token:
            pickle.dump(creds, token)
    return creds


def create_message(message_text, to, subject, sender='me'):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode().decode())}


def send_email(message_data, creds, user_id='me'):
    if not creds.valid:
        creds = get_credentials()

    service = build('gmail', 'v1', credentials=creds)
    try:
        message = (service.users().messages().send(userId=user_id, body=message_data)
                   .execute())
        print(f"Message Id: {message['id']}")
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
