FROM python

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
RUN pip3 install flask
RUN git clone https://github.com/BrazovskyVladimir/Web-calculator.git .

EXPOSE 5000

CMD ["python", "main.py"]
