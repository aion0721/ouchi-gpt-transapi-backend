from fastapi import FastAPI, Body
from typing import Optional
from translate import Translator

app = FastAPI()

@app.post("/ja_to_en", summary="Japanese to English Translation", description="Translate Japanese text to English.")
async def translate_ja_to_en(text: Optional[str] = Body(..., embed=True)):
    translator = Translator(from_lang="ja", to_lang="en")
    translation = translator.translate(text)
    return {"original_text": text, "translated_text": translation}

@app.post("/en_to_ja", summary="English to Japanese Translation", description="Translate English text to Japanese.")
async def translate_en_to_ja(text: Optional[str] = Body(..., embed=True)):
    translator = Translator(from_lang="en", to_lang="ja")
    translation = translator.translate(text)
    return {"original_text": text, "translated_text": translation}
