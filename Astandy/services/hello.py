from secrets import token_bytes

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicNumbers

import Astandy
from Astandy.generated.protos import hello_message_pb2 as hello
from Astandy.types.service import Service

class HelloRemoteService(Service):
    def __init__(self):
        super().__init__()

        self._rsa_key: RSAPrivateKey
        self._public_nums: RSAPublicNumbers
        
    def generate_keys(self):
        self._rsa_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=1024
        )
        self._public_nums = self._rsa_key.public_key().public_numbers()

    async def hello(self: 'Astandy.StandClient'):
        iv = token_bytes(16)

        request = hello.HelloRequest(
            n=self._public_nums.n.to_bytes(128, "big"),
            e=self._public_nums.e.to_bytes(3, "big"),
            iv=iv,
        )
        response = await self.raw.HelloRemoteService.hello(self, request)

        key = self._rsa_key.decrypt(
            response.key,
            padding.PKCS1v15()
        )
        self.cipher.new_aes_cipher(key, iv)

        return True
