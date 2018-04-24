# db credentials
from enum import Enum

DB_URL = 'localhost:3306'
DB_USERNAME = 'root'
DB_PWD = 'root'
DB_NAME = 'dev'

URL_PREFIX = 'http://localhost:5000/' #domain name

# gnearted candidates
OFF_SET = 64 * 64
CANDIDATES = ['L', 'T', 'u', 'r', 'Y', 'k', 'Z', 's', 'V', 'e', 'A', '2', 'j', 'R', 'g', '_', 'i', 'h', 'S', 'W', 'x', 'v', 'N', 'b', '3', 'o', 'E', 'l', '8', '6', 'f', 'y', 'a', 'm', 'U', 'w', '-', 't', 'p', '4', '1', 'z', 'G', '9', 'Q', 'n', '5', '7', 'B', 'c', 'O', 'd', 'D', 'F', 'M', 'q', 'P', 'C', 'I', 'X', '0', 'J', 'K', 'H']


class Status(Enum):
    SUCCESS = "SUCCESS"
    NOT_PRESENT = "NOT PRESENT"
    UNKNOWN_ERROR = "UNKNOWN ERROR"
    NOT_FOUND = "NOT FOUND"
    INTERNAL_SERVER_ERROR = "INTERNAL SERVER ERROR"
    # url status
    INITIALIZE = "INITIALIZE"
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"





