FROM python:3.8-slim

# Copy app handler code
COPY ./kafka_sample.py kafka_sample.py
COPY ./driver_stats.parquet .

# Install dependencies
RUN pip3 install kafka-python==2.0.2
RUN pip3 install pandas
RUN pip3 install pyarrow

CMD [ "python", "-u", "kafka_sample.py", "--mode", "setup", "--bootstrap_servers", "broker:29092"]