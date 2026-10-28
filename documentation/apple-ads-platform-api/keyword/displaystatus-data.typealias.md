# Keyword.DisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Rolled-up delivery state for a keyword, combining advertiser settings and parent entity status.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Keyword.DisplayStatus
```

## Possible Values

- `RUNNING`: The keyword is actively participating in ad auctions.
- `PAUSED`: The keyword has been paused by the advertiser.
- `DELETED`: The keyword has been soft-deleted.
- `AD_GROUP_ON_HOLD`: The keyword’s parent ad group is on hold, stopping keyword delivery.
- `CAMPAIGN_ON_HOLD`: The keyword’s parent campaign is on hold, stopping keyword delivery.

## Discussion

Because it rolls up the full hierarchy, a keyword can show `AD_GROUP_ON_HOLD` or `CAMPAIGN_ON_HOLD` even when its own status is otherwise fine.

### Example

```json
{
  "displayStatus": "RUNNING"
}
```

See [`KeywordDisplayStatus`](../keyworddisplaystatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keyword/displaystatus-data.typealias)*