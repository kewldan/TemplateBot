docker container stop fsb
docker container rm fsb
docker image rm fsbi
docker build -t fsbi .
docker run -d -p 4003:4003 --name fsb --mount type=bind,source=/home/freeshop/data,target=/Application/data fsbi
docker container ls