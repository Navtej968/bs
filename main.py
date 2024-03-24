from get_prompt import get_prompt, style_list
from keep_alive import keep_alive
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
from ensta import Host

#insta = Host()


def login():
  insta = Host(os.environ['username'], os.environ['password'])
  return host
  
  
def getimage():
  engine_id = "stable-diffusion-v1-6"
  response = requests.post(
    f"https://api.stability.ai/v1/generation/{engine_id}/text-to-image",
    headers={
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": "sk-3T9bZCmys1ku91a4V2Hz1IhfUYG9DloaGuHBxK35OfxuOuuc"
    },
    json={
      "text_prompts": [{
        "text": get_prompt()
      }],
      "cfg_scale": 7,
      "clip_guidance_preset": "FAST_BLUE",
      "height": 512,
      "width": 512,
      "style_preser": style_list[random.randrange(0, 16)],
      "samples": 1,
      "steps": 30,
    })
  data = response.json()
  byte = (data['artifacts'][0]['base64'])
  decoded = base64.b64decode(byte)
  img = Image.open(io.BytesIO(decoded))
  img.save('pic.jpg')


def upload_img(insta):
  upload_id = insta.get_upload_id("pic.jpg")
  insta.upload_photo(upload_id,"pewpewpew \n #art#aiart#idk")
  os.remove("pic.jpg")


def main():
  keep_alive()
  while (True):
    insta = login()
    getimage()
    upload_img(insta)
    print(get_prompt())
    time.sleep(21600)


main()
