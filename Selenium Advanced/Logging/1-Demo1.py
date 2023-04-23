import logging

logging.basicConfig(filename="G:\\INFOSYS Lectures & Codes\\Python Testing Codes\\Python Codes\\Selenium Logs\\test.log"
                    , format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt= '%m/%d/%Y %I: %M: %S %p'
                    , level=logging.DEBUG

                    )

logging.debug("This is a debug message")
logging.info("This is a info message")

logging.critical("This is a critical message")
logging.error("This is a error message")
logging.warning("This is a warning message")

