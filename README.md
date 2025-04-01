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
