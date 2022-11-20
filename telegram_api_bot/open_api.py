import os
import openai
import requests
openai.api_key=''
openai.Model.list()
def img_gen(word):
    try:
        response = openai.Image.create(prompt=word,n=1,size="1024x1024")
        image_url = response['data'][0]['url']
        return image_url
    except:
        error_response = "sorry!"
        return error_response
