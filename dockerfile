FROM python:3.10
WORKDIR /calculadora
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "calculadora.py"]
