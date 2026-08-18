# SearchTermPopularityRow

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A single search term popularity data row.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object SearchTermPopularityRow
```

#### Discussion

Each `SearchTermPopularityRow` represents one combination of time period, country or region, genre, and search term in a search term popularity report. The date field present depends on the granularity in [`SearchTermPopularityTimeRange`](searchtermpopularitytimerange.md): `week` for `WEEKLY_SUN_SAT`, `month` for `MONTHLY`.

##### Popularity Metrics

The response provides three popularity scales, each scoped differently.

##### Example

```json
{
  "week": "2025-01-05",
  "countryOrRegion": "US",
  "genre": "GAMES",
  "searchTerm": "awayfinder",
  "rankInGenre": 42,
  "searchPopularityInGenre": 78,
  "searchPopularity1to100": 65,
  "searchPopularity1to5": 4
}
```

## Properties

- `week` (date): The start date of the completed weekly range in YYYY-MM-DD format. Present when granularity is `WEEKLY_SUN_SAT`. Read-only.
- `month` (string): Calendar month of the report snapshot in YYYY-MM format. Present when granularity is `MONTHLY`. Read-only.
- `countryOrRegion` (string): ISO 3166-1 alpha-2 country or region code. Read-only.
- `genre` (string): App Store genre classification. Read-only.
- `searchTerm` (string): The search term. Only terms meeting eligibility criteria (≥ 500 searches) are included. Read-only.
- `rankInGenre` (integer): Rank of the search term by search volume within its country/region and genre. Rank `1` = highest volume. Up to 500 search terms per country/genre combination. Read-only.
- `searchPopularityInGenre` (integer): Popularity within country/region and genre on a 1–100 scale. `100` = most popular within that genre. Read-only.
- `searchPopularity1to100` (integer): Popularity score on a 1–100 scale across all genres within the country or region. `100` = most popular overall. Use to compare a term’s in-genre popularity against its market-wide popularity. Read-only.
- `searchPopularity1to5` (integer): Popularity across all genres within country/region on a 1–5 scale. `5` = most popular. Matches the Search Popularity metric displayed in Campaign Management. Read-only.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/searchtermpopularityrow)*