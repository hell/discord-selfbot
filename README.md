# discord-selfbot
A simple Discord self-bot with some message features only.

Requirements:

[Python 3.7+](https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe)

```
discord
pyyaml
```


Installation:

1. Install Python 3.7+ with the ticked 'ADD TO PATH' button.
2. Open command prompt as administrator and install the following modules.
3. Open settings.yml with any text editor and paste your token. 

```py
pip install discord
pip install pyyaml
```

Additional information:
If you do not have 2fa enabled, you may want to use get_discord_token.py in order to easily fetch your token. Just put the file in the same folder and run the script, enter your credentials and the token will be automatically placed in the needed file and copied to your clipboard. 

You would need to additionally install pyperclip and requests in order to use it.

```py
pip install pyperclip
pip install requests
```

Commands:

```
.clear (OPTIONAL: username) -> deletes all of the messages in the current channel if the username is not specified, otherwise deletes the messages with the specified person (tries to find it using the username you've specified) 

.attachments (OPTIONAL: username) -> deletes all of the attachments/images you've sent in the current channel if the username is not specified, works the same way as .clear

.edit "TEXT" (OPTIONAL: username) -> edits all of your messages in the current channel if the username is not specified, works the same way as .clear

.clearfriends -> deletes all of your messages with every single person you have added

```


