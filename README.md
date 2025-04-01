# Selenium Gradient Farming Bot

This project automates the farming process using Selenium and Chrome, with the **Gradient node extension**. It includes functionality for proxy handling, Telegram notifications, automatic farming every 24 hours, and logging.

## Features
- **Farming Process**: Automates farming actions using Selenium and the Gradient node extension.
- **Proxy Support**: Automatically switches to backup proxies if the main proxy fails.
- **Telegram Notifications**: Sends updates about the farming process, including start, success, failure, and errors.
- **Error Handling**: Automatically restarts the farming process if it fails.
- **Logging**: Logs all actions, including errors, in a `farming_results.log` file.
- **Scheduling**: Runs the farming task every 24 hours using the `schedule` library.

## Requirements

- Python 3.6+
- **Selenium**: For automating the browser interaction.
- **webdriver-manager**: To manage ChromeDriver installations.
- **python-telegram-bot**: To send Telegram notifications.
- **schedule**: To schedule the bot to run periodically.

## Installation

### 1. Install Dependencies

First, install the necessary Python libraries by running:

```bash
pip install selenium webdriver-manager python-telegram-bot schedule

### 2. Set Up Your Telegram Bot
Create a bot using BotFather on Telegram.

Get your bot's API Token.

Find your Chat ID by using a service like @userinfobot on Telegram.

### 3. Configure the Script
Replace the placeholder YOUR_TELEGRAM_BOT_API_TOKEN in the script with your bot's API Token.

Replace YOUR_CHAT_ID with your actual Chat ID.

Update the extension_path variable to the local path where your Gradient node extension is stored.

Set the proxy values in the proxies list with your proxy information (if you need to use proxies).

### Run the Script
Save the script as **farming_bot.py** and run it:
```bash
python farming_bot.py

### 4. How It Works
The bot will run the farming process every 24 hours automatically.

It will send Telegram notifications when farming starts, finishes, or fails.

All actions are logged in the **farming_results.log** file for monitoring and debugging.

## Monitoring and Debugging
The script logs all actions and errors in the **farming_results.log** file. You can use this file to monitor the status of the farming process.

You will receive Telegram notifications with real-time updates.

Example Log Messages
Farming Started:

```bash
Farming session started.
Farming process started.
Farming started successfully.
Error Encountered:

```bash
Error encountered: Unexpected error: Farming did not start correctly.
Farming Session Ended:

```bash
Farming session ended.

Additional Notes
You can modify the script to schedule the farming process at a specific time by changing the schedule.every(24).hours.do(run_farming) line to schedule.every().day.at("09:00").do(run_farming) to run the task every day at 9:00 AM.

The bot handles automatic proxy switching, and you can add more proxies to the proxies list if needed.

Ensure that your Gradient node extension is correctly installed and accessible in the path you provide for extension_path.
