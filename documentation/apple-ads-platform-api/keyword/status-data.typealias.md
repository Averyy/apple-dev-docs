# Keyword.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable serving state for this keyword.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Keyword.Status
```

## Possible Values

- `ENABLED`: Keyword is active and eligible to serve.
- `PAUSED`: Keyword is paused and will not serve.

## Discussion

This field controls auction eligibility directly, separate from the system-computed factors reflected in [`Keyword.DisplayStatus`](./displaystatus-data.typealias.md).

### Example

```json
{
  "status": "ENABLED"
}
```

See [`KeywordStatus`](../keywordstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keyword/status-data.typealias)*