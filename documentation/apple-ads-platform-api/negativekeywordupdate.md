# NegativeKeywordUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating an existing negative keyword.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object NegativeKeywordUpdate
```

#### Discussion

`NegativeKeywordUpdate` is the request payload for modifying an existing negative keyword. An update request can include only `status`. The schema rejects `text` and `matchType`. Set `status` to `PAUSED` to temporarily allow traffic from the excluded term, or `ENABLED` to re-activate the exclusion.

##### Example

```json
{
  "status": "PAUSED"
}
```

## Topics

### Type Aliases
- [type NegativeKeywordUpdate.Status](negativekeywordupdate/status-data.typealias.md)
  Whether this negative keyword should be active after the update.

## Properties

- `status` (NegativeKeywordUpdate.Status): Whether this negative keyword is active. See [`NegativeKeywordStatus`](negativekeywordstatus.md). Mutable.

## See Also

- [object NegativeKeyword](negativekeyword.md)
  A keyword exclusion that prevents ads from showing when a search query matches the excluded term.
- [object NegativeKeywordCreate](negativekeywordcreate.md)
  The request body for creating a new negative keyword.
- [object NegativeKeywordResponse](negativekeywordresponse.md)
  The response object for a negative keyword operation.
- [object NegativeKeywordQueryResponse](negativekeywordqueryresponse.md)
  The response object for a negative keyword query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeywordupdate)*