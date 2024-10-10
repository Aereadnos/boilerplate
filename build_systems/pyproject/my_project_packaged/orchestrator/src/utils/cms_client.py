#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os

class StrapiClient:
    def __init__(self, base_url= 'http://localhost:1337', token= os.getenv('STRAPI_TOKEN')):
        self.base_url = base_url
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
        }

    def post_lesson(self, lesson_text:str ):
        url = f'{self.base_url}/api/lessontestriches'
        data = {
            "data": {
                "raw": f"{lesson_text}"
            }
        }
        print(data)
        response = requests.post(url=url, json=data, headers=self.headers)
        print(response.status_code)
        print(response.json())
        return response


