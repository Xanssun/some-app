from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    mongodb_connection_uri: str = Field(default='mongodb://mongodb:27017', alias='MONGO_DB_CONNECTION_URI')
    mongodb_chat_database: str = Field(default='admin', alias='MONGODB_CHAT_DATABASE')
    mongodb_chat_collection: str = Field(default='admin', alias='MONGODB_CHAT_COLLECTION')
