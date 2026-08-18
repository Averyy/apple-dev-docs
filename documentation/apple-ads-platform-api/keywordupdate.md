# KeywordUpdate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for updating an existing Keyword object.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object KeywordUpdate
```

#### Discussion

`KeywordUpdate` is the request payload for modifying an existing keyword. The request accepts only `bid` and `status` fields. You cannot include `text` or `matchType` in an update request. The schema does not accept these fields.

##### Example

```json
{
  "bid": {
    "amount": "2.50",
    "currency": "USD"
  },
  "status": "ENABLED"
}
```

## Topics

### Type Aliases
- [type KeywordUpdate.Status](keywordupdate/status-data.typealias.md)
  Whether this keyword should be active and eligible to serve after the update.

## Properties

- `bid` (Money): Per-keyword bid override as a `Money` object. See [`Money`](money.md). Must be a valid `Money` value. `null` is not accepted and returns an error. Mutable.
- `status` (KeywordUpdate.Status): Whether this keyword is active and eligible to serve. Values: `ENABLED` or `PAUSED`. See [`KeywordStatus`](keywordstatus.md). Mutable.

## See Also

- [object Keyword](keyword.md)
  The targeting unit that connects a user’s App Store search query to an ad group’s ads.
- [object KeywordCreate](keywordcreate.md)
  The request body for creating a new Keyword object.
- [object KeywordResponse](keywordresponse.md)
  The response object for a Keyword operation.
- [object KeywordQueryResponse](keywordqueryresponse.md)
  The response object for a Keyword query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordupdate)*