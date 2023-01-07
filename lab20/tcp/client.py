import socket

from tcp.utils.constants import PORT, HOST
from tcp.utils.user import User

def send_request(user):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            try:
                message = user.create_message()
                message_encoded = bytes(message, 'UTF-8')
                s.sendall(message_encoded)

                user.new_message(new_msg=input(f'>{user.username}: '))
            except socket.timeout:
                print('REQUEST TIMED OUT')
                break
            except KeyboardInterrupt:
                print('Client has ended the request')
                break
def start_client_connection(user):
    send_request(user)



if __name__ == "__main__":
    user1 = User(username='BobbyFisher69', message='Hello, everybody!')
    start_client_connection(user=user1)
