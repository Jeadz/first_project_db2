import os
import streamlit as st
from dotenv import load_dotenv
from mysql.connector import pooling, Error

class Connection:
    HOST = os.getenv("DB_HOST")
    DATABASE = os.getenv("DB_NAME")
    USERNAME = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    POOL_SIZE = 5
    POOL_NAME = "inari_restaurant_db"
    pool = None
    
    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                return cls.pool
            except Exception as e:
                st.error(f'An error has ocurried: {e}')
        else:
            return cls.pool
        
    @classmethod
    def get_conn(cls):
        return cls.get_pool().get_connection()
    
    @classmethod
    def release_conn(cls, conn):
        conn.close()
        
