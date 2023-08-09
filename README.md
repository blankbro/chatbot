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
streamlit run Chatbot.py
```

### 服务器部署

```
# 拉取最新代码
git clone https://github.com/timeway/chatbot.git
cd chatbot

# 一键运行
./launch.sh
```