# KeywordCreate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Whether this keyword is active and eligible to serve at creation.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string KeywordCreate.Status
```

## Possible Values

- `ENABLED`: Keyword is active and eligible to serve.
- `PAUSED`: Keyword is paused and will not serve.

#### Discussion

Include `status` in the create request to determine whether the new keyword begins competing in auctions immediately or starts paused.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`KeywordStatus`](../keywordstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordcreate/status-data.typealias)*