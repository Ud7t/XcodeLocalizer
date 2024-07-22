import datetime
import deepl
import json

DEEPL_API_KEY = ''

# Add target langauges for translation here
LANGUAGE_IDENTIFIERS = ['en', 'uk', 'ro']

if not DEEPL_API_KEY:
    raise ValueError("The DEEPL_API_KEY needs to be set!")

translator = deepl.Translator(DEEPL_API_KEY)

def translate_string(string, target_language):
    try:
        result = translator.translate_text(string, target_lang=target_language.upper())
        print(f"{target_language.upper()}: {result.text}")
        return result.text
    except deepl.DeepLException as e:
        print(f"{type(e).__name__}: {e}")
        return None

def load_json(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(json_data, json_path):
    with open(json_path, "w", encoding='utf-8') as f:
        json.dump(json_data, ensure_ascii=False, fp=f, indent=4)

def process_string_key(json_data, key, strings, language_identifiers):
    localizations = strings.get("localizations", {})

    for language in language_identifiers:
        if language not in localizations or not localizations[language].get("stringUnit", {}).get("value"):
            source_language = json_data["sourceLanguage"]
            source_string = (
                localizations.get("en", {}).get("stringUnit", {}).get("value", key)
            )
            if language == source_language:
                translated_string = source_string
            else:
                translated_string = translate_string(source_string, language)
                if translated_string is None:
                    continue # Skip saving if translation failed

            localizations[language] = {
                "stringUnit": {
                    "state": "translated",
                    "value": translated_string,
                }
            }
        else:
            print(f"{language} has already been translated")

    strings["localizations"] = localizations
    json_data["strings"][key] = strings

def main(json_path):
    json_data = load_json(json_path)
    strings_keys = list(json_data["strings"].keys())

    print(f"\nFound {len(strings_keys)} keys\n")

    for key_index, key in enumerate(strings_keys):
        if not key:
            continue
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{'-'*40}\n[{now}]\n", f"{key_index + 1}/{len(strings_keys)}: {key}")

        strings = json_data["strings"].get(key, {"extractionState": "manual", "localizations": {}})
        process_string_key(json_data, key, strings, LANGUAGE_IDENTIFIERS)
        save_json(json_data, json_path)

if __name__ == "__main__":
    json_path = input("Enter the string catalog's (.xcstrings) file path:\n").strip(' "\'')
    main(json_path)
