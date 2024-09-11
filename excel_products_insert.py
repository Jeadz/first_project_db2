from db_connection import Connection
import streamlit as st
import pandas as pd

class ExcelInsertProducts:
    
    def insert_excel_bulk(self, excel_file, table_name='products'):
        if excel_file is not None:
            try:
               
                df = pd.read_excel(excel_file)
                
                if 'date_added' in df.columns:
                    df['date_added'] = pd.to_datetime(df['date_added']).dt.date
                    
                df['notes'].fillna('', inplace=True)
                
                st.write("Preview of uploaded file:")
                st.dataframe(df)
                
                
                submit = st.button("Submit")
                
                if submit:
                    conn = None
                    try:
                        conn = Connection.get_conn()
                        cursor = conn.cursor()

                        
                        INSERT_QUERY = f'INSERT INTO {table_name} (product_name, availability, date_added, amount, notes, state) VALUES (%s, %s, %s, %s, %s, %s)'

                        
                        products_data = df.to_records(index=False).tolist()
                        cursor.executemany(INSERT_QUERY, products_data)

                        
                        conn.commit()
                        st.success(f'{cursor.rowcount} rows insert successfully')
                    except Exception as e:
                        st.error(f'Error: {e}')
                        if conn:
                            conn.rollback()
                    finally:
                        if conn:
                            cursor.close()
                            Connection.release_conn(conn)
            except Exception as e:
                st.error(f'Error tring processing Excel file: {e}')
        else:
            st.error("Select a valid Excel file.")
