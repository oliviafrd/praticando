FROM python:3.10
WORKDIR /calculadora
COPY . .
RUN pip install -m requirements.txt
CMD ["python", "calculadora.py"]
