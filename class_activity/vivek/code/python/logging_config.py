
# import logging

# # change config
# logging.basicConfig(level=logging.DEBUG)

# logging.debug("debug")
# logging.info("info")


import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug("Application starting up...")
logging.info("User 'priya' logged in")
logging.warning("API response took longer than expected")
logging.error("Failed to connect to payment gateway")
logging.critical("Database is completely unreachable!")