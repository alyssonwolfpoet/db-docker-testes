from pymongo import MongoClient

# Conectar ao MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco_de_dados']
colecao = db['minha_colecao']

# Função para criar um documento
def criar_documento(dados):
    resultado = colecao.insert_one(dados)
    print(f'Documento criado com id: {resultado.inserted_id}')

# Função para ler documentos
def ler_documentos():
    documentos = colecao.find()
    for doc in documentos:
        print(doc)

# Função para atualizar um documento
def atualizar_documento(filtro, novos_dados):
    resultado = colecao.update_one(filtro, {'$set': novos_dados})
    print(f'Documentos atualizados: {resultado.modified_count}')

# Função para deletar um documento
def deletar_documento(filtro):
    resultado = colecao.delete_one(filtro)
    print(f'Documentos deletados: {resultado.deleted_count}')

# Exemplo de uso
if __name__ == "__main__":
    # Criar um documento
    criar_documento({"nome": "Alice", "idade": 30})

    # Ler documentos
    print("Documentos na coleção:")
    ler_documentos()

    # Atualizar um documento
    atualizar_documento({"nome": "Alice"}, {"idade": 31})

    # Ler documentos novamente
    print("Documentos após atualização:")
    ler_documentos()

    # Deletar um documento
    deletar_documento({"nome": "Alice"})

    # Ler documentos novamente
    print("Documentos após deleção:")
    ler_documentos()
