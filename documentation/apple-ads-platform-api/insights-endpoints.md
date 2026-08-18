# Insights Endpoints

**Framework**: Apple Ads Platform API

Query impression share and search term popularity data for your apps.

**Availability**:
- apple-ads-platform-api 1.0+

#### Overview

To look deeply into performance across your campaign group and identify growth opportunities, use the search term popularity and impression share APIs. Both endpoints apply only to App Store app campaigns (`promotedObjectType` `APPSTORE_APP`). Apple Maps (`BUSINESS_BRAND`) campaigns have no Insights equivalent.

#### Query the Available Endpoints

Query the following endpoints to retrieve insights data:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/insights/apps/impression-share/query` | Retrieves impression share data for the specified keywords and time range. See [`Impression Share Query`](query-app-impression-share-data.md). |
| `POST` | `/v1/insights/apps/search-term-popularity/query` | Retrieves search term popularity rankings by App Store country or region and genre. See [`Search Term Popularity Query`](query-app-search-term-popularity-data.md). |

##### Measure Impression Share

Impression share reports measure your share of available impressions relative to competitors for a given set of keywords or app categories. The report shows how often your ad appeared in any ad position for a specific search term, out of the total number of searches on that search term, in the same App Store country or region. Use impression share data to understand how competitive you are on a given search term and how much headroom exists to increase reach.

To retrieve impression share data, use `POST /v1/insights/apps/impression-share/query`. You must filter on `promotedObjectId`, or the request fails with a 400 error. The endpoint returns results synchronously with pagination. The following table lists the granularity options and limits for impression share queries:

| Field | Details |
| --- | --- |
| Granularity | `DAILY` or `WEEKLY_SUN_SAT` |
| `DAILY` max range | 30 days (inclusive) |
| `WEEKLY_SUN_SAT` max range | 4 weeks (`LAST_4_WEEK`) |
| Weekly start date | When `WEEKLY_SUN_SAT`, `timeRange.start` must be a Sunday |
| Timezone | Fixed to UTC |
| Maximum pageSize | 5000 |
| Maximum sort fields | 2 |

The `options.impressionShareReportType` field controls which ad positions the calculation includes:

| Report Type | Description |
| --- | --- |
| `FIRST_SLOT` | Measures impression share for the first ad position only. |
| `ALL_SLOTS` | Measures impression share aggregated across all ad positions. |

The `lowImpressionShare` and `highImpressionShare` fields use single-digit precision for values from 1–90% (both fields are equal). For values above 90%, both fields encode the 91–100% bucket (`0.91` / `1.0`) to avoid false precision near market saturation.

Each row also returns `rank` (the app’s stack-ranked position by impression share for that search term and country, `1` = highest) and `searchPopularity1to5` (relative search volume for the term, `5` = most popular).

##### Discover Search Term Popularity

Search term popularity reports show the relative ranking of search terms by volume within a given App Store country or region and genre. Use search term popularity data to discover high-volume search terms, understand seasonal trends, and prioritize keyword additions.

Use monthly and weekly search term popularity data to understand search volume trends and identify high-opportunity terms.

To retrieve search term popularity data, use `POST /v1/insights/apps/search-term-popularity/query`. This endpoint always uses UTC. The following table lists the granularity options and limits for search term popularity queries:

| Field | Details |
| --- | --- |
| Granularity | `WEEKLY_SUN_SAT` or `MONTHLY` |
| Timezone | Fixed to UTC |
| Maximum pageSize | 5000 |
| Maximum sort fields | 2 (default: `genre ASC`, `rankInGenre ASC`) |

The response always returns all dimension fields: `countryOrRegion`, `genre`, `searchTerm`, and the date field for the selected granularity (`week` or `month`). Request additional fields via the `fields` array:

| Optional Field | Description |
| --- | --- |
| `rankInGenre` | The search term’s rank by volume within the genre. |
| `searchPopularityInGenre` | Relative popularity score within the genre, on a 1–100 scale. |
| `searchPopularity1to100` | Popularity score on a 1–100 scale across all genres within the country or region. `100` = most popular overall. |
| `searchPopularity1to5` | Simplified popularity tier on a 1–5 scale. |

## Topics

- [Impression Share Query](query-app-impression-share-data.md)
  Retrieve impression share data showing how often your ads appear relative to total eligible impressions for a given search term and country.
- [Search Term Popularity Query](query-app-search-term-popularity-data.md)
  Retrieve the relative search volume ranking of search terms for a given App Store genre and country or region.

## See Also

- [Managing Reports](reports.md)
  Retrieve performance data for campaigns, ad groups, ads, keywords, and search terms.
- [Recommendations Endpoints](recommendations-endpoints.md)
  Endpoints for querying, applying, and dismissing budget and Target CPA recommendations.
- [Suggestions Endpoints](suggestions-endpoints.md)
  Endpoints for querying keyword, phrase, category, and Target CPA suggestions.
- [Insights Data Objects](insights-data-objects.md)
  Build the request and response objects for impression share and search term popularity queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/insights-endpoints)*