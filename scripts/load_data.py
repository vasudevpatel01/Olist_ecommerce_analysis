import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
import sys
sys.path.append(r'C:\Users\SHWETA\Olist_Ecommerce_Analysis')
from logs.logger_config import setup_logger
from config.db_config import DB_Config

logger = setup_logger(__name__)

engine = create_engine(f"mysql+pymysql://{DB_Config['user']}:{DB_Config['password']}@{DB_Config['host']}/{DB_Config['DB']}")

# Map CSV files to database table names
file_table_map = {
    "olist_customers_dataset.csv": "customers",
    "olist_orders_dataset.csv": "orders",
    "olist_order_items_dataset.csv": "order_items",
    "olist_geolocation_dataset.csv" : "geolocation" ,
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
    "olist_order_payments_dataset.csv": "payments",
    "olist_order_reviews_dataset.csv": "reviews",
    "product_category_name_translation.csv": "product_category_translation",
}
data_folder = 'data'



def load_csv_to_sql():
    try:
        for filename,table_name in file_table_map.items():
            file_path = os.path.join(data_folder,filename)
            df = pd.read_csv(file_path)
            df.to_sql(name=table_name,con= engine,if_exists="replace",index=False)
            logger.info(f"{table_name} table created with {len(df)} rows")
    except FileNotFoundError as e:
        logger.exception(f"{filename} not found: {e}")
    except SQLAlchemyError as e:
        logger.exception(f"An error occured: {e}")
    except Exception as e:
        logger.error(f"Failed to load {file_path} into {table_name}: {e}")

        
    