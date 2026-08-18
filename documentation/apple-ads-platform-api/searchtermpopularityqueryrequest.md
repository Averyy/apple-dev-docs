# SearchTermPopularityQueryRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request body for the search term popularity query endpoint.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SearchTermPopularityQueryRequest
```

#### Discussion

`SearchTermPopularityQueryRequest` is the request body for the search term popularity endpoint. Timezone is fixed to UTC.

To scope results to specific countries or genres, use `filters`. `timeRange` is required and specifies the date window to query.

##### Example

```json
{
  "fields": [
    "rankInGenre",
    "searchPopularityInGenre",
    "searchPopularity1to100",
    "searchPopularity1to5"
  ],
  "filters": [
    {
      "field": "countryOrRegion",
      "operator": "EQUALS",
      "value": "US"
    },
    {
      "field": "genre",
      "operator": "EQUALS",
      "value": "PRODUCTIVITY_UTILITIES"
    }
  ],
  "sorting": [
    {
      "field": "rankInGenre",
      "order": "ASC"
    }
  ],
  "timeRange": {
    "start": "2025-01-05",
    "end": "2025-01-11",
    "granularity": "WEEKLY_SUN_SAT"
  },
  "pagination": {
    "offset": 0,
    "pageSize": 20
  }
}
```

## Properties

- `filters` ([Filter]): Filter conditions to narrow results. Genre values are free-text strings matching App Store genre names (e.g., `PRODUCTIVITY_UTILITIES`, `TRAVEL`). There is no fixed enum of allowed values.
- `sorting` ([Sorting]): Sort criteria. Maximum 2 sort fields. Default genre ASC, rankInGenre ASC.
- `timeRange` (SearchTermPopularityTimeRange) *(required)*: See [`SearchTermPopularityTimeRange`](searchtermpopularitytimerange.md) for details.
- `pagination` (RequestPagination): See [`RequestPagination`](requestpagination.md) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/searchtermpopularityqueryrequest)*