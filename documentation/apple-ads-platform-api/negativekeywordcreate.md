# NegativeKeywordCreate

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The request body for creating a new negative keyword.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object NegativeKeywordCreate
```

#### Discussion

`NegativeKeywordCreate` is the request payload for adding a negative keyword to a campaign or ad group.

##### Example

```json
{
  "campaignId": 123456789,
  "text": "AwayFinder competitor app",
  "matchType": "PHRASE",
  "status": "ENABLED"
}
```

## Topics

### Type Aliases
- [type NegativeKeywordCreate.MatchType](negativekeywordcreate/matchtype-data.typealias.md)
  The matching behavior to use when creating this negative keyword.
- [type NegativeKeywordCreate.Status](negativekeywordcreate/status-data.typealias.md)
  Whether this negative keyword is active at creation.

## Properties

- `campaignId` (int64): Scopes this negative keyword to a specific campaign. Required for campaign-level negatives when calling `POST /v1/negative-keywords` directly. Must not be set for ad group-level negatives.
- `adGroupId` (int64): Scopes this negative keyword to a specific ad group. Required for ad group-level negatives when calling `POST /v1/negative-keywords` directly. Do not set `campaignId` when providing this field.
- `text` (string) *(required)*: The keyword text to exclude. Immutable after creation. To correct it, delete the existing record and create a new one.
- `matchType` (NegativeKeywordCreate.MatchType): The match type for this negative keyword. See [`KeywordMatchType`](keywordmatchtype.md). Defaults to `BROAD` if omitted. Immutable after creation.
- `status` (NegativeKeywordCreate.Status): Whether this negative keyword is active. See [`NegativeKeywordStatus`](negativekeywordstatus.md). Defaults to `ENABLED` if omitted.

## See Also

- [object NegativeKeyword](negativekeyword.md)
  A keyword exclusion that prevents ads from showing when a search query matches the excluded term.
- [object NegativeKeywordUpdate](negativekeywordupdate.md)
  The request body for updating an existing negative keyword.
- [object NegativeKeywordResponse](negativekeywordresponse.md)
  The response object for a negative keyword operation.
- [object NegativeKeywordQueryResponse](negativekeywordqueryresponse.md)
  The response object for a negative keyword query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeywordcreate)*