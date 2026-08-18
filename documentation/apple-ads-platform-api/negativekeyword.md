# NegativeKeyword

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A keyword exclusion that prevents ads from showing when a search query matches the excluded term.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object NegativeKeyword
```

#### Discussion

A `NegativeKeyword` prevents ads from showing when a search query matches the excluded term.

- `EXACT` match negatives block only searches that precisely match the term.
- `BROAD` match negatives block a wider range of related queries.
- `PHRASE` match negatives block Apple Maps searches that match the term and close variants.

Pausing a negative keyword (`status: PAUSED`) temporarily re-enables traffic from that term without permanently removing the exclusion. A `deleted` negative keyword is soft-deleted and excluded from serving but remains accessible in query results.

You can use fields marked **Filterable** in the dictionary keys as filter criteria in query endpoint requests. See [`Calling the Apple Ads Platform API`](calling-apple-ads-platform-api.md) for details on constructing queries.

##### Example

```json
{
  "id": 777888999,
  "adAccountId": 123456789,
  "campaignId": 444555666,
  "text": "free app",
  "matchType": "BROAD",
  "status": "ENABLED",
  "creationTime": "2025-01-10T08:00:00.000",
  "modificationTime": "2025-01-10T08:00:00.000",
  "deleted": false
}
```

## Topics

### Type Aliases
- [type NegativeKeyword.MatchType](negativekeyword/matchtype-data.typealias.md)
  The matching behavior used to compare this negative keyword against user search queries.
- [type NegativeKeyword.Status](negativekeyword/status-data.typealias.md)
  Advertiser-configurable active state for this negative keyword.

## Properties

- `adAccountId` (int64): The ad account this negative keyword belongs to. Informational. Read-only.
- `campaignId` (int64): The campaign ID. Negative keywords can be defined at campaign or ad group level. Filterable (`EQUALS`). Immutable after creation.
- `adGroupId` (int64): The ad group this negative keyword belongs to. Null if defined at campaign level. Filterable (`EQUALS`, `IN`, `IS_NULL`, `IS_NOT_NULL`, `NOT_EQUALS`). Immutable after creation.
- `text` (string): The original advertiser-given keyword text. Filterable (`EQUALS`, `STARTS_WITH`). Immutable after creation.
- `matchType` (NegativeKeyword.MatchType): Match type for this negative keyword. The schema accepts all four `KeywordMatchType` values (`EXACT`, `BROAD`, `PHRASE`, `CATEGORY`). In practice, `EXACT` and `BROAD` apply to App Store negatives and `PHRASE` applies to Apple Maps negatives. `CATEGORY` is not supported for negative keywords. See [`KeywordMatchType`](keywordmatchtype.md). Filterable (`EQUALS`, `IN`). Immutable after creation.
- `status` (NegativeKeyword.Status): Whether the negative keyword is active or paused. See [`NegativeKeywordStatus`](negativekeywordstatus.md). Filterable (`EQUALS`, `IN`). Mutable.
- `id` (int64): System-assigned unique identifier. Read-only.
- `creationTime` (date-time): Timestamp when the negative keyword was created. Read-only.
- `modificationTime` (date-time): Timestamp of the last modification. Read-only.
- `deleted` (boolean): Whether the negative keyword has been deleted. Read-only.

## See Also

- [object NegativeKeywordCreate](negativekeywordcreate.md)
  The request body for creating a new negative keyword.
- [object NegativeKeywordUpdate](negativekeywordupdate.md)
  The request body for updating an existing negative keyword.
- [object NegativeKeywordResponse](negativekeywordresponse.md)
  The response object for a negative keyword operation.
- [object NegativeKeywordQueryResponse](negativekeywordqueryresponse.md)
  The response object for a negative keyword query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/negativekeyword)*