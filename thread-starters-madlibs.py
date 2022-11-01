from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import random
import pandas as pd
import enum
#from xvfbwrapper import Xvfb

def madlib(yourcat):

  USR = os.getenv("USR")
  PASS = os.getenv("PASS")

  rper = ""

  class Clans(enum.Enum):
    solsticeClan = 12
    celestialClan = 9
    wickedClan = 13
    mechanicalHeart = 11

  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--no-sandbox") # linux only
  chrome_options.add_argument('--window-size=1920,1080')
  service = ChromeService(executable_path=os.environ.get("CHROMEDRIVER_PATH"))
  browser = webdriver.Chrome(service=service, options=chrome_options)


  browser.get('https://sinisterhaven.com/index.php?act=Login')


      # log in
  browser.find_element_by_xpath("//input[@name='UserName']").send_keys(USR)
  browser.find_element_by_xpath("//input[@name='PassWord']").send_keys(PASS)
  browser.find_element_by_xpath("//input[@name='submit']").click();

  #csv files for all the clans
  class ClanSheets(enum.Enum):
    solsticeClan = "https://docs.google.com/spreadsheets/d/e/2PACX-1vREzwVYgNn9fMWkbWZkBjfR7wyq8cJZHhNJZNsZwl7q9I74dd2wcnHI1L7pp0cZ3efWyI288pxI938P/pub?output=csv"
    celestialClan ="https://docs.google.com/spreadsheets/d/e/2PACX-1vRQxuVrni8D2NFcyXW2E3ox-MQQ9hFmKLGiWmzFfHpgahblK-qfJ7uvv0zEfoZoZQUwwPBfPfZcA1-q/pub?output=csv"
    wickedClan = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTltZ11jnjhEZEvjkfJX6Ty9CWC0vBcM7zOMVT59gNmbgftmWzyPToR6YLt1QkVOzQWmV2CnRFLha20/pub?output=csv"
    mechanicalHeart= "https://docs.google.com/spreadsheets/d/e/2PACX-1vRH1ffZviTAzoOy9SqErVR2GmAydqPwSTcZHcOZH8bR9RKcPnPeQ_c7GNTYElCVKkYRJXM32KjBxwE-/pub?output=csv"

  randomclanname = random.choice(["solsticeClan", "celestialClan", "wickedClan", "mechanicalHeart"])

   #Picks a random clan, then selects a random character
  def word_selected(randomclanname):
    randomclan = ClanSheets[randomclanname].value
    if randomclanname == "mechanicalHeart":
      word_file = pd.read_csv(randomclan)
      secret_character = random.choice(word_file["First Name"])
      rper = word_file[word_file["Character Name"]==secret_character]['Roleplayer Username'].iloc[0]
      return secret_character.lower(), rper
    else: 
      word_file = pd.read_csv(randomclan)
      secret_character = random.choice(word_file["Character Name"])
      rper = word_file[word_file["Character Name"]==secret_character]['Roleplayer Username'].iloc[0]
      return secret_character.lower(), rper

  secret_character, rper = word_selected(randomclanname)


  #csv file for random things 
  randomthread = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTue9uyLwA3ugUP5J_7eiz-c-Q-v6Tu_Va2aYa_AT1lzEoR9rgBp44cBaq42gQxpBw3SJpYptK6JDfk/pub?output=csv"

  random_word_file = pd.read_csv(randomthread)
  random_object = random.choice(random_word_file["Object"])
  random_action = random.choice(random_word_file["Action"])
  random_adjective  = random.choice(random_word_file["Adjective"])
  random_color  = random.choice(random_word_file["Color"])
  random_location  = random.choice(random_word_file["Location"])
  random_ing  = random.choice(random_word_file["INGaction"])
  random_animal  = random.choice(random_word_file["Animal"])
  random_weather  = random.choice(random_word_file["Weather"])


  secret_character = secret_character.capitalize()



  #Thread starters 
  thread_one = yourcat + " and " + secret_character + " travel to " + random_location + " and while there they come across a " + random_adjective + \
               " " + random_object + ". It is not something they have seen before and the two are puzzled for a moment. " + \
               "The two are determined to show it off to their clan-mates." 

  thread_two = yourcat + " and" + " " + secret_character + " stumble across a " + random_animal + " while out " + random_ing + ". The two begin to " + \
               random_action + ". With the sun setting behind them, they must decide if they shall continue to " + random_action + " or return back home."

  thread_three = yourcat + " and " + secret_character + " have secretly met each other at " + random_location + \
                 ". They know they are not supposed to be together at this time, lest further rumors and gossip spread about them. " + \
                 "But they are here now, and only a(an) " + random_object + " can stop them."

  thread_four = yourcat + " was hunting at(in) " + random_location + " but instead of prey they find " + secret_character + " playing with a " + \
                random_object + ". What will " + yourcat + " do? Join in on the fun, scare " + secret_character + \
                ", or perhaps they will even decide to take the " + random_object

  thread_five = "Near the border, a " + random_animal + " appears and attempts to attack " + yourcat + ". It is unknown why the animal is doing so but " + \
                secret_character + " witnesses this. Now escape the " + random_animal + " and its friends which have now joined in."

  thread_six = yourcat + " and "  + secret_character +  " have traveled to " + random_location +  " They have come due to a rumor they heard that " + \
               random_animal + " can be spotted here. They are trying to find out if it is true. The rumor also advises that " + random_animal + \
               " only appears when the weather is " + random_weather + " and "  + random_object +  " is present." 

  thread_seven = "The " + random_location + " has a problem, an infestation of " + random_animal + ". " + yourcat +  \
                 " is the one who first noticed the problem when they were there to " + random_action + \
                 yourcat + " is determined to fix the problem. With " + yourcat + " and " + secret_character + \
                 " working together they should be able to do something about the infestation."


  thread_starter = random.choice([thread_one, thread_two, thread_three, thread_four, thread_five, thread_seven])
  thread_starter += " @[" + rper + "]"

  # go post thread

  board = Clans[randomclanname].value
  browser.get('https://sinisterhaven.com/index.php?act=Post&CODE=00&f=' + str(board))
  threadname = "Random Thread with " + secret_character + " and " + yourcat
  try:
    threadname += " and a " + random_object
  except:
    print("continue")
  x = browser.find_element_by_xpath("//input[@name='TopicTitle']").send_keys(threadname)
  x = browser.find_element_by_xpath("//textarea[@name='Post']").send_keys(thread_starter)
  browser.find_element_by_xpath("//input[@name='submit']").click()
  WebDriverWait(browser, 5)
  url = browser.current_url
  browser.quit()

  return "I made a thread for you! " + str(url)
