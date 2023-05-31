FROM python:3.9.10-slim-buster
RUN apt-get update && apt-get install python-tk python3-tk tk-dev -y
COPY . /usr/local/src/chatbot
WORKDIR /usr/local/src/chatbot
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["streamlit", "run", "client/Chat.py", "--server.port", "80", "--server.enableXsrfProtection", "false"]