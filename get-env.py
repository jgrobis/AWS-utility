import os

#Adding required .env var.
os.environ['access_key_env'] = input("Provide your access key for AWS: \n")
os.environ['secret_env'] = input("Provide your access secret key for AWS: \n")
os.environ['region_env'] = input("Provide your region info (like: eu-central-1) for AWS: \n")