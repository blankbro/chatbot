FROM python:3.9.10-slim-buster
RUN apt-get update && apt-get install python-tk python3-tk tk-dev -y

COPY requirements.txt /usr/local/src/chatbot/requirements.txt
WORKDIR /usr/local/src/chatbot
RUN pip install -r requirements.txt

COPY .streamlit/secrets.toml /usr/local/src/chatbot/.streamlit/secrets.toml
COPY Chatbot.py /usr/local/src/chatbot/Chatbot.py

EXPOSE 80
CMD ["streamlit", "run", "Chatbot.py", "--server.port", "80", "--server.enableXsrfProtection", "false"]