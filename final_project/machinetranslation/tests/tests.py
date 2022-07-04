'''Test translator.py'''
import translator


def test_french_to_english_null():
    '''confirm that french to english will return null when passed null'''
    if translator.french_to_english('') == '':
        print('french_to_english passes null')
def test_english_to_french_null():
    '''confirm that english to french will return null when passed null'''
    if translator.english_to_french('') == '':
        print('english_to_french passes null')
def test_french_to_english_translation():
    '''confirm accurate translation from french to english'''
    if translator.french_to_english('bonjour') == 'hello':
        print('bonjour translates to hello')
def test_english_to_french_translation():
    '''confirm accurate translation from english to french'''
    if translator.english_to_french('hello') == 'bonjour':
        print('hello translates to bonjour')
