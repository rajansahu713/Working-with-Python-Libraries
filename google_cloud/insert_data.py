from google.cloud import storage

def upload_to_gcs(bucket_name, local_file_path, gcs_file_path):
    # Initialize Google Cloud Storage client
    client = storage.Client()

    # Access the specified bucket
    bucket = client.bucket(bucket_name)

    # Path to the local file you want to upload
    blob = bucket.blob(gcs_file_path)

    # Upload the local file to Google Cloud Storage
    blob.upload_from_filename(local_file_path)

    print(f"File {local_file_path} uploaded to {bucket_name} as {gcs_file_path}")

# Replace these values with your own
bucket_name = 'rajan_testing'
local_file_path = 'file.txt'
gcs_file_path = 'file.txt'

upload_to_gcs(bucket_name, local_file_path, gcs_file_path)