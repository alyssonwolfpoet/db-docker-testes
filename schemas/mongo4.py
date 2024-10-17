from pymongo import MongoClient

class MongoDBClient:
    def __init__(self, uri='mongodb://localhost:27017/', db_name='meu_banco_de_dados', collection_name='minha_colecao'):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def criar_documento(self, dados):
        resultado = self.collection.insert_one(dados)
        print(f'Documento criado com id: {resultado.inserted_id}')

    def ler_documentos(self):
        documentos = self.collection.find()
        return [doc for doc in documentos]

    def atualizar_documento(self, filtro, novos_dados):
        resultado = self.collection.update_one(filtro, {'$set': novos_dados})
        print(f'Documentos atualizados: {resultado.modified_count}')

    def deletar_documento(self, filtro):
        resultado = self.collection.delete_one(filtro)
        print(f'Documentos deletados: {resultado.deleted_count}')

if __name__ == "__main__":
    mongo_client = MongoDBClient()

    # Criar um documento
    mongo_client.criar_documento({"nome": "Alice", "idade": 30})

    # Ler documentos
    print("Documentos na coleção:")
    documentos = mongo_client.ler_documentos()
    for doc in documentos:
        print(doc)

    # Atualizar um documento
    mongo_client.atualizar_documento({"nome": "Alice"}, {"idade": 31})

    # Ler documentos novamente
    print("Documentos após atualização:")
    documentos = mongo_client.ler_documentos()
    for doc in documentos:
        print(doc)

    # Deletar um documento
    mongo_client.deletar_documento({"nome": "Alice"})
  
    # Ler documentos novamente
    print("Documentos após deleção:")
    documentos = mongo_client.ler_documentos()
    for doc in documentos:
        print(doc)