Para rodar o MongoDB em um contêiner Docker, você pode seguir estes passos:

### Passo 1: Instalar o Docker

Certifique-se de que o Docker esteja instalado em sua máquina. Você pode baixar e instalar o Docker [aqui](https://docs.docker.com/get-docker/).

### Passo 2: Baixar e Executar o MongoDB

Execute o seguinte comando no terminal para baixar e iniciar o MongoDB:

```bash
docker run --name mongo -d -p 27017:27017 -v mongo_data:/data/db mongo
```

### Explicação do Comando

- `--name mongo`: Nomeia o contêiner como "mongo".
- `-d`: Executa o contêiner em segundo plano (modo "detached").
- `-p 27017:27017`: Mapeia a porta 27017 do contêiner para a porta 27017 da sua máquina.
- `-v mongo_data:/data/db`: Cria um volume chamado "mongo_data" para persistência de dados, garantindo que os dados não sejam perdidos ao reiniciar o contêiner.
- `mongo`: O nome da imagem do MongoDB que será usada.

### Passo 3: Verificar se o MongoDB Está em Execução

Para verificar se o MongoDB está funcionando, você pode usar o comando:

```bash
docker ps
```

Isso mostrará os contêineres em execução. Você deve ver o contêiner "mongo" listado.

### Passo 4: Conectar ao MongoDB

Você pode se conectar ao MongoDB usando um cliente de MongoDB ou pela linha de comando. Para acessar o shell do MongoDB no contêiner, execute:

```bash
docker exec -it mongo mongo
```

### Passo 5: Usar o MongoDB com Python

Depois de iniciar o MongoDB, você pode usar o código Python que forneci anteriormente para realizar operações CRUD. Certifique-se de que seu script Python se conecte ao MongoDB na URL `mongodb://localhost:27017/`.

### Parar e Remover o Contêiner

Quando terminar de usar o MongoDB, você pode parar e remover o contêiner com os seguintes comandos:

```bash
docker stop mongo
docker rm mongo
```

Se precisar de mais alguma informação ou ajuda, é só avisar!