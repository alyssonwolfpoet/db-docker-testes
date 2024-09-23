docker run --name mongodb -d mongo:latest
docker exec -it mongodb mongo
#robomongo & mongo express 27017

docker run -it --rm --name mongo mongo:latest mongod

https://github.com/docker-library/mongo/issues/558

docker exec -it mongodb mongosh
