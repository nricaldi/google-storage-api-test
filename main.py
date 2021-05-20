import os
from google.cloud import storage

""" 
Get credentials
"""

# storage_client = storage.Client.from_service_account_json(f"{os.path.dirname(os.path.abspath(__file__))}/.google_storage_credentials.json")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.google_storage_credentials.json'

storage_client = storage.Client()

# Print the object 
# print(storage_client)
# print(dir(storage_client))

"""
Create a new bucket
"""

def create_bucket(name):
    bucket_name = name
    bucket = storage_client.bucket(bucket_name)
    bucket.location = 'US'
    storage_client.create_bucket(bucket)


# bucket = create_bucket('nico_data_bucket')


"""
Print Bucket Details
"""
# vars(bucket)

"""
Accessing a Specific Bucket
"""

my_bucket = storage_client.get_bucket('nico_data_bucket')
# print(vars(my_bucket))

"""
Upload Files
"""

def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)

        return True
    except Exception as e:
        print(e)
        return False
        
file_path = os.path.join(os.getcwd(), 'files_to_upload/')
upload_to_bucket('Freshman lbs - nico', os.path.join(file_path, 'freshman_lbs.csv'), 'nico_data_bucket')
upload_to_bucket('files_to_upload/Nile - nico', os.path.join(file_path, 'nile.csv'), 'nico_data_bucket')

"""
Download Files
"""

def download_file_from_bucket(blob_name, file_path, bucket_name):
    try: 
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)

        # wb = wrtie as binary
        with open(file_path, 'wb') as f:
            storage_client.download_blob_to_file(blob, f)

        return True
        
    except Exception as e:
        print(e)
        return False

bucket_name = 'nico_data_bucket'
# download_file_from_bucket('Freshman lbs - nico', os.path.join(os.getcwd(), 'file_one.csv'), bucket_name)
# download_file_from_bucket('files_to_upload/Nile - nico', os.path.join(os.getcwd(), 'file_2.csv'), bucket_name)

def delete_file_from_bucket(bucket_name, blob_name):
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.delete()

        print(f"Blob {blob_name} deleted.")
        return True

    except Exception as e:
        print(e)
        return False

delete_file_from_bucket(bucket_name, 'Freshman lbs - nico')
