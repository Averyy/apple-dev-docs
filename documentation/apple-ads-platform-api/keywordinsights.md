# KeywordInsights

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Insights for keyword reporting rows.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object KeywordInsights
```

#### Discussion

`KeywordInsights` provides performance insights attached to a keyword report row. Currently includes bid recommendation data.

##### Example

```json
{
  "bidRecommendation": {
    "suggestedBidAmount": 2.35
  }
}
```

## Properties

- `bidRecommendation` (ReportingKeywordBidRecommendation): Suggested bid information for this keyword. See [`ReportingKeywordBidRecommendation`](reportingkeywordbidrecommendation.md). Read-only.

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
- [object SearchTermPopularityTimeRange](searchtermpopularitytimerange.md)
  Time range for search term popularity queries.
- [object ImpressionShareResultContainer](impressionshareresultcontainer.md)
  Container holding the array of impression share rows a query returns.
- [object SearchTermPopularityResultContainer](searchtermpopularityresultcontainer.md)
  Container holding the array of search term popularity rows a query returns.
- [object ReportingKeywordBidRecommendation](reportingkeywordbidrecommendation.md)
  Keyword bid recommendation details, including a suggested bid amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/keywordinsights)*