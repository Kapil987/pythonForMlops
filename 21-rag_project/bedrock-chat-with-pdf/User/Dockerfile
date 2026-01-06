FROM python:3.11
EXPOSE 8084
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8084", "--server.address=0.0.0.0" ]
# ENTRYPOINT [ "streamlit", "run", "app1.py", "--server.port=8084", "--server.address=0.0.0.0" ]
# ENTRYPOINT [ "streamlit", "run", "app2-ui.py", "--server.port=8084", "--server.address=0.0.0.0" ]
