from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
try:
    r=10/0
except Exception as e:
    logging.info("Divide by zero exception")
    raise USvisaException(e, sys) from e