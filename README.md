# IPCA Data Web Scraper

Projeto simples em Python que não utiliza a emulação de navegadores como Selenium, faz a raspagem de dados através de requisições HTTP usando as bibliotecas `requests` e `BeautifulSoup`

## Pré-requisitos

- Python 3.x
- Libs Python:
  - `requests`
  - `beautifulsoup4`

## Instalação

1. Clone o repositório

```bash
git clone https://github.com/joaosenger/ipca_web_scraper.git
cd ipca_web_scraper
```

2. Crie um ambiente virtual (não é obrigatório, mas é recomendado):

```bash
python -m venv venv
source venv/bin/activate # Para Linux/MacOS
.\venv\Scripts\Activate.ps1 # Para Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

Basta executar o script `scraper.py` para raspar os dados e salvá-los no banco de dados.

```bash
python scraper.py
```

## Linter: Flake8

O Linter Flake8 está configurado no projeto. Recomendo que ao implementar novas funcionalidades nesse script o padrão de código e boas práticas da PEP 8 sejam mantidos.

Para executar a verificação do linter:

```bash
flake8
```
