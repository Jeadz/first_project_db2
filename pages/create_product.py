from manuallity_insert_product import ProductInsertManually
from excel_products_insert import ExcelInsertProducts
import streamlit as st

class CreateProduct:
    st.title("Create Product")
    
    option_insert = st.radio(
        'Select a option:',
        ['Insert from Excel', 'Insert Manually']
    )
    
    if option_insert == "Insert Manually":
        ProductInsertManually().insert_product()
    else:
        excel_file = st.file_uploader("Load Excel Products File", type=["xls", "xlsx"])
        if excel_file:
            ExcelInsertProducts().insert_excel_bulk(excel_file)
