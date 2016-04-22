## key commands





### docker instance on Mac OS


1. Install docker and create a virtualbox

[I'm an inline-style link](https://docs.docker.com/mac/step_one/)

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

```
docker-machine create --driver virtualbox --virtualbox-cpu-count 2 --virtualbox-memory "4096" \
 --virtualbox-disk-size "10000" spark
```

```sh
docker-machine env spark
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.101:2376"
export DOCKER_CERT_PATH="/Users/zyan/.docker/machine/machines/spark"
export DOCKER_MACHINE_NAME="spark"
docker-machine env spark
```

```{r, engine='bash', count_lines}

```

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```

```
No language indicated, so no syntax highlighting.
But let's throw in a <b>tag</b>.
```


  2. build image or load from a tar file







### build new image
    `sudo docker build -t datasci/ipyspark160 . `
    sudo docker build --rm=true --no-cache -t datasci/ipyspark161 .
    docker build --rm 

### create a container
    sudo docker run -v /data:/data -it -p 8888:8888 --name ipyspark161 datasci/ipyspark161 /bin/bash
    sudo docker run -v /data:/data -it -p 8883:8888 --name model datasci/model /bin/bash
    sudo docker run -v /data:/data -it -p 8883:8888 --name model datasci/ipyspark160 /bin/bash
    sudo docker run -v /data:/data --name model datasci/model /bin/bash

### setup notebook and check
    sudo docker attach ipyspark160
    cd ~
    sh run_ipython.sh
    http://hostname:port

### remove docker image
    1. remove one image
    docker rmi -f 5a02181db761
    2. remove all <none> images
    docker rmi -f $(docker images -a | grep "^<none>" | awk '{print $3}')
    sudo docker rm -f $(sudo docker ps -a -q | grep -v <good_container_1> | grep -v <good_container_2>)


### kill docker container
    docker kill -s 7f9335be640a
    docker ps -a | grep Exited | awk '{print $1}'
    docker rm --force `docker ps -qa`
    docker rm -f $(docker ps -a | grep Exited | awk '{print $1}')
    
    
### setup docker on OS
    docker-machine create --driver virtualbox --virtualbox-cpu-count 2 --virtualbox-memory "4096" \
        --virtualbox-disk-size "10000" spark

    zyan@:~ $ docker-machine env spark
    export DOCKER_TLS_VERIFY="1"
    export DOCKER_HOST="tcp://192.168.99.101:2376"
    export DOCKER_CERT_PATH="/Users/zyan/.docker/machine/machines/spark"
    export DOCKER_MACHINE_NAME="spark"

    docker-machine env spark
