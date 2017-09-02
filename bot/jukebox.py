"""
Guenthers jukebox
"""

import json

from os import path

class Jukebox:
    """
    Manages sounds by keeping a list of dictionaries containing trigger words and sound file paths in sync with the
    sounds.json file.
    """
    SOUNDS_FILE = path.join(path.dirname(__file__), 'sounds.json')

    def __init__(self):
        self.sounds = self.load_sounds()

    def get_sound(self, trigger):
        """
        Returns the corresponding sound file path for a trigger word or none if no such trigger word exists
        """
        for sound in self.sounds:
            if sound['trigger'].lower() == trigger.lower():
                return sound['sound']

        return None

    def get_sounds(self):
        return self.sounds

    def load_sounds(self):
        """
        Initially load the sounds from the sounds file into the sounds list
        """
        with open(self.SOUNDS_FILE, 'r') as sounds_file:
            return json.load(sounds_file)

    def persist_sounds(self):
        """
        Persist the sounds list into the sounds file
        """
        with open(self.SOUNDS_FILE, 'w') as sounds_file:
            json.dump(self.sounds, sounds_file)

    def add_sound(self, trigger, sound):
        """
        Add a sound to the sound list and persist it
        """
        self.sounds.append({'trigger': trigger, 'sound': sound})
        self.persist_sounds()

    def remove_sound(self, trigger):
        """
        Remove a sound from the sound list and persist it
        """
        map(lambda d: d.pop(trigger), self.sounds)
        self.persist_sounds()
