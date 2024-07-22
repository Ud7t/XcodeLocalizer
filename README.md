# Xcode String Catalog Localizer
A Python tool that automatically translates an Xcode project's strings catalog into the desired languages. It currently supports translation using either Google Translate or DeepL.

**Note**: It is recommended to have someone review and correct the translations before deploying them to production.

## Requirements

- Python 3.6 or higher.
- `googletrans==4.0.0-rc1` or higher (Google Translate API for Python).
- `deepl==1.18.0` or higher (DeepL API for Python).
- A DeepL api key (if you want to use DeepL). You can obtain one for free [here](https://www.deepl.com/en/your-account/keys).

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Ud7t/xcode-string-catalog-localizer.git
   cd xcode-strings-localizer
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
   
## Usage
Decide whether you want to use Google Translate or DeepL. Use the appropriate file.

- The list of languages supported by the DeepL API can be found [here](https://developers.deepl.com/docs/resources/supported-languages).
- The list of languages supported by the Google Translate API can be found [here](https://py-googletrans.readthedocs.io/en/latest/).


If you would like to use DeepL, please set the `DEEPL_API_KEY` variable to your API key (which can be obtained for free [here](https://www.deepl.com/en/your-account/keys)).

Add the languages you want to translate to in the LANGUAGE_IDENTIFIERS variable in the appropriate script.

Now run the script:

```bash
python3 localizer_DeepL.py
```
or
```bash
python3 localizer_Google_Translate.py
```
You will be prompted to enter the path to string catalog file. The path may look like this:
`/Users/your_name/Documents/your_Xcode_project/Localizable.xcstrings`.
You can get the path by dragging and dropping the file into the terminal.

Now press enter and watch the magic unfold!
## Contributing
Contributions are encouraged! Please open an issue or submit a PR for any enhancements or bug fixes.


