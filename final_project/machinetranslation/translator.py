'''Contains translate functions from French to English and back'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Translate from English to French'''
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))

def french_to_english(french_text):
    '''Translate from French to English'''
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
