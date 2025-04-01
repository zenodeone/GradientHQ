# GradientHQ
How to Run the Bot:
Follow these steps to get the bot up and running:

Install Dependencies: First, install the necessary Python libraries:

bash
Salin
Edit
pip install selenium webdriver-manager python-telegram-bot schedule
Set Up Your Telegram Bot:

Create a bot using BotFather on Telegram (as explained earlier).

Get your bot's API Token.

Find your Chat ID by using a service like @userinfobot on Telegram.

Configure the Script:

Replace the placeholder YOUR_TELEGRAM_BOT_API_TOKEN with your bot's API Token.

Replace YOUR_CHAT_ID with your actual Chat ID.

Update the extension_path variable to the local path where your Gradient node extension is stored.

Set the proxy values in the proxies list with your proxy information.

Run the Script: Save the script to a Python file, e.g., farming_bot.py, and run it:

bash
Salin
Edit
python farming_bot.py
The bot will:

Run the farming process every 24 hours automatically.

Send Telegram notifications when farming starts, finishes, or fails.

Log all actions in the farming_results.log file.

Monitoring and Debugging:

The script logs all actions and errors in the farming_results.log file.

You can monitor the Telegram chat for real-time updates.

Example Log Messages:
Farming Started:

arduino
Salin
Edit
Farming session started.
Farming process started.
Farming started successfully.
Error Encountered:

vbnet
Salin
Edit
Error encountered: Unexpected error: Farming did not start correctly.
Farming Session Ended:

nginx
Salin
Edit
Farming session ended.
Now, your Selenium Gradient Farming Bot will run automatically, notify you via Telegram, and handle any errors gracefully.
