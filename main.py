from get_prompt import get_prompt, style_list
from keep_alive import keep_alive
import urllib
from PIL import Image
import requests
import json
import random
import base64
import time
import io
import os
from instagrapi import Client


def login():
  host = Client()
  host.login(os.environ['username'], os.environ['password'])
  return host
  
  
def getimage():
  prompt = get_prompt().replace(' ','-')
  urllib.request.urlretrieve(f'https://image.pollinations.ai/prompt/{prompt}', 'pic.jpg')


def upload_img(insta):
  insta.photo_upload("pic.jpg","pewpewpew \n #art#aiart#idk")
  os.remove("pic.jpg")


def main():
  keep_alive()
  while (True):
    mobile = login()
    getimage()
    upload_img(mobile)
    print(get_prompt())
    time.sleep(21600)


main()
