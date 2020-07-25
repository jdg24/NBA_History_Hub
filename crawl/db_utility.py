import psycopg2

def connect(database, username, password, host, port):
    return psycopg2.connect(
        database=database,
        user=username,
        password=password,
        host=host,
        port=port
    )
