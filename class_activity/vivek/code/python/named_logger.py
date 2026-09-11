import logging

logger = logging.getLogger("MyAppLogger")
logger.setLevel(logging.DEBUG)

# Handler 1: writes to a file
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

# Handler 2: shows in the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)     # console only shows WARNING and above

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug("Detailed debug info")           # only goes to the FILE
logger.warning("Something looks off")          # goes to BOTH the file AND the console