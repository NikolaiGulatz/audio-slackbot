# GuentherPi

GuentherPi is a friendly slack chat bot which can be run on a raspberry pi to let the raspberry play certain sounds upon writing trigger words to the bot. It is particulary useful for raising the level of fun in the office or annoying your co-workers.

## Dependencies

1. python 2.7 or 3.5+ with pip
2. python-gst-1.0 (`sudo apt-get install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools`)

## Installation

1. Create a bot user named "guenther" for you slack team named
2. Copy the example sounds file and add some own triggers and sound files
3. Install the requirements
  * `pip install -r requirements.txt`
4. Start GuentherPi and pass the slack api token `GUENTHER_SLACK_API_TOKEN=<token> python run.py`
5. In your slack team type `@guenther play trololol`

For "production" ( ͡° ͜ʖ ͡°) use the easiest way is to start it in a screen session.

## Built-in commands

Commands are extracted from the messages you send to GuentherPi, so `@guenther which sounds do you have?` will also trigger the `sounds` command.

### `@guenther sounds`

Posts a list of all available trigger commands to the channel.

## Troubleshooting

### It doesn't work in virtualenv

It does not seem to be possible to install the `gi` package in virtualenv ¯\_(ツ)_/¯ 

### It doesn't work on macOS

Install `pyobjc` using `pip`

