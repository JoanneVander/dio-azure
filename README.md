Conectando ao Azure OpenAI e Traduzindo Texto

Este repositório demonstra como conectar-se ao Azure OpenAI usando a biblioteca langchain_openai e traduzir texto para português. O código é dividido em três partes principais: importação da classe, criação do cliente e definição da função de tradução.

1. Importação da Classe:

from langchain_openai.chat_models.azure import AzureChatOpenAI

Importa a classe AzureChatOpenAI necessária para interagir com o serviço.

2. Criação do Cliente Azure OpenAI:

client = AzureChatOpenAI(
    azure_endpoint= "https://dio-oai-bootcamp-dev-eastus-001.openai.azure.com/", # **ATENÇÃO:** Substitua pelo ENDPOINT
    api_key= "xxxx",  # **ATENÇÃO:** Substitua pela sua chave API
    api_version= "2024-02-15-preview",
    deployment_name= "gpt-4o-mini",
    max_retries=0
)

Cria uma instância do cliente AzureChatOpenAI com as credenciais e configurações do seu serviço Azure OpenAI. É CRUCIAL substituir a chave API de exemplo pela sua chave real. A segurança da sua chave API é fundamental. Evite commitar chaves diretamente no repositório; considere usar variáveis de ambiente.

3. Função de Tradução:

def translate_article(text, lang="pt-br"):
  messages = [
("system", "Você atua como tradutor de textos."),
("user", f"Traduza o seguinte texto para {lang}: {text}")]
  response = client.invoke(messages)
  return response.content

Define uma função translate_article que recebe o texto e o idioma de destino (padrão: "pt-br"). Utiliza a técnica de prompt engineering para instruir o modelo a traduzir.

4. Exemplo de Uso:

text_to_translate = "Let's see if the deployment was successful."
translated_text = translate_article(text_to_translate)
print(translated_text)

Demonstra como usar a função de tradução com um exemplo.

5. Integração com Extração de Texto de URL:

Se você precisar extrair texto de uma URL antes da tradução, adicione uma função como esta (este exemplo necessita de uma biblioteca adicional, como requests e beautifulsoup4):

import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text(" ", strip=True)
    return text

url = "YOUR_URL_HERE" # Substitua pela URL desejada
text = extract_text_from_url(url)
translated_text = translate_article(text)
print(translated_text)

Lembre-se de instalar as bibliotecas necessárias: pip install requests beautifulsoup4

Segurança: Nunca compartilhe sua chave API publicamente. Utilize variáveis de ambiente para armazená-la de forma segura.

Limitação de Tokens: Modelos de linguagem grandes têm limites de tokens. Textos muito longos podem precisar ser divididos em partes menores para serem traduzidos.

Este README fornece uma estrutura clara e concisa para o seu código no GitHub. Lembre-se de adicionar um arquivo requirements.txt listando as dependências (langchain, openai, requests, beautifulsoup4). A inclusão de testes unitários também é recomendada para garantir a qualidade do código.
