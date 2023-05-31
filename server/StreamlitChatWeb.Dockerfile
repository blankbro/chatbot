FROM python:3.9.10-slim-buster
RUN apt-get update && apt-get install python-tk python3-tk tk-dev -y
COPY ./server/requirements.txt /usr/local/src/chatbot/requirements.txt
WORKDIR /usr/local/src/chatbot
RUN pip install -r requirements.txt
COPY ./server/ /usr/local/src/chatbot
EXPOSE 80
CMD ["streamlit", "run", "Chat.py", "--server.port", "80", "--server.enableXsrfProtection", "false"]