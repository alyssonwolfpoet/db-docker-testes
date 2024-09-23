Claro! Aqui está um script em Bash que você pode usar para rodar o seu contêiner Docker do PostgreSQL com as configurações que você especificou. Você pode salvá-lo em um arquivo, por exemplo, `start_postgres.sh`.

```bash
#!/bin/bash

# Nome do contêiner
CONTAINER_NAME="squard7-postgres"

# Configurações do PostgreSQL
POSTGRES_USER="alysson"
POSTGRES_PASSWORD="senhabanco"
POSTGRES_DB="db"

# Volumes
VOLUME_NAME="pgdata"

# Parar e remover contêiner se já estiver rodando
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Parando e removendo contêiner existente..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Criar volume se não existir
if [ -z "$(docker volume ls -q -f name=$VOLUME_NAME)" ]; then
    echo "Criando volume $VOLUME_NAME..."
    docker volume create $VOLUME_NAME
fi

# Executar o contêiner
echo "Iniciando o contêiner $CONTAINER_NAME..."
docker run --name $CONTAINER_NAME \
    -e POSTGRES_USER=$POSTGRES_USER \
    -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
    -e POSTGRES_DB=$POSTGRES_DB \
    -p 5432:5432 \
    -v $VOLUME_NAME:/var/lib/postgresql/data \
    -d postgres

echo "Contêiner $CONTAINER_NAME iniciado com sucesso!"
```

### Instruções para usar o script:

1. **Crie o arquivo**:
   ```bash
   nano start_postgres.sh
   ```

2. **Cole o código acima** e salve o arquivo.

3. **Dê permissão de execução ao script**:
   ```bash
   chmod +x start_postgres.sh
   ```

4. **Execute o script**:
   ```bash
   ./start_postgres.sh
   ```

Isso deve configurar e iniciar o seu contêiner PostgreSQL conforme suas especificações. Se precisar de mais ajustes, é só avisar!