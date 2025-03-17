
# Instagram Unfollower Bot

An automated tool to unfollow Instagram accounts using Python and Selenium.

## Overview

This bot helps you automate the process of unfollowing accounts on Instagram. It's completely free and easy to use, requiring only Python and the Selenium library.

## Features

- Automatically logs into your Instagram account using credentials from config.ini
- Navigates to your profile without any manual intervention
- Systematically unfollows accounts with a single script execution
- Includes random delays to mimic human behavior
- Handles errors gracefully

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome browser
- ChromeDriver compatible with your Chrome version

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install selenium
```

3. Make sure ChromeDriver is installed and in your PATH or in the same directory as the script

## Configuration

1. Open the `config.ini` file
2. Replace the placeholder values with your Instagram credentials:

```ini
[credentials]
username = your_username
password = your_password
```

## Usage

Simply run the script with Python:

```bash
python ig-unfollower-bot.py
```

The bot will automatically:
1. Launch Chrome and navigate to Instagram
2. Log in using your credentials from config.ini
3. Navigate to your profile
4. Start unfollowing accounts one by one
5. Take regular breaks to avoid detection

No manual interaction is required after starting the script.

## Customization

- To run Chrome in headless mode (invisible), uncomment the line: `# options.add_argument('--headless')`
- Adjust the sleep times or loop counts in the script for different pacing

## Safety Precautions

- Use this bot responsibly to avoid Instagram's automated systems detecting unusual activity
- The script includes random delays to mimic human behavior
- Consider running it for short periods rather than unfollowing many accounts at once
- Be aware that automation tools may violate Instagram's terms of service

## Disclaimer

This bot is for educational purposes only. Use at your own risk. The developers are not responsible for any consequences resulting from the use of this tool.
