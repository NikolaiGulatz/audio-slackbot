# Guenther

Guenther is a friendly slack chat bot which can be run on a raspberry pi to play certain sounds upon writing trigger words to him. It is particulary useful for raising the level of fun in the office or annoying your co-workers.

## Installation

1. Create a new virtualenv environment with python 3.6
    * Example: `virtualenv -p /usr/local/Cellar/python2/3.6.0/bin/python3.6 venv`

2. Activate the venv environment
    * `. venv/bin/activate`

3. Install the requirements
    * `pip install -r requirements.txt`

4. Copy the example sounds file and configure your sounds
    * `cp sounds.example.json sounds.json`

## Usage

Create a bot user for your slack team, activate the virtual environment, start Guenther and pass the bot user API token as an environment variable: `GUENTHER_SLACK_API_TOKEN=<token> python run.py`

For "production" use the easiest way to have Guenther run permanently is to start him in a screen session.

## Built-in commands

### `sounds`

Posts a list of all available trigger commands to the channel.
