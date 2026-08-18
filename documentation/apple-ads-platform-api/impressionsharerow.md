# ImpressionShareRow

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single impression share data row.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ImpressionShareRow
```

#### Discussion

Each `ImpressionShareRow` represents one combination of date, search term, and country or region in an impression share report. The date field present depends on the granularity chosen in [`ImpressionShareTimeRange`](impressionsharetimerange.md): `day` for `DAILY` granularity, `week` for `WEEKLY_SUN_SAT` granularity.

##### Impression Share Encoding

`lowImpressionShare` and `highImpressionShare` use a tiered encoding:

| Impression share | `lowImpressionShare` | `highImpressionShare` |
| --- | --- | --- |
| 0% | `0` | `0` |
| 1% – 90% | `x` (e.g. `0.23`) | `x` (same value) |
| 91% – 100% | `0.91` | `1` |

When both fields are equal and less than `0.91`, the value is a precise single-digit percentage. When `highImpressionShare` is `1`, the app holds more than 90% impression share for that term.

##### Example

```json
{
  "day": "2025-01-10",
  "appName": "AwayFinder",
  "promotedObjectId": "123456789",
  "countryOrRegion": "US",
  "searchTerm": "travel planner",
  "lowImpressionShare": 0.23,
  "highImpressionShare": 0.23,
  "rank": 1,
  "searchPopularity1to5": 4
}
```

## Properties

- `day` (date): Date in YYYY-MM-DD format. Present when granularity is `DAILY`. Read-only.
- `week` (date): Week start date (Sunday) in YYYY-MM-DD format. Present when granularity is `WEEKLY_SUN_SAT`. Read-only.
- `appName` (string): Display name of the promoted app. Read-only.
- `promotedObjectId` (string): The Adam ID (App Store app identifier) of the promoted app. Serialized as a JSON string representation of an int64. Read-only.
- `countryOrRegion` (string): ISO 3166-1 alpha-2 country or region code (e.g., `US`, `CA`, `GB`). Read-only.
- `searchTerm` (string): The search term. Privacy-filtered: suppressed for terms with fewer than 10 impressions. Read-only.
- `lowImpressionShare` (double): Lower bound of the app’s impression share (0–1). See encoding table above. Read-only.
- `highImpressionShare` (double): Upper bound of the app’s impression share (0–1). See encoding table above. Read-only.
- `rank` (integer): Stack-ranked position by impression share for this search term and country combination. Rank `1` = highest impression share. Read-only.
- `searchPopularity1to5` (integer): Relative search popularity for the search term on a 1–5 scale. `5` = most popular. Read-only.

## See Also

- [object ImpressionShareQueryRequest](impressionsharequeryrequest.md)
  Request body for the impression share query endpoint.
- [object ImpressionShareQueryResponse](impressionsharequeryresponse.md)
  The impression share query endpoint returns this response wrapper.
- [object ImpressionShareTimeRange](impressionsharetimerange.md)
  Time range for impression share queries.
- [object ImpressionShareOptions](impressionshareoptions.md)
  Report options for impression share queries.
- [object SearchTermPopularityQueryRequest](searchtermpopularityqueryrequest.md)
  Request body for the search term popularity query endpoint.
- [object SearchTermPopularityQueryResponse](searchtermpopularityqueryresponse.md)
  A response wrapper for search term popularity query results.
- [object SearchTermPopularityRow](searchtermpopularityrow.md)
  A single search term popularity data row.
- [object SearchTermPopularityTimeRange](searchtermpopularitytimerange.md)
  Time range for search term popularity queries.
- [object ImpressionShareResultContainer](impressionshareresultcontainer.md)
  Container holding the array of impression share rows a query returns.
- [object SearchTermPopularityResultContainer](searchtermpopularityresultcontainer.md)
  Container holding the array of search term popularity rows a query returns.
- [object KeywordInsights](keywordinsights.md)
  Insights for keyword reporting rows.
- [object ReportingKeywordBidRecommendation](reportingkeywordbidrecommendation.md)
  Keyword bid recommendation details, including a suggested bid amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/impressionsharerow)*