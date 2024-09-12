from db_connection import Connection

class ProductHelper:
    
    conn = None
    QUERY_SELECT = 'SELECT product_id, product_name FROM products;'
    
    @classmethod
    def select_products(cls):
        products = []
        try:
            conn = Connection.get_conn()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(cls.QUERY_SELECT)
            products = cursor.fetchall()
            return products
        except Exception as e:
            print(f"Error trying access data base: {e}")
        finally:
            if conn is not None:
                cursor.close()
                Connection.release_conn(conn)
