from urllib.parse import quote, unquote
import base64
import html
import codecs

class Encoders:

    # Base64Codec
    @staticmethod
    def encode_Base64(text: str) -> str:
        text_bytes = text.encode('utf-8')
        text_bytes_base64 = base64.b64encode(text_bytes)
        text_base64 = text_bytes_base64.decode('utf-8')
        return text_base64

    @staticmethod
    def decode_Base64(text: str) -> str:
        text_bytes = text.encode('utf-8')
        text_bytes_decoded = base64.b64decode(text_bytes)
        text_decoded = text_bytes_decoded.decode('utf-8')
        return text_decoded

    # Base32Codec
    @staticmethod
    def encode_Base32(text: str) -> str:
        text_bytes = text.encode('utf-8')
        text_bytes_base32 = base64.b32encode(text_bytes)
        text_base32 = text_bytes_base32.decode('utf-8')
        return text_base32

    @staticmethod
    def decode_Base32(text: str) -> str:
        text_bytes = text.encode('utf-8')
        text_bytes_decoded = base64.b32decode(text_bytes)
        text_decoded = text_bytes_decoded.decode('utf-8')
        return text_decoded

    # Base85Codec
    @staticmethod
    def encode_Base85(text: str) -> str:
        text_bytes = text.encode('utf-8')
        text_bytes_base85 = base64.b85encode(text_bytes)
        text_base85 = text_bytes_base85.decode('utf-8')
        return text_base85

    @staticmethod
    def decode_Base85(text: str) -> str:
        text_bytes = text.encode('utf-8')
        text_bytes_decoded = base64.b85decode(text_bytes)
        text_decoded = text_bytes_decoded.decode('utf-8')
        return text_decoded

    # Base64URLCodec(TextStrategy):
    @staticmethod
    def encode_Base64URL(text: str) -> str:
        text_bytes = text.encode('utf-8')
        text_bytes_base64 = base64.urlsafe_b64encode(text_bytes)
        text_base64 = text_bytes_base64.decode('utf-8')
        return text_base64

    @staticmethod
    def decode_Base64URL(text: str) -> str:
        text += "=" * (-len(text) % 4)
        text_bytes = text.encode('utf-8')
        text_bytes_decoded = base64.urlsafe_b64decode(text_bytes)
        text_decoded = text_bytes_decoded.decode('utf-8')
        return text_decoded

    # HexCodec(TextStrategy):
    @staticmethod
    def encode_Hex(text: str) -> str:
        text_bytes = text.encode('utf-8')
        text_bytes_hex = text_bytes.hex()
        return text_bytes_hex

    @staticmethod
    def decode_Hex(text: str) -> str:
        text_bytes = bytes.fromhex(text)
        text_decoded = text_bytes.decode('utf-8')
        return text_decoded

    # UrlCodec(TextStrategy):
    @staticmethod
    def encode_Url(text: str) -> str:
        return quote(text, safe='~()*!.\'')

    @staticmethod
    def decode_Url(text: str) -> str:
        return unquote(text)

    @staticmethod
    def encode_Html(text: str) -> str:
        return html.escape(text)

    @staticmethod
    def decode_Html(text: str) -> str:
        return html.unescape(text)

    @staticmethod
    def encode_rot13(text: str) -> str:
        return codecs.encode(text, 'rot_13')

    @staticmethod
    def decode_rot13(text: str) -> str:
        return codecs.decode(text, 'rot_13')