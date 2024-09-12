import streamlit as st
import pandas as pd
from product_db_helper import ProductHelper
from supplier_db_helper import SupplierHelper

st.title("Upload Suppliers")

def extract_suppliers_from_excel(excel_file, product_id):

    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        st.error(f'Error reading Excel File: {e}')
        return []
    
    df['phone'] = df['phone'].astype(str)
    df['product_id'] = product_id

    SupplierHelper.insert_suppliers_in_bulk(df, product_id)

   
    st.write(df)

products = ProductHelper.select_products()

product_dict = {product['product_id']: product['product_name'] for product in products}
products_ids = list(product_dict.keys())

select_product_id = st.selectbox("Select a Product", products_ids, format_func=lambda product_id: product_dict[product_id])


uploaded_file = st.file_uploader("Load Suppliers Excel File", type=["xls", "xlsx"])


if st.button("Save Suppliers"):
    if uploaded_file is not None:
        extract_suppliers_from_excel(uploaded_file, select_product_id)
        st.success("Suppliers saved successfully")
    else:
        st.error('Load a valid Excel File.')
