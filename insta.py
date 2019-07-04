#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time
import requests

def get_media_id(url):
    req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
    media_id = req.json()['media_id']
    return media_id


API = InstagramAPI("<username>", "<password>")
API.login()
mid = get_media_id('https://www.instagram.com/p/BuO0mBuhWLe/')
API.getMediaLikers(mid)
Likers = API.LastJson
print(Likers)
