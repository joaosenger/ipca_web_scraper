import requests
from bs4 import BeautifulSoup
import sqlite3


# Raspagem dos dados
def extract_ipca_data():
    url = 'https://www.idealsoftwares.com.br/indices/ipca_ibge.html'

    response = requests.get(url=url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    table = soup.find_all(
        name='table',
        attrs={'class': 'table table-bordered table-striped text-center'},
    )[1]

    ipca_data = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if cols:
            month_year = cols[0].text.strip()
            value = cols[1].text.strip().replace(',', '.').replace(' ', '').replace('\n', '')
            if value:
                month, year = month_year.split('/')
                ipca_data.append((int(year), month, float(value)))

    return ipca_data


# Salva os dados raspados em um banco SQLITE
def create_and_populate_db(ipca_data):
    conn = sqlite3.connect('ipca_data.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE ipca (
        year INTEGER,
        month TEXT,
        value REAL
    )
    ''')

    cursor.executemany('''
    INSERT INTO ipca (year, month, value) VALUES (?, ?, ?)
    ''', ipca_data)

    conn.commit()
    conn.close()

    print("Dados inseridos com sucesso no banco de dados SQLite!")


ipca_data = extract_ipca_data()
create_and_populate_db(ipca_data)
