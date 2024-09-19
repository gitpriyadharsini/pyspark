FROM python:3.8-slim

# Install PySpark
RUN pip install pyspark

# Copy your PySpark script into the container
COPY etl.py /app/etl.py

# Set the working directory
WORKDIR /app

# Command to run the PySpark script
CMD ["spark-submit", "etl.py"]
