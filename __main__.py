import tweepy
import os
import socket

host_name = os.environ['HOST_NAME']
host_port = os.environ['HOST_PORT']
current_time = os.environ['CURRENT_TIME']
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']


def main():
    """
    lambda declared entry point
    """
    status = 'Update: IP addresses of ' + host_name + ': \n'+current_time+'\n'

    for addr in socket.getaddrinfo(host_name, host_port):
        if addr[1] == socket.SOCK_STREAM:
            status += '\n'+addr[4][0]

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(status)


if __name__ == '__main__':
    main()
