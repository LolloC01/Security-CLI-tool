from enum import Enum

class EncodeAlgorithm(str, Enum):
    base64 = "base64"
    base32 = "base32"
    base85 = "base85"
    base64url = "base64url"
    hex = "hex"
    url = "url"
    html = "html"
    rot13 = "rot13"