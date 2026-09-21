from .algorithm import EncodeAlgorithm as Algorithm
from .implementations import Encoders
from dataclasses import dataclass
from typing import Callable


@dataclass
class Codec:
    encode: Callable[[str], str]
    decode: Callable[[str], str]


CODEC = {
    Algorithm.base64: Codec(encode=Encoders.encode_Base64, decode=Encoders.decode_Base64),
    Algorithm.base32: Codec(encode=Encoders.encode_Base32, decode=Encoders.decode_Base32),
    Algorithm.base85: Codec(encode=Encoders.encode_Base85, decode=Encoders.decode_Base85),
    Algorithm.base64url: Codec(encode=Encoders.encode_Base64URL, decode=Encoders.decode_Base64URL),
    Algorithm.hex: Codec(encode=Encoders.encode_Hex, decode=Encoders.decode_Hex),
    Algorithm.url: Codec(encode=Encoders.encode_Url, decode=Encoders.decode_Url),
    Algorithm.html: Codec(encode=Encoders.encode_Html, decode=Encoders.decode_Html),
    Algorithm.rot13: Codec(encode=Encoders.encode_rot13, decode=Encoders.decode_rot13),
}