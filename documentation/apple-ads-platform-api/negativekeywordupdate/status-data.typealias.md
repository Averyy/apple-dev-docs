# NegativeKeywordUpdate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Whether this negative keyword should be active after the update.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string NegativeKeywordUpdate.Status
```

## Possible Values

- `ENABLED`: The negative keyword is active and will suppress ad delivery for matching search queries.
- `PAUSED`: The negative keyword is paused and will not suppress any search queries until re-enabled.

#### Discussion

Set this to `PAUSED` to temporarily allow traffic from the excluded term without deleting the negative keyword.

##### Example

```json
{
  "status": "PAUSED"
}
```

See [`NegativeKeywordStatus`](../negativekeywordstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeywordupdate/status-data.typealias)*