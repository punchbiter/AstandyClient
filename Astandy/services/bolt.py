import Astandy
from Astandy.generated.protos import common_message_pb2 as common
from Astandy.types.service import Service

class BoltRemoteService(Service):
    async def subscribe(self: 'Astandy.StandClient', topic: str):
        '''
        :param topic: topic name
        '''

        await self.raw.BoltRemoteService.subscribe2(
            self,
            common.SubscribeRequest(topic=topic)
        )

        return True

    async def subscribe_trade(self: 'Astandy.StandClient', item_definition_id: int):
        return await self.subscribe(f"marketplace_trade_{item_definition_id}")
