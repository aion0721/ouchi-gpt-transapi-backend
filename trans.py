from translate import Translator

translator = Translator(from_lang="en",to_lang="ja")
translation = translator.translate("It is no use crying over spilt milk.")

print(translation)