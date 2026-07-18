import requests

def get_localitites(province_code):

    request_url = "https://www.correoargentino.com.ar/sites/all/modules/custom/ca_forms/api/wsFacade.php"

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:152.0) Gecko/20100101 Firefox/152.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://www.correoargentino.com.ar/',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.correoargentino.com.ar',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Cookie': 'TSc77a954b029=0869a17c0bab2800d5e615217abc97ac81738d37027a27ffa64d742a135c512fa9bfcf32ad6dbfa6420501736f54d3a2; TSfd9fef68027=0869a17c0bab2000373a5a3a611d849f1b17d7de6faedf2031d9af389ad7134976080e67218ba77d0817a36b8b1130008eed2ffb8fd5da09fb63894c08c83301e62ae6efa5e1bd78a393604140022577520c7977f7a8673de6f878eff540fd8a; visid_incap_3331562=lLTlLk/mQx+sYmD7HA/R5dyrWmoAAAAAQUIPAAAAAACTD8pQoZ6guh6fhcz7iBBj; nlbi_3331562=pV2cTSGooHkEUlvI8AHJwAAAAADafJpJcHjI+3A88Nzn2zJC; incap_ses_123_3331562=oONxQOFdZ2eL1Ccsdfy0AdyrWmoAAAAAn67o3DZ/v0jR3aznmmI6GQ==; BIGipServerPL_PROD_WWW=3356098826.47873.0000; has_js=1; _gcl_au=1.1.839780671.1784327138',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0',
        'TE': 'trailers'
    }

    payload = {
        'action': 'localidades',
        'localidad': 'none',
        'calle': '',
        'altura': '',
        'provincia': province_code
    }

    response = requests.post(request_url, headers=headers, data=payload)

    # eliminamos el UTF-8 BOM (Byte Order Mark)
    response.encoding = "utf-8-sig"

    return response.json()