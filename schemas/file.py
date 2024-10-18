import pymongo
from pymongo import MongoClient
import gridfs
import os

def connect_to_mongo(uri, db_name):
    """Conecta ao MongoDB e retorna a instância do GridFS."""
    client = MongoClient(uri)
    db = client[db_name]
    return db, gridfs.GridFS(db)

def insert_pdf(file_path, fs, filename):
    """Insere um arquivo PDF no GridFS."""
    try:
        with open(file_path, 'rb') as f:
            fs.put(f, filename=filename)
        print('Arquivo PDF inserido com sucesso!')
    except FileNotFoundError:
        print(f'Erro: O arquivo "{file_path}" não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro ao inserir o arquivo: {e}')

def retrieve_pdf(fs, filename, output_path):
    """Recupera um arquivo PDF do GridFS."""
    try:
        file_data = fs.find_one({'filename': filename})
        if file_data:
            with open(output_path, 'wb') as f:
                f.write(file_data.read())
            print('Arquivo PDF recuperado com sucesso!')
        else:
            print(f'Erro: O arquivo "{filename}" não foi encontrado no GridFS.')
    except Exception as e:
        print(f'Ocorreu um erro ao recuperar o arquivo: {e}')

def main():
    uri = 'mongodb://localhost:27017/'  # Substitua pela sua URI
    db_name = 'meuBanco'  # Substitua pelo seu banco de dados
    file_path = 'IntroducaoaosSistemasEmbarcados.pdf'  # Substitua pelo caminho do seu PDF
    filename = 'meuArquivo.pdf'  # Nome para armazenar no MongoDB
    output_path = 'recuperado_' + filename  # Caminho para salvar o PDF recuperado

    db, fs = connect_to_mongo(uri, db_name)

    # Inserir o PDF
    insert_pdf(file_path, fs, filename)

    # Recuperar o PDF
    retrieve_pdf(fs, filename, output_path)

    # Fechar a conexão
    db.client.close()

if __name__ == "__main__":
    main()

# import pymongo
# from pymongo import MongoClient
# import gridfs

# # Conectar ao MongoDB
# client = MongoClient('mongodb://localhost:27017/')  # substitua pela sua URI
# db = client['meuBanco']  # substitua pelo seu banco de dados
# fs = gridfs.GridFS(db)

# # Caminho do arquivo PDF
# file_path = 'IntroducaoaosSistemasEmbarcados.pdf'  # substitua pelo caminho do seu PDF

# # Inserir o arquivo PDF no GridFS
# with open(file_path, 'rb') as f:
#     fs.put(f, filename='meuArquivo.pdf')

# print('Arquivo PDF inserido com sucesso!')

# # Fechar a conexão
# client.close()
