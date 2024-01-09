from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
import json

def postgres_to_json_sqlalchemy(connection_string, table_name):
    engine = create_engine(connection_string)

    metadata = MetaData(engine)

    table = Table(table_name, metadata, autoload=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(table).all()

    rows = [dict(row) for row in results]

    json_data = json.dumps(rows, indent=2)

    return json_data


# Пример
postgres_connection_string = "postgresql://user:password@host:port/database"
table_name = "table_name"
json_output = postgres_to_json_sqlalchemy(postgres_connection_string, table_name)
print(json_output)
