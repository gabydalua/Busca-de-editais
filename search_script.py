import requests
import json
import urllib.parse

API_KEY = 'AIzaSyB8rPU-s8jiCvrxNUi-xcb47CO9EFvVWhw' # Chave do Google Custom Search API
CX = 'e075a6be72d7b4905' # ID do Mecanismo de Pesquisa Personalizado

# Lista de tópicos para busca
queries = [
    'editais para projetos sociais em aberto',
    'editais para projetos de inovação em aberto',
    'editais projetos para leis de incentivo',
    'editais de licitação para projetos'
]

# Limitar o número de resultados (máximo permitido é 10)
num_results = 10

results = {}

# Função para buscar e salvar resultados
def search_and_save_results(query):
    try:
        encoded_query = urllib.parse.quote_plus(query)
        url = f'https://www.googleapis.com/customsearch/v1?q={encoded_query}&key={API_KEY}&cx={CX}&num={num_results}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            results[query] = data.get('items', [])
        else:
            results[query] = []
    except Exception as e:
        results[query] = []

# Executa a busca para cada tópico
for query in queries:
    search_and_save_results(query)

# Salva os resultados em um arquivo JSON
with open('/content/search_results.json', 'w') as f:
    json.dump(results, f)

from google.colab import files
files.download('/content/search_results.json')
