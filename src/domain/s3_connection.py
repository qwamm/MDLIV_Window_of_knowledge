import asyncio
import os
from contextlib import asynccontextmanager

from aiobotocore.session import get_session
from botocore.exceptions import ClientError
from fastapi import UploadFile
import boto3


class S3Client:
    def __init__(
            self,
            access_key: str,
            secret_key: str,
            endpoint_url: str,
            bucket_name: str,
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(
            self,
            file: UploadFile,
            where: str=''
    ) -> str | None:
        try:
            async with self.get_client() as client:
                await client.put_object(
                    Bucket=self.bucket_name,
                    Key='buc1/' if where=='' else (where+'/') + file.filename,
                    Body=file.file,
                )
                return file.filename + "/" + file.filename
        except ClientError as e:
            return None

    async def delete_file(self, object_name: str) -> bool | None:
        try:
            async with self.get_client() as client:
                await client.delete_object(Bucket=self.bucket_name, Key=object_name)
                return True
        except ClientError as e:
            return None

    async def get_file(self, object_name: str, directory: str=''):
        try:
            async with self.get_client() as client:
                response = await client.get_object(Bucket=self.bucket_name, Key=directory + '/' + object_name)
                data = await response["Body"].read()
                try:
                    os.mkdir(directory)
                except:
                    pass
                with open(f"{directory}/{object_name}", "wb") as file:
                    file.write(data)
                print(f"File {object_name} downloaded to {directory}/{object_name}")
                return f"{directory}/{object_name}"
        except ClientError as e:
            print(f"Error downloading file: {e}")

    # async def get_files(self, kb: str):
    #     try:
    #         async with self.get_client() as client:
    #             response = await client.get_object(Bucket=self.bucket_name)
    #             data = await response["Body"].read()
    #             with open(f"file_tmp/{kb+'/'}", "wb") as file:
    #                 file.write(data)
    #             print(f"File {object_name} downloaded to file_path/{object_name}")
    #             return f"file_tmp/{object_name}"
    #     except ClientError as e:
    #         print(f"Error downloading file: {e}")


    async def get_files_in_knowbase(self, knowbase_name: str):
        try:
            async with self.get_client() as client:
                s3_client = client

                # Initialize the resulting s3_object_key_list to an empty list
                s3_object_key_list = []

                # Arguments to be used for list_object_v2
                operation_parameters = {
                    'Bucket': self.bucket_name,
                    'Prefix': f"{knowbase_name}/"
                }

                done = False
                while not done:
                    s3_response = await s3_client.list_objects_v2(**operation_parameters)
                    for s3_object in s3_response['Contents']:
                        s3_object_key = s3_object['Key']
                        s3_object_key_list.append(s3_object_key)
                    nextContinuationToken = s3_response.get('NextContinuationToken')

                    if nextContinuationToken is None:
                        done = True
                    else:
                        operation_parameters['ContinuationToken'] = nextContinuationToken

                files = []
                for s3_object_key in s3_object_key_list:
                    files.append(s3_object_key.split("/")[-1])
                return files
        except ClientError as e:
            print(f"Error: {e}")