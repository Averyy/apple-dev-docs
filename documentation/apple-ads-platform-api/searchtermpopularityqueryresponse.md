# SearchTermPopularityQueryResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A response wrapper for search term popularity query results.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
object SearchTermPopularityQueryResponse
```

#### Discussion

Each row in `result.rows` always includes the following dimension fields:

| Field | Description |
| --- | --- |
| `countryOrRegion` | The App Store country or region for the search volume data |
| `genre` | The App Store genre category |
| `searchTerm` | The search term text |
| `week` or `month` | The date field corresponding to the selected granularity |

Rows include the following dimension fields only when requested via the request’s `fields` array.

| Field | Description |
| --- | --- |
| `rankInGenre` | The search term’s rank by volume within the genre of the given App Store country or region. |
| `searchPopularityInGenre` | Relative popularity score within the genre (1–100) of the given App Store country or region. |
| `searchPopularity1to100` | Popularity score on a 1–100 scale across all genres within the country or region with `100` = most popular overall |
| `searchPopularity1to5` | Relative popularity on a 1–5 scale across all genres of the given App Store country or region. |

See [`SearchTermPopularityRow`](searchtermpopularityrow.md) for field descriptions.

##### Example

```json
{
  "result": {
    "rows": [
      {
        "week": "2025-01-05",
        "countryOrRegion": "US",
        "genre": "PRODUCTIVITY_UTILITIES",
        "searchTerm": "task manager",
        "rankInGenre": 1,
        "searchPopularityInGenre": 95,
        "searchPopularity1to100": 88,
        "searchPopularity1to5": 5
      }
    ]
  },
  "pagination": {
    "offset": 0,
    "pageSize": 20,
    "totalCount": 1
  }
}
```

## Properties

- `result` (SearchTermPopularityResultContainer): Container object holding the matching rows. Contains a `rows` array of [`SearchTermPopularityRow`](searchtermpopularityrow.md) objects. See [`SearchTermPopularityResultContainer`](searchtermpopularityresultcontainer.md). Read-only.
- `pagination` (ResponsePagination): Pagination metadata for the current result page, including `offset`, `pageSize`, and `totalCount` for retrieving subsequent pages. Read-only.
- `error` (Error): See [`Error`](error.md) for details. Read-only.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/searchtermpopularityqueryresponse)*