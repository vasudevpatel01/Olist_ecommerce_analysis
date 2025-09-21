from sqlalchemy import create_engine
import sys
sys.path.append(r'C:\Users\SHWETA\Olist_Ecommerce_Analysis')
from logs.logger_config import setup_logger
from config.db_config import DB_Config
from scripts.load_data import load_csv_to_sql
from scripts.clean_data import CleanData


logger = setup_logger(__name__)

tables = [
    'order_items',                # child
    'payments',                   # child
    'reviews',                    # child
    'orders',                     # parent
    'customers',                  # parent
    'products',                   # independent
    'sellers',                    # independent
    'geolocation',                # independent
    'product_category_translation' # independent
]

engine = create_engine(f"mysql+pymysql://{DB_Config['user']}:{DB_Config['password']}@{DB_Config['host']}/{DB_Config['DB']}")

def main():
    # Load raw data into database
    load_csv_to_sql()
    logger.info(f"All tables created successfully")

    # Class object for CleanData Class
    clean_obj = CleanData(engine)
    for table in tables:
        clean_obj.clean_table(table)
    clean_obj.close()
    logger.info("Cleaning completed successfully!")

    
if __name__=="__main__":
    main()
    logger.info("Workflow Completed !")

