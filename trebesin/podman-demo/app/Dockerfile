FROM python:3.11 # See https://index.docker.io/_/python
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
EXPOSE 8081
ENV PYTHONUNBUFFERED=1
CMD ["python3", "web.py"]
