import pytest
from unittest import mock

from audio_slackbot import Bot


@pytest.fixture
def bot(config):
    return Bot(config)


def test_init(bot):
    assert isinstance(bot, Bot)
    assert isinstance(bot._config, dict)


def test_hello(bot):
    bot._hello(data="foo")


@mock.patch("playsound.playsound")
def test_play_sound(bot):
    bot._play_sound("/path/to/file.mp3")


@mock.patch.object(Bot, "_play_sound")
def test_read_message_with_trigger(mock__play_sound, bot):
    text = {"data": {"text": "foo bar test"}}

    bot._read_message(**text)

    mock__play_sound.assert_called_once_with("/path/to/file.mp3")


@mock.patch.object(Bot, "_play_sound")
def test_read_message_without_trigger(mock__play_sound, bot):
    text = {"data": {"text": "foo bar"}}

    bot._read_message(**text)

    mock__play_sound.assert_not_called()
