import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile


base_dir = os.path.dirname(os.path.abspath(__file__))
outpur_dir = os.path.join(base_dir, '..', 'Arquivos')
os.makedirs(outpur_dir,exist_ok=True)

page_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

def get_pdf_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']

            if href.endswith('.pdf') and "Anexo" in href:
                links.append(href)

        print(f"{len(links)} PDF files found.")

        return links
    except requests.exceptions.RequestException as es:
        print(f"Request error: {es}")
        return []


def download_pdf(url, folder):
    try:
        response = requests.get(url)
        response.raise_for_status()

        file_name = url.split("/")[-1]
        file_path = os.path.join(folder, file_name)

        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Download completed: {file_name}")
        return file_path
    except requests.exceptions.RequestException as e:
        print(f"Download error: {e}")
        return None

def zip_files(file_paths, zip_path):
    with ZipFile(zip_path, "w") as zip_file:
        for file in file_paths:
            zip_file.write(file, os.path.basename(file))
            print(f"{os.path.basename(file)} added to zip")
    print(f"Zipped file Successfully in {zip_path}")

pdf_urls = get_pdf_links(page_url)

downloaded_pdfs = [download_pdf(url, outpur_dir) for url in pdf_urls]

zip_path = os.path.join(outpur_dir, "anexos_zipados.zip")
zip_files(downloaded_pdfs, zip_path)
