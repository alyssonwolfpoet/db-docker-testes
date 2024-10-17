Claro! Aqui está a versão refatorada de todo o projeto, incluindo a parte de retornar todos os documentos de uma coleção com base em uma referência. Vamos estruturar o código de maneira mais organizada, utilizando uma classe para encapsular as operações.

### Código Refatorado Completo

```python
from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoDBClient:
    def __init__(self, uri='mongodb://localhost:27017/', db_name='meu_banco_de_dados'):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def criar_documento(self, collection_name, dados):
        collection = self.db[collection_name]
        resultado = collection.insert_one(dados)
        print(f'Documento criado com id: {resultado.inserted_id}')

    def ler_documentos(self, collection_name):
        collection = self.db[collection_name]
        documentos = collection.find()
        return [doc for doc in documentos]

    def atualizar_documento(self, collection_name, filtro, novos_dados):
        collection = self.db[collection_name]
        resultado = collection.update_one(filtro, {'$set': novos_dados})
        print(f'Documentos atualizados: {resultado.modified_count}')

    def deletar_documento(self, collection_name, filtro):
        collection = self.db[collection_name]
        resultado = collection.delete_one(filtro)
        print(f'Documentos deletados: {resultado.deleted_count}')

    def deletar_todos_documentos(self, collection_name):
        collection = self.db[collection_name]
        resultado = collection.delete_many({})
        print(f'Documentos deletados: {resultado.deleted_count}')

    def retornar_posts_por_usuario(self, usuario_id):
        posts = self.db.posts.find({"usuario_id": usuario_id})
        return [post for post in posts]

if __name__ == "__main__":
    mongo_client = MongoDBClient()

    # Criar documentos de exemplo
    mongo_client.criar_documento("usuarios", {"nome": "Alice", "idade": 30})
    mongo_client.criar_documento("usuarios", {"nome": "Bob", "idade": 25})

    # Criar posts de exemplo
    mongo_client.criar_documento("posts", {"titulo": "Post 1", "usuario_id": ObjectId("id_do_usuario_aqui")})
    mongo_client.criar_documento("posts", {"titulo": "Post 2", "usuario_id": ObjectId("id_do_usuario_aqui")})

    # Ler documentos
    print("Usuários na coleção:")
    usuarios = mongo_client.ler_documentos("usuarios")
    for usuario in usuarios:
        print(usuario)

    # Atualizar um documento
    mongo_client.atualizar_documento("usuarios", {"nome": "Alice"}, {"idade": 31})

    # Deletar todos os posts
    mongo_client.deletar_todos_documentos("posts")

    # Retornar posts por usuário
    usuario_id = ObjectId("id_do_usuario_aqui")  # Substitua pelo ID do usuário desejado
    posts = mongo_client.retornar_posts_por_usuario(usuario_id)

    print(f"Posts do usuário {usuario_id}:")
    for post in posts:
        print(post)

    # Deletar todos os usuários
    mongo_client.deletar_todos_documentos("usuarios")
```

### O que foi mudado:

1. **Uso de Métodos Genéricos**: A maioria das operações CRUD agora aceita um `collection_name` como argumento, permitindo que você manipule diferentes coleções de forma mais flexível.
2. **Encapsulamento de Lógica**: Todos os métodos estão encapsulados dentro da classe `MongoDBClient`, melhorando a modularidade.
3. **Uso de `ObjectId`**: A função para retornar posts por usuário agora suporta `ObjectId`, permitindo referências diretas.

### Como Usar

1. **Instale as Dependências**:
   - Certifique-se de ter `pymongo` e `bson` instalados.
   
   ```bash
   pip install pymongo
   ```

2. **Execute o Código**:
   - Substitua `"id_do_usuario_aqui"` pelo ID real do usuário ao testar.
   - Execute o script em um ambiente onde o MongoDB esteja rodando.

### Conclusão

Esta versão refatorada proporciona uma estrutura mais clara e flexível para realizar operações no MongoDB com Python. Se precisar de mais alguma coisa ou ajustes, é só avisar!