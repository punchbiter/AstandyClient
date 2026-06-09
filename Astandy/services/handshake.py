import Astandy
from Astandy.generated.protos import auth_message_pb2 as auth
from Astandy.types.service import Service

class HandshakeRemoteService(Service):
    async def handshake(self: 'Astandy.StandClient', handshake: str):
        await self.raw.HandshakeRemoteService.encryptedHandshake(
            self,
            auth.Handshake(ticket=handshake)
        )
        return True
