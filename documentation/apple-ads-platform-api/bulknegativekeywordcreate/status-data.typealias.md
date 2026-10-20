# BulkNegativeKeywordCreate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The negative keyword’s status for a bulk negative-keyword create item.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BulkNegativeKeywordCreate.Status
```

## Possible Values

- `ENABLED`: The negative keyword is active and will suppress ad delivery for matching search queries.
- `PAUSED`: The negative keyword is paused and will not suppress any search queries until re-enabled.

#### Discussion

Set this within each item’s `data` to determine whether the negative keyword begins suppressing matching search queries as soon as the bulk create request completes.

##### Example

```json
{
  "status": "ENABLED"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulknegativekeywordcreate/status-data.typealias)*