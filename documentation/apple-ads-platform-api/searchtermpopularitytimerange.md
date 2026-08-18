# SearchTermPopularityTimeRange

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Time range for search term popularity queries.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SearchTermPopularityTimeRange
```

#### Discussion

`SearchTermPopularityTimeRange` specifies the date window and granularity for a search term popularity report. Date format and retention period differ by granularity.

> **Note**: **Note:** For `MONTHLY` granularity, the response truncates the date field to `YYYY-MM`.

##### Example

```json
{
  "start": "2025-01-01",
  "end": "2025-03-31",
  "timeZone": "UTC",
  "granularity": "MONTHLY"
}
```

## Properties

- `start` (string) *(required)*: The start date of the range, in `YYYY-MM-DD` format.
- `end` (string) *(required)*: The end date of the range, in `YYYY-MM-DD` format.
- `timeZone` (string): Timezone. Fixed to `UTC`. Not user-configurable. Default: `"UTC"`.
- `granularity` (string) *(required)*: Aggregation period. `WEEKLY_SUN_SAT` uses fixed Sunday–Saturday weeks and is generated Mondays at 07:00 UTC for the preceding Sunday through Saturday week, with a rolling retention of 65 weeks. `MONTHLY` uses calendar months and is refreshed on the 5th of each month UTC for the prior calendar month, with a rolling retention of 15 months. Possible values: `WEEKLY_SUN_SAT`, `MONTHLY`.

## See Also

- [object ImpressionShareQueryRequest](impressionsharequeryrequest.md)
  Request body for the impression share query endpoint.
- [object ImpressionShareQueryResponse](impressionsharequeryresponse.md)
  The impression share query endpoint returns this response wrapper.
- [object ImpressionShareRow](impressionsharerow.md)
  A single impression share data row.
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
- [object ImpressionShareResultContainer](impressionshareresultcontainer.md)
  Container holding the array of impression share rows a query returns.
- [object SearchTermPopularityResultContainer](searchtermpopularityresultcontainer.md)
  Container holding the array of search term popularity rows a query returns.
- [object KeywordInsights](keywordinsights.md)
  Insights for keyword reporting rows.
- [object ReportingKeywordBidRecommendation](reportingkeywordbidrecommendation.md)
  Keyword bid recommendation details, including a suggested bid amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/searchtermpopularitytimerange)*