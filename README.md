# Kerala COVID19 Counts - Telegram Bot

This repository contains the Python (v3.7) code for the [Kerala COVID19 Counts Telegram bot](https://t.me/KeralaCovid19Bot).

## Using the bot

1. Search for the bot in Telegram using either **Kerala COVID 19 Counts** or **@@KeralaCovid19Bot**
2. Click **START** to begin conversing with the bot
3. To retrieve the latest COVID 19 stats for Kerala, send either `/klcovid` or `/klcorona`

## Commands
1. `/start` - To start interacting with the bot and get a welcome message
2. `/klcovid` - Retrieve the state and district-wise stats
3. `/klcorona` - Retrieve the state and district-wise stats

## Creating a local setup

1. Clone the current repository - `git clone https://github.com/AbhishekPednekar84/covid19-kl-bot`
2. Create a virtual environment - `python -m venv venv`
3. Activate the virtual environment - `venv\Sctipts\activate.bar` (Windows), `source venv/bin/activate` (OSx / Linux)
4. Install the project dependencies - `pip install -r requirements.txt`
5. Create a `.env` file and add an environment variable called `TELEGRAM_TOKEN` (refer to `.env.example`)
6. Run the code - `python bot/server.py` or `python3 bot/server.py`
7. To run the tests - `pytest`
