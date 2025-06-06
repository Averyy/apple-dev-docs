# Get Search Term-Level Reports

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Fetches reports for search terms within a campaign.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Search Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to fetch reports for search terms in your campaigns. See [`ReportingSearchTerm`](reportingsearchterm.md) for [`Condition`](condition.md) operators and field values to filter results with a [`Selector`](selector.md).

The limit for search term-level reports is 10 impressions. Search term-level reports only support a `timeZone` value of `ORTZ`. The `orderBy` [`Selector`](selector.md) specifies fields to sort the records list by `ASCENDING` or `DESCENDING`. All [`ReportingSearchTerm`](reportingsearchterm.md) fields are available to the `orderBy` [`Selector`](selector.md).

##### Payload Example Get Search Term Level Reports

## Request Body

The report request body consisting of metrics and dimensions to use as filters.

## See Also

- [Get Campaign-Level Reports](get-campaign-level-reports.md)
  Fetches reports for campaigns.
- [Get Ad Group-Level Reports](get-ad-group-level-reports.md)
  Fetches reports for ad groups within a campaign.
- [Get Keyword-Level Reports](get-keyword-level-reports.md)
  Fetches reports for targeting keywords within a campaign.
- [Get Keyword-Level within Ad Group Reports](get-keyword-level-within-ad-group-reports.md)
  Fetches reports for targeting keywords within an ad group.
- [Get Search Term-Level within Ad Group Reports](get-search-term-level-within-ad-group-reports.md)
  Fetches reports for search terms within an ad group.
- [Get Ad-Level Reports](get-ad-level-reports.md)
  Fetches ad performance data within a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/get-search-term-level-reports)*