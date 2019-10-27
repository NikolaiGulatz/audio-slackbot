import io
import os
import pytest
from unittest import mock

from audio_slackbot import run


class MockRTMClient:
    def __init__(self, *args, **kwargs):
        pass

    def start(*args, **kwargs):
        pass

    def run_on(*args, **kwargs):
        def callback(*args, **kwargs):
            pass

        return callback


class FakeArg:
    def __init__(self, config):
        self.config = config


class FakeArgParser:
    def __init__(self, *args, **kwargs):
        pass

    def add_argument(*args, **kwargs):
        pass

    def parse_args(*args, **kwargs):
        sample_config = (
            b"triggers:\n" b'  - trigger: "test"\n' b'    sound: "/path/to/file.mp3"\n'
        )

        return FakeArg(io.TextIOWrapper(io.BytesIO(sample_config)))


@mock.patch("slack.RTMClient", new=MockRTMClient)
@mock.patch("argparse.ArgumentParser", new=FakeArgParser)
@mock.patch.dict(os.environ, {"SLACK_API_TOKEN": "secret"})
def test_run():
    run()
