### Install docker container on Mac OS


1. Install docker and create a virtualbox

Install Docker on Mac

[https://docs.docker.com/mac/step_one/](https://docs.docker.com/mac/step_one/)

Create a virtual box, called 'spark'

```
docker-machine create --driver virtualbox --virtualbox-cpu-count 2 --virtualbox-memory "4096" \
 --virtualbox-disk-size "10000" ipyspark
```

Setup virtual box environment
```sh
docker-machine env ipyspark
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/zyan/.docker/machine/machines/ipyspark"
export DOCKER_MACHINE_NAME="ipyspark"
docker-machine env ipyspark
```

```sh
docker-machine ls
docker-machine stop/start
```

2. Build image or load from a tar file

```sh
docker build --rm=true --no-cache -t zyan/model .
cat model.tar | docker import - model:latest
```

3. Run a container
```
docker run -v /Users/zyan:/data -it -p 8888:8888 --name model ipyspark161 /bin/bash
```


### Common docker commands - cheetsheet

1. build new image
```
`sudo docker build -t datasci/ipyspark160 . `
sudo docker build --rm=true --no-cache -t datasci/ipyspark161 .
docker build --rm
```

2. create a container
```sh
sudo docker run -v /data:/data -it -p 8888:8888 --name ipyspark161 datasci/ipyspark161 /bin/bash
sudo docker run -v /data:/data -it -p 8883:8888 --name model datasci/model /bin/bash
sudo docker run -v /data:/data -it -p 8883:8888 --name model datasci/ipyspark160 /bin/bash
sudo docker run -v /data:/data --name model datasci/model /bin/bash
```

3. setup notebook and check
```
sudo docker attach ipyspark160
cd ~
sh run_ipython.sh
http://hostname:port
```
4. remove docker image
```
1. remove one image
docker rmi -f 5a02181db761
2. remove all <none> images
docker rmi -f $(docker images -a | grep "^<none>" | awk '{print $3}')
sudo docker rm -f $(sudo docker ps -a -q | grep -v <good_container_1> | grep -v <good_container_2>)
```

5. kill docker container
```
docker kill -s 7f9335be640a
docker ps -a | grep Exited | awk '{print $1}'
docker rm --force `docker ps -qa`
docker rm -f $(docker ps -a | grep Exited | awk '{print $1}')
```
