import requests

REQUEST_URL = (
    "https://www.correoargentino.com.ar/sites/all/modules/custom/ca_forms/api/wsFacade.php"
)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:152.0) Gecko/20100101 Firefox/152.0',
    'X-Requested-With': 'XMLHttpRequest'
}

session = requests.Session()
session.headers.update(HEADERS)

def get_localities(province_code):

    payload = {
        'action': 'localidades',
        'localidad': 'none',
        'calle': '',
        'altura': '',
        'provincia': province_code
    }

    response = session.post(REQUEST_URL, data=payload)

    # eliminamos el UTF-8 BOM (Byte Order Mark)
    response.encoding = "utf-8-sig"

    return response.json()
