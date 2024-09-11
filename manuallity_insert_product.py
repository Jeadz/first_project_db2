from db_connection import Connection
import streamlit as st

class ProductInsertManually:
    
    INSERT_QUERY = 'INSERT INTO products(product_name, availability, date_added, amount, notes, state) VALUES (%s, %s, %s, %s, %s, %s)'
    
    
    @classmethod
    def insert_product(cls):
        availability_options = ['available', 'out of stock']
        state_options = ['Paid', 'To Paid']
    
        name = st.text_input('Product name')
        availability = st.selectbox('availability', availability_options)
        date_added = st.date_input('Date Added')
        amount = st.number_input('Amount', min_value=0, value=0,step=1)
        state = st.selectbox('State',state_options)
        notes = st.text_area(label='Notes',placeholder='Write a note',height=150,max_chars=250)
        
        if not name or not availability or not date_added or not amount or not state :
            st.error('All fields are requiered')
        
        submit = st.button("Submit") 
        if submit:
            conn = None
            try:
                conn = Connection.get_conn()
                cursor = conn.cursor(dictionary=True)
                values = (name, availability, date_added,amount,notes,state)
                cursor.execute(cls.INSERT_QUERY, values)
                conn.commit()
                st.success(f'The product {name}, has been inserted successfully')
            except Exception as e:
                st.error(f'An error has ocurred: {e}')
            finally:
                if conn is not None:
                    cursor.close()
                    Connection.release_conn(conn)
                