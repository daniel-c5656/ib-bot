# IB Bot: A simple Discord bot for IB communities.

## What is it, and what can it do?

IB Bot is a Discord bot built on Python, particularly the hikari and hikari-lightbulb frameworks. In its current stage, it can post files of relevance to IB students and serve as a simple text-based calculator.

### Calculator

Has basic functions (+, -, *, /) as well as advanced functions such as trigonometric functions. It relies on Python's builtin math module, the documentation of which can be found at https://docs.python.org/3/library/math.html.

## Setup

1. Go to https://discord.com/developers/applications and create a new bot with appropriate privledges (administrator is a safe option). You may Google how to do this if you're not sure.
2. Replace "YOUR TOKEN HERE" in main.py with your bot's token.
3. Invite the bot to your server server of choice (one that you have permission to, of course), then copy the server's ID and replace "SERVER ID HERE" in main.py with the ID as an integer, leaving in the form of a tuple.
4. Activate the virtual environment and run main.py! You should see the bot come online and slash commands show up in Discord. Try running /sanitycheck.
5. Most commands, specifically involving files, will not work at this stage (the files cannot be included in this repo due to copyright). However, the files are readily available online.
6. Place files with these names in the "files" folder:
- chem_consts.png (picture of chemistry constants)
- phys_consts.png (picture of physics constants)
- chem_db.pdf (chemistry databooklet)
- phys_db.pdf (physics databooklet)

Reset the bot, and that's it! IB Bot should be ready for hosting.

## Credits

Code written by Daniel C, IB Session May 2023.

Hikari: https://github.com/hikari-py/hikari

Hikari-lightbulb: https://github.com/tandemdude/hikari-lightbulb

IB and all of its documents belong to the International Baccalaureate Organization (IBO).