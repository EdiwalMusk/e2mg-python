from googletrans import Translator

translator = Translator()
result = translator.translate('酒店设施非常不错', src='zh-cn', dest='en')
print(result.text)


result = translator.translate(result.text, dest='zh-cn', src='en')
print(result.text)