# KeywordUpdate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Whether this keyword should be active and eligible to serve after the update.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string KeywordUpdate.Status
```

#### Discussion

Send `status: PAUSED` to stop an existing keyword from competing in auctions, or `ENABLED` to resume it.

##### Example

```json
{
  "status": "PAUSED"
}
```

See [`KeywordStatus`](keywordstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordupdate/status-data.typealias)*