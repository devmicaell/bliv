import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")
BASE_URL = "https://www.googleapis.com/books/v1"

class GoogleBooksAPI:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL

    def buscar_livros(self, query, max_resultados=30):
        endpoint = f"{self.base_url}/volumes"
        params = {
            "q": query,
            "key": self.api_key,
            "maxResults": max_resultados
        }
        resposta = requests.get(endpoint, params=params)
        return resposta.json()

def formatar_info_livro(livro):

    volume_info = livro.get("volumeInfo", {})
    saleinfo = livro.get("saleInfo", {})
    id = livro.get("id")
    titulo = volume_info.get("title", "Sem título")
    autores = volume_info.get("authors", ["Autor desconhecido"])
    ano = volume_info.get("publishedDate", "Desconhecido")
    paginas = volume_info.get("pageCount", "Indefinido")
    imagem = volume_info.get("imageLinks", {}).get("thumbnail", "")

    retail_price = saleinfo.get("retailPrice", {})
    value = retail_price.get("amount", "Indisponível")
    currency_code = retail_price.get("currencyCode", "")

    currency_symbols = {
        "BRL": "R$",
        "USD": "$",
        "GBP": "£",
        "EUR": "€"
    }

    currency_symbol = currency_symbols.get(currency_code, currency_code)

    valor_final = f"{currency_symbol}{value}" if value != "Indisponível" else "Indisponível"


    return {
        "id": id,
        "title": titulo,
        "author": ', '.join(autores),
        "release_year": ano,
        "pages": paginas,
        "image": imagem,
        "value": valor_final,
    }