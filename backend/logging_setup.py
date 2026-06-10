import logging

def get_logger(name, log_file = 'expense_manager.log', level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # Create logger and set minimum level for this logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create handler where the logs go
    file_handler = logging.FileHandler(log_file)

    # Create a formatter to decide what the logs look lie
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # add handler to your logger
    logger.addHandler(file_handler)

    return logger