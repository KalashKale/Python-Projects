#From the Higher Order Functions exercise

def translator(language):
    translations = {
    'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
    'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
    'japanese': {'hello': 'こんにちは / konnichiwa', 'goodbye': 'さようなら / sayōnara', 'thank you': 'ありがとう / arigatō'},
    'korean': {'hello': '안녕하세요 / annyeonghaseyo','goodbye': '안녕히 가세요 / annyeonghi gaseyo', 'thank you': '감사합니다 / gamsahamnida'}
    }

    def translate_word(word):
      if word.lower() in translations[language]:
        return translations[language][word.lower()]
      else:
        return 'Translation not available'

    return translate_word


translate_to_korean = translator('korean')
print(translate_to_korean('hello'))