FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .
#SHELL ["/bin/bash", "-c"]

RUN pip3 install -r requirements.txt

# Expose port you want your app on
EXPOSE 5900

HEALTHCHECK CMD curl --fail http://localhost:5900/_stcore/health

# Run
ENTRYPOINT [“streamlit”, “run”, “main_app.py”, “–server.port=5900”, “–server.address=0.0.0.0”]