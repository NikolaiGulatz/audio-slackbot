import logging
import json
import re

from slackclient import SlackClient
from playsound import playsound
from sounds import Sounds

class Guenther:
    """
    Guenther is a friendly slack chat bot which can be run on a raspberry pi to play certain sounds upon writing certain
    trigger words to him. It is particulary useful for raising the level of fun in the office or annoy your co-workers.
    """

    INTERNAL_TRIGGERS = {
        'sounds': 'list_sounds'
    }

    def __init__(self, api_token=None):
        self.logger = self.get_logger()
        self.client = self.get_client(api_token)
        self.user_id = self.get_user_id()
        self.locked = False
        self.sounds = Sounds()

    @staticmethod
    def get_client(api_token):
        if not api_token:
            raise ValueError('No API token specified')

        return SlackClient(api_token)

    @staticmethod
    def get_logger():
        logger = logging.getLogger('guenther')
        logger.setLevel(logging.INFO)

        logger_handler = logging.StreamHandler()
        logger_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(formatter)
        logger.addHandler(logger_handler)

        return logger

    @staticmethod
    def play_sound(sound):
        """
        Play a sound file
        """
        playsound(sound)

    def get_user_id(self):
        user_list = self.client.api_call('users.list')

        if not user_list.get('ok'):
            raise RuntimeError('Could not load user list: %s' % user_list.get('error'))

        for user in user_list.get('members'):
            if user.get('name') == 'guenther':
                self.logger.info('Bot user id is ' + user.get('id'))
                return user.get('id')

        return None

    def run(self):
        """
        Start listening to messages
        """
        if self.client.rtm_connect():
            self.logger.info('Connected to RTM')

            while True:
                for event in self.client.rtm_read():
                    if 'text' in event and event['text'].startswith("<@%s>" % self.user_id):
                        self.logger.info('Message received: {}'.format(json.dumps(event, indent=2)))
                        self.handle_event(event)

    def handle_event(self, event):
        """
        Handle a event, e.g. a direct message to the bot
        """
        tokens = re.compile(r'\w+').findall(event['text'])

        for token in tokens:
            if token in self.INTERNAL_TRIGGERS:
                self.handle_internal_trigger(token, event)
                break

            if self.handle_sound_trigger(token, event):
                break

    def handle_internal_trigger(self, token, event):
        """
        Handles non sound triggers
        """
        if token not in self.INTERNAL_TRIGGERS:
            return False

        handler = getattr(self, self.INTERNAL_TRIGGERS[token])
        handler(event)

    def handle_sound_trigger(self, token, event):
        """
        Handles sound triggers
        """
        sound = self.sounds.get_sound(token)

        if sound:
            self.logger.info('Playing sound {} for trigger {}'.format(sound, token))

            self.client.api_call(
                'chat.postMessage',
                channel=event['channel'],
                text=':musical_score:',
                as_user=True
            )

            self.play_sound(sound)
            return True

        return False

    def list_sounds(self, event):
        """
        Post a list of available triggers
        """
        sounds = self.sounds.get_sounds()

        self.client.api_call(
            'chat.postMessage',
            channel=event['channel'],
            text=', '.join([sound['trigger'] for sound in sounds]),
            as_user=True
        )
