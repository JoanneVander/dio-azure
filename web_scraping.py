!pip install requests beautifulsoup4 openai langchain-openai

import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
        texto = soup.get_text(separator=' ')
        # Limpar texto
        # Change 'text' to 'texto' here
        linhas = (line.strip() for line in texto.splitlines())
        parts = (phrase.strip() for line in linhas for phrase in line.split("  "))
        texto_limpo = '\n'.join(part for part in parts if part)
        return texto_limpo  # This return was in the wrong place
    else:
        print(f"Failed to fetch URL. Status code: {response.status_code}")
        return None

from langchain_openai.chat_models.azure import AzureChatOpenAI

client = AzureChatOpenAI(
    azure_endpoint= "https://dio-oai-bootcamp-dev-eastus-001.openai.azure.com/",
    api_key= "xxxxx",
    api_version= "2024-02-15-preview",
    deployment_name= "gpt-4o-mini",
    max_retries=0
)

def translate_article(text, lang):
  messages = [
      ("system", "Você atua como tradutor e textos"),
      ("user", f"Traduza o {text} para o idioma {lang} e responda em markdown")
  ]
  response = client.invoke(messages)
  print(response.content)
  return response.content

translate_article("Lest's see if the deployment was succeeded.", "português")

url = 'https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo'
text = extract_text_from_url(url)
article = translate_article(text, "pt-br")

print(article)
