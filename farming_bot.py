import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import logging
from telegram import Bot

# Telegram Bot Setup
API_TOKEN = "YOUR_TELEGRAM_BOT_API_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# Set up logging configuration
logging.basicConfig(
    filename="farming_results.log",  # Log file name
    level=logging.INFO,  # Log all messages with INFO level and above
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format with timestamp
)

# Path to the Gradient node extension (Update this path to your local extension directory)
extension_path = "/path/to/gradient/node/extension"

# List of proxies to try, in order of priority
proxies = [
    "http://<proxy_address>:<proxy_port>",  # Main proxy
    "http://<backup_proxy_address>:<backup_proxy_port>",  # Backup proxy
    "http://<additional_proxy_address>:<additional_proxy_port>"  # Additional proxies can be added here
]

# Telegram Notification Function
def send_telegram_message(message):
    bot = Bot(token=API_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

# Function to log messages with timestamp
def log_message(message, level="info"):
    if level == "error":
        logging.error(message)
    else:
        logging.info(message)

# Function to configure proxy settings for the Chrome driver
def setup_driver(proxy=None):
    chrome_options = Options()
    if proxy:
        chrome_options.add_argument(f'--proxy-server={proxy}')
    chrome_options.add_argument(f'--load-extension={extension_path}')
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Function to test if the proxy is working
def test_proxy(driver):
    try:
        # Try to access a simple page to verify the proxy works
        driver.get("http://www.google.com")
        return True
    except WebDriverException as e:
        log_message(f"Error with the proxy: {e}", "error")
        return False

# Function to simulate the farming process
def start_farming(driver):
    try:
        # Switch to the extension window
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if "Gradient" in driver.title:  # Identify the Gradient extension window
                break

        # Wait for the farming button to load
        time.sleep(2)

        # Find the farming button by its ID or another locator
        farming_button = driver.find_element(By.ID, "farming-button")  # Update the ID if necessary
        farming_button.click()
        log_message("Farming button clicked.")
        send_telegram_message("Farming process started.")

        # Wait for a few seconds for the farming process to start
        time.sleep(3)

        # Check the farming status
        status = driver.find_element(By.ID, "farming-status").text  # Update the ID if necessary
        if "Running" in status:
            log_message("Farming started successfully.")
            send_telegram_message("Farming started successfully.")
        else:
            raise Exception("Farming did not start correctly.")

    except (NoSuchElementException, TimeoutException) as e:
        error_message = f"Error: Failed to find the farming button or start the farming process. Details: {str(e)}"
        log_message(error_message, "error")
        send_telegram_message(f"Error encountered: {error_message}")
        print(error_message)
        return False
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        log_message(error_message, "error")
        send_telegram_message(f"Error encountered: {error_message}")
        print(error_message)
        return False
    return True

# Function to handle restarting the farming process
def restart_farming_process(driver):
    log_message("Restarting the farming process from the beginning.")
    send_telegram_message("Restarting the farming process.")
    driver.quit()
    time.sleep(2)  # Wait before restarting
    return setup_driver()

# Function to manage proxy switching automatically
def get_working_proxy():
    for proxy in proxies:
        driver = setup_driver(proxy)
        if test_proxy(driver):
            log_message(f"Using proxy: {proxy}")
            return driver
        else:
            log_message(f"Proxy {proxy} failed, trying next proxy.")
            driver.quit()
    # If all proxies fail, return None to indicate failure
    log_message("All proxies failed.")
    send_telegram_message("All proxies failed.")
    return None

# Function to run the farming process
def run_farming():
    # Get the working proxy automatically
    driver = get_working_proxy()
    
    if driver is None:
        log_message("Failed to connect with any proxy.", "error")
        send_telegram_message("Failed to connect with any proxy.")
        print("Failed to connect with any proxy.")
        return  # Exit if no proxy is working
    
    # Log the start of the farming session
    log_message("Starting farming session...")
    send_telegram_message("Farming session started.")

    farming_success = False
    while not farming_success:
        # Start farming process
        farming_success = start_farming(driver)
        
        # If farming fails, restart the process
        if not farming_success:
            driver = restart_farming_process(driver)

    # Always log the end of the session and close the driver
    log_message("Farming session ended.")
    send_telegram_message("Farming session ended.")
    driver.quit()

# Schedule the farming task to run every 24 hours at a specified time
schedule.every(24).hours.do(run_farming)  # Run every 24 hours

# Alternatively, schedule at a specific time (e.g., 9:00 AM every day)
# schedule.every().day.at("09:00").do(run_farming)

# Function to keep the script running and checking the schedule
def keep_running():
    while True:
        schedule.run_pending()
        time.sleep(1)  # Sleep for 1 second between checks

if __name__ == "__main__":
    keep_running()
