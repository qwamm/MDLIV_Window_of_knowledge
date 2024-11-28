import asyncio
from contextlib import asynccontextmanager

from aiobotocore.session import get_session
from botocore.exceptions import ClientError
from fastapi import UploadFile


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
    ) -> str | None:
        try:
            async with self.get_client() as client:
                await client.put_object(
                    Bucket=self.bucket_name,
                    Key="buc1/" + file.filename,
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

    async def get_file(self, object_name: str):
        try:
            async with self.get_client() as client:
                response = await client.get_object(Bucket=self.bucket_name, Key=object_name)
                data = await response["Body"].read()
                with open(f"file_tmp/{object_name}", "wb") as file:
                    file.write(data)
                print(f"File {object_name} downloaded to file_path/{object_name}")
                return f"file_tmp/{object_name}"
        except ClientError as e:
            print(f"Error downloading file: {e}")
