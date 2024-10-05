FROM prefecthq/prefect:2-python3.11

WORKDIR /app

COPY . /app

RUN pip3 install minio pymongo pandas 

ENV PREFECT_API_URL=http://server:4200/api
ENV PREFECT_EXPERIMENTAL_ENABLE_EXTRA_RUNNER_ENDPOINTS=True
ENV PREFECT_RUNNER_SERVER_HOST=127.0.0.1

CMD ["sh", "-c", "sleep 1 && python ./s3_to_mongo.py"]
