from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time
import random
import configparser
import os

def random_sleep(min_seconds=1, max_seconds=3):
    """Sleep for a random amount of time within a range to mimic human behavior"""
    time.sleep(random.uniform(min_seconds, max_seconds))

def get_credentials():
    """Read credentials from config.ini file"""
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_path)
    
    try:
        username = config['credentials']['username']
        password = config['credentials']['password']
        return username, password
    except (KeyError, configparser.NoSectionError):
        print("Error: Could not read credentials from config.ini")
        print("Make sure config.ini has a [credentials] section with username and password")
        exit(1)

def main():
      options = webdriver.ChromeOptions()
      
      # **** Uncomment the line below if you want to run Chrome in headless mode
      # options.add_argument('--headless')
      
      options.add_argument('--disable-blink-features=AutomationControlled')
      options.add_experimental_option('excludeSwitches', ['enable-automation'])
      options.add_experimental_option('useAutomationExtension', False)
      driver = webdriver.Chrome(options=options)
      
      driver.set_window_size(1366, 768)
      
      driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
      
      wait = WebDriverWait(driver, 10)
      
      try:
            # Get credentials from config file
            username, password = get_credentials()
            
            driver.get("https://instagram.com")
            random_sleep(2, 4)
         
            username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"loginForm\"]/div[1]/div[1]/div/label/input")))
            username_field.clear()
            for char in username:
                  username_field.send_keys(char)
                  time.sleep(random.uniform(0.05, 0.1))
            random_sleep(2,5)
      
            
            password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"loginForm\"]/div[1]/div[2]/div/label/input")))
            password_field.clear()
            for char in password:
                  password_field.send_keys(char)
                  time.sleep(random.uniform(0.05, 0.1))
            random_sleep()
            
            password_field.submit()
            random_sleep(4, 6)


            driver.get(f"https://instagram.com/{username}")
            random_sleep(2, 4)
      
        
            loop_count = 0
            max_loops = 1000
      
            
            while loop_count < max_loops:
  
                  print(f"Starting loop {loop_count + 1}")
                  
                  following_link = wait.until(EC.element_to_be_clickable((By.XPATH, 
                        "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span")))
                  following_link.click()
                  random_sleep(2, 3)
                  
                  unfollow_button = wait.until(EC.element_to_be_clickable((By.XPATH, 
                        "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button/div/div")))
                  unfollow_button.click()
                  random_sleep(1, 2)
                  
                  confirm_unfollow = wait.until(EC.element_to_be_clickable((By.XPATH, 
                        "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]")))
                  confirm_unfollow.click()
                  random_sleep(2, 3)
                  
                  close_button = wait.until(EC.element_to_be_clickable((By.XPATH, 
                        "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")))
                  close_button.click()
                  random_sleep(2, 3)
                  
                  loop_count += 1
                  print(f"Successfully completed loop {loop_count}")
                  
                  if loop_count % 10 == 0:
                        print(f"Taking a longer break after {loop_count} loops")
                        time.sleep(random.uniform(30, 60))
                  
      
      except Exception as e:
            print(f"An error occurred: {e}")
            driver.quit()
      
      finally:
            random_sleep(2, 4)

if __name__ == "__main__":
      while True:
            main()