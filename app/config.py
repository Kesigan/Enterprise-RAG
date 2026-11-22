from functools import lru_cache
from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    aws_access_key_id:str=''
    aws_secret_access_key:str=''
    aws_region:str='us-east-1'
    s3_bucket_name:str=Field(default='',validation_alias=AliasChoices('S3_BUCKET','S3_BUCKET_NAME','s3_bucket_name'))
    database_url:str=''
    bedrock_embedded_model:str=Field(default='amazon.titan-embed-text-v2:0',validation_alias=AliasChoices('BEDROCK_EMBED_MODEL','BEDROCK_EMBEDDED_MODEL','bedrock_embedded_model'))
    bedrock_chat_model:str='amazon.nova-lite-v1:0'
    embedding_dimension:int=Field(default=1024,validation_alias=AliasChoices('EMBED_DIM','EMBEDDING_DIMENSION','embedding_dimension'))
    max_upload_bytes:int=10485760
    pinecone_api_key:str=''
    pinecone_index_name:str='enterprise-rag-vector-index'
    pinecone_cloud:str='aws'
    pinecone_region:str='us-east-1'
    pinecone_ready_timeout:int=180
    min_relevance:float=0.25
    hitl_enabled:bool=True
    memory_turns:int=6

@lru_cache()
def settings() -> Settings:
    return Settings()

