# ImpressionShareQueryRequest

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Request body for the impression share query endpoint.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object ImpressionShareQueryRequest
```

#### Discussion

`ImpressionShareQueryRequest` is the request body for the impression share endpoint. Timezone is fixed to UTC.

`timeRange` specifies the date window to query. `options` allows additional configuration of the impression share calculation.

##### Example

```json
{
  "fields": [],
  "filters": [
    {
      "field": "promotedObjectId",
      "operator": "EQUALS",
      "value": "123456789"
    },
    {
      "field": "countryOrRegion",
      "operator": "EQUALS",
      "value": "US"
    }
  ],
  "sorting": [
    {
      "field": "highImpressionShare",
      "order": "DESC"
    }
  ],
  "timeRange": {
    "start": "2025-01-01",
    "end": "2025-01-07",
    "timeZone": "UTC",
    "granularity": "DAILY"
  },
  "pagination": {
    "offset": 0,
    "pageSize": 20
  },
  "options": {
    "impressionShareReportType": "FIRST_SLOT"
  }
}
```

## Properties

- `filters` ([Filter]) *(required)*: Filter conditions. A filter on `promotedObjectId` is required. Omitting it will result in a 400 error.
- `sorting` ([Sorting]): Sort criteria. Maximum 2 sort fields.
- `timeRange` (ImpressionShareTimeRange) *(required)*: See [`ImpressionShareTimeRange`](impressionsharetimerange.md) for details.
- `pagination` (RequestPagination): Pagination controls. Default `pageSize` is `100`. Maximum `pageSize` is `5000`. See [`RequestPagination`](requestpagination.md) for details.
- `options` (ImpressionShareOptions): See [`ImpressionShareOptions`](impressionshareoptions.md) for details.

## See Also

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
- [object KeywordInsights](keywordinsights.md)
  Insights for keyword reporting rows.
- [object ReportingKeywordBidRecommendation](reportingkeywordbidrecommendation.md)
  Keyword bid recommendation details, including a suggested bid amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/impressionsharequeryrequest)*