import snowflake.connector
from snowflake.connector.errors import ProgrammingError

class SnowflakeConnector:
    def __init__(self, account, user, role, warehouse, database, schema, authenticator='externalbrowser'):
        self.account = account
        self.user = user
        self.role = role
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.authenticator = authenticator
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = snowflake.connector.connect(
                user=self.user,
                account=self.account,
                authenticator=self.authenticator,
                role=self.role,
                warehouse=self.warehouse,
                database=self.database,
                schema=self.schema
            )
            self.cursor = self.conn.cursor()
        except ProgrammingError as e:
            print(f"An error occurred while connecting: {e}")
            self.conn = None
        except Exception as e:
            print(f"An unexpected error occurred while connecting: {e}")
            self.conn = None

    def fetch_rows(self, table_name, limit=100):
        if not self.conn:
            print("No active connection to Snowflake. Call connect() first.")
            return None
        try:
            self.cursor.execute(f"SELECT * FROM {table_name} LIMIT {limit}")
            rows = self.cursor.fetchall()
            return rows
        except ProgrammingError as e:
            print(f"An error occurred while fetching rows: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred while fetching rows: {e}")
            return None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
