from get_prompt import get_prompt, style_list
from keep_alive import keep_alive
import urllib.request
#from typing import BinaryIO
from PIL import Image
import requests
import json
import random
import base64
import time
import io
import os
#from insta_share import Instagram
from ensta import Mobile

#insta = Host()


def login():
  mobile = Mobile(os.environ['username'], os.environ['password'])
  return mobile
  
  
# def getimage():
#   engine_id = "stable-diffusion-v1-6"
#   response = requests.post(
#     f"https://api.stability.ai/v1/generation/{engine_id}/text-to-image",
#     headers={
#       "Content-Type": "application/json",
#       "Accept": "application/json",
#       "Authorization": "sk-LZ9mrQgoLzIQYKmbZhj6GBJipSYHcJAzPgZhRo6wDpoK5v8A"
#     },
#     json={
#       "text_prompts": [{
#         "text": get_prompt()
#       }],
#       "cfg_scale": 7,
#       "clip_guidance_preset": "FAST_BLUE",
#       "height": 512,
#       "width": 512,
#       "style_preser": style_list[random.randrange(0, 16)],
#       "samples": 1,
#       "steps": 30,
#     })
#   data = response.json()
#   byte = (data['artifacts'][0]['base64'])
#   decoded = base64.b64decode(byte)
#   img = Image.open(io.BytesIO(decoded))
#   img.save('pic.jpg')

def get_img():
  prompt = get_prompt()
  urllib.request.urlretrieve(f'https://image.pollinations.ai/prompt/{prompt}', 'pic.png')

def upload_img(mobile):
  upload_id = mobile.get_upload_id("pic.png")
  mobile.upload_photo(upload_id,"pewpewpew \n #art#aiart#idk")
  os.remove("pic.png")


def main():
  keep_alive()
  while (True):
    mobile = login()
    get_img()
    upload_img(mobile)
    print(get_prompt())
    time.sleep(21600)


main()
