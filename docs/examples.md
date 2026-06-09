# Examples

## Calling a Generated Service

Generated service methods call `client.rpc_call` internally and return parsed protobuf responses.

```python
import asyncio

from Astandy import StandClient
from Astandy.generated.protos import matches_message_pb2


client = StandClient("token")


async def main():
    await client.start()

    request = matches_message_pb2.GetPlayerMatchesRequest()
    response = await client.raw.MatchesRemoteService.getPlayerMatches(client, request)

    client.logger.info("matches: %s", response)
    await client.stop()


if __name__ == "__main__":
    asyncio.run(main())
```

## Low-Level RPC

Use this form when you need the generated `RpcTarget` directly.

```python
from Astandy.generated.protos import matches_message_pb2

request = matches_message_pb2.GetPlayerMatchesRequest()
target = client.raw.MatchesRemoteService.getPlayerMatchesRequest(request)
raw_response = await client.rpc_call(target)
response = client.raw.MatchesRemoteService.getPlayerMatchesResponse(raw_response)
```

## Event Listener

Generated event decorators are available on `StandClient` through the generated mixin.

```python
import asyncio

from Astandy import StandClient
from Astandy.generated.events import AchievementsRemoteEventListenerOnAchievementsUpdatedEventUpdate


client = StandClient("token")


@client.onAchievementsUpdatedEvent()
async def achievements_updated(
    client: StandClient,
    update: AchievementsRemoteEventListenerOnAchievementsUpdatedEventUpdate,
):
    client.logger.info("achievements updated: %s", update.data)


async def main():
    await client.start()
    await client.idle()


if __name__ == "__main__":
    asyncio.run(main())
```
