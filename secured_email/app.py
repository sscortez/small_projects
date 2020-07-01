
import base64

from secured_email.gpg_builder import MyGPG
from secured_email.send_email import get_credentials, create_message, send_email


if __name__ == "__main__":

    credentials = get_credentials()
    my_gpg = MyGPG()

    while True:
        message_input = input("Give us the message:")
        recipient_input = input("Proivde the email of the target recipient:")
        subject_input = input("Provide the subject of the email:")

        if message_input and recipient_input and subject_input:
            encrypted_message = my_gpg.encrypt_data(message_input)
            # encrypted_message = base64.b64encode(encrypted_message.data).decode('utf-8')

            message_payload = create_message(message_input, recipient_input, subject_input)

            print("Sending message...")
            res = send_email(message_payload, credentials)
            if res:
                print("Message sent")
                break
        else:
            print("Please provide sufficient input")
