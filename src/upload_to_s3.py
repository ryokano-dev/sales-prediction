import boto3

s3 = boto3.client('s3')
bucket_name = 'my-sales-prediction'
s3.upload_file('data/preprocessed_sales.csv', bucket_name, 'preprocessed_sales.csv')
print("the file was uploaded on S3")