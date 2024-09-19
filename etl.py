from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("ETL Example").getOrCreate()

# Read the CSV file
input_path = "/home/user/file.csv"
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Transform the data (example: filter rows where 'age' > 30)
transformed_df = df.filter(df['age'] > 30)

# Write the transformed data to a new CSV file
output_path = "/home/user/file_out.csv"
transformed_df.write.csv(output_path, header=True)

# Stop the Spark session
spark.stop()
