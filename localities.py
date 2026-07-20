import requests

class LocalitiesError(Exception):
    """Error específico al obtener localidades."""
    pass

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

    try:

        response = session.post(REQUEST_URL, data=payload, timeout=10)

        response.raise_for_status()

        # eliminamos el UTF-8 BOM (Byte Order Mark)
        response.encoding = "utf-8-sig"

        data = response.json()

    except requests.exceptions.Timeout as e:

        raise LocalitiesError("El servidor tardó demasiado en responder") from e

    except requests.exceptions.ConnectionError as e:

        raise LocalitiesError("No se pudo conectar con el servidor") from e

    except requests.exceptions.HTTPError as e:

        raise LocalitiesError(f"El servidor devolvió un error HTTP: {response.status_code}") from e

    except requests.exceptions.RequestException as e:

        raise LocalitiesError(f"Error inesperado en la petición HTTP: {e}") from e

    except ValueError as e:

        raise LocalitiesError("La respuesta recibida no contiene un JSON válido") from e

    # Validamos que realmente recibimos la lista de localidades
    if not isinstance(data, list):

        raise LocalitiesError("La respuesta JSON no tiene el formato esperado")

    return data
