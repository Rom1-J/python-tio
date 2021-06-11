BASE_URL = "https://tio.run"
API_URL = f"{BASE_URL}/cgi-bin/run/api"
JSON_URL = f"{BASE_URL}/languages.json"

PAYLOAD = {
    "lang": [],
    ".code.tio": "",
    ".input.tio": "",
    "TIO_CFLAGS": [],
    "TIO_OPTIONS": [],
    "args": [],
}

NULL = "\x00"
