import deepl
import os
import json
import time

auth_key = "your auth_key"
translator = deepl.Translator(auth_key)

today = time.strftime("%Y_%m_%d", time.localtime())
DB = f"history{today}.json"

def load_data(db):
    try:
        with open(db, "r", encoding='utf-8') as f:
            data = json.load(f)
            return data
    except:
        return {}

def save_data(db, data):
    with open(db, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def multiTranslate(text):

    result = translator.translate_text(text, target_lang="IT", formality="more")
    print(result.text)
    r1 = result.text

    result = translator.translate_text(text, target_lang="IT", formality="less")
    print(result.text)
    r2 = result.text

    result = translator.translate_text(text, target_lang="EN-US")
    print(result.text)
    r3 = result.text

    data = load_data(DB)
    data[text] = [r1, r2, r3]
    save_data(DB, data)


for __name__ in "__main__":
    text = input("Enter the text you want to translate or insert q to exit:")
    if text == "q":
        break
    elif text == "cls":
        os.system("cls")
    else:
        multiTranslate(text)



#reference: https://github.com/DeepLcom/deepl-python
#official document: https://www.deepl.com/zh/docs-api/translating-text/request/
