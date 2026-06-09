import Astandy
from Astandy.generated.protos import player_message_pb2 as player
from Astandy.types.service import Service

class PlayerRemoteService(Service):
    async def me(self: 'Astandy.StandClient'):
        '''
        Get handshake owner's player profile
        '''

        response = await self.raw.PlayerRemoteService.getPlayer2(self, player.GetPlayerRequest())

        return response
