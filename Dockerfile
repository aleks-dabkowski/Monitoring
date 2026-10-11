FROM python:3.13 
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080

RUN useradd app
USER app

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0", "8080"]