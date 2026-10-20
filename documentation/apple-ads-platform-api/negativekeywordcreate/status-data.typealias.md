# NegativeKeywordCreate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Whether this negative keyword is active at creation.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string NegativeKeywordCreate.Status
```

## Possible Values

- `ENABLED`: The negative keyword is active and will suppress ad delivery for matching search queries.
- `PAUSED`: The negative keyword is paused and will not suppress any search queries until re-enabled.

#### Discussion

Include `status` in the create request to determine whether the negative keyword begins suppressing matching search queries immediately or starts paused.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`NegativeKeywordStatus`](../negativekeywordstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeywordcreate/status-data.typealias)*