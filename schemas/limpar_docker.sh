#!/bin/bash

# Script para limpar contêineres, imagens e volumes no Docker

echo "=== Limpeza de Recursos Docker ==="

# Exibindo os recursos do ambiente
echo "Listando contêineres em execução:"
docker container ls

echo "Listando todos os contêineres:"
docker container ls -a

echo "Listando imagens:"
docker image ls

echo "Listando volumes:"
docker volume ls

echo "Listando redes:"
docker network ls

echo "=== Resumo do Ambiente Docker ==="
docker info

# Limpar todos os recursos não utilizados
echo "Removendo contêineres, redes e imagens não usadas..."
docker system prune -a --volumes -f

# Removendo recursos individualmente (opcional)
# Descomente as linhas abaixo se desejar usar esses comandos
# echo "Removendo contêineres não utilizados..."
# docker container prune -f

# echo "Removendo imagens não utilizadas..."
# docker image prune -a -f

# echo "Removendo volumes não utilizados..."
# docker volume prune -f

# echo "Removendo redes não utilizadas..."
# docker network prune -f

# Parar todos os contêineres
echo "Parando todos os contêineres..."
docker container stop $(docker container ls -a -q)

# Limpeza adicional com combinação de comandos
echo "Realizando limpeza final..."
docker system prune -a -f --volumes

echo "=== Limpeza Concluída ==="
