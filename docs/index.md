# Astandy

Astandy is an async SO2 client.

Most user code should call generated services through `client.raw`:

```python
from Astandy.generated.protos import matches_message_pb2

request = matches_message_pb2.GetPlayerMatchesRequest()
response = await client.raw.MatchesRemoteService.getPlayerMatches(client, request)
```

[Quick Start Here!](examples.md)