# Migration from 0.2 to 0.3

Old code often looked like this:

```python
response = client.raw.PlayerRemoteService.getPlayer2Response(
    await client.send_request(
        *client.raw.PlayerRemoteService.getPlayer2Request(request)
    )
)
```

Use this form instead:

```python
response = await client.raw.PlayerRemoteService.getPlayer2(client, request)
```

The low-level form is still available:

```python
target = client.raw.PlayerRemoteService.getPlayer2Request(request)
raw_response = await client.rpc_call(target)
response = client.raw.PlayerRemoteService.getPlayer2Response(raw_response)
```

# Migration from 0.1.3 to 0.2
 
Simply add await to client.start(), client.idle() and client.stop()
