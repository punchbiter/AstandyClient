# Raw Generated API

## HelloRemoteService
### hello

```python
from Astandy.generated.protos import hello_message_pb2

request: hello_message_pb2.HelloRequest = hello_message_pb2.HelloRequest(args_here)
response: hello_message_pb2.HelloResponse = await client.raw.HelloRemoteService.hello(client, request)
```

## AvatarRemoteService
### getAvatars2

```python
from Astandy.generated.protos import common_message_pb2

request: common_message_pb2.GetAvatarsRequest = common_message_pb2.GetAvatarsRequest(args_here)
response: common_message_pb2.GetAvatarsResponse = await client.raw.AvatarRemoteService.getAvatars2(client, request)
```

### getDefaultAvatars

```python
from Astandy.generated.protos import avatar_message_pb2

request: avatar_message_pb2.GetDefaultAvatarsRequest = avatar_message_pb2.GetDefaultAvatarsRequest(args_here)
response: avatar_message_pb2.GetDefaultAvatarsResponse = await client.raw.AvatarRemoteService.getDefaultAvatars(client, request)
```

## PlayerRemoteService
### getPlayerById3

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.GetPlayerByIdRequest = player_message_pb2.GetPlayerByIdRequest(args_here)
response: player_message_pb2.GetPlayerByIdResponse = await client.raw.PlayerRemoteService.getPlayerById3(client, request)
```

### deleteAccountByPermission

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.DeleteAccountByPermissionRequest = player_message_pb2.DeleteAccountByPermissionRequest(args_here)
response: player_message_pb2.DeleteAccountByPermissionResponse = await client.raw.PlayerRemoteService.deleteAccountByPermission(client, request)
```

### setDefaultAvatar

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.SetDefaultAvatarRequest = player_message_pb2.SetDefaultAvatarRequest(args_here)
response: player_message_pb2.SetDefaultAvatarResponse = await client.raw.PlayerRemoteService.setDefaultAvatar(client, request)
```

### getPlayerByUid

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.GetPlayerByUidRequest = player_message_pb2.GetPlayerByUidRequest(args_here)
response: player_message_pb2.GetPlayerByUidResponse = await client.raw.PlayerRemoteService.getPlayerByUid(client, request)
```

### setAwayStatus2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.SetAwayStatusRequest = player_message_pb2.SetAwayStatusRequest(args_here)
response: player_message_pb2.SetAwayStatusResponse = await client.raw.PlayerRemoteService.setAwayStatus2(client, request)
```

### setPlayerFirebaseToken2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.SetPlayerFirebaseTokenRequest = player_message_pb2.SetPlayerFirebaseTokenRequest(args_here)
response: player_message_pb2.SetPlayerFirebaseTokenResponse = await client.raw.PlayerRemoteService.setPlayerFirebaseToken2(client, request)
```

### getPlayerSettings2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.GetPlayerSettingsRequest = player_message_pb2.GetPlayerSettingsRequest(args_here)
response: player_message_pb2.GetPlayerSettingsResponse = await client.raw.PlayerRemoteService.getPlayerSettings2(client, request)
```

### setOnlineStatus2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.SetOnlineStatusRequest = player_message_pb2.SetOnlineStatusRequest(args_here)
response: player_message_pb2.SetOnlineStatusResponse = await client.raw.PlayerRemoteService.setOnlineStatus2(client, request)
```

### setPlayerAvatar2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.SetPlayerAvatarRequest = player_message_pb2.SetPlayerAvatarRequest(args_here)
response: player_message_pb2.SetPlayerAvatarResponse = await client.raw.PlayerRemoteService.setPlayerAvatar2(client, request)
```

### getPlayer2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.GetPlayerRequest = player_message_pb2.GetPlayerRequest(args_here)
response: player_message_pb2.GetPlayerResponse = await client.raw.PlayerRemoteService.getPlayer2(client, request)
```

### banMe2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.BanMeRequest = player_message_pb2.BanMeRequest(args_here)
response: player_message_pb2.BanMeResponse = await client.raw.PlayerRemoteService.banMe2(client, request)
```

### setPlayerSettings2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.SetPlayerSettingsRequest = player_message_pb2.SetPlayerSettingsRequest(args_here)
response: player_message_pb2.SetPlayerSettingsResponse = await client.raw.PlayerRemoteService.setPlayerSettings2(client, request)
```

### setAndGetPlayerName2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.SetAndGetPlayerNameRequest = player_message_pb2.SetAndGetPlayerNameRequest(args_here)
response: player_message_pb2.SetAndGetPlayerNameResponse = await client.raw.PlayerRemoteService.setAndGetPlayerName2(client, request)
```

### setPlayerName2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.SetPlayerNameRequest = player_message_pb2.SetPlayerNameRequest(args_here)
response: player_message_pb2.SetPlayerNameResponse = await client.raw.PlayerRemoteService.setPlayerName2(client, request)
```

### getOnlineStatus2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.GetOnlineStatusRequest = player_message_pb2.GetOnlineStatusRequest(args_here)
response: player_message_pb2.GetOnlineStatusResponse = await client.raw.PlayerRemoteService.getOnlineStatus2(client, request)
```

## RentMarketRemoteService
### getRentMarketSettings

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.GetRentMarketSettingsRequest = rent_market_message_pb2.GetRentMarketSettingsRequest(args_here)
response: rent_market_message_pb2.GetRentMarketSettingsResponse = await client.raw.RentMarketRemoteService.getRentMarketSettings(client, request)
```

### createRentPurchaseRequest

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.CreateRentPurchaseRequestRequest = rent_market_message_pb2.CreateRentPurchaseRequestRequest(args_here)
response: rent_market_message_pb2.CreateRentPurchaseRequestResponse = await client.raw.RentMarketRemoteService.createRentPurchaseRequest(client, request)
```

### getRentTrade

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.GetRentTradeRequest = rent_market_message_pb2.GetRentTradeRequest(args_here)
response: rent_market_message_pb2.GetRentTradeResponse = await client.raw.RentMarketRemoteService.getRentTrade(client, request)
```

### getRentTrades

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.GetRentTradesRequest = rent_market_message_pb2.GetRentTradesRequest(args_here)
response: rent_market_message_pb2.GetRentTradesResponse = await client.raw.RentMarketRemoteService.getRentTrades(client, request)
```

### getPlayerRentOpenRequests

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.GetPlayerRentOpenRequestsRequest = rent_market_message_pb2.GetPlayerRentOpenRequestsRequest(args_here)
response: rent_market_message_pb2.GetPlayerRentOpenRequestsResponse = await client.raw.RentMarketRemoteService.getPlayerRentOpenRequests(client, request)
```

### createRentSale

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.CreateRentSaleRequest = rent_market_message_pb2.CreateRentSaleRequest(args_here)
response: rent_market_message_pb2.CreateRentSaleResponse = await client.raw.RentMarketRemoteService.createRentSale(client, request)
```

### getPlayerRentProcessingRequests

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.GetPlayerRentProcessingRequestsRequest = rent_market_message_pb2.GetPlayerRentProcessingRequestsRequest(args_here)
response: rent_market_message_pb2.GetPlayerRentProcessingRequestsResponse = await client.raw.RentMarketRemoteService.getPlayerRentProcessingRequests(client, request)
```

### getPlayerRentClosedRequestsCount

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.GetPlayerRentClosedRequestsCountRequest = rent_market_message_pb2.GetPlayerRentClosedRequestsCountRequest(args_here)
response: rent_market_message_pb2.GetPlayerRentClosedRequestsCountResponse = await client.raw.RentMarketRemoteService.getPlayerRentClosedRequestsCount(client, request)
```

### getPlayerRentClosedRequests

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.GetPlayerRentClosedRequestsRequest = rent_market_message_pb2.GetPlayerRentClosedRequestsRequest(args_here)
response: rent_market_message_pb2.GetPlayerRentClosedRequestsResponse = await client.raw.RentMarketRemoteService.getPlayerRentClosedRequests(client, request)
```

### getFilteredRentTradeOpenSaleRequests

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.GetRentTradeOpenSaleRequestsRequest = rent_market_message_pb2.GetRentTradeOpenSaleRequestsRequest(args_here)
response: rent_market_message_pb2.GetRentTradeOpenSaleRequestsResponse = await client.raw.RentMarketRemoteService.getFilteredRentTradeOpenSaleRequests(client, request)
```

### createRentPurchaseRequestBySale

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.CreateRentPurchaseRequestBySaleRequest = rent_market_message_pb2.CreateRentPurchaseRequestBySaleRequest(args_here)
response: rent_market_message_pb2.CreateRentPurchaseRequestBySaleResponse = await client.raw.RentMarketRemoteService.createRentPurchaseRequestBySale(client, request)
```

### getRentTradeOpenSaleRequests

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.GetRentTradeOpenSaleRequestsRequest = rent_market_message_pb2.GetRentTradeOpenSaleRequestsRequest(args_here)
response: rent_market_message_pb2.GetRentTradeOpenSaleRequestsResponse = await client.raw.RentMarketRemoteService.getRentTradeOpenSaleRequests(client, request)
```

### cancelRentRequest

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.CancelRentRequestRequest = rent_market_message_pb2.CancelRentRequestRequest(args_here)
response: rent_market_message_pb2.CancelRentRequestResponse = await client.raw.RentMarketRemoteService.cancelRentRequest(client, request)
```

### getRentTradeOpenPurchaseRequests

```python
from Astandy.generated.protos import rent_market_message_pb2

request: rent_market_message_pb2.GetRentTradeOpenPurchaseRequestsRequest = rent_market_message_pb2.GetRentTradeOpenPurchaseRequestsRequest(args_here)
response: rent_market_message_pb2.GetRentTradeOpenPurchaseRequestsResponse = await client.raw.RentMarketRemoteService.getRentTradeOpenPurchaseRequests(client, request)
```

## SystemMessagesRemoteService
### getSystemMessages

```python
from Astandy.generated.protos import system_messages_message_pb2

request: system_messages_message_pb2.GetSystemMessagesRequest = system_messages_message_pb2.GetSystemMessagesRequest(args_here)
response: system_messages_message_pb2.GetSystemMessagesResponse = await client.raw.SystemMessagesRemoteService.getSystemMessages(client, request)
```

### countUnreadSystemMessages

```python
from Astandy.generated.protos import system_messages_message_pb2

request: system_messages_message_pb2.CountUnreadSystemMessagesRequest = system_messages_message_pb2.CountUnreadSystemMessagesRequest(args_here)
response: system_messages_message_pb2.CountUnreadSystemMessagesResponse = await client.raw.SystemMessagesRemoteService.countUnreadSystemMessages(client, request)
```

### deleteSystemMessages

```python
from Astandy.generated.protos import system_messages_message_pb2

request: system_messages_message_pb2.DeleteSystemMessagesRequest = system_messages_message_pb2.DeleteSystemMessagesRequest(args_here)
response: system_messages_message_pb2.DeleteSystemMessagesResponse = await client.raw.SystemMessagesRemoteService.deleteSystemMessages(client, request)
```

### getSystemMessageDetails

```python
from Astandy.generated.protos import system_messages_message_pb2

request: system_messages_message_pb2.GetSystemMessageDetailsRequest = system_messages_message_pb2.GetSystemMessageDetailsRequest(args_here)
response: system_messages_message_pb2.GetSystemMessageDetailsResponse = await client.raw.SystemMessagesRemoteService.getSystemMessageDetails(client, request)
```

### readSystemMessages

```python
from Astandy.generated.protos import system_messages_message_pb2

request: system_messages_message_pb2.ReadSystemMessagesRequest = system_messages_message_pb2.ReadSystemMessagesRequest(args_here)
response: system_messages_message_pb2.ReadSystemMessagesResponse = await client.raw.SystemMessagesRemoteService.readSystemMessages(client, request)
```

## NewsFeedRemoteService
### sendNews2

```python
from Astandy.generated.protos import newsfeed_message_pb2

request: newsfeed_message_pb2.SendNewsRequest = newsfeed_message_pb2.SendNewsRequest(args_here)
response: newsfeed_message_pb2.SendNewsResponse = await client.raw.NewsFeedRemoteService.sendNews2(client, request)
```

### getItems2

```python
from Astandy.generated.protos import newsfeed_message_pb2

request: newsfeed_message_pb2.GetItemsRequest = newsfeed_message_pb2.GetItemsRequest(args_here)
response: newsfeed_message_pb2.GetItemsResponse = await client.raw.NewsFeedRemoteService.getItems2(client, request)
```

## GSClanStatsRemoteService
### getClanStats

```python
from Astandy.generated.protos import gs_clan_stats_message_pb2

request: gs_clan_stats_message_pb2.GSGetClanStatsRequest = gs_clan_stats_message_pb2.GSGetClanStatsRequest(args_here)
response: gs_clan_stats_message_pb2.GSGetClanStatsResponse = await client.raw.GSClanStatsRemoteService.getClanStats(client, request)
```

### saveClanStats

```python
from Astandy.generated.protos import gs_clan_stats_message_pb2

request: gs_clan_stats_message_pb2.GSSaveClanStatsRequest = gs_clan_stats_message_pb2.GSSaveClanStatsRequest(args_here)
response: gs_clan_stats_message_pb2.GSSaveClanStatsResponse = await client.raw.GSClanStatsRemoteService.saveClanStats(client, request)
```

## IdTokenRemoteService
### getIdToken

```python
from Astandy.generated.protos import id_token_message_pb2

request: id_token_message_pb2.GetIdTokenRequest = id_token_message_pb2.GetIdTokenRequest(args_here)
response: id_token_message_pb2.GetIdTokenResponse = await client.raw.IdTokenRemoteService.getIdToken(client, request)
```

## AchievementRemoteService
### getPlayerAchievements

```python
from Astandy.generated.protos import achievement_message_pb2

request: achievement_message_pb2.GetPlayerAchievementsRequest = achievement_message_pb2.GetPlayerAchievementsRequest(args_here)
response: achievement_message_pb2.GetPlayerAchievementsResponse = await client.raw.AchievementRemoteService.getPlayerAchievements(client, request)
```

### getAchievementDefinitions

```python
from Astandy.generated.protos import achievement_message_pb2

request: achievement_message_pb2.GetAchievementDefinitionsRequest = achievement_message_pb2.GetAchievementDefinitionsRequest(args_here)
response: achievement_message_pb2.GetAchievementDefinitionsResponse = await client.raw.AchievementRemoteService.getAchievementDefinitions(client, request)
```

### getCurrentPlayerAchievements

```python
from Astandy.generated.protos import achievement_message_pb2

request: achievement_message_pb2.GetCurrentPlayerAchievementsRequest = achievement_message_pb2.GetCurrentPlayerAchievementsRequest(args_here)
response: achievement_message_pb2.GetCurrentPlayerAchievementsResponse = await client.raw.AchievementRemoteService.getCurrentPlayerAchievements(client, request)
```

## HandshakeRemoteService
### encryptedHandshake

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.Handshake = auth_message_pb2.Handshake(args_here)
response: auth_message_pb2.HandshakeResponse = await client.raw.HandshakeRemoteService.encryptedHandshake(client, request)
```

### logout2

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.LogoutRequest = auth_message_pb2.LogoutRequest(args_here)
response: auth_message_pb2.LogoutResponse = await client.raw.HandshakeRemoteService.logout2(client, request)
```

## TestAuthRemoteService
### encryptedAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.TestAuthRequest = auth_message_pb2.TestAuthRequest(args_here)
response: auth_message_pb2.TestAuthResponse = await client.raw.TestAuthRemoteService.encryptedAuth(client, request)
```

### encryptedAuth2

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.TestAuthRequest = auth_message_pb2.TestAuthRequest(args_here)
response: auth_message_pb2.TestAuthResponse = await client.raw.TestAuthRemoteService.encryptedAuth2(client, request)
```

## TwitchAuthRemoteService
### linkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.TwitchLinkAuthRequest = auth_message_pb2.TwitchLinkAuthRequest(args_here)
response: auth_message_pb2.TwitchLinkAuthResponse = await client.raw.TwitchAuthRemoteService.linkAuth(client, request)
```

### unLinkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.TwitchUnLinkAuthRequest = auth_message_pb2.TwitchUnLinkAuthRequest(args_here)
response: auth_message_pb2.TwitchUnLinkAuthResponse = await client.raw.TwitchAuthRemoteService.unLinkAuth(client, request)
```

## RateGameRemoteService
### dontAskLater

```python
from Astandy.generated.protos import rate_message_pb2

request: rate_message_pb2.DontAskLaterRequest = rate_message_pb2.DontAskLaterRequest(args_here)
response: rate_message_pb2.DontAskLaterResponse = await client.raw.RateGameRemoteService.dontAskLater(client, request)
```

### askLater

```python
from Astandy.generated.protos import rate_message_pb2

request: rate_message_pb2.AskLaterRequest = rate_message_pb2.AskLaterRequest(args_here)
response: rate_message_pb2.AskLaterResponse = await client.raw.RateGameRemoteService.askLater(client, request)
```

### getLastRateGame

```python
from Astandy.generated.protos import rate_message_pb2

request: rate_message_pb2.GetLastRateGameRequest = rate_message_pb2.GetLastRateGameRequest(args_here)
response: rate_message_pb2.GetLastRateGameResponse = await client.raw.RateGameRemoteService.getLastRateGame(client, request)
```

### rateGame

```python
from Astandy.generated.protos import rate_message_pb2

request: rate_message_pb2.RateGameRequest = rate_message_pb2.RateGameRequest(args_here)
response: rate_message_pb2.RateGameResponse = await client.raw.RateGameRemoteService.rateGame(client, request)
```

## VkAuthRemoteService
### encryptedAuth2

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.VkAuthRequest = auth_message_pb2.VkAuthRequest(args_here)
response: auth_message_pb2.VkAuthResponse = await client.raw.VkAuthRemoteService.encryptedAuth2(client, request)
```

### encryptedAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.VkAuthRequest = auth_message_pb2.VkAuthRequest(args_here)
response: auth_message_pb2.VkAuthResponse = await client.raw.VkAuthRemoteService.encryptedAuth(client, request)
```

### unLinkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.VkUnLinkAuthRequest = auth_message_pb2.VkUnLinkAuthRequest(args_here)
response: auth_message_pb2.VkUnLinkAuthResponse = await client.raw.VkAuthRemoteService.unLinkAuth(client, request)
```

### linkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.VkLinkAuthRequest = auth_message_pb2.VkLinkAuthRequest(args_here)
response: auth_message_pb2.VkLinkAuthResponse = await client.raw.VkAuthRemoteService.linkAuth(client, request)
```

## GameSettingsRemoteService
### getGameSettingsEncrypted2

```python
from Astandy.generated.protos import game_settings_message_pb2

request: game_settings_message_pb2.GetGameSettingsEncryptedRequest = game_settings_message_pb2.GetGameSettingsEncryptedRequest(args_here)
response: game_settings_message_pb2.GetGameSettingsEncryptedResponse = await client.raw.GameSettingsRemoteService.getGameSettingsEncrypted2(client, request)
```

## GdprRemoteService
### getRequestsEncrypted

```python
from Astandy.generated.protos import gdpr_message_pb2

request: gdpr_message_pb2.GetRequestsEncryptedRequest = gdpr_message_pb2.GetRequestsEncryptedRequest(args_here)
response: gdpr_message_pb2.GetRequestsEncryptedResponse = await client.raw.GdprRemoteService.getRequestsEncrypted(client, request)
```

### recoverAccount

```python
from Astandy.generated.protos import gdpr_message_pb2

request: gdpr_message_pb2.RecoverAccountRequest = gdpr_message_pb2.RecoverAccountRequest(args_here)
response: gdpr_message_pb2.RecoverAccountResponse = await client.raw.GdprRemoteService.recoverAccount(client, request)
```

### createRequestEncrypted

```python
from Astandy.generated.protos import gdpr_message_pb2

request: gdpr_message_pb2.CreateRequestEncryptedRequest = gdpr_message_pb2.CreateRequestEncryptedRequest(args_here)
response: gdpr_message_pb2.CreateRequestEncryptedResponse = await client.raw.GdprRemoteService.createRequestEncrypted(client, request)
```

### deleteAccount

```python
from Astandy.generated.protos import gdpr_message_pb2

request: gdpr_message_pb2.DeleteAccountRequest = gdpr_message_pb2.DeleteAccountRequest(args_here)
response: gdpr_message_pb2.DeleteAccountResponse = await client.raw.GdprRemoteService.deleteAccount(client, request)
```

## SeasonalStatsRemoteService
### getCurrentClanStatsForSeason

```python
from Astandy.generated.protos import seasonal_stats_message_pb2

request: seasonal_stats_message_pb2.GetCurrentClanStatsForSeasonRequest = seasonal_stats_message_pb2.GetCurrentClanStatsForSeasonRequest(args_here)
response: seasonal_stats_message_pb2.GetCurrentClanStatsForSeasonResponse = await client.raw.SeasonalStatsRemoteService.getCurrentClanStatsForSeason(client, request)
```

### getPlayerStatsForSeason

```python
from Astandy.generated.protos import seasonal_stats_message_pb2

request: seasonal_stats_message_pb2.GetPlayerStatsForSeasonRequest = seasonal_stats_message_pb2.GetPlayerStatsForSeasonRequest(args_here)
response: seasonal_stats_message_pb2.GetPlayerStatsForSeasonResponse = await client.raw.SeasonalStatsRemoteService.getPlayerStatsForSeason(client, request)
```

### getStatsForSeason

```python
from Astandy.generated.protos import seasonal_stats_message_pb2

request: seasonal_stats_message_pb2.GetStatsForSeasonRequest = seasonal_stats_message_pb2.GetStatsForSeasonRequest(args_here)
response: seasonal_stats_message_pb2.GetPlayerStatsForSeasonResponse = await client.raw.SeasonalStatsRemoteService.getStatsForSeason(client, request)
```

### getClanStatsForSeason

```python
from Astandy.generated.protos import seasonal_stats_message_pb2

request: seasonal_stats_message_pb2.GetClanStatsForSeasonRequest = seasonal_stats_message_pb2.GetClanStatsForSeasonRequest(args_here)
response: seasonal_stats_message_pb2.GetClanStatsForSeasonResponse = await client.raw.SeasonalStatsRemoteService.getClanStatsForSeason(client, request)
```

## MatchesRemoteService
### getPlayerMatches

```python
from Astandy.generated.protos import matches_message_pb2

request: matches_message_pb2.GetPlayerMatchesRequest = matches_message_pb2.GetPlayerMatchesRequest(args_here)
response: matches_message_pb2.GetPlayerMatchesResponse = await client.raw.MatchesRemoteService.getPlayerMatches(client, request)
```

### getMatch

```python
from Astandy.generated.protos import matches_message_pb2

request: matches_message_pb2.GetMatchRequest = matches_message_pb2.GetMatchRequest(args_here)
response: matches_message_pb2.GetMatchResponse = await client.raw.MatchesRemoteService.getMatch(client, request)
```

### getClanMatches

```python
from Astandy.generated.protos import matches_message_pb2

request: matches_message_pb2.GetClanMatchesRequest = matches_message_pb2.GetClanMatchesRequest(args_here)
response: matches_message_pb2.GetClanMatchesResponse = await client.raw.MatchesRemoteService.getClanMatches(client, request)
```

### getCurrentPlayerLastMatch

```python
from Astandy.generated.protos import matches_message_pb2

request: matches_message_pb2.GetCurrentPlayerLastMatchRequest = matches_message_pb2.GetCurrentPlayerLastMatchRequest(args_here)
response: matches_message_pb2.GetCurrentPlayerLastMatchResponse = await client.raw.MatchesRemoteService.getCurrentPlayerLastMatch(client, request)
```

## GameServerRemoteService
### serverHandshake2

```python
from Astandy.generated.protos import gameserver_message_pb2

request: gameserver_message_pb2.ServerHandshake = gameserver_message_pb2.ServerHandshake(args_here)
response: gameserver_message_pb2.ServerHandshakeResponse = await client.raw.GameServerRemoteService.serverHandshake2(client, request)
```

### logout2

```python
from Astandy.generated.protos import gameserver_message_pb2

request: gameserver_message_pb2.ServerLogoutRequest = gameserver_message_pb2.ServerLogoutRequest(args_here)
response: gameserver_message_pb2.ServerLogoutResponse = await client.raw.GameServerRemoteService.logout2(client, request)
```

## GameSeasonRemoteService
### getGameSeasons2

```python
from Astandy.generated.protos import game_season_message_pb2

request: game_season_message_pb2.GetGameSeasonsRequest = game_season_message_pb2.GetGameSeasonsRequest(args_here)
response: game_season_message_pb2.GetGameSeasonsResponse = await client.raw.GameSeasonRemoteService.getGameSeasons2(client, request)
```

## GoogleInAppRemoteService
### buyInApp2

```python
from Astandy.generated.protos import inapps_message_pb2

request: inapps_message_pb2.GoogleBuyInappRequest = inapps_message_pb2.GoogleBuyInappRequest(args_here)
response: inapps_message_pb2.GoogleBuyInappResponse = await client.raw.GoogleInAppRemoteService.buyInApp2(client, request)
```

## GuestAuthRemoteService
### encryptedAuth2

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.GuestAuthRequest = auth_message_pb2.GuestAuthRequest(args_here)
response: auth_message_pb2.GuestAuthResponse = await client.raw.GuestAuthRemoteService.encryptedAuth2(client, request)
```

### encryptedAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.GuestAuthRequest = auth_message_pb2.GuestAuthRequest(args_here)
response: auth_message_pb2.GuestAuthResponse = await client.raw.GuestAuthRemoteService.encryptedAuth(client, request)
```

## GameServerAccusationRemoteService
### accusationByServer

```python
from Astandy.generated.protos import accusation_message_pb2

request: accusation_message_pb2.AccusationByServerRequest = accusation_message_pb2.AccusationByServerRequest(args_here)
response: accusation_message_pb2.AccusationByServerResponse = await client.raw.GameServerAccusationRemoteService.accusationByServer(client, request)
```

## ClanRemoteService
### setClanDescription2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.SetClanDescriptionRequest = clan_actions_message_pb2.SetClanDescriptionRequest(args_here)
response: clan_actions_message_pb2.SetClanDescriptionResponse = await client.raw.ClanRemoteService.setClanDescription2(client, request)
```

### getClanByTag

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetClanByTagRequest = clan_actions_message_pb2.GetClanByTagRequest(args_here)
response: clan_actions_message_pb2.GetClanByTagResponse = await client.raw.ClanRemoteService.getClanByTag(client, request)
```

### getClanSettings2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetClanSettingsRequest = clan_actions_message_pb2.GetClanSettingsRequest(args_here)
response: clan_actions_message_pb2.GetClanSettingsResponse = await client.raw.ClanRemoteService.getClanSettings2(client, request)
```

### getClanJoinRequestsCount2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetClanJoinRequestsCountRequest = clan_actions_message_pb2.GetClanJoinRequestsCountRequest(args_here)
response: clan_actions_message_pb2.GetClanJoinRequestsCountResponse = await client.raw.ClanRemoteService.getClanJoinRequestsCount2(client, request)
```

### validateClanName2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.ValidateClanNameRequest = clan_actions_message_pb2.ValidateClanNameRequest(args_here)
response: clan_actions_message_pb2.ValidateClanNameResponse = await client.raw.ClanRemoteService.validateClanName2(client, request)
```

### getRoles2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetRolesRequest = clan_actions_message_pb2.GetRolesRequest(args_here)
response: clan_actions_message_pb2.GetRolesResponse = await client.raw.ClanRemoteService.getRoles2(client, request)
```

### increaseMaxMembersCount2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.IncreaseMaxMembersCountRequest = clan_actions_message_pb2.IncreaseMaxMembersCountRequest(args_here)
response: clan_actions_message_pb2.IncreaseMaxMembersCountResponse = await client.raw.ClanRemoteService.increaseMaxMembersCount2(client, request)
```

### assignLeaderRole2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.AssignLeaderRoleRequest = clan_actions_message_pb2.AssignLeaderRoleRequest(args_here)
response: clan_actions_message_pb2.AssignLeaderRoleResponse = await client.raw.ClanRemoteService.assignLeaderRole2(client, request)
```

### declineJoinRequest2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.DeclineJoinRequestRequest = clan_actions_message_pb2.DeclineJoinRequestRequest(args_here)
response: clan_actions_message_pb2.DeclineJoinRequestResponse = await client.raw.ClanRemoteService.declineJoinRequest2(client, request)
```

### leaveClan2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.LeaveClanRequest = clan_actions_message_pb2.LeaveClanRequest(args_here)
response: clan_actions_message_pb2.LeaveClanResponse = await client.raw.ClanRemoteService.leaveClan2(client, request)
```

### findClan2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.FindClanRequest = clan_actions_message_pb2.FindClanRequest(args_here)
response: clan_actions_message_pb2.FindClanResponse = await client.raw.ClanRemoteService.findClan2(client, request)
```

### requestToJoinClan2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.RequestToJoinClanRequest = clan_actions_message_pb2.RequestToJoinClanRequest(args_here)
response: clan_actions_message_pb2.RequestToJoinClanResponse = await client.raw.ClanRemoteService.requestToJoinClan2(client, request)
```

### cancelJoinRequest2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.CancelJoinRequestRequest = clan_actions_message_pb2.CancelJoinRequestRequest(args_here)
response: clan_actions_message_pb2.CancelJoinRequestResponse = await client.raw.ClanRemoteService.cancelJoinRequest2(client, request)
```

### deleteClosedInviteRequest2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.DeleteClosedInviteRequestRequest = clan_actions_message_pb2.DeleteClosedInviteRequestRequest(args_here)
response: clan_actions_message_pb2.DeleteClosedInviteRequestResponse = await client.raw.ClanRemoteService.deleteClosedInviteRequest2(client, request)
```

### setClanAvatar2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.SetClanAvatarRequest = clan_actions_message_pb2.SetClanAvatarRequest(args_here)
response: clan_actions_message_pb2.SetClanAvatarResponse = await client.raw.ClanRemoteService.setClanAvatar2(client, request)
```

### kickMember2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.KickMemberRequest = clan_actions_message_pb2.KickMemberRequest(args_here)
response: clan_actions_message_pb2.KickMemberResponse = await client.raw.ClanRemoteService.kickMember2(client, request)
```

### changeClanType2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.ChangeClanTypeRequest = clan_actions_message_pb2.ChangeClanTypeRequest(args_here)
response: clan_actions_message_pb2.ChangeClanTypeResponse = await client.raw.ClanRemoteService.changeClanType2(client, request)
```

### deleteClosedJoinRequest2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.DeleteClosedJoinRequestRequest = clan_actions_message_pb2.DeleteClosedJoinRequestRequest(args_here)
response: clan_actions_message_pb2.DeleteClosedJoinRequestResponse = await client.raw.ClanRemoteService.deleteClosedJoinRequest2(client, request)
```

### getPlayerInviteRequests2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetPlayerInviteRequestsRequest = clan_actions_message_pb2.GetPlayerInviteRequestsRequest(args_here)
response: clan_actions_message_pb2.GetPlayerInviteRequestsResponse = await client.raw.ClanRemoteService.getPlayerInviteRequests2(client, request)
```

### createClan2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.CreateClanRequest = clan_actions_message_pb2.CreateClanRequest(args_here)
response: clan_actions_message_pb2.CreateClanResponse = await client.raw.ClanRemoteService.createClan2(client, request)
```

### getClan2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetClanRequest = clan_actions_message_pb2.GetClanRequest(args_here)
response: clan_actions_message_pb2.GetClanResponse = await client.raw.ClanRemoteService.getClan2(client, request)
```

### getPlayerInviteRequestsCount2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetPlayerInviteRequestsCountRequest = clan_actions_message_pb2.GetPlayerInviteRequestsCountRequest(args_here)
response: clan_actions_message_pb2.GetPlayerInviteRequestsCountResponse = await client.raw.ClanRemoteService.getPlayerInviteRequestsCount2(client, request)
```

### validateClanTag2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.ValidateClanTagRequest = clan_actions_message_pb2.ValidateClanTagRequest(args_here)
response: clan_actions_message_pb2.ValidateClanTagResponse = await client.raw.ClanRemoteService.validateClanTag2(client, request)
```

### getClanMembers2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetClanMembersRequest = clan_actions_message_pb2.GetClanMembersRequest(args_here)
response: clan_actions_message_pb2.GetClanMembersResponse = await client.raw.ClanRemoteService.getClanMembers2(client, request)
```

### renameClan2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.RenameClanRequest = clan_actions_message_pb2.RenameClanRequest(args_here)
response: clan_actions_message_pb2.RenameClanResponse = await client.raw.ClanRemoteService.renameClan2(client, request)
```

### getClanJoinRequests2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetClanJoinRequestsRequest = clan_actions_message_pb2.GetClanJoinRequestsRequest(args_here)
response: clan_actions_message_pb2.GetClanJoinRequestsResponse = await client.raw.ClanRemoteService.getClanJoinRequests2(client, request)
```

### getClanClosedInviteRequestsCount2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetClanClosedInviteRequestsCountRequest = clan_actions_message_pb2.GetClanClosedInviteRequestsCountRequest(args_here)
response: clan_actions_message_pb2.GetClanClosedInviteRequestsCountResponse = await client.raw.ClanRemoteService.getClanClosedInviteRequestsCount2(client, request)
```

### getPlayerJoinRequests2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetPlayerJoinRequestsRequest = clan_actions_message_pb2.GetPlayerJoinRequestsRequest(args_here)
response: clan_actions_message_pb2.GetPlayerJoinRequestsResponse = await client.raw.ClanRemoteService.getPlayerJoinRequests2(client, request)
```

### getClanById2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetClanByIdRequest = clan_actions_message_pb2.GetClanByIdRequest(args_here)
response: clan_actions_message_pb2.GetClanByIdResponse = await client.raw.ClanRemoteService.getClanById2(client, request)
```

### getClanMembersById2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetClanMembersByIdRequest = clan_actions_message_pb2.GetClanMembersByIdRequest(args_here)
response: clan_actions_message_pb2.GetClanMembersByIdResponse = await client.raw.ClanRemoteService.getClanMembersById2(client, request)
```

### assignRoleToMember2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.AssignRoleToMemberRequest = clan_actions_message_pb2.AssignRoleToMemberRequest(args_here)
response: clan_actions_message_pb2.AssignRoleToMemberResponse = await client.raw.ClanRemoteService.assignRoleToMember2(client, request)
```

### cancelInviteRequest2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.CancelInviteRequestRequest = clan_actions_message_pb2.CancelInviteRequestRequest(args_here)
response: clan_actions_message_pb2.CancelInviteRequestResponse = await client.raw.ClanRemoteService.cancelInviteRequest2(client, request)
```

### getRecommendedClans2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetRecommendedClansRequest = clan_actions_message_pb2.GetRecommendedClansRequest(args_here)
response: clan_actions_message_pb2.GetRecommendedClansResponse = await client.raw.ClanRemoteService.getRecommendedClans2(client, request)
```

### declineInviteRequest2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.DeclineInviteRequestRequest = clan_actions_message_pb2.DeclineInviteRequestRequest(args_here)
response: clan_actions_message_pb2.DeclineInviteRequestResponse = await client.raw.ClanRemoteService.declineInviteRequest2(client, request)
```

### inviteToClan2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.InviteToClanRequest = clan_actions_message_pb2.InviteToClanRequest(args_here)
response: clan_actions_message_pb2.InviteToClanResponse = await client.raw.ClanRemoteService.inviteToClan2(client, request)
```

### getClanInviteRequests2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetClanInviteRequestsRequest = clan_actions_message_pb2.GetClanInviteRequestsRequest(args_here)
response: clan_actions_message_pb2.GetClanInviteRequestsResponse = await client.raw.ClanRemoteService.getClanInviteRequests2(client, request)
```

### getPlayerClosedJoinRequestsCount2

```python
from Astandy.generated.protos import clan_actions_message_pb2

request: clan_actions_message_pb2.GetPlayerClosedJoinRequestsCountRequest = clan_actions_message_pb2.GetPlayerClosedJoinRequestsCountRequest(args_here)
response: clan_actions_message_pb2.GetPlayerClosedJoinRequestsCountResponse = await client.raw.ClanRemoteService.getPlayerClosedJoinRequestsCount2(client, request)
```

## GameCenterAuthRemoteService
### encryptedAuth2

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.GameCenterAuthRequest = auth_message_pb2.GameCenterAuthRequest(args_here)
response: auth_message_pb2.GameCenterAuthResponse = await client.raw.GameCenterAuthRemoteService.encryptedAuth2(client, request)
```

### linkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.GameCenterLinkAuthRequest = auth_message_pb2.GameCenterLinkAuthRequest(args_here)
response: auth_message_pb2.GameCenterLinkAuthResponse = await client.raw.GameCenterAuthRemoteService.linkAuth(client, request)
```

### unLinkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.GameCenterUnLinkAuthRequest = auth_message_pb2.GameCenterUnLinkAuthRequest(args_here)
response: auth_message_pb2.GameCenterUnLinkAuthResponse = await client.raw.GameCenterAuthRemoteService.unLinkAuth(client, request)
```

### encryptedAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.GameCenterAuthRequest = auth_message_pb2.GameCenterAuthRequest(args_here)
response: auth_message_pb2.GameCenterAuthResponse = await client.raw.GameCenterAuthRemoteService.encryptedAuth(client, request)
```

## GameServerGameEventRemoteService
### setChallengeProgressesByServer

```python
from Astandy.generated.protos import challenges_message_pb2

request: challenges_message_pb2.ProgressChallengesByServerRequest = challenges_message_pb2.ProgressChallengesByServerRequest(args_here)
response: challenges_message_pb2.ProgressChallengesByServerResponse = await client.raw.GameServerGameEventRemoteService.setChallengeProgressesByServer(client, request)
```

### getCurrentGameEventsByServer

```python
from Astandy.generated.protos import game_event_message_pb2

request: game_event_message_pb2.GetCurrentGameEventsByServerRequest = game_event_message_pb2.GetCurrentGameEventsByServerRequest(args_here)
response: game_event_message_pb2.GetCurrentGameEventsByServerResponse = await client.raw.GameServerGameEventRemoteService.getCurrentGameEventsByServer(client, request)
```

### progressGameEventsByServer

```python
from Astandy.generated.protos import game_event_message_pb2

request: game_event_message_pb2.ProgressGameEventsByServerRequest = game_event_message_pb2.ProgressGameEventsByServerRequest(args_here)
response: game_event_message_pb2.ProgressGameEventsByServerResponse = await client.raw.GameServerGameEventRemoteService.progressGameEventsByServer(client, request)
```

### getAllChallengesByServer

```python
from Astandy.generated.protos import game_event_message_pb2

request: game_event_message_pb2.GetAllChallengesByServerRequest = game_event_message_pb2.GetAllChallengesByServerRequest(args_here)
response: game_event_message_pb2.GetAllChallengesByServerResponse = await client.raw.GameServerGameEventRemoteService.getAllChallengesByServer(client, request)
```

### progressGameEventByServer

```python
from Astandy.generated.protos import game_event_message_pb2

request: game_event_message_pb2.ProgressGameEventByServerRequest = game_event_message_pb2.ProgressGameEventByServerRequest(args_here)
response: game_event_message_pb2.ProgressGameEventByServerResponse = await client.raw.GameServerGameEventRemoteService.progressGameEventByServer(client, request)
```

## ClanMessagesRemoteService
### getClanChatMessages2

```python
from Astandy.generated.protos import clan_messages_message_pb2

request: clan_messages_message_pb2.GetClanChatMessagesRequest = clan_messages_message_pb2.GetClanChatMessagesRequest(args_here)
response: clan_messages_message_pb2.GetClanChatMessagesResponse = await client.raw.ClanMessagesRemoteService.getClanChatMessages2(client, request)
```

### readClanChatMessages2

```python
from Astandy.generated.protos import clan_messages_message_pb2

request: clan_messages_message_pb2.ReadClanChatMessagesRequest = clan_messages_message_pb2.ReadClanChatMessagesRequest(args_here)
response: clan_messages_message_pb2.ReadClanChatMessagesResponse = await client.raw.ClanMessagesRemoteService.readClanChatMessages2(client, request)
```

### getClanLogMessages2

```python
from Astandy.generated.protos import clan_messages_message_pb2

request: clan_messages_message_pb2.GetClanLogMessagesRequest = clan_messages_message_pb2.GetClanLogMessagesRequest(args_here)
response: clan_messages_message_pb2.GetClanLogMessagesResponse = await client.raw.ClanMessagesRemoteService.getClanLogMessages2(client, request)
```

### sendClanChatMessage2

```python
from Astandy.generated.protos import clan_messages_message_pb2

request: clan_messages_message_pb2.SendClanChatMessageRequest = clan_messages_message_pb2.SendClanChatMessageRequest(args_here)
response: clan_messages_message_pb2.SendClanChatMessageResponse = await client.raw.ClanMessagesRemoteService.sendClanChatMessage2(client, request)
```

### getUnreadLogMessagesCount2

```python
from Astandy.generated.protos import clan_messages_message_pb2

request: clan_messages_message_pb2.GetUnreadLogMessagesCountRequest = clan_messages_message_pb2.GetUnreadLogMessagesCountRequest(args_here)
response: clan_messages_message_pb2.GetUnreadLogMessagesCountResponse = await client.raw.ClanMessagesRemoteService.getUnreadLogMessagesCount2(client, request)
```

### readClanLogMessages2

```python
from Astandy.generated.protos import clan_messages_message_pb2

request: clan_messages_message_pb2.ReadClanLogMessagesRequest = clan_messages_message_pb2.ReadClanLogMessagesRequest(args_here)
response: clan_messages_message_pb2.ReadClanLogMessagesResponse = await client.raw.ClanMessagesRemoteService.readClanLogMessages2(client, request)
```

### getClanMessages2

```python
from Astandy.generated.protos import clan_messages_message_pb2

request: clan_messages_message_pb2.GetClanMessagesRequest = clan_messages_message_pb2.GetClanMessagesRequest(args_here)
response: clan_messages_message_pb2.GetClanMessagesResponse = await client.raw.ClanMessagesRemoteService.getClanMessages2(client, request)
```

### getUnreadChatMessagesCount2

```python
from Astandy.generated.protos import clan_messages_message_pb2

request: clan_messages_message_pb2.GetUnreadChatMessagesCountRequest = clan_messages_message_pb2.GetUnreadChatMessagesCountRequest(args_here)
response: clan_messages_message_pb2.GetUnreadChatMessagesCountResponse = await client.raw.ClanMessagesRemoteService.getUnreadChatMessagesCount2(client, request)
```

## ReferralRemoteService
### findPlayerState

```python
from Astandy.generated.protos import referral_message_pb2

request: referral_message_pb2.FindReferralStateRequest = referral_message_pb2.FindReferralStateRequest(args_here)
response: referral_message_pb2.FindReferralStateResponse = await client.raw.ReferralRemoteService.findPlayerState(client, request)
```

### getSettings

```python
from Astandy.generated.protos import referral_message_pb2

request: referral_message_pb2.GetReferralSystemSettingsRequest = referral_message_pb2.GetReferralSystemSettingsRequest(args_here)
response: referral_message_pb2.GetReferralSystemSettingsResponse = await client.raw.ReferralRemoteService.getSettings(client, request)
```

### getRecruitById

```python
from Astandy.generated.protos import referral_message_pb2

request: referral_message_pb2.GetRecruitByIdRequest = referral_message_pb2.GetRecruitByIdRequest(args_here)
response: referral_message_pb2.GetRecruitByIdResponse = await client.raw.ReferralRemoteService.getRecruitById(client, request)
```

### getPlayerState

```python
from Astandy.generated.protos import referral_message_pb2

request: referral_message_pb2.GetReferralPlayerStateRequest = referral_message_pb2.GetReferralPlayerStateRequest(args_here)
response: referral_message_pb2.GetReferralPlayerStateResponse = await client.raw.ReferralRemoteService.getPlayerState(client, request)
```

### getRecruits

```python
from Astandy.generated.protos import referral_message_pb2

request: referral_message_pb2.GetRecruitsByOffsetRequest = referral_message_pb2.GetRecruitsByOffsetRequest(args_here)
response: referral_message_pb2.GetRecruitsByOffsetResponse = await client.raw.ReferralRemoteService.getRecruits(client, request)
```

### subscribeToCommander

```python
from Astandy.generated.protos import referral_message_pb2

request: referral_message_pb2.SubscribeToCommanderRequest = referral_message_pb2.SubscribeToCommanderRequest(args_here)
response: referral_message_pb2.SubscribeToCommanderResponse = await client.raw.ReferralRemoteService.subscribeToCommander(client, request)
```

## UgcRemoteService
### saveFeedback2

```python
from Astandy.generated.protos import ugc_message_pb2

request: ugc_message_pb2.SaveFeedbackRequest = ugc_message_pb2.SaveFeedbackRequest(args_here)
response: ugc_message_pb2.SaveFeedbackResponse = await client.raw.UgcRemoteService.saveFeedback2(client, request)
```

### listUgc2

```python
from Astandy.generated.protos import ugc_message_pb2

request: ugc_message_pb2.ListUgcRequest = ugc_message_pb2.ListUgcRequest(args_here)
response: ugc_message_pb2.ListUgcResponse = await client.raw.UgcRemoteService.listUgc2(client, request)
```

### listFeedback2

```python
from Astandy.generated.protos import ugc_message_pb2

request: ugc_message_pb2.ListFeedbackRequest = ugc_message_pb2.ListFeedbackRequest(args_here)
response: ugc_message_pb2.ListFeedbackResponse = await client.raw.UgcRemoteService.listFeedback2(client, request)
```

## GameServerInAppRemoteService
### getPlayersInAppPurchasesByServer

```python
from Astandy.generated.protos import inapps_message_pb2

request: inapps_message_pb2.GetPlayersInAppPurchasesByServerRequest = inapps_message_pb2.GetPlayersInAppPurchasesByServerRequest(args_here)
response: inapps_message_pb2.GetPlayersInAppPurchasesByServerResponse = await client.raw.GameServerInAppRemoteService.getPlayersInAppPurchasesByServer(client, request)
```

## PlayerStatsRemoteService
### getGlobalStats2

```python
from Astandy.generated.protos import player_stats_message_pb2

request: player_stats_message_pb2.GetGlobalStatsRequest = player_stats_message_pb2.GetGlobalStatsRequest(args_here)
response: player_stats_message_pb2.GetGlobalStatsResponse = await client.raw.PlayerStatsRemoteService.getGlobalStats2(client, request)
```

### getCurrentStats

```python
from Astandy.generated.protos import player_stats_message_pb2

request: player_stats_message_pb2.GetCurrentStatsRequest = player_stats_message_pb2.GetCurrentStatsRequest(args_here)
response: player_stats_message_pb2.GetCurrentStatsResponse = await client.raw.PlayerStatsRemoteService.getCurrentStats(client, request)
```

### resetStats2

```python
from Astandy.generated.protos import player_stats_message_pb2

request: player_stats_message_pb2.ResetStatsRequest = player_stats_message_pb2.ResetStatsRequest(args_here)
response: player_stats_message_pb2.ResetStatsResponse = await client.raw.PlayerStatsRemoteService.resetStats2(client, request)
```

### getPlayerStats2

```python
from Astandy.generated.protos import player_stats_message_pb2

request: player_stats_message_pb2.GetPlayerStatsRequest = player_stats_message_pb2.GetPlayerStatsRequest(args_here)
response: player_stats_message_pb2.GetPlayerStatsResponse = await client.raw.PlayerStatsRemoteService.getPlayerStats2(client, request)
```

### getStats

```python
from Astandy.generated.protos import None, player_stats_message_pb2

request: None = None(args_here)
response: player_stats_message_pb2.Stats = await client.raw.PlayerStatsRemoteService.getStats(client, request)
```

### storeStats2

```python
from Astandy.generated.protos import player_stats_message_pb2

request: player_stats_message_pb2.StorePlayerStatsRequest = player_stats_message_pb2.StorePlayerStatsRequest(args_here)
response: player_stats_message_pb2.StorePlayerStatsResponse = await client.raw.PlayerStatsRemoteService.storeStats2(client, request)
```

## AppleIdAuthRemoteService
### linkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.AppleIdLinkAuthRequest = auth_message_pb2.AppleIdLinkAuthRequest(args_here)
response: auth_message_pb2.AppleIdLinkAuthResponse = await client.raw.AppleIdAuthRemoteService.linkAuth(client, request)
```

### encryptedAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.AppleIdAuthRequest = auth_message_pb2.AppleIdAuthRequest(args_here)
response: auth_message_pb2.AppleIdAuthResponse = await client.raw.AppleIdAuthRemoteService.encryptedAuth(client, request)
```

### unLinkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.AppleIdUnLinkAuthRequest = auth_message_pb2.AppleIdUnLinkAuthRequest(args_here)
response: auth_message_pb2.AppleIdUnLinkAuthResponse = await client.raw.AppleIdAuthRemoteService.unLinkAuth(client, request)
```

### encryptedAuth2

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.AppleIdAuthRequest = auth_message_pb2.AppleIdAuthRequest(args_here)
response: auth_message_pb2.AppleIdAuthResponse = await client.raw.AppleIdAuthRemoteService.encryptedAuth2(client, request)
```

## ClanMemberStatsRemoteService
### getCurrentClanMemberStats

```python
from Astandy.generated.protos import clan_member_stats_message_pb2

request: clan_member_stats_message_pb2.GetCurrentClanMemberStatsRequest = clan_member_stats_message_pb2.GetCurrentClanMemberStatsRequest(args_here)
response: clan_member_stats_message_pb2.GetCurrentClanMemberStatsResponse = await client.raw.ClanMemberStatsRemoteService.getCurrentClanMemberStats(client, request)
```

### saveCurrentClanMemberStats

```python
from Astandy.generated.protos import clan_member_stats_message_pb2

request: clan_member_stats_message_pb2.SaveCurrentClanMemberStatsRequest = clan_member_stats_message_pb2.SaveCurrentClanMemberStatsRequest(args_here)
response: clan_member_stats_message_pb2.SaveCurrentClanMemberStatsResponse = await client.raw.ClanMemberStatsRemoteService.saveCurrentClanMemberStats(client, request)
```

### getClanMembersStats

```python
from Astandy.generated.protos import clan_member_stats_message_pb2

request: clan_member_stats_message_pb2.GetClanMembersStatsRequest = clan_member_stats_message_pb2.GetClanMembersStatsRequest(args_here)
response: clan_member_stats_message_pb2.GetClanMembersStatsResponse = await client.raw.ClanMemberStatsRemoteService.getClanMembersStats(client, request)
```

## GameServerAchievementRemoteService
### giveAchievements

```python
from Astandy.generated.protos import achievement_message_pb2

request: achievement_message_pb2.GiveAchievementsRequest = achievement_message_pb2.GiveAchievementsRequest(args_here)
response: achievement_message_pb2.GiveAchievementsResponse = await client.raw.GameServerAchievementRemoteService.giveAchievements(client, request)
```

## DlcRemoteService
### getAllReleasedDlc

```python
from Astandy.generated.protos import dlc_message_pb2

request: dlc_message_pb2.ReleasedDlcRequest = dlc_message_pb2.ReleasedDlcRequest(args_here)
response: dlc_message_pb2.DlcResponse = await client.raw.DlcRemoteService.getAllReleasedDlc(client, request)
```

### getAllDlc

```python
from Astandy.generated.protos import dlc_message_pb2

request: dlc_message_pb2.PreviewDlcRequest = dlc_message_pb2.PreviewDlcRequest(args_here)
response: dlc_message_pb2.DlcResponse = await client.raw.DlcRemoteService.getAllDlc(client, request)
```

## GameServerStatsRemoteService
### storePlayersStats2

```python
from Astandy.generated.protos import player_stats_message_pb2

request: player_stats_message_pb2.StorePlayersStatsRequest = player_stats_message_pb2.StorePlayersStatsRequest(args_here)
response: player_stats_message_pb2.StorePlayersStatsResponse = await client.raw.GameServerStatsRemoteService.storePlayersStats2(client, request)
```

### storeStats2

```python
from Astandy.generated.protos import player_stats_message_pb2

request: player_stats_message_pb2.StoreStatsRequest = player_stats_message_pb2.StoreStatsRequest(args_here)
response: player_stats_message_pb2.StoreStatsResponse = await client.raw.GameServerStatsRemoteService.storeStats2(client, request)
```

### getStats2

```python
from Astandy.generated.protos import player_stats_message_pb2

request: player_stats_message_pb2.GetStatsRequest = player_stats_message_pb2.GetStatsRequest(args_here)
response: player_stats_message_pb2.GetStatsResponse = await client.raw.GameServerStatsRemoteService.getStats2(client, request)
```

### getPlayerStats

```python
from Astandy.generated.protos import player_stats_message_pb2

request: player_stats_message_pb2.GetPlayerStatsRequest = player_stats_message_pb2.GetPlayerStatsRequest(args_here)
response: player_stats_message_pb2.GetPlayerStatsResponse = await client.raw.GameServerStatsRemoteService.getPlayerStats(client, request)
```

### getPlayersStatsV2

```python
from Astandy.generated.protos import player_stats_message_pb2

request: player_stats_message_pb2.GetPlayersStatsRequest = player_stats_message_pb2.GetPlayersStatsRequest(args_here)
response: player_stats_message_pb2.GetPlayersStatsResponse = await client.raw.GameServerStatsRemoteService.getPlayersStatsV2(client, request)
```

### storePlayerStats2

```python
from Astandy.generated.protos import player_stats_message_pb2

request: player_stats_message_pb2.StorePlayerStatsRequest = player_stats_message_pb2.StorePlayerStatsRequest(args_here)
response: player_stats_message_pb2.StorePlayerStatsResponse = await client.raw.GameServerStatsRemoteService.storePlayerStats2(client, request)
```

## FriendsRemoteService
### getOnlineStatus2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.GetOnlineStatusRequest = player_message_pb2.GetOnlineStatusRequest(args_here)
response: player_message_pb2.GetOnlineStatusResponse = await client.raw.FriendsRemoteService.getOnlineStatus2(client, request)
```

### revokeFriendRequest2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.RevokeFriendRequestRequest = friends_message_pb2.RevokeFriendRequestRequest(args_here)
response: friends_message_pb2.RevokeFriendRequestResponse = await client.raw.FriendsRemoteService.revokeFriendRequest2(client, request)
```

### getPlayerFriendsIds2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.GetPlayerFriendsIdsRequest = friends_message_pb2.GetPlayerFriendsIdsRequest(args_here)
response: friends_message_pb2.GetPlayerFriendsIdsResponse = await client.raw.FriendsRemoteService.getPlayerFriendsIds2(client, request)
```

### removeFriend2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.RemoveFriendRequest = friends_message_pb2.RemoveFriendRequest(args_here)
response: friends_message_pb2.RemoveFriendResponse = await client.raw.FriendsRemoteService.removeFriend2(client, request)
```

### getPlayerFriendByUid2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.GetPlayerFriendByUidRequest = friends_message_pb2.GetPlayerFriendByUidRequest(args_here)
response: friends_message_pb2.GetPlayerFriendByUidResponse = await client.raw.FriendsRemoteService.getPlayerFriendByUid2(client, request)
```

### ignoreFriendRequest2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.IgnoreFriendRequestRequest = friends_message_pb2.IgnoreFriendRequestRequest(args_here)
response: friends_message_pb2.IgnoreFriendRequestResponse = await client.raw.FriendsRemoteService.ignoreFriendRequest2(client, request)
```

### sendFriendRequest2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.SendFriendRequestRequest = friends_message_pb2.SendFriendRequestRequest(args_here)
response: friends_message_pb2.SendFriendRequestResponse = await client.raw.FriendsRemoteService.sendFriendRequest2(client, request)
```

### getPlayerFriendsCount2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.GetPlayerFriendsCountRequest = friends_message_pb2.GetPlayerFriendsCountRequest(args_here)
response: friends_message_pb2.GetPlayerFriendsCountResponse = await client.raw.FriendsRemoteService.getPlayerFriendsCount2(client, request)
```

### acceptFriendRequest2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.AcceptFriendRequestRequest = friends_message_pb2.AcceptFriendRequestRequest(args_here)
response: friends_message_pb2.AcceptFriendRequestResponse = await client.raw.FriendsRemoteService.acceptFriendRequest2(client, request)
```

### searchPlayers2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.SearchPlayersRequest = friends_message_pb2.SearchPlayersRequest(args_here)
response: friends_message_pb2.SearchPlayersResponse = await client.raw.FriendsRemoteService.searchPlayers2(client, request)
```

### getPlayersCount2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.GetPlayersCountRequest = friends_message_pb2.GetPlayersCountRequest(args_here)
response: friends_message_pb2.GetPlayersCountResponse = await client.raw.FriendsRemoteService.getPlayersCount2(client, request)
```

### ignoreAllFriendRequests

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.IgnoreAllFriendRequestsRequest = friends_message_pb2.IgnoreAllFriendRequestsRequest(args_here)
response: friends_message_pb2.IgnoreAllFriendRequestsResponse = await client.raw.FriendsRemoteService.ignoreAllFriendRequests(client, request)
```

### unblockFriend2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.UnblockFriendRequest = friends_message_pb2.UnblockFriendRequest(args_here)
response: friends_message_pb2.UnblockFriendResponse = await client.raw.FriendsRemoteService.unblockFriend2(client, request)
```

### getPlayerFriends2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.GetPlayerFriendsRequest = friends_message_pb2.GetPlayerFriendsRequest(args_here)
response: friends_message_pb2.GetPlayerFriendsResponse = await client.raw.FriendsRemoteService.getPlayerFriends2(client, request)
```

### blockFriend2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.BlockFriendRequest = friends_message_pb2.BlockFriendRequest(args_here)
response: friends_message_pb2.BlockFriendResponse = await client.raw.FriendsRemoteService.blockFriend2(client, request)
```

### getPlayerFriendById2

```python
from Astandy.generated.protos import friends_message_pb2

request: friends_message_pb2.GetPlayerFriendByIdRequest = friends_message_pb2.GetPlayerFriendByIdRequest(args_here)
response: friends_message_pb2.GetPlayerFriendByIdResponse = await client.raw.FriendsRemoteService.getPlayerFriendById2(client, request)
```

### getPlayerById2

```python
from Astandy.generated.protos import player_message_pb2

request: player_message_pb2.GetPlayerByIdRequest = player_message_pb2.GetPlayerByIdRequest(args_here)
response: player_message_pb2.GetPlayerByIdResponse = await client.raw.FriendsRemoteService.getPlayerById2(client, request)
```

## MarketplaceRemoteService
### getMarketplaceSettings2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.GetMarketplaceSettingsRequest = marketplace_message_pb2.GetMarketplaceSettingsRequest(args_here)
response: marketplace_message_pb2.GetMarketplaceSettingsResponse = await client.raw.MarketplaceRemoteService.getMarketplaceSettings2(client, request)
```

### getPlayerProcessingRequests2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.GetPlayerProcessingRequestRequest = marketplace_message_pb2.GetPlayerProcessingRequestRequest(args_here)
response: marketplace_message_pb2.GetPlayerProcessingRequestResponse = await client.raw.MarketplaceRemoteService.getPlayerProcessingRequests2(client, request)
```

### getFilteredTradeOpenSaleRequests

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.GetTradeOpenSaleRequestsRequest = marketplace_message_pb2.GetTradeOpenSaleRequestsRequest(args_here)
response: marketplace_message_pb2.GetTradeOpenSaleRequestsResponse = await client.raw.MarketplaceRemoteService.getFilteredTradeOpenSaleRequests(client, request)
```

### getPlayerClosedRequestsCount2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.GetPlayerClosedRequestsCountRequest = marketplace_message_pb2.GetPlayerClosedRequestsCountRequest(args_here)
response: marketplace_message_pb2.GetPlayerClosedRequestsCountResponse = await client.raw.MarketplaceRemoteService.getPlayerClosedRequestsCount2(client, request)
```

### createMultipleSales

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.CreateMultipleSalesRequest = marketplace_message_pb2.CreateMultipleSalesRequest(args_here)
response: marketplace_message_pb2.CreateMultipleSalesResponse = await client.raw.MarketplaceRemoteService.createMultipleSales(client, request)
```

### getPlayerOpenRequests2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.GetPlayerOpenRequestsRequest = marketplace_message_pb2.GetPlayerOpenRequestsRequest(args_here)
response: marketplace_message_pb2.GetPlayerOpenRequestsResponse = await client.raw.MarketplaceRemoteService.getPlayerOpenRequests2(client, request)
```

### createPurchaseRequestBySale2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.CreatePurchaseRequestBySaleRequest = marketplace_message_pb2.CreatePurchaseRequestBySaleRequest(args_here)
response: marketplace_message_pb2.CreatePurchaseRequestBySaleResponse = await client.raw.MarketplaceRemoteService.createPurchaseRequestBySale2(client, request)
```

### getTrades2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.GetTradesRequest = marketplace_message_pb2.GetTradesRequest(args_here)
response: marketplace_message_pb2.GetTradesResponse = await client.raw.MarketplaceRemoteService.getTrades2(client, request)
```

### getPlayerClosedRequests2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.GetPlayerClosedRequestsRequest = marketplace_message_pb2.GetPlayerClosedRequestsRequest(args_here)
response: marketplace_message_pb2.GetPlayerClosedRequestsResponse = await client.raw.MarketplaceRemoteService.getPlayerClosedRequests2(client, request)
```

### getTradeOpenSaleRequests2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.GetTradeOpenSaleRequestsRequest = marketplace_message_pb2.GetTradeOpenSaleRequestsRequest(args_here)
response: marketplace_message_pb2.GetTradeOpenSaleRequestsResponse = await client.raw.MarketplaceRemoteService.getTradeOpenSaleRequests2(client, request)
```

### getTradeOpenPurchaseRequests2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.GetTradeOpenPurchaseRequestsRequest = marketplace_message_pb2.GetTradeOpenPurchaseRequestsRequest(args_here)
response: marketplace_message_pb2.GetTradeOpenPurchaseRequestsResponse = await client.raw.MarketplaceRemoteService.getTradeOpenPurchaseRequests2(client, request)
```

### cancelRequest2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.CancelRequestRequest = marketplace_message_pb2.CancelRequestRequest(args_here)
response: marketplace_message_pb2.CancelRequestResponse = await client.raw.MarketplaceRemoteService.cancelRequest2(client, request)
```

### getTrade2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.GetTradeRequest = marketplace_message_pb2.GetTradeRequest(args_here)
response: marketplace_message_pb2.GetTradeResponse = await client.raw.MarketplaceRemoteService.getTrade2(client, request)
```

### createSale

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.CreateSaleRequest = marketplace_message_pb2.CreateSaleRequest(args_here)
response: marketplace_message_pb2.CreateSaleResponse = await client.raw.MarketplaceRemoteService.createSale(client, request)
```

### createPurchaseRequest2

```python
from Astandy.generated.protos import marketplace_message_pb2

request: marketplace_message_pb2.CreatePurchaseRequestRequest = marketplace_message_pb2.CreatePurchaseRequestRequest(args_here)
response: marketplace_message_pb2.CreatePurchaseRequestResponse = await client.raw.MarketplaceRemoteService.createPurchaseRequest2(client, request)
```

## TournamentsRemoteService
### finishTournament2

```python
from Astandy.generated.protos import tournaments_message_pb2

request: tournaments_message_pb2.FinishTournamentRequest = tournaments_message_pb2.FinishTournamentRequest(args_here)
response: tournaments_message_pb2.FinishTournamentResponse = await client.raw.TournamentsRemoteService.finishTournament2(client, request)
```

### leaveTournament2

```python
from Astandy.generated.protos import tournaments_message_pb2

request: tournaments_message_pb2.LeaveTournamentRequest = tournaments_message_pb2.LeaveTournamentRequest(args_here)
response: tournaments_message_pb2.LeaveTournamentResponse = await client.raw.TournamentsRemoteService.leaveTournament2(client, request)
```

### announceTournament2

```python
from Astandy.generated.protos import tournaments_message_pb2

request: tournaments_message_pb2.AnnounceTournamentRequest = tournaments_message_pb2.AnnounceTournamentRequest(args_here)
response: tournaments_message_pb2.AnnounceTournamentResponse = await client.raw.TournamentsRemoteService.announceTournament2(client, request)
```

### joinTournament2

```python
from Astandy.generated.protos import tournaments_message_pb2

request: tournaments_message_pb2.JoinTournamentRequest = tournaments_message_pb2.JoinTournamentRequest(args_here)
response: tournaments_message_pb2.JoinTournamentResponse = await client.raw.TournamentsRemoteService.joinTournament2(client, request)
```

### tournaments2

```python
from Astandy.generated.protos import tournaments_message_pb2

request: tournaments_message_pb2.TournamentsRequest = tournaments_message_pb2.TournamentsRequest(args_here)
response: tournaments_message_pb2.TournamentsResponse = await client.raw.TournamentsRemoteService.tournaments2(client, request)
```

### playTournamentGame2

```python
from Astandy.generated.protos import tournaments_message_pb2

request: tournaments_message_pb2.PlayTournamentGameRequest = tournaments_message_pb2.PlayTournamentGameRequest(args_here)
response: tournaments_message_pb2.PlayTournamentGameResponse = await client.raw.TournamentsRemoteService.playTournamentGame2(client, request)
```

### getTournament2

```python
from Astandy.generated.protos import tournaments_message_pb2

request: tournaments_message_pb2.GetTournamentRequest = tournaments_message_pb2.GetTournamentRequest(args_here)
response: tournaments_message_pb2.GetTournamentResponse = await client.raw.TournamentsRemoteService.getTournament2(client, request)
```

### startTournament2

```python
from Astandy.generated.protos import tournaments_message_pb2

request: tournaments_message_pb2.StartTournamentRequest = tournaments_message_pb2.StartTournamentRequest(args_here)
response: tournaments_message_pb2.StartTournamentResponse = await client.raw.TournamentsRemoteService.startTournament2(client, request)
```

## MatchmakingRemoteService
### refuseInvitationToLobby2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.RefuseInvitationToLobbyRequest = matchmaking_message_pb2.RefuseInvitationToLobbyRequest(args_here)
response: matchmaking_message_pb2.RefuseInvitationToLobbyResponse = await client.raw.MatchmakingRemoteService.refuseInvitationToLobby2(client, request)
```

### leaveLobby2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.LeaveLobbyRequest = matchmaking_message_pb2.LeaveLobbyRequest(args_here)
response: matchmaking_message_pb2.LeaveLobbyResponse = await client.raw.MatchmakingRemoteService.leaveLobby2(client, request)
```

### getGameServerPlayers2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.GetGameServerPlayersRequest = matchmaking_message_pb2.GetGameServerPlayersRequest(args_here)
response: matchmaking_message_pb2.GetGameServerPlayersResponse = await client.raw.MatchmakingRemoteService.getGameServerPlayers2(client, request)
```

### searchLobby

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.SearchLobbyRequest = matchmaking_message_pb2.SearchLobbyRequest(args_here)
response: matchmaking_message_pb2.SearchLobbyResponse = await client.raw.MatchmakingRemoteService.searchLobby(client, request)
```

### revokePlayerInvitationToLobby2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.RevokePlayerInvitationToLobbyRequest = matchmaking_message_pb2.RevokePlayerInvitationToLobbyRequest(args_here)
response: matchmaking_message_pb2.RevokePlayerInvitationToLobbyResponse = await client.raw.MatchmakingRemoteService.revokePlayerInvitationToLobby2(client, request)
```

### getLobbyOwner2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.GetLobbyOwnerRequest = matchmaking_message_pb2.GetLobbyOwnerRequest(args_here)
response: matchmaking_message_pb2.GetLobbyOwnerResponse = await client.raw.MatchmakingRemoteService.getLobbyOwner2(client, request)
```

### joinLobbyAs2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.JoinLobbyAsRequest = matchmaking_message_pb2.JoinLobbyAsRequest(args_here)
response: matchmaking_message_pb2.JoinLobbyAsResponse = await client.raw.MatchmakingRemoteService.joinLobbyAs2(client, request)
```

### kickPlayerFromLobby2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.KickPlayerFromLobbyRequest = matchmaking_message_pb2.KickPlayerFromLobbyRequest(args_here)
response: matchmaking_message_pb2.KickPlayerFromLobbyResponse = await client.raw.MatchmakingRemoteService.kickPlayerFromLobby2(client, request)
```

### joinLobby2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.JoinLobbyRequest = matchmaking_message_pb2.JoinLobbyRequest(args_here)
response: matchmaking_message_pb2.JoinLobbyResponse = await client.raw.MatchmakingRemoteService.joinLobby2(client, request)
```

### setLobbyPhotonGame2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.SetLobbyPhotonGameRequest = matchmaking_message_pb2.SetLobbyPhotonGameRequest(args_here)
response: matchmaking_message_pb2.SetLobbyPhotonGameResponse = await client.raw.MatchmakingRemoteService.setLobbyPhotonGame2(client, request)
```

### createLobbyWithSpectators2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.CreateLobbyWithSpectatorsRequest = matchmaking_message_pb2.CreateLobbyWithSpectatorsRequest(args_here)
response: matchmaking_message_pb2.CreateLobbyWithSpectatorsResponse = await client.raw.MatchmakingRemoteService.createLobbyWithSpectators2(client, request)
```

### requestLobbyList2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.RequestLobbyListRequest = matchmaking_message_pb2.RequestLobbyListRequest(args_here)
response: matchmaking_message_pb2.RequestLobbyListResponse = await client.raw.MatchmakingRemoteService.requestLobbyList2(client, request)
```

### getGameServerDetails2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.GetGameServerDetailsRequest = matchmaking_message_pb2.GetGameServerDetailsRequest(args_here)
response: matchmaking_message_pb2.GetGameServerDetailsResponse = await client.raw.MatchmakingRemoteService.getGameServerDetails2(client, request)
```

### deleteLobbyData2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.DeleteLobbyDataRequest = matchmaking_message_pb2.DeleteLobbyDataRequest(args_here)
response: matchmaking_message_pb2.DeleteLobbyDataResponse = await client.raw.MatchmakingRemoteService.deleteLobbyData2(client, request)
```

### invitePlayerToLobby2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.InvitePlayerToLobbyRequest = matchmaking_message_pb2.InvitePlayerToLobbyRequest(args_here)
response: matchmaking_message_pb2.InvitePlayerToLobbyResponse = await client.raw.MatchmakingRemoteService.invitePlayerToLobby2(client, request)
```

### setLobbyMaxMembers2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.SetLobbyMaxMembersRequest = matchmaking_message_pb2.SetLobbyMaxMembersRequest(args_here)
response: matchmaking_message_pb2.SetLobbyMaxMembersResponse = await client.raw.MatchmakingRemoteService.setLobbyMaxMembers2(client, request)
```

### changeLobbyPlayerType2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.ChangeLobbyPlayerTypeRequest = matchmaking_message_pb2.ChangeLobbyPlayerTypeRequest(args_here)
response: matchmaking_message_pb2.ChangeLobbyPlayerTypeResponse = await client.raw.MatchmakingRemoteService.changeLobbyPlayerType2(client, request)
```

### getLobbyGameServer2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.GetLobbyGameServerRequest = matchmaking_message_pb2.GetLobbyGameServerRequest(args_here)
response: matchmaking_message_pb2.GetLobbyGameServerResponse = await client.raw.MatchmakingRemoteService.getLobbyGameServer2(client, request)
```

### setLobbyName2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.SetLobbyNameRequest = matchmaking_message_pb2.SetLobbyNameRequest(args_here)
response: matchmaking_message_pb2.SetLobbyNameResponse = await client.raw.MatchmakingRemoteService.setLobbyName2(client, request)
```

### invitePlayerToLobbyAs2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.InvitePlayerToLobbyAsRequest = matchmaking_message_pb2.InvitePlayerToLobbyAsRequest(args_here)
response: matchmaking_message_pb2.InvitePlayerToLobbyAsResponse = await client.raw.MatchmakingRemoteService.invitePlayerToLobbyAs2(client, request)
```

### changeLobbyOtherPlayerType2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.ChangeLobbyOtherPlayerTypeRequest = matchmaking_message_pb2.ChangeLobbyOtherPlayerTypeRequest(args_here)
response: matchmaking_message_pb2.ChangeLobbyOtherPlayerTypeResponse = await client.raw.MatchmakingRemoteService.changeLobbyOtherPlayerType2(client, request)
```

### requestInternetServerList2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.RequestInternetServerListRequest = matchmaking_message_pb2.RequestInternetServerListRequest(args_here)
response: matchmaking_message_pb2.RequestInternetServerListResponse = await client.raw.MatchmakingRemoteService.requestInternetServerList2(client, request)
```

### setLobbyData2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.SetLobbyDataRequest = matchmaking_message_pb2.SetLobbyDataRequest(args_here)
response: matchmaking_message_pb2.SetLobbyDataResponse = await client.raw.MatchmakingRemoteService.setLobbyData2(client, request)
```

### setLobbyType2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.SetLobbyTypeRequest = matchmaking_message_pb2.SetLobbyTypeRequest(args_here)
response: matchmaking_message_pb2.SetLobbyTypeResponse = await client.raw.MatchmakingRemoteService.setLobbyType2(client, request)
```

### getLobbyPhotonGame2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.GetLobbyPhotonGameRequest = matchmaking_message_pb2.GetLobbyPhotonGameRequest(args_here)
response: matchmaking_message_pb2.GetLobbyPhotonGameResponse = await client.raw.MatchmakingRemoteService.getLobbyPhotonGame2(client, request)
```

### getLobby2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.GetLobbyRequest = matchmaking_message_pb2.GetLobbyRequest(args_here)
response: matchmaking_message_pb2.GetLobbyResponse = await client.raw.MatchmakingRemoteService.getLobby2(client, request)
```

### setLobbyOwner2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.SetLobbyOwnerRequest = matchmaking_message_pb2.SetLobbyOwnerRequest(args_here)
response: matchmaking_message_pb2.SetLobbyOwnerResponse = await client.raw.MatchmakingRemoteService.setLobbyOwner2(client, request)
```

### getInvitesToLobby2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.GetInvitesToLobbyRequest = matchmaking_message_pb2.GetInvitesToLobbyRequest(args_here)
response: matchmaking_message_pb2.GetInvitesToLobbyResponse = await client.raw.MatchmakingRemoteService.getInvitesToLobby2(client, request)
```

### setLobbyJoinable2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.SetLobbyJoinableRequest = matchmaking_message_pb2.SetLobbyJoinableRequest(args_here)
response: matchmaking_message_pb2.SetLobbyJoinableResponse = await client.raw.MatchmakingRemoteService.setLobbyJoinable2(client, request)
```

### getLobbyMembers2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.GetLobbyMembersRequest = matchmaking_message_pb2.GetLobbyMembersRequest(args_here)
response: matchmaking_message_pb2.GetLobbyMembersResponse = await client.raw.MatchmakingRemoteService.getLobbyMembers2(client, request)
```

### setLobbyGameServer2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.SetLobbyGameServerRequest = matchmaking_message_pb2.SetLobbyGameServerRequest(args_here)
response: matchmaking_message_pb2.SetLobbyGameServerResponse = await client.raw.MatchmakingRemoteService.setLobbyGameServer2(client, request)
```

### setLobbyMaxSpectators2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.SetLobbyMaxSpectatorsRequest = matchmaking_message_pb2.SetLobbyMaxSpectatorsRequest(args_here)
response: matchmaking_message_pb2.SetLobbyMaxSpectatorsResponse = await client.raw.MatchmakingRemoteService.setLobbyMaxSpectators2(client, request)
```

### sendLobbyChatMsg2

```python
from Astandy.generated.protos import matchmaking_message_pb2

request: matchmaking_message_pb2.SendLobbyChatMsgRequest = matchmaking_message_pb2.SendLobbyChatMsgRequest(args_here)
response: matchmaking_message_pb2.SendLobbyChatMsgResponse = await client.raw.MatchmakingRemoteService.sendLobbyChatMsg2(client, request)
```

## GetAppsInAppRemoteService
### buyInApp

```python
from Astandy.generated.protos import inapps_message_pb2

request: inapps_message_pb2.GetAppsBuyInappRequest = inapps_message_pb2.GetAppsBuyInappRequest(args_here)
response: inapps_message_pb2.GetAppsBuyInappResponse = await client.raw.GetAppsInAppRemoteService.buyInApp(client, request)
```

## BoltRemoteService
### subscribe2

```python
from Astandy.generated.protos import common_message_pb2

request: common_message_pb2.SubscribeRequest = common_message_pb2.SubscribeRequest(args_here)
response: common_message_pb2.SubscribeResponse = await client.raw.BoltRemoteService.subscribe2(client, request)
```

### unsubscribe2

```python
from Astandy.generated.protos import common_message_pb2

request: common_message_pb2.UnsubscribeRequest = common_message_pb2.UnsubscribeRequest(args_here)
response: common_message_pb2.UnsubscribeResponse = await client.raw.BoltRemoteService.unsubscribe2(client, request)
```

## LeaderboardRemoteService
### getPlayerRank

```python
from Astandy.generated.protos import leaderboard_message_pb2

request: leaderboard_message_pb2.GetPlayerRankRequest = leaderboard_message_pb2.GetPlayerRankRequest(args_here)
response: leaderboard_message_pb2.GetPlayerRankResponse = await client.raw.LeaderboardRemoteService.getPlayerRank(client, request)
```

### getPlayerLeaderBoard

```python
from Astandy.generated.protos import leaderboard_message_pb2

request: leaderboard_message_pb2.GetPlayerLeaderboardRequest = leaderboard_message_pb2.GetPlayerLeaderboardRequest(args_here)
response: leaderboard_message_pb2.GetPlayerLeaderboardResponse = await client.raw.LeaderboardRemoteService.getPlayerLeaderBoard(client, request)
```

### getClanLeaderBoard

```python
from Astandy.generated.protos import leaderboard_message_pb2

request: leaderboard_message_pb2.GetClanLeaderboardRequest = leaderboard_message_pb2.GetClanLeaderboardRequest(args_here)
response: leaderboard_message_pb2.GetClanLeaderboardResponse = await client.raw.LeaderboardRemoteService.getClanLeaderBoard(client, request)
```

### getClanRank

```python
from Astandy.generated.protos import leaderboard_message_pb2

request: leaderboard_message_pb2.GetClanRankRequest = leaderboard_message_pb2.GetClanRankRequest(args_here)
response: leaderboard_message_pb2.GetClanRankResponse = await client.raw.LeaderboardRemoteService.getClanRank(client, request)
```

## AccountLinkRemoteService
### getLinkedAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.GetLinkedAuthRequest = auth_message_pb2.GetLinkedAuthRequest(args_here)
response: auth_message_pb2.GetLinkedAuthResponse = await client.raw.AccountLinkRemoteService.getLinkedAuth(client, request)
```

## ClanStatsRemoteService
### getClanStats

```python
from Astandy.generated.protos import clan_stats_message_pb2

request: clan_stats_message_pb2.GetClanStatsRequest = clan_stats_message_pb2.GetClanStatsRequest(args_here)
response: clan_stats_message_pb2.GetClanStatsResponse = await client.raw.ClanStatsRemoteService.getClanStats(client, request)
```

### getCurrentClanStats

```python
from Astandy.generated.protos import clan_stats_message_pb2

request: clan_stats_message_pb2.GetCurrentClanStatsRequest = clan_stats_message_pb2.GetCurrentClanStatsRequest(args_here)
response: clan_stats_message_pb2.GetCurrentClanStatsResponse = await client.raw.ClanStatsRemoteService.getCurrentClanStats(client, request)
```

## AppStoreInAppRemoteService
### buyInApp2

```python
from Astandy.generated.protos import inapps_message_pb2

request: inapps_message_pb2.AppStoreBuyInappRequest = inapps_message_pb2.AppStoreBuyInappRequest(args_here)
response: inapps_message_pb2.AppStoreBuyInappResponse = await client.raw.AppStoreInAppRemoteService.buyInApp2(client, request)
```

## GroupRemoteService
### joinGroup2

```python
from Astandy.generated.protos import groups_message_pb2

request: groups_message_pb2.JoinGroupRequest = groups_message_pb2.JoinGroupRequest(args_here)
response: groups_message_pb2.JoinGroupResponse = await client.raw.GroupRemoteService.joinGroup2(client, request)
```

### leaveGroup2

```python
from Astandy.generated.protos import groups_message_pb2

request: groups_message_pb2.LeaveGroupRequest = groups_message_pb2.LeaveGroupRequest(args_here)
response: groups_message_pb2.LeaveGroupResponse = await client.raw.GroupRemoteService.leaveGroup2(client, request)
```

### createGroup2

```python
from Astandy.generated.protos import groups_message_pb2

request: groups_message_pb2.CreateGroupRequest = groups_message_pb2.CreateGroupRequest(args_here)
response: groups_message_pb2.CreateGroupResponse = await client.raw.GroupRemoteService.createGroup2(client, request)
```

## HuaweiAuthRemoteService
### encryptedAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.HuaweiAuthRequest = auth_message_pb2.HuaweiAuthRequest(args_here)
response: auth_message_pb2.HuaweiAuthResponse = await client.raw.HuaweiAuthRemoteService.encryptedAuth(client, request)
```

### linkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.HuaweiLinkAuthRequest = auth_message_pb2.HuaweiLinkAuthRequest(args_here)
response: auth_message_pb2.HuaweiLinkAuthResponse = await client.raw.HuaweiAuthRemoteService.linkAuth(client, request)
```

### unLinkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.HuaweiUnLinkAuthRequest = auth_message_pb2.HuaweiUnLinkAuthRequest(args_here)
response: auth_message_pb2.HuaweiUnLinkAuthResponse = await client.raw.HuaweiAuthRemoteService.unLinkAuth(client, request)
```

### encryptedAuth2

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.HuaweiAuthRequest = auth_message_pb2.HuaweiAuthRequest(args_here)
response: auth_message_pb2.HuaweiAuthResponse = await client.raw.HuaweiAuthRemoteService.encryptedAuth2(client, request)
```

## GoogleAuthRemoteService
### linkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.GoogleLinkAuthRequest = auth_message_pb2.GoogleLinkAuthRequest(args_here)
response: auth_message_pb2.GoogleLinkAuthResponse = await client.raw.GoogleAuthRemoteService.linkAuth(client, request)
```

### unLinkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.GoogleUnLinkAuthRequest = auth_message_pb2.GoogleUnLinkAuthRequest(args_here)
response: auth_message_pb2.GoogleUnLinkAuthResponse = await client.raw.GoogleAuthRemoteService.unLinkAuth(client, request)
```

### encryptedAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.GoogleAuthRequest = auth_message_pb2.GoogleAuthRequest(args_here)
response: auth_message_pb2.GoogleAuthResponse = await client.raw.GoogleAuthRemoteService.encryptedAuth(client, request)
```

### encryptedAuth2

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.GoogleAuthRequest = auth_message_pb2.GoogleAuthRequest(args_here)
response: auth_message_pb2.GoogleAuthResponse = await client.raw.GoogleAuthRemoteService.encryptedAuth2(client, request)
```

## InventoryRemoteService
### setInventoryItemPublicity

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.SetInventoryItemPublicityRequest = inventory_message_pb2.SetInventoryItemPublicityRequest(args_here)
response: inventory_message_pb2.SetInventoryItemPublicityResponse = await client.raw.InventoryRemoteService.setInventoryItemPublicity(client, request)
```

### getRecipeInfo

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.GetRecipeInfoRequest = inventory_message_pb2.GetRecipeInfoRequest(args_here)
response: inventory_message_pb2.GetRecipeInfoResponse = await client.raw.InventoryRemoteService.getRecipeInfo(client, request)
```

### activateCouponEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.ActivateCouponRequest = inventory_message_pb2.ActivateCouponRequest(args_here)
response: inventory_message_pb2.ActivateCouponResponse = await client.raw.InventoryRemoteService.activateCouponEncrypted(client, request)
```

### setInventoryItemFlagsEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.SetInventoryItemFlagsRequest = inventory_message_pb2.SetInventoryItemFlagsRequest(args_here)
response: inventory_message_pb2.SetInventoryItemFlagsResponse = await client.raw.InventoryRemoteService.setInventoryItemFlagsEncrypted(client, request)
```

### unmountInventoryItemEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.UnmountInventoryItemRequest = inventory_message_pb2.UnmountInventoryItemRequest(args_here)
response: inventory_message_pb2.UnmountInventoryItemResponse = await client.raw.InventoryRemoteService.unmountInventoryItemEncrypted(client, request)
```

### removeInventoryItemPropertyEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.RemoveItemModificationRequest = inventory_message_pb2.RemoveItemModificationRequest(args_here)
response: inventory_message_pb2.RemoveItemModificationResponse = await client.raw.InventoryRemoteService.removeInventoryItemPropertyEncrypted(client, request)
```

### getInventoryItemPropertyDefinitionsEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.GetInventoryItemPropertyDefinitionsRequest = inventory_message_pb2.GetInventoryItemPropertyDefinitionsRequest(args_here)
response: inventory_message_pb2.GetInventoryItemPropertyDefinitionsResponse = await client.raw.InventoryRemoteService.getInventoryItemPropertyDefinitionsEncrypted(client, request)
```

### setInventoryItemsPropertiesEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.SetItemsModificationsRequest = inventory_message_pb2.SetItemsModificationsRequest(args_here)
response: inventory_message_pb2.SetItemsModificationsResponse = await client.raw.InventoryRemoteService.setInventoryItemsPropertiesEncrypted(client, request)
```

### getOtherPlayerPublicItemsEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.GetAllOtherPlayerPublicItemsRequest = inventory_message_pb2.GetAllOtherPlayerPublicItemsRequest(args_here)
response: inventory_message_pb2.GetAllOtherPlayerPublicItemsResponse = await client.raw.InventoryRemoteService.getOtherPlayerPublicItemsEncrypted(client, request)
```

### buyInventoryItemEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.BuyInventoryItemRequest = inventory_message_pb2.BuyInventoryItemRequest(args_here)
response: inventory_message_pb2.BuyInventoryItemResponse = await client.raw.InventoryRemoteService.buyInventoryItemEncrypted(client, request)
```

### getPlayerInventoryEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.GetPlayerInventoryRequest = inventory_message_pb2.GetPlayerInventoryRequest(args_here)
response: inventory_message_pb2.GetPlayerInventoryResponse = await client.raw.InventoryRemoteService.getPlayerInventoryEncrypted(client, request)
```

### getRecipeState

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.GetRecipeStateRequest = inventory_message_pb2.GetRecipeStateRequest(args_here)
response: inventory_message_pb2.GetRecipeStateResponse = await client.raw.InventoryRemoteService.getRecipeState(client, request)
```

### consumeInventoryItemEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.ConsumeInventoryItemRequest = inventory_message_pb2.ConsumeInventoryItemRequest(args_here)
response: inventory_message_pb2.ConsumeInventoryItemResponse = await client.raw.InventoryRemoteService.consumeInventoryItemEncrypted(client, request)
```

### tradeInventoryItemsEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.TradeInventoryItemsRequest = inventory_message_pb2.TradeInventoryItemsRequest(args_here)
response: inventory_message_pb2.TradeInventoryItemsResponse = await client.raw.InventoryRemoteService.tradeInventoryItemsEncrypted(client, request)
```

### getInventoryItemDefinitionsEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.GetInventoryItemDefinitionsRequest = inventory_message_pb2.GetInventoryItemDefinitionsRequest(args_here)
response: inventory_message_pb2.GetInventoryItemDefinitionsResponse = await client.raw.InventoryRemoteService.getInventoryItemDefinitionsEncrypted(client, request)
```

### transferInventoryItemsEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.TransferInventoryItemsRequest = inventory_message_pb2.TransferInventoryItemsRequest(args_here)
response: inventory_message_pb2.TransferInventoryItemsResponse = await client.raw.InventoryRemoteService.transferInventoryItemsEncrypted(client, request)
```

### executeRecipeEncrypted2

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.ExecuteRecipeRequest = inventory_message_pb2.ExecuteRecipeRequest(args_here)
response: inventory_message_pb2.ExecuteRecipeEncrypted2Response = await client.raw.InventoryRemoteService.executeRecipeEncrypted2(client, request)
```

### sellInventoryItemEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.SellInventoryItemRequest = inventory_message_pb2.SellInventoryItemRequest(args_here)
response: inventory_message_pb2.SellInventoryItemResponse = await client.raw.InventoryRemoteService.sellInventoryItemEncrypted(client, request)
```

### mountInventoryItemEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.MountInventoryItemRequest = inventory_message_pb2.MountInventoryItemRequest(args_here)
response: inventory_message_pb2.MountInventoryItemResponse = await client.raw.InventoryRemoteService.mountInventoryItemEncrypted(client, request)
```

### getRecipeStatusEncrypted

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.GetRecipeStatusRequest = inventory_message_pb2.GetRecipeStatusRequest(args_here)
response: inventory_message_pb2.GetRecipeStatusResponse = await client.raw.InventoryRemoteService.getRecipeStatusEncrypted(client, request)
```

## ContentCreatorRemoteService
### subscribeCreator

```python
from Astandy.generated.protos import content_creator_message_pb2

request: content_creator_message_pb2.SubscribeCreatorRequest = content_creator_message_pb2.SubscribeCreatorRequest(args_here)
response: content_creator_message_pb2.SubscribeCreatorResponse = await client.raw.ContentCreatorRemoteService.subscribeCreator(client, request)
```

### findCreatorSubscription

```python
from Astandy.generated.protos import content_creator_message_pb2

request: content_creator_message_pb2.GetSubscribedCreatorRequest = content_creator_message_pb2.GetSubscribedCreatorRequest(args_here)
response: content_creator_message_pb2.GetSubscribedCreatorResponse = await client.raw.ContentCreatorRemoteService.findCreatorSubscription(client, request)
```

### findCreator

```python
from Astandy.generated.protos import content_creator_message_pb2

request: content_creator_message_pb2.FindCreatorRequest = content_creator_message_pb2.FindCreatorRequest(args_here)
response: content_creator_message_pb2.FindCreatorResponse = await client.raw.ContentCreatorRemoteService.findCreator(client, request)
```

### unsubscribeCreator

```python
from Astandy.generated.protos import content_creator_message_pb2

request: content_creator_message_pb2.UnsubscribeCreatorRequest = content_creator_message_pb2.UnsubscribeCreatorRequest(args_here)
response: content_creator_message_pb2.UnsubscribeCreatorResponse = await client.raw.ContentCreatorRemoteService.unsubscribeCreator(client, request)
```

## FacebookAuthRemoteService
### encryptedAuth2

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.FacebookAuthRequest = auth_message_pb2.FacebookAuthRequest(args_here)
response: auth_message_pb2.FacebookAuthResponse = await client.raw.FacebookAuthRemoteService.encryptedAuth2(client, request)
```

### unLinkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.FacebookUnLinkAuthRequest = auth_message_pb2.FacebookUnLinkAuthRequest(args_here)
response: auth_message_pb2.FacebookUnLinkAuthResponse = await client.raw.FacebookAuthRemoteService.unLinkAuth(client, request)
```

### linkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.FacebookLinkAuthRequest = auth_message_pb2.FacebookLinkAuthRequest(args_here)
response: auth_message_pb2.FacebookLinkAuthResponse = await client.raw.FacebookAuthRemoteService.linkAuth(client, request)
```

### encryptedAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.FacebookAuthRequest = auth_message_pb2.FacebookAuthRequest(args_here)
response: auth_message_pb2.FacebookAuthResponse = await client.raw.FacebookAuthRemoteService.encryptedAuth(client, request)
```

## GSMatchesRemoteService
### finishMatch

```python
from Astandy.generated.protos import matches_message_pb2

request: matches_message_pb2.FinishMatchRequest = matches_message_pb2.FinishMatchRequest(args_here)
response: matches_message_pb2.FinishMatchResponse = await client.raw.GSMatchesRemoteService.finishMatch(client, request)
```

## GameServerInventoryRemoteService
### setItemsModificationsByServer

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.SetItemsModificationsByServerRequest = inventory_message_pb2.SetItemsModificationsByServerRequest(args_here)
response: inventory_message_pb2.SetItemsModificationsByServerResponse = await client.raw.GameServerInventoryRemoteService.setItemsModificationsByServer(client, request)
```

### executeRecipeByServer

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.ExecuteRecipeByServerRequest = inventory_message_pb2.ExecuteRecipeByServerRequest(args_here)
response: inventory_message_pb2.ExecuteRecipeByServerResponse = await client.raw.GameServerInventoryRemoteService.executeRecipeByServer(client, request)
```

### giveInventoryByServer

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.GiveInventoryByServerRequest = inventory_message_pb2.GiveInventoryByServerRequest(args_here)
response: inventory_message_pb2.GiveInventoryByServerResponse = await client.raw.GameServerInventoryRemoteService.giveInventoryByServer(client, request)
```

### consumeItemsByServer

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.ConsumeItemsByServerRequest = inventory_message_pb2.ConsumeItemsByServerRequest(args_here)
response: inventory_message_pb2.ConsumeItemsByServerResponse = await client.raw.GameServerInventoryRemoteService.consumeItemsByServer(client, request)
```

### getPlayerInventoryItemsByServer

```python
from Astandy.generated.protos import inventory_message_pb2

request: inventory_message_pb2.PlayerInventoryItemsByServerRequest = inventory_message_pb2.PlayerInventoryItemsByServerRequest(args_here)
response: inventory_message_pb2.PlayerInventoryItemsByServerResponse = await client.raw.GameServerInventoryRemoteService.getPlayerInventoryItemsByServer(client, request)
```

## OffersRemoteService
### getSpecialOffers

```python
from Astandy.generated.protos import offers_message_pb2

request: offers_message_pb2.GetSpecialOffersRequest = offers_message_pb2.GetSpecialOffersRequest(args_here)
response: offers_message_pb2.GetSpecialOffersResponse = await client.raw.OffersRemoteService.getSpecialOffers(client, request)
```

## StorageRemoteService
### writeFile2

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.WriteFileRequest = storage_message_pb2.WriteFileRequest(args_here)
response: storage_message_pb2.WriteFileResponse = await client.raw.StorageRemoteService.writeFile2(client, request)
```

### readAllFiles2

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.ReadAllFilesRequest = storage_message_pb2.ReadAllFilesRequest(args_here)
response: storage_message_pb2.ReadAllFilesResponse = await client.raw.StorageRemoteService.readAllFiles2(client, request)
```

### writeFile

```python
from Astandy.generated.protos import None

request: None = None(args_here)
response: None = await client.raw.StorageRemoteService.writeFile(client, request)
```

### deleteFile2

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.DeleteFileRequest = storage_message_pb2.DeleteFileRequest(args_here)
response: storage_message_pb2.DeleteFileResponse = await client.raw.StorageRemoteService.deleteFile2(client, request)
```

### unshareFile

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.UnshareFileRequest = storage_message_pb2.UnshareFileRequest(args_here)
response: storage_message_pb2.UnshareFileResponse = await client.raw.StorageRemoteService.unshareFile(client, request)
```

### getFilenames

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.GetFilenamesRequest = storage_message_pb2.GetFilenamesRequest(args_here)
response: storage_message_pb2.GetFilenamesResponse = await client.raw.StorageRemoteService.getFilenames(client, request)
```

### shareFile

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.ShareFileRequest = storage_message_pb2.ShareFileRequest(args_here)
response: storage_message_pb2.ShareFileResponse = await client.raw.StorageRemoteService.shareFile(client, request)
```

### readPlayerPublicFiles

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.ReadPlayerPublicFilesRequest = storage_message_pb2.ReadPlayerPublicFilesRequest(args_here)
response: storage_message_pb2.ReadPlayerPublicFilesResponse = await client.raw.StorageRemoteService.readPlayerPublicFiles(client, request)
```

### readFile3

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.ReadFile3Request = storage_message_pb2.ReadFile3Request(args_here)
response: storage_message_pb2.ReadFile3Response = await client.raw.StorageRemoteService.readFile3(client, request)
```

### changeFileAccessMode

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.ChangeFileAccessModeRequest = storage_message_pb2.ChangeFileAccessModeRequest(args_here)
response: storage_message_pb2.ChangeFileAccessModeResponse = await client.raw.StorageRemoteService.changeFileAccessMode(client, request)
```

### readPublicFile

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.ReadPublicFileRequest = storage_message_pb2.ReadPublicFileRequest(args_here)
response: storage_message_pb2.ReadPublicFileResponse = await client.raw.StorageRemoteService.readPublicFile(client, request)
```

### readFile2

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.ReadFileRequest = storage_message_pb2.ReadFileRequest(args_here)
response: storage_message_pb2.ReadFileResponse = await client.raw.StorageRemoteService.readFile2(client, request)
```

### readFiles

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.ReadFilesRequest = storage_message_pb2.ReadFilesRequest(args_here)
response: storage_message_pb2.ReadFilesResponse = await client.raw.StorageRemoteService.readFiles(client, request)
```

### getSharedFile

```python
from Astandy.generated.protos import storage_message_pb2

request: storage_message_pb2.GetSharedFileRequest = storage_message_pb2.GetSharedFileRequest(args_here)
response: storage_message_pb2.GetSharedFileResponse = await client.raw.StorageRemoteService.getSharedFile(client, request)
```

## BoltIdAuthRemoteService
### unLinkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.BoltIdUnLinkAuthRequest = auth_message_pb2.BoltIdUnLinkAuthRequest(args_here)
response: auth_message_pb2.BoltIdUnLinkAuthResponse = await client.raw.BoltIdAuthRemoteService.unLinkAuth(client, request)
```

### encryptedAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.BoltIdAuthRequest = auth_message_pb2.BoltIdAuthRequest(args_here)
response: auth_message_pb2.BoltIdAuthResponse = await client.raw.BoltIdAuthRemoteService.encryptedAuth(client, request)
```

### encryptedAuth2

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.BoltIdAuthRequest = auth_message_pb2.BoltIdAuthRequest(args_here)
response: auth_message_pb2.BoltIdAuthResponse = await client.raw.BoltIdAuthRemoteService.encryptedAuth2(client, request)
```

### linkAuth

```python
from Astandy.generated.protos import auth_message_pb2

request: auth_message_pb2.BoltIdLinkAuthRequest = auth_message_pb2.BoltIdLinkAuthRequest(args_here)
response: auth_message_pb2.BoltIdLinkAuthResponse = await client.raw.BoltIdAuthRemoteService.linkAuth(client, request)
```

## GameServerPlayerRemoteService
### checkBan

```python
from Astandy.generated.protos import common_message_pb2

request: common_message_pb2.CheckBanGamePlayerRequest = common_message_pb2.CheckBanGamePlayerRequest(args_here)
response: common_message_pb2.CheckBanGamePlayerResponse = await client.raw.GameServerPlayerRemoteService.checkBan(client, request)
```

### banGamePlayer

```python
from Astandy.generated.protos import common_message_pb2

request: common_message_pb2.BanGamePlayerRequest = common_message_pb2.BanGamePlayerRequest(args_here)
response: common_message_pb2.BanGamePlayerResponse = await client.raw.GameServerPlayerRemoteService.banGamePlayer(client, request)
```

### setPhotonGame2

```python
from Astandy.generated.protos import common_message_pb2

request: common_message_pb2.SetPhotonGameRequest = common_message_pb2.SetPhotonGameRequest(args_here)
response: common_message_pb2.SetPhotonGameResponse = await client.raw.GameServerPlayerRemoteService.setPhotonGame2(client, request)
```

### banGamePlayerCustom

```python
from Astandy.generated.protos import common_message_pb2

request: common_message_pb2.BanGamePlayerCustomRequest = common_message_pb2.BanGamePlayerCustomRequest(args_here)
response: common_message_pb2.BanGamePlayerResponse = await client.raw.GameServerPlayerRemoteService.banGamePlayerCustom(client, request)
```

## GameEventRemoteService
### getCurrentChallenges

```python
from Astandy.generated.protos import challenges_message_pb2

request: challenges_message_pb2.GetCurrentChallengesRequest = challenges_message_pb2.GetCurrentChallengesRequest(args_here)
response: challenges_message_pb2.GetCurrentChallengesResponse = await client.raw.GameEventRemoteService.getCurrentChallenges(client, request)
```

### getPlayerGameEventsProgresses

```python
from Astandy.generated.protos import game_event_message_pb2

request: game_event_message_pb2.GetPlayerGameEventsProgressesRequest = game_event_message_pb2.GetPlayerGameEventsProgressesRequest(args_here)
response: game_event_message_pb2.GetPlayerGameEventsProgressesResponse = await client.raw.GameEventRemoteService.getPlayerGameEventsProgresses(client, request)
```

### getCachedPlayerGameEvents

```python
from Astandy.generated.protos import game_event_message_pb2

request: game_event_message_pb2.GetCachedPlayerGameEventsRequest = game_event_message_pb2.GetCachedPlayerGameEventsRequest(args_here)
response: game_event_message_pb2.GetCachedPlayerGameEventsResponse = await client.raw.GameEventRemoteService.getCachedPlayerGameEvents(client, request)
```

### getPlayerGameEventProgress

```python
from Astandy.generated.protos import game_event_message_pb2

request: game_event_message_pb2.GetPlayerGameEventProgressRequest = game_event_message_pb2.GetPlayerGameEventProgressRequest(args_here)
response: game_event_message_pb2.GetPlayerGameEventProgressResponse = await client.raw.GameEventRemoteService.getPlayerGameEventProgress(client, request)
```

### processChallenge

```python
from Astandy.generated.protos import challenges_message_pb2

request: challenges_message_pb2.ProgressChallengeRequest = challenges_message_pb2.ProgressChallengeRequest(args_here)
response: challenges_message_pb2.ProgressChallengeResponse = await client.raw.GameEventRemoteService.processChallenge(client, request)
```

### saveChallengeDefinition3

```python
from Astandy.generated.protos import challenges_message_pb2

request: challenges_message_pb2.SaveChallengeDefinition2Request = challenges_message_pb2.SaveChallengeDefinition2Request(args_here)
response: challenges_message_pb2.SaveChallengeDefinition2Response = await client.raw.GameEventRemoteService.saveChallengeDefinition3(client, request)
```

### claimAllRewardsOfSpecificPasses

```python
from Astandy.generated.protos import game_event_message_pb2

request: game_event_message_pb2.ClaimAllRewardsOfSpecificPasses = game_event_message_pb2.ClaimAllRewardsOfSpecificPasses(args_here)
response: game_event_message_pb2.ClaimRewardsResponse = await client.raw.GameEventRemoteService.claimAllRewardsOfSpecificPasses(client, request)
```

### getPlayerCurrentGameEvents2

```python
from Astandy.generated.protos import game_event_message_pb2

request: game_event_message_pb2.GetPlayerCurrentGameEventsRequest = game_event_message_pb2.GetPlayerCurrentGameEventsRequest(args_here)
response: game_event_message_pb2.GetPlayerCurrentGameEventsResponse = await client.raw.GameEventRemoteService.getPlayerCurrentGameEvents2(client, request)
```

### claimSpecificLevelReward

```python
from Astandy.generated.protos import game_event_message_pb2

request: game_event_message_pb2.ClaimSpecificLevelRewardRequest = game_event_message_pb2.ClaimSpecificLevelRewardRequest(args_here)
response: game_event_message_pb2.ClaimRewardsResponse = await client.raw.GameEventRemoteService.claimSpecificLevelReward(client, request)
```

### getAllChallenges

```python
from Astandy.generated.protos import challenges_message_pb2

request: challenges_message_pb2.GetAllChallengesRequest = challenges_message_pb2.GetAllChallengesRequest(args_here)
response: challenges_message_pb2.GetAllChallengesResponse = await client.raw.GameEventRemoteService.getAllChallenges(client, request)
```

### progressGameEvent

```python
from Astandy.generated.protos import game_event_message_pb2

request: game_event_message_pb2.ProgressGameEventRequest = game_event_message_pb2.ProgressGameEventRequest(args_here)
response: game_event_message_pb2.ProgressGameEventResponse = await client.raw.GameEventRemoteService.progressGameEvent(client, request)
```

## GlobalChatRemoteService
### sendGlobalChatMessage2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.SendGlobalMsgRequest = chat_message_pb2.SendGlobalMsgRequest(args_here)
response: chat_message_pb2.GetGlobalMsgsResponse = await client.raw.GlobalChatRemoteService.sendGlobalChatMessage2(client, request)
```

## AppGalleryInAppRemoteService
### buyInApp

```python
from Astandy.generated.protos import inapps_message_pb2

request: inapps_message_pb2.AppGalleryBuyInappRequest = inapps_message_pb2.AppGalleryBuyInappRequest(args_here)
response: inapps_message_pb2.AppGalleryBuyInappResponse = await client.raw.AppGalleryInAppRemoteService.buyInApp(client, request)
```

## GameAnnouncementRemoteService
### getAllAnnouncements

```python
from Astandy.generated.protos import newsfeed_message_pb2

request: newsfeed_message_pb2.GetAllGameAnnouncementsRequest = newsfeed_message_pb2.GetAllGameAnnouncementsRequest(args_here)
response: newsfeed_message_pb2.GetAllGameAnnouncementsResponse = await client.raw.GameAnnouncementRemoteService.getAllAnnouncements(client, request)
```

## ChatRemoteService
### deleteGroupMsgs2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.DeleteGroupMsgsRequest = chat_message_pb2.DeleteGroupMsgsRequest(args_here)
response: chat_message_pb2.DeleteGroupMsgsResponse = await client.raw.ChatRemoteService.deleteGroupMsgs2(client, request)
```

### sendFriendMsg2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.SendFriendMsgRequest = chat_message_pb2.SendFriendMsgRequest(args_here)
response: chat_message_pb2.SendFriendMsgResponse = await client.raw.ChatRemoteService.sendFriendMsg2(client, request)
```

### getFriendMsgsByOffset2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.GetFriendMsgsByOffsetRequest = chat_message_pb2.GetFriendMsgsByOffsetRequest(args_here)
response: chat_message_pb2.GetFriendMsgsByOffsetResponse = await client.raw.ChatRemoteService.getFriendMsgsByOffset2(client, request)
```

### getFriendMsgsByPage2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.GetFriendMsgsByPageRequest = chat_message_pb2.GetFriendMsgsByPageRequest(args_here)
response: chat_message_pb2.GetFriendMsgsByPageResponse = await client.raw.ChatRemoteService.getFriendMsgsByPage2(client, request)
```

### getUnreadChatUsersCount2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.GetUnreadChatUsersCountRequest = chat_message_pb2.GetUnreadChatUsersCountRequest(args_here)
response: chat_message_pb2.GetUnreadChatUsersCountResponse = await client.raw.ChatRemoteService.getUnreadChatUsersCount2(client, request)
```

### sendGroupMsg2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.SendGroupMsgRequest = chat_message_pb2.SendGroupMsgRequest(args_here)
response: chat_message_pb2.SendGroupMsgResponse = await client.raw.ChatRemoteService.sendGroupMsg2(client, request)
```

### getChatUser

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.GetChatUserRequest = chat_message_pb2.GetChatUserRequest(args_here)
response: chat_message_pb2.GetChatUserResponse = await client.raw.ChatRemoteService.getChatUser(client, request)
```

### readGroupMsgs2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.ReadGroupMsgsRequest = chat_message_pb2.ReadGroupMsgsRequest(args_here)
response: chat_message_pb2.ReadGroupMsgsResponse = await client.raw.ChatRemoteService.readGroupMsgs2(client, request)
```

### getChatUsersLite

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.GetChatUsersLiteRequest = chat_message_pb2.GetChatUsersLiteRequest(args_here)
response: chat_message_pb2.GetChatUsersLiteResponse = await client.raw.ChatRemoteService.getChatUsersLite(client, request)
```

### getChatUsersByOffset2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.GetChatUsersByOffsetRequest = chat_message_pb2.GetChatUsersByOffsetRequest(args_here)
response: chat_message_pb2.GetChatUsersByOffsetResponse = await client.raw.ChatRemoteService.getChatUsersByOffset2(client, request)
```

### readFriendMsgs2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.ReadFriendMsgsRequest = chat_message_pb2.ReadFriendMsgsRequest(args_here)
response: chat_message_pb2.ReadFriendMsgsResponse = await client.raw.ChatRemoteService.readFriendMsgs2(client, request)
```

### getChatUsersByPage2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.GetChatUsersByPageRequest = chat_message_pb2.GetChatUsersByPageRequest(args_here)
response: chat_message_pb2.GetChatUsersByPageResponse = await client.raw.ChatRemoteService.getChatUsersByPage2(client, request)
```

### getChatUsers2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.GetChatUsersRequest = chat_message_pb2.GetChatUsersRequest(args_here)
response: chat_message_pb2.GetChatUsersResponse = await client.raw.ChatRemoteService.getChatUsers2(client, request)
```

### getGroupMsgs2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.GetGroupMsgsRequest = chat_message_pb2.GetGroupMsgsRequest(args_here)
response: chat_message_pb2.GetGroupMsgsResponse = await client.raw.ChatRemoteService.getGroupMsgs2(client, request)
```

### deleteFriendMsgs2

```python
from Astandy.generated.protos import chat_message_pb2

request: chat_message_pb2.DeleteFriendMsgsRequest = chat_message_pb2.DeleteFriendMsgsRequest(args_here)
response: chat_message_pb2.DeleteFriendMsgsResponse = await client.raw.ChatRemoteService.deleteFriendMsgs2(client, request)
```

## InAppRemoteService
### findCreatorSubscription

```python
from Astandy.generated.protos import content_creator_message_pb2

request: content_creator_message_pb2.GetSubscribedCreatorRequest = content_creator_message_pb2.GetSubscribedCreatorRequest(args_here)
response: content_creator_message_pb2.GetSubscribedCreatorResponse = await client.raw.InAppRemoteService.findCreatorSubscription(client, request)
```

### findCreator

```python
from Astandy.generated.protos import content_creator_message_pb2

request: content_creator_message_pb2.FindCreatorRequest = content_creator_message_pb2.FindCreatorRequest(args_here)
response: content_creator_message_pb2.FindCreatorResponse = await client.raw.InAppRemoteService.findCreator(client, request)
```

### unsubscribeCreator

```python
from Astandy.generated.protos import content_creator_message_pb2

request: content_creator_message_pb2.UnsubscribeCreatorRequest = content_creator_message_pb2.UnsubscribeCreatorRequest(args_here)
response: content_creator_message_pb2.UnsubscribeCreatorResponse = await client.raw.InAppRemoteService.unsubscribeCreator(client, request)
```

### getSubscribedCreator

```python
from Astandy.generated.protos import content_creator_message_pb2

request: content_creator_message_pb2.GetSubscribedCreatorRequest = content_creator_message_pb2.GetSubscribedCreatorRequest(args_here)
response: content_creator_message_pb2.GetSubscribedCreatorResponse = await client.raw.InAppRemoteService.getSubscribedCreator(client, request)
```

### subscribeCreator

```python
from Astandy.generated.protos import content_creator_message_pb2

request: content_creator_message_pb2.SubscribeCreatorRequest = content_creator_message_pb2.SubscribeCreatorRequest(args_here)
response: content_creator_message_pb2.SubscribeCreatorResponse = await client.raw.InAppRemoteService.subscribeCreator(client, request)
```

## Generated Events

Generated events are resolved by exact `(listener, event)` first, then by numeric code.

## Event Listener Index

- [InAppsRemoteEventListener](#inappsremoteeventlistener) - `1` events
- [AchievementsRemoteEventListener](#achievementsremoteeventlistener) - `1` events
- [GameEventRemoteEventListener](#gameeventremoteeventlistener) - `5` events
- [FriendsRemoteEventListener](#friendsremoteeventlistener) - `8` events
- [MatchmakingRemoteEventListener](#matchmakingremoteeventlistener) - `21` events
- [RentMarketRemoteEventListener](#rentmarketremoteeventlistener) - `5` events
- [ReferralRemoteEventListener](#referralremoteeventlistener) - `1` events
- [AdsRemoteEventListener](#adsremoteeventlistener) - `1` events
- [OfferRemoteEventListener](#offerremoteeventlistener) - `1` events
- [MatchesRemoteEventListener](#matchesremoteeventlistener) - `1` events
- [ClanStatsRemoteEventListener](#clanstatsremoteeventlistener) - `1` events
- [ClanMessagesRemoteEventListener](#clanmessagesremoteeventlistener) - `1` events
- [SystemMessagesRemoteEventListener](#systemmessagesremoteeventlistener) - `1` events
- [GlobalChatRemoteEventListener](#globalchatremoteeventlistener) - `1` events
- [ClansRemoteEventListener](#clansremoteeventlistener) - `24` events
- [InventoryRemoteEventListener](#inventoryremoteeventlistener) - `2` events
- [PlayerStatsRemoteEventListener](#playerstatsremoteeventlistener) - `1` events
- [MarketplaceRemoteEventListener](#marketplaceremoteeventlistener) - `5` events
- [MessagesRemoteEventListener](#messagesremoteeventlistener) - `1` events
- [InternalRemoteEventListener](#internalremoteeventlistener) - `4` events
- [OfferWallRemoteEventListener](#offerwallremoteeventlistener) - `1` events

## InAppsRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onInAppEvent` | `119` | `OnInAppEvent` | `InAppsRemoteEventListenerOnInAppEventUpdate` |

## AchievementsRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onAchievementsUpdatedEvent` | `0` | `OnAchievementsUpdatedEvent` | `AchievementsRemoteEventListenerOnAchievementsUpdatedEventUpdate` |

## GameEventRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onProgressSharedGameEvent` | `109` | `OnProgressSharedGameEvent` | `GameEventRemoteEventListenerOnProgressSharedGameEventUpdate` |
| `onProgressChallengeEvent` | `108` | `OnProgressChallengeEvent` | `GameEventRemoteEventListenerOnProgressChallengeEventUpdate` |
| `onSharedGameEventLevelAchieved` | `110` | `OnSharedGameEventLevelAchieved` | `GameEventRemoteEventListenerOnSharedGameEventLevelAchievedUpdate` |
| `onProgressGameEvent` | `106` | `OnProgressGameEvent` | `GameEventRemoteEventListenerOnProgressGameEventUpdate` |
| `onGamePassChanged` | `107` | `OnGamePassChangedEvent` | `GameEventRemoteEventListenerOnGamePassChangedUpdate` |

## FriendsRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onPlayerStatusChangedEvent` | `11` | `OnPlayerStatusChangedEvent` | `FriendsRemoteEventListenerOnPlayerStatusChangedEventUpdate` |
| `onFriendAvatarChangedEvent` | `12` | `OnFriendAvatarChangedEvent` | `FriendsRemoteEventListenerOnFriendAvatarChangedEventUpdate` |
| `onFriendRemovedEvent` | `17` | `OnFriendRemovedEvent` | `FriendsRemoteEventListenerOnFriendRemovedEventUpdate` |
| `onNewFriendshipRequestEvent` | `13` | `OnNewFriendshipRequestEvent` | `FriendsRemoteEventListenerOnNewFriendshipRequestEventUpdate` |
| `onPlayerAttributesChanged` | `16` | `OnPlayerAttributesChanged` | `FriendsRemoteEventListenerOnPlayerAttributesChangedUpdate` |
| `onFriendAddedEvent` | `15` | `OnFriendAddedEvent` | `FriendsRemoteEventListenerOnFriendAddedEventUpdate` |
| `onRevokeFriendshipRequestEvent` | `18` | `OnRevokeFriendshipRequestEvent` | `FriendsRemoteEventListenerOnRevokeFriendshipRequestEventUpdate` |
| `onFriendNameChangedEvent` | `14` | `OnFriendNameChangedEvent` | `FriendsRemoteEventListenerOnFriendNameChangedEventUpdate` |

## MatchmakingRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onNewPlayerInvitedToLobbyEvent` | `63` | `OnNewPlayerInvitedToLobbyEvent` | `MatchmakingRemoteEventListenerOnNewPlayerInvitedToLobbyEventUpdate` |
| `onLobbyMaxMembersChangedEvent` | `67` | `OnLobbyMaxMembersChangedEvent` | `MatchmakingRemoteEventListenerOnLobbyMaxMembersChangedEventUpdate` |
| `onNewPlayerJoinedLobbyEvent` | `66` | `OnNewPlayerJoinedLobbyEvent` | `MatchmakingRemoteEventListenerOnNewPlayerJoinedLobbyEventUpdate` |
| `onPlayerLeftLobbyEvent` | `69` | `OnPlayerLeftLobbyEvent` | `MatchmakingRemoteEventListenerOnPlayerLeftLobbyEventUpdate` |
| `onNewSpectatorJoinedLobbyEvent` | `76` | `OnNewSpectatorJoinedLobbyEvent` | `MatchmakingRemoteEventListenerOnNewSpectatorJoinedLobbyEventUpdate` |
| `onRevokeInviteToLobbyEvent` | `72` | `OnRevokeInviteToLobbyEvent` | `MatchmakingRemoteEventListenerOnRevokeInviteToLobbyEventUpdate` |
| `onLobbyChatMessageEvent` | `64` | `OnLobbyChatMessageEvent` | `MatchmakingRemoteEventListenerOnLobbyChatMessageEventUpdate` |
| `onLobbyDataChangedEvent` | `61` | `OnLobbyDataChangedEvent` | `MatchmakingRemoteEventListenerOnLobbyDataChangedEventUpdate` |
| `onLobbyMaxSpectatorsChangedEvent` | `71` | `OnLobbyMaxSpectatorsChangedEvent` | `MatchmakingRemoteEventListenerOnLobbyMaxSpectatorsChangedEventUpdate` |
| `onRefuseInviteToLobbyEvent` | `75` | `OnRefuseInviteToLobbyEvent` | `MatchmakingRemoteEventListenerOnRefuseInviteToLobbyEventUpdate` |
| `onLobbyPlayerTypeChangedEvent` | `78` | `OnLobbyPlayerTypeChangedEvent` | `MatchmakingRemoteEventListenerOnLobbyPlayerTypeChangedEventUpdate` |
| `onReceivedSpectatorInviteToLobbyEvent` | `79` | `OnReceivedSpectatorInviteToLobbyEvent` | `MatchmakingRemoteEventListenerOnReceivedSpectatorInviteToLobbyEventUpdate` |
| `onLobbyPhotonGameChangedEvent` | `68` | `OnLobbyPhotonGameChangedEvent` | `MatchmakingRemoteEventListenerOnLobbyPhotonGameChangedEventUpdate` |
| `onNewSpectatorInvitedToLobbyEvent` | `77` | `OnNewSpectatorInvitedToLobbyEvent` | `MatchmakingRemoteEventListenerOnNewSpectatorInvitedToLobbyEventUpdate` |
| `onPlayerKickedFromLobbyEvent` | `74` | `OnPlayerKickedFromLobbyEvent` | `MatchmakingRemoteEventListenerOnPlayerKickedFromLobbyEventUpdate` |
| `onLobbyJoinableChangedEvent` | `62` | `OnLobbyJoinableChangedEvent` | `MatchmakingRemoteEventListenerOnLobbyJoinableChangedEventUpdate` |
| `onLobbyGameServerChangedEvent` | `80` | `OnLobbyGameServerChangedEvent` | `MatchmakingRemoteEventListenerOnLobbyGameServerChangedEventUpdate` |
| `onReceivedInviteToLobbyEvent` | `65` | `OnReceivedInviteToLobbyEvent` | `MatchmakingRemoteEventListenerOnReceivedInviteToLobbyEventUpdate` |
| `onLobbyNameChangedEvent` | `81` | `OnLobbyNameChangedEvent` | `MatchmakingRemoteEventListenerOnLobbyNameChangedEventUpdate` |
| `onLobbyTypeChangedEvent` | `70` | `OnLobbyTypeChangedEvent` | `MatchmakingRemoteEventListenerOnLobbyTypeChangedEventUpdate` |
| `onLobbyOwnerChangedEvent` | `73` | `OnLobbyOwnerChangedEvent` | `MatchmakingRemoteEventListenerOnLobbyOwnerChangedEventUpdate` |

## RentMarketRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onRentTradeUpdated` | `130` | `OnRentTradeUpdatedEvent` | `RentMarketRemoteEventListenerOnRentTradeUpdatedUpdate` |
| `onRentTradeRequestClosed` | `131` | `OnRentTradeRequestClosedEvent` | `RentMarketRemoteEventListenerOnRentTradeRequestClosedUpdate` |
| `onPlayerRentRequestOpened` | `134` | `OnPlayerRentRequestOpenedEvent` | `RentMarketRemoteEventListenerOnPlayerRentRequestOpenedUpdate` |
| `onRentTradeRequestOpened` | `132` | `OnRentTradeRequestOpenedEvent` | `RentMarketRemoteEventListenerOnRentTradeRequestOpenedUpdate` |
| `onPlayerRentRequestClosed` | `133` | `OnPlayerRentRequestClosedEvent` | `RentMarketRemoteEventListenerOnPlayerRentRequestClosedUpdate` |

## ReferralRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onPlayerStateChangedEvent` | `140` | `OnPlayerStateChangedEvent` | `ReferralRemoteEventListenerOnPlayerStateChangedEventUpdate` |

## AdsRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onAdRewardEvent` | `116` | `OnAdRewardEvent` | `AdsRemoteEventListenerOnAdRewardEventUpdate` |

## OfferRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onOfferChanged` | `0` | `OnOfferChangedEvent` | `OfferRemoteEventListenerOnOfferChangedUpdate` |

## MatchesRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `OnMatchFinished` | `95` | `OnMatchFinishedEvent` | `MatchesRemoteEventListenerOnMatchFinishedUpdate` |

## ClanStatsRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onClanStatsUpdated` | `59` | `OnClanStatsUpdatedEvent` | `ClanStatsRemoteEventListenerOnClanStatsUpdatedUpdate` |

## ClanMessagesRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onIncomingClanChatMessageEvent` | `58` | `OnIncomingClanChatMessageEvent` | `ClanMessagesRemoteEventListenerOnIncomingClanChatMessageEventUpdate` |

## SystemMessagesRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onSystemMessageReceived` | `126` | `OnSystemMessageReceivedEvent` | `SystemMessagesRemoteEventListenerOnSystemMessageReceivedUpdate` |

## GlobalChatRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onIncomingGlobalChatMessageEvent` | `0` | `OnIncomingGlobalChatMessageEvent` | `GlobalChatRemoteEventListenerOnIncomingGlobalChatMessageEventUpdate` |

## ClansRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onLeftFromClan` | `46` | `OnLeftFromClan` | `ClansRemoteEventListenerOnLeftFromClanUpdate` |
| `onPlayerAttributesChanged` | `36` | `OnPlayerAttributesChanged` | `ClansRemoteEventListenerOnPlayerAttributesChangedUpdate` |
| `onKickedEvent` | `50` | `OnKickedEvent` | `ClansRemoteEventListenerOnKickedEventUpdate` |
| `onAssignedLeaderRoleEvent` | `47` | `OnAssignedLeaderRoleEvent` | `ClansRemoteEventListenerOnAssignedLeaderRoleEventUpdate` |
| `OnInviteRequestCancelledEvent` | `51` | `OnInviteRequestCancelledEvent` | `ClansRemoteEventListenerOnInviteRequestCancelledEventUpdate` |
| `onClanAvatarChangedEvent` | `49` | `OnClanAvatarChangedEvent` | `ClansRemoteEventListenerOnClanAvatarChangedEventUpdate` |
| `onPlayerNameChangedEvent` | `34` | `OnPlayerNameChangedEvent` | `ClansRemoteEventListenerOnPlayerNameChangedEventUpdate` |
| `OnJoinedToClan` | `39` | `OnJoinedToClanEvent` | `ClansRemoteEventListenerOnJoinedToClanUpdate` |
| `onClanDescriptionChangedEvent` | `54` | `OnClanDescriptionChangedEvent` | `ClansRemoteEventListenerOnClanDescriptionChangedEventUpdate` |
| `OnJoinRequestTaken` | `33` | `OnJoinRequestTakenEvent` | `ClansRemoteEventListenerOnJoinRequestTakenUpdate` |
| `onReadClosedInviteRequestEvent` | `38` | `OnReadClosedInviteRequestEvent` | `ClansRemoteEventListenerOnReadClosedInviteRequestEventUpdate` |
| `onClanTypeChanged` | `48` | `OnClanTypeChanged` | `ClansRemoteEventListenerOnClanTypeChangedUpdate` |
| `onPlayerAvatarChangedEvent` | `32` | `OnPlayerAvatarChangedEvent` | `ClansRemoteEventListenerOnPlayerAvatarChangedEventUpdate` |
| `onClanMemberDeclinedRequestEvent` | `41` | `OnClanMemberDeclinedRequestEvent` | `ClansRemoteEventListenerOnClanMemberDeclinedRequestEventUpdate` |
| `onOnlineStatusChangedEvent` | `31` | `OnOnlineStatusChangedEvent` | `ClansRemoteEventListenerOnOnlineStatusChangedEventUpdate` |
| `OnAssignedRoleEvent` | `43` | `OnAssignedRoleEvent` | `ClansRemoteEventListenerOnAssignedRoleEventUpdate` |
| `OnInvitedToClanEvent` | `44` | `OnInvitedToClanEvent` | `ClansRemoteEventListenerOnInvitedToClanEventUpdate` |
| `OnMemberJoinedToClan` | `35` | `OnMemberJoinedToClanEvent` | `ClansRemoteEventListenerOnMemberJoinedToClanUpdate` |
| `onClanTagAndNameChanged` | `52` | `OnClanTagAndNameChanged` | `ClansRemoteEventListenerOnClanTagAndNameChangedUpdate` |
| `onJoinRequestDeclinedEvent` | `45` | `OnJoinRequestDeclinedEvent` | `ClansRemoteEventListenerOnJoinRequestDeclinedEventUpdate` |
| `onClanMembersCountIncreased` | `53` | `OnClanMaxMembersCountIncreased` | `ClansRemoteEventListenerOnClanMembersCountIncreasedUpdate` |
| `onInviteRequestDeclinedEvent` | `40` | `OnInviteRequestDeclinedEvent` | `ClansRemoteEventListenerOnInviteRequestDeclinedEventUpdate` |
| `OnKickedMember` | `42` | `OnKickedMemberEvent` | `ClansRemoteEventListenerOnKickedMemberUpdate` |
| `OnJoinRequestCancelledEvent` | `37` | `OnJoinRequestCancelledEvent` | `ClansRemoteEventListenerOnJoinRequestCancelledEventUpdate` |

## InventoryRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onCouponActivated` | `112` | `OnCouponActivatedEvent` | `InventoryRemoteEventListenerOnCouponActivatedUpdate` |
| `onInventoryChanged` | `111` | `OnInventoryChangedEvent` | `InventoryRemoteEventListenerOnInventoryChangedUpdate` |

## PlayerStatsRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onStatsUpdatedEvent` | `101` | `OnStatsUpdatedEvent` | `PlayerStatsRemoteEventListenerOnStatsUpdatedEventUpdate` |

## MarketplaceRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onTradeRequestOpened` | `3` | `OnTradeRequestOpenedEvent` | `MarketplaceRemoteEventListenerOnTradeRequestOpenedUpdate` |
| `onTradeUpdated` | `1` | `OnTradeUpdatedEvent` | `MarketplaceRemoteEventListenerOnTradeUpdatedUpdate` |
| `onPlayerRequestClosed` | `4` | `OnPlayerRequestClosedEvent` | `MarketplaceRemoteEventListenerOnPlayerRequestClosedUpdate` |
| `onPlayerRequestOpened` | `5` | `OnPlayerRequestOpenedEvent` | `MarketplaceRemoteEventListenerOnPlayerRequestOpenedUpdate` |
| `onTradeRequestClosed` | `2` | `OnTradeRequestClosedEvent` | `MarketplaceRemoteEventListenerOnTradeRequestClosedUpdate` |

## MessagesRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onMsgFromFriendEvent` | `121` | `OnMsgFromFriendEvent` | `MessagesRemoteEventListenerOnMsgFromFriendEventUpdate` |

## InternalRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onPlayerKicked` | `0` | `OnPlayerKicked` | `InternalRemoteEventListenerOnPlayerKickedUpdate` |
| `onDisconnectPlayers` | `0` | `OnDisconnectPlayers` | `InternalRemoteEventListenerOnDisconnectPlayersUpdate` |
| `onPlayerBanned` | `0` | `OnPlayerBanned` | `InternalRemoteEventListenerOnPlayerBannedUpdate` |
| `onDeviceBanned` | `0` | `OnDeviceBanned` | `InternalRemoteEventListenerOnDeviceBannedUpdate` |

## OfferWallRemoteEventListener

| Event Method | Code | Payload | Update Class |
| --- | ---: | --- | --- |
| `onOfferWallRewardedEvent` | `0` | `OnOfferWallRewardedEvent` | `OfferWallRemoteEventListenerOnOfferWallRewardedEventUpdate` |
