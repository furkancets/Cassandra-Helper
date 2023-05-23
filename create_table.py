from cassandra.cluster import Cluster

def cassandra_create_table():

    """
    Connection object for Cassandra
    :return: session, cluster
    """
    cluster = Cluster(['127.0.0.1'], port=9042)

    session = cluster.connect("test_app")

    session.execute("""
       CREATE TABLE IF NOT EXISTS hadi_bakalim (
            unique_id text,
            name text,
            age int,
            address text,
            PRIMARY KEY (unique_id)
            )
        """)

    return session, cluster


if __name__ == "__main__":
    cassandra_create_table()
