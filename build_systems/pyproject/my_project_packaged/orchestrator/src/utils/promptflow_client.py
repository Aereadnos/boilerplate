import requests
import json

class PFGeneratorClient:
    def __init__(self):
        self.url = "https://generators.azurewebsites.net/score"
        self.headers = {
            "Content-Type": "application/json"
        }

    def generate_summary(self, language, text, voice="professional"):
        data = {
            "language": language,
            "text": text,
            "type": "summary",
            "voice": voice
        }

        response = requests.post(self.url, headers=self.headers, json=data)

        if response.status_code == 200:
            return response.json()['GeneratedResult']
        else:
            return {
                "error": f"Request failed with status code {response.status_code}",
                "response_text": response.text
            }

    def generate_quiz(self, language: str, text:str, voice :str ="professional" ):
        data = {
            "language": language,
            "text": text,
            "type": "quiz",
            "voice": voice
        }

        response = requests.post(self.url, headers=self.headers, json=data)

        if response.status_code == 200:
            text_block = str(response.json()['GeneratedResult'])
            print(text_block)
            data = json.loads(text_block[text_block.find('{'):text_block.rfind('}') + 1])
            first_key = next(iter(data))
            quiz_object = data.get(first_key)
            return quiz_object if quiz_object is not None else {"error": "failed to parse" }

        else:
            return {
                "error": f"Request failed with status code {response.status_code}",
                "response_text": response.text
            }

