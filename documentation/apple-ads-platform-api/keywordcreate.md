# KeywordCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for creating a new Keyword object.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object KeywordCreate
```

#### Discussion

`KeywordCreate` is the request payload for adding a keyword to an ad group via `POST /v1/keywords`, after the ad group has already been created. `AdGroupCreate` doesn’t support keywords inline. See the properties below for field-level requirements, mutability, and defaults.

##### Example

```json
{
  "adGroupId": 555666777,
  "text": "photo editor",
  "matchType": "EXACT",
  "bid": {
    "amount": "2.50",
    "currency": "USD"
  },
  "status": "ENABLED"
}
```

## Topics

### Type Aliases
- [type KeywordCreate.MatchType](keywordcreate/matchtype-data.typealias.md)
  The matching behavior to use when creating this keyword.
- [type KeywordCreate.Status](keywordcreate/status-data.typealias.md)
  Whether this keyword is active and eligible to serve at creation.

## Properties

- `adGroupId` (int64) *(required)*: The ad group this keyword targets.
- `text` (string) *(required)*: The keyword text as entered by the advertiser. Cannot be changed after creation. To change it, delete the keyword and create a new one.
- `matchType` (KeywordCreate.MatchType): The match type for this keyword. Values: `EXACT`, `BROAD`, `PHRASE`, `CATEGORY`. See [`KeywordMatchType`](keywordmatchtype.md). Immutable after creation. To change it, delete the keyword and create a new one.
- `bid` (Money): Per-keyword bid override as a `Money` object. See [`Money`](money.md). Overrides the ad group default bid. Omit or pass `null` to default to the ad group’s `BidStrategy` bid. Not used with Maximize Conversions bid strategy campaigns.
- `status` (KeywordCreate.Status): Whether this keyword is active and eligible to serve. Values: `ENABLED`, `PAUSED`. See [`KeywordStatus`](keywordstatus.md).

## See Also

- [object Keyword](keyword.md)
  The targeting unit that connects a user’s App Store search query to an ad group’s ads.
- [object KeywordUpdate](keywordupdate.md)
  The request body for updating an existing Keyword object.
- [object KeywordResponse](keywordresponse.md)
  The response object for a Keyword operation.
- [object KeywordQueryResponse](keywordqueryresponse.md)
  The response object for a Keyword query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordcreate)*