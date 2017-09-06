import os

from guenther.guenther import Guenther

if __name__ == '__main__':
    API_TOKEN = os.environ['GUENTHER_SLACK_API_TOKEN']
    Guenther(api_token=API_TOKEN).run()
