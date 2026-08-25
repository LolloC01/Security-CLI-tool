from enum import Enum


class Algorithm(str, Enum):
    md5 = "md5"
    sha1 = "sha1"
    sha256 = "sha256"
    sha512 = "sha512"
    blake2b = "blake2b"
    blake3 = "blake3"