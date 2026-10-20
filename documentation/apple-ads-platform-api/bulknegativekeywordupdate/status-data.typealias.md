# BulkNegativeKeywordUpdate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The updated negative keyword status for a bulk negative-keyword update item.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BulkNegativeKeywordUpdate.Status
```

## Possible Values

- `ENABLED`: The negative keyword is active and will suppress ad delivery for matching search queries.
- `PAUSED`: The negative keyword is paused and will not suppress any search queries until re-enabled.

#### Discussion

Include this field within an item’s `data` to re-enable or pause the negative keyword’s suppression as part of the same bulk update request.

##### Example

```json
{
  "status": "PAUSED"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/bulknegativekeywordupdate/status-data.typealias)*