Please ensure you have Python 3.9+ installed.

Create `venv` environment for Python:

```console
python -m venv .venv

# 进入虚拟环境
source .venv/bin/activate

# 退出虚拟环境
deactivate
```

Install `PIP` Requirements

```console
pip install -r src/requirements.txt
```

服务器部署命令备忘

```
# 删除旧镜像
docker image rm -f chatbot

# 打包新镜像
git pull
docker build . -f StreamlitWebApp.Dockerfile -t chatbot

# 停止旧应用
docker rm -f chatbot

# 启动新应用
docker run -d --env-file .env -p 8090:80 --name chatbot chatbot 

# 清除未被使用的镜像及其数据
docker image prune -a 

```