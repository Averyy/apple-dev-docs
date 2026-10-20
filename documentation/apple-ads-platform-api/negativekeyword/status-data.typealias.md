# NegativeKeyword.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable active state for this negative keyword.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string NegativeKeyword.Status
```

## Possible Values

- `ENABLED`: The negative keyword is active and will suppress ad delivery for matching search queries.
- `PAUSED`: The negative keyword is paused and will not suppress any search queries until re-enabled.

#### Discussion

This field controls suppression directly; pausing it lets matching search queries resume triggering ads again.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`NegativeKeywordStatus`](../negativekeywordstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeyword/status-data.typealias)*