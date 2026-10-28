# KeywordUpdate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Whether this keyword should be active and eligible to serve after the update.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string KeywordUpdate.Status
```

## Possible Values

- `ENABLED`: Keyword is active and eligible to serve.
- `PAUSED`: Keyword is paused and will not serve.

## Discussion

Send `status: PAUSED` to stop an existing keyword from competing in auctions, or `ENABLED` to resume it.

### Example

```json
{
  "status": "PAUSED"
}
```

See [`KeywordStatus`](../keywordstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordupdate/status-data.typealias)*