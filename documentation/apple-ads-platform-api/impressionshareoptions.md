# ImpressionShareOptions

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Report options for impression share queries.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ImpressionShareOptions
```

#### Discussion

`ImpressionShareOptions` controls how a query aggregates impression share data. Set `impressionShareReportType` in the `options` field of an [`ImpressionShareQueryRequest`](impressionsharequeryrequest.md) to choose between first-slot-only or all-slots data.

##### Example

```json
{
  "impressionShareReportType": "ALL_SLOTS"
}
```

## Properties

- `impressionShareReportType` (string): The ad position scope for impression share metrics. `FIRST_SLOT` (default): Impression share and metrics for the top ad position only. `ALL_SLOTS`: Impression share and metrics aggregated across all ad positions. Default: `"FIRST_SLOT"`.

## See Also

- [object ImpressionShareQueryRequest](impressionsharequeryrequest.md)
  Request body for the impression share query endpoint.
- [object ImpressionShareQueryResponse](impressionsharequeryresponse.md)
  The impression share query endpoint returns this response wrapper.
- [object ImpressionShareRow](impressionsharerow.md)
  A single impression share data row.
- [object ImpressionShareTimeRange](impressionsharetimerange.md)
  Time range for impression share queries.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/impressionshareoptions)*