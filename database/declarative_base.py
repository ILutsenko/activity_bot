from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

base = declarative_base(metadata=MetaData(schema="main"))
