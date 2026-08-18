# Keyword

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The targeting unit that connects a user’s App Store search query to an ad group’s ads.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Keyword
```

#### Discussion

A `Keyword` is the targeting unit that connects a user’s App Store search query to an ad group’s ads. Each keyword belongs to a single ad group and inherits the ad group’s default bid unless you set a bid in the keyword’s `bid` field. The `text` and `matchType` fields are immutable after creation. To change them, delete the keyword and create a new one.

- `BROAD` match serves ads when a user’s search term contains the keyword or close variants, maximizing reach.
- `EXACT` match restricts delivery to searches that precisely match the keyword, giving tighter control over targeting and spend.
- `PHRASE` match allows flexibility while staying focused on the keyword’s intent.
- `CATEGORY` match targets based on the Maps business category associated with the keyword.

Pausing a keyword via `status` halts delivery without deleting the object, preserving historical performance data. A `deleted` keyword is soft-deleted and excluded from serving but remains queryable.

You can use fields marked **Filterable** in the dictionary keys as filter criteria in query endpoint requests. See [`Calling the Apple Ads Platform API`](calling-apple-ads-platform-api.md) for details on constructing queries.

##### Example

```json
{
  "adAccountId": 123456789,
  "campaignId": 987654321,
  "adGroupId": 555666777,
  "text": "awayfinder travel app",
  "matchType": "EXACT",
  "bid": {
    "amount": "2.50",
    "currency": "USD"
  },
  "status": "ENABLED",
  "id": 111222333,
  "creationTime": "2025-01-10T08:00:00.000",
  "modificationTime": "2025-01-12T09:30:00.000",
  "deleted": false,
  "displayStatus": "RUNNING"
}
```

## Topics

### Type Aliases
- [type Keyword.DisplayStatus](keyword/displaystatus-data.typealias.md)
  Rolled-up delivery state for a keyword, combining advertiser settings and parent entity status.
- [type Keyword.MatchType](keyword/matchtype-data.typealias.md)
  The matching behavior used to compare this keyword against user search queries.
- [type Keyword.Status](keyword/status-data.typealias.md)
  Advertiser-configurable serving state for this keyword.

## Properties

- `adAccountId` (int64): The ad account this keyword belongs to. Informational. Read-only.
- `campaignId` (int64): The campaign ID of the parent campaign for this keyword. Informational. Filterable (`EQUALS`). Read-only.
- `adGroupId` (int64): The ad group this keyword belongs to. Filterable (`EQUALS`, `IN`). Immutable after creation.
- `text` (string): The original advertiser-given keyword text. Filterable (`EQUALS`, `STARTS_WITH`). Immutable after creation.
- `matchType` (Keyword.MatchType): Keyword match type. Values: `EXACT`, `BROAD`, `PHRASE`, `CATEGORY`. See [`KeywordMatchType`](keywordmatchtype.md). Filterable (`EQUALS`, `IN`). Immutable after creation.
- `bid` (Money): Keyword bid amount override. Overrides the ad group default bid. On create, omit or pass `null` to default to the ad group’s bid strategy. On update, `bid` must be a valid `Money` object. `null` returns an error. Not used with Maximize Conversions bid strategy campaigns. See [`Money`](money.md). Mutable.
- `status` (Keyword.Status): Whether the keyword is active and eligible to serve. See [`KeywordStatus`](keywordstatus.md). Filterable (`EQUALS`, `IN`). Mutable.
- `id` (int64): The unique identifier for this keyword. Filterable (`EQUALS`, `IN`). Read-only.
- `creationTime` (date-time): Timestamp when the keyword was created. Read-only.
- `modificationTime` (date-time): Timestamp of the last modification to the keyword. Read-only.
- `deleted` (boolean): Indicates if the keyword has been deleted. Filterable (`EQUALS`). Read-only.
- `displayStatus` (Keyword.DisplayStatus): The computed display status of the keyword, reflecting the combined state of the keyword, its ad group, and campaign. See [`KeywordDisplayStatus`](keyworddisplaystatus.md). Read-only.

## See Also

- [object KeywordCreate](keywordcreate.md)
  The request body for creating a new Keyword object.
- [object KeywordUpdate](keywordupdate.md)
  The request body for updating an existing Keyword object.
- [object KeywordResponse](keywordresponse.md)
  The response object for a Keyword operation.
- [object KeywordQueryResponse](keywordqueryresponse.md)
  The response object for a Keyword query, containing matched results and pagination metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keyword)*