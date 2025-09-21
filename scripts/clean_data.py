import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
import sys
sys.path.append(r"C:\Users\SHWETA\Olist_Ecommerce_Analysis")
from logs.logger_config import setup_logger
from config.db_config import DB_Config

# Initialize logger
logger = setup_logger(__name__)

engine = create_engine(f"mysql+pymysql://{DB_Config['user']}:{DB_Config['password']}@{DB_Config['host']}/{DB_Config['DB']}")

class CleanData():
    def __init__(self,engine):
        self.engine = engine
        self.conn = engine.connect()
        logger.info("Database connection established.")

    def clean_table(self,table_name):
        """Cleans the specified table by deleting nulls, invalid data, duplicates, and normalizing columns."""
        
        try:
            # Clean customers table
            if table_name == 'customers':
                delete_null_query = f"""
                    DELETE FROM {table_name} 
                    WHERE customer_id IS NULL 
                    OR customer_zip_code_prefix IS NULL 
                    OR customer_unique_id IS NULL;
                """
                self.conn.execute(text(delete_null_query))
                logger.info(f"{table_name}: Null rows deleted.")

                
            # Clean orders table
            if table_name == 'orders':
                delete_query = f"""
                    DELETE FROM {table_name} 
                    WHERE order_status IS NULL 
                    OR order_purchase_timestamp IS NULL 
                    OR order_estimated_delivery_date IS NULL;
                """
                self.conn.execute(text(delete_query))
                logger.info(f"{table_name}: Null rows deleted.")
                
                to_date_time = f"""
                    ALTER TABLE {table_name} 
                    MODIFY order_purchase_timestamp DATETIME,
                    MODIFY order_approved_at DATETIME,
                    MODIFY order_delivered_carrier_date DATETIME,
                    MODIFY order_delivered_customer_date DATETIME,
                    MODIFY order_estimated_delivery_date DATETIME;
                    """
                self.conn.execute(text(to_date_time))
                logger.info(f"column convrted to datetime {table_name}")

                update_query = f"""
                    UPDATE {table_name} 
                    SET order_status = 'canceled' 
                    WHERE order_status = 'shipped' 
                    AND order_delivered_customer_date IS NULL;
                """
                self.conn.execute(text(update_query))
                logger.info(f"{table_name}: Updated shipped orders with null delivery date to 'canceled'.")

            # Clean sellers table
            if table_name == 'sellers':
                         
                delete_null_query = f"""
                    DELETE FROM {table_name} 
                    WHERE seller_id IS NULL 
                    OR seller_zip_code_prefix IS NULL 
                    OR seller_city IS NULL 
                    OR seller_state IS NULL;
                """
                self.conn.execute(text(delete_null_query))
                logger.info(f"{table_name}: Null rows deleted.")

                normalization_query = f"""
                    UPDATE {table_name} 
                    SET seller_city = LOWER(seller_city), 
                        seller_state = UPPER(seller_state);
                """
                self.conn.execute(text(normalization_query))
                logger.info(f"{table_name}: Columns normalized (city lowercase, state uppercase).")

            # Clean products table
            if table_name == 'products':
                delete_null_query = f"""
                    DELETE FROM {table_name} 
                    WHERE product_id IS NULL 
                    OR product_category_name IS NULL;
                """
                self.conn.execute(text(delete_null_query))
                logger.info(f"{table_name}: Null rows deleted.")
                
                delete_negative_query = f"""
                    DELETE FROM {table_name} 
                    WHERE product_weight_g <= 0 
                    OR product_length_cm <= 0 
                    OR product_height_cm <= 0 
                    OR product_width_cm <= 0;
                """
                self.conn.execute(text(delete_negative_query))
                logger.info(f"{table_name}: Negative/zero numeric values deleted.")   

                delete_none_query = f"""
                    DELETE FROM {table_name} 
                    WHERE product_name_lenght = 0 
                    OR product_description_lenght = 0;
                """
                self.conn.execute(text(delete_none_query))
                logger.info(f"{table_name}: Empty name/description rows deleted.")

                normalization_query = f"""
                    UPDATE {table_name} 
                    SET product_category_name = LOWER(product_category_name);
                """
                self.conn.execute(text(normalization_query))
                logger.info(f"{table_name}: product_category_name normalized to lowercase.")

            # Clean reviews table
            if table_name == 'reviews':
                delete_null_query = f"""
                    DELETE FROM {table_name} 
                    WHERE review_id IS NULL 
                    OR order_id IS NULL 
                    OR review_score IS NULL;
                """
                self.conn.execute(text(delete_null_query))
                logger.info(f"{table_name}: Null rows deleted.")
                
                delete_invalid_scores = f"""
                    DELETE FROM {table_name} 
                    WHERE review_score NOT BETWEEN 1 AND 5;
                """
                self.conn.execute(text(delete_invalid_scores))
                logger.info(f"{table_name}: Invalid review scores removed.")

            # Clean product_category_translation table
            if table_name == 'product_category_translation':
                delete_null_query = f"""
                    DELETE FROM {table_name} 
                    WHERE product_category_name IS NULL 
                    OR product_category_name_english IS NULL;
                """
                self.conn.execute(text(delete_null_query))
                logger.info(f"{table_name}: Null rows deleted.")
                
                normalization_query = f"""
                    UPDATE {table_name} 
                    SET product_category_name = LOWER(product_category_name),
                        product_category_name_english = LOWER(product_category_name_english);
                """
                self.conn.execute(text(normalization_query))
                logger.info(f"{table_name}: Columns normalized to lowercase.")


            # Clean payments table
            if table_name == 'payments':
                delete_null_query = f"""
                    DELETE FROM {table_name} 
                    WHERE order_id IS NULL 
                    OR payment_type IS NULL 
                    OR payment_value IS NULL;
                """
                self.conn.execute(text(delete_null_query))
                logger.info(f"{table_name}: Null rows deleted.")
                
                remove_invalid_values = f"""
                    DELETE FROM {table_name} 
                    WHERE payment_value <= 0 
                    OR payment_installments < 1;
                """
                self.conn.execute(text(remove_invalid_values))
                logger.info(f"{table_name}: Invalid payment values removed.")
                
                normalization_query = f"""
                    UPDATE {table_name} 
                    SET payment_type = TRIM(LOWER(payment_type));
                """
                self.conn.execute(text(normalization_query))
                logger.info(f"{table_name}: payment_type normalized.")

            # Clean order_items table
            if table_name == 'order_items':
                delete_null_query = f"""
                    DELETE FROM {table_name} 
                    WHERE price IS NULL;
                """
                self.conn.execute(text(delete_null_query))
                logger.info(f"{table_name}: Null rows deleted.")
                
                
                to_date_time = f"""
                    ALTER TABLE {table_name}
                    MODIFY shipping_limit_date DATETIME;
                    """
                
                self.conn.execute(text(to_date_time))
                logger.info(f"column converted to datetime : {table_name}")

                remove_invalid_values= f"""
                    DELETE FROM {table_name} 
                    WHERE price <= 0 
                    OR freight_value < 0;
                """
                self.conn.execute(text(remove_invalid_values))
                logger.info(f"{table_name}: Invalid numeric values removed.")

            # Clean geolocation table
            if table_name == "geolocation":
                delete_null_query = f"""
                    DELETE FROM {table_name} 
                    WHERE geolocation_zip_code_prefix IS NULL 
                    OR geolocation_lat IS NULL 
                    OR geolocation_lng IS NULL;
                """
                self.conn.execute(text(delete_null_query))
                logger.info(f"{table_name}: Null rows deleted.")
                
                delete_invalid_scores = f"""
                    DELETE FROM {table_name} 
                    WHERE geolocation_lat NOT BETWEEN -90 AND 90 
                    OR geolocation_lng NOT BETWEEN -180 AND 180;
                """
                self.conn.execute(text(delete_invalid_scores))
                logger.info(f"{table_name}: Invalid latitude/longitude values removed.")

            

        except Exception as e:
            logger.exception(f"An error occured: {e}")

    def close(self):
        """Close the database connection."""
        self.conn.close()
        logger.info("Database connection closed.")
