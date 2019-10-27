# audio-slackbot

A Slack bot which plays sounds from the filesystem upon certain triggers. Install and configure
it on a RaspberryPi, connect some speakers and have fun.

## Requirements

1. python ^3.6

## Quickstart

1. Install the package:
   * `$ pip install --user --upgrade audio-slackbot`
2. Set up the Slack bot:
   * Create a new Slack bot in your worksapce settings
   * Export the API token to your environment: `$ export SLACK_API_TOKEN="xoxb-2349..."`
   * Invite the bot to some Slack channels in your workspace
3. Create a configuration file with the following format:

```yaml
# sounds.yaml
---
triggers:
  - word: "trololol"
    sound: "/home/pi/sounds/trololol.wav"
```

4. Start the bot:
   * `$ audio_slackbot --config /home/pi/sounds.yaml`

## macOS

On macOS you need to install `PyObjC` and `AppKit` as well:

```shell
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:/usr/local/opt/libffi/lib/pkgconfig"
pip install --user PyObjC AppKit
```
