import logging


def setup_logger(name,log_file=r'C:\Users\SHWETA\Olist_Ecommerce_Analysis\logs\project.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # File Handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)

    # Console Handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add handlers
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger