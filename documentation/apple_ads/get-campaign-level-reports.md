# Get Campaign-Level Reports

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches reports for campaigns.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 3](apple-search-ads-campaign-management-api-3.md)
- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to fetch reports for your campaigns. See [`ReportingCampaign`](reportingcampaign.md) and [`CampaignAppDetail`](campaignappdetail.md) for [`Condition`](condition.md) operators and field values to filter results with a [`Selector`](selector.md).

See the `groupBy` parameter description in the [`ReportingRequest`](reportingrequest.md) for supported values per targeting dimension.

The `orderBy` [`Selector`](selector.md) specifies fields to sort the records list by `ASCENDING` or `DESCENDING`. All [`ReportingCampaign`](reportingcampaign.md) fields are available to the `orderBy` [`Selector`](selector.md) except `servingStateReasons`, `app`, `app:{appName}`, and `app:{adamId}`.

##### Payload Example 1 Get Campaign Level Reports

##### Payload Example 2 Get Campaign Level Reports

##### Payload Example 3 Get Campaign Level Reports with Granularity

## Request Body

The report request body consisting of metrics and dimensions to use as filters.

## See Also

- [Get Ad Group-Level Reports](get-ad-group-level-reports.md)
  Fetches reports for ad groups within a campaign.
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

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-campaign-level-reports)*