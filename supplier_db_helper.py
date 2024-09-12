from db_connection import Connection
import streamlit as st

class SupplierHelper:
    
    @classmethod
    def insert_suppliers_in_bulk(cls, df, product_id, table_name='suppliers'):
        conn = None
        cursor = None
        
        try:
            df['product_id'] = product_id

            
            conn = Connection.get_conn()
            cursor = conn.cursor()

            
            INSERT_QUERY = f"""
            INSERT INTO {table_name} (full_name, phone, company, email, address, notes, product_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            
            suppliers_data = df.to_records(index=False).tolist()

            cursor.executemany(INSERT_QUERY, suppliers_data)
            conn.commit()
            
            st.success(f'{cursor.rowcount}ssuppliers inserted successfully.')

        except Exception as e:
            st.error(f'Error: {e}')
            if conn:
                conn.rollback()

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                Connection.release_conn(conn)
