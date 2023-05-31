### 本地部署

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
pip install -r requirements.txt
```

run

```console
streamlit run Chat.py
```

### 服务器部署

```
# 拉取最新代码
git clone https://github.com/timeway/chatbot.git
git pull

# 删除旧镜像
docker image rm -f chatbot

# 打包新镜像
docker build . -f server/StreamlitWebApp.Dockerfile -t chatbot

# 停止旧应用
docker rm -f chatbot

# 启动新应用
docker run -d --env-file server/.env -p 8090:80 --name chatbot chatbot 

# 清除未被使用的镜像及其数据
docker image prune -a 

```