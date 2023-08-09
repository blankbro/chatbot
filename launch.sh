#!/bin/bash

# 发生错误则退出
set -e

# 拉取最新代码
git pull

# 删除旧容器
if docker ps -a | grep -q "chatbot"; then
    docker rm -f chatbot
fi

# 删除旧镜像
if docker image ls | grep -q "chatbot"; then
    docker image rm -f chatbot
fi

# 打包新镜像
docker build . -t chatbot

# 启动新容器
docker run -d -p 8082:80 --name chatbot chatbot

# 清除未被使用的镜像及其数据
docker image prune -a
