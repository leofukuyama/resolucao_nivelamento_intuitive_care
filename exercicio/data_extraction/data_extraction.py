import os
import tabula
import pandas as pd
from zipfile import ZipFile

def process_file(anexo_path, csv_path):
    tables = tabula.read_pdf(anexo_path, pages="all", multiple_tables=True)
    filtered_tables = []

    filter_tables(tables, filtered_tables, csv_path)

def filter_tables(tables, filtered_tables, csv_path):
    for i, table in enumerate(tables):
        if table.shape[1] == 13:
            filtered_tables.append(table)

    if filtered_tables:
        final_df = pd.concat(filtered_tables, ignore_index=True)

        final_df = final_df.loc[:, ~final_df.columns.str.contains('^Unnamed')]

        if "RN" in final_df.columns:
            final_df = final_df.drop(columns=["RN"])

        final_df.replace({
            "OD": "Seg. Odontológica",
            "AMB": "Seg. Ambulatorial",
            "HCO": "Seg. Hospitalar Com Obstetrícia",
            "HSO": "Seg. Hospitalar Sem Obstetrícia",
            "REF": "Plano Referência",
            "PAC": "Procedimento de Alta Complexidade",
            "DUT": "Diretriz de Utilização"
        }, inplace=True)

        save_csv(final_df, csv_path)
    else:
        print("No 13 columns table found.")

def save_csv(final_df, csv_path):
    csv_file_path = os.path.join(csv_path, "tabela_anexo_I.csv")
    final_df.to_csv(csv_file_path, index=False)
    print(".CSV file created.")

    zip_files(csv_file_path, csv_path)

def zip_files(csv_file_path, zip_path):
    zip_file_path = os.path.join(zip_path, "Teste_LeonardoOliveira.zip")
    with ZipFile(zip_file_path, "w") as zip_file:
        zip_file.write(csv_file_path, os.path.basename(csv_file_path))
        print(f"{os.path.basename(csv_file_path)} added to zip")

    print(f"Zipped file successfully in {zip_file_path}")

arquivos_path = "..\\Arquivos\\"
pdf_path = arquivos_path + "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

process_file(pdf_path, arquivos_path)
