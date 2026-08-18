# ImpressionShareTimeRange

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Time range for impression share queries.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ImpressionShareTimeRange
```

#### Discussion

`ImpressionShareTimeRange` specifies the date window and granularity for an impression share report.

##### Example

```json
{
  "start": "2025-01-01",
  "end": "2025-01-30",
  "timeZone": "UTC",
  "granularity": "DAILY"
}
```

## Properties

- `start` (date) *(required)*: Start date in YYYY-MM-DD format. When `granularity` is `WEEKLY_SUN_SAT`, this date must be a Sunday.
- `end` (date) *(required)*: End date in YYYY-MM-DD format.
- `timeZone` (string): Timezone. Fixed to `UTC`. Not user-configurable. Default: `"UTC"`.
- `granularity` (string) *(required)*: Aggregation period. `DAILY` aggregates per day, with a maximum window of 30 days (inclusive), and populates the `day` field (not the `week` field) in each row. `WEEKLY_SUN_SAT` aggregates per Sunday-to-Saturday week, with a maximum window of 4 weeks (`LAST_4_WEEK`), and populates the `week` field (not the `day` field) with the Sunday start date. The `start` date must be a Sunday. Possible values: `DAILY`, `WEEKLY_SUN_SAT`.

## See Also

- [object ImpressionShareQueryRequest](impressionsharequeryrequest.md)
  Request body for the impression share query endpoint.
- [object ImpressionShareQueryResponse](impressionsharequeryresponse.md)
  The impression share query endpoint returns this response wrapper.
- [object ImpressionShareRow](impressionsharerow.md)
  A single impression share data row.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/impressionsharetimerange)*