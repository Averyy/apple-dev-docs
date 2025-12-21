# Get Ad Group-Level Reports

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches reports for ad groups within a campaign.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to fetch reports for your ad groups in campaigns. See [`ReportingAdGroup`](reportingadgroup.md) for [`Condition`](condition.md) operators and field values to filter results with an object [`Selector`](selector.md). See the `groupBy` parameter description in the [`ReportingRequest`](reportingrequest.md) for supported values per targeting dimension. The `orderBy` [`Selector`](selector.md) specifies fields to sort the records list by `ASCENDING` or `DESCENDING`. All [`ReportingAdGroup`](reportingadgroup.md) fields are available to the `orderBy` [`Selector`](selector.md) except `adGroupServingStateReasons`.

##### Payload Example 1 Ad Group Level Reports

##### Payload Example 2 Ad Group Level Reports

## Request Body

The report request body consisting of metrics and dimensions to use as filters.

## See Also

- [Get Campaign-Level Reports](get-campaign-level-reports.md)
  Fetches reports for campaigns.
- [Get Keyword-Level Reports](get-keyword-level-reports.md)
  Fetches reports for targeting keywords within a campaign.
- [Get Keyword-Level within Ad Group Reports](get-keyword-level-within-ad-group-reports.md)
  Fetches reports for targeting keywords within an ad group.
- [Get Search Term-Level Reports](get-search-term-level-reports.md)
  Fetches reports for search terms within a campaign.
- [Get Search Term-Level within Ad Group Reports](get-search-term-level-within-ad-group-reports.md)
  Fetches reports for search terms within an ad group.
- [Get Ad-Level Reports](get-ad-level-reports.md)
  Fetches ad performance data within a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-ad-group-level-reports)*