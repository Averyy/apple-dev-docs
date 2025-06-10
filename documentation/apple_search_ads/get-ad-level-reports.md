# Get Ad-Level Reports

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Fetches ad performance data within a campaign.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Search Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)
- [Apple Search Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)

#### Discussion

Use this endpoint to return performance data for `ads` within your campaigns. The `orderBy` [`Selector`](selector.md) is required in ad-level report requests. See [`ReportingAd`](reportingad.md) to identify fields you can use with `orderBy`. To filter results, use selector [`Condition`](condition.md) operators and field values that the `ReportingAd` object specifies. You can only perform `GroupBy` on the [`CountryOrRegion`](countryorregion.md) field. See [`ReportingRequest`](reportingrequest.md).

Historical ad-level metrics for the `APPSTORE_SEARCH_TAB` placement from before API version 5.2 release are reported against `adId=-1`. For `APPSTORE_SEARCH_TAB` ad-level metrics after API version 5.2 release, all default product page ads are reported against a new, real `adId` in reporting payloads.

You can map your campaign installations by `adId` through the [`AdServices`](https://developer.apple.com/documentation/AdServices) attribution framework.

##### Payload Example Get Ad Level Reports

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
- [Get Search Term-Level Reports](get-search-term-level-reports.md)
  Fetches reports for search terms within a campaign.
- [Get Search Term-Level within Ad Group Reports](get-search-term-level-within-ad-group-reports.md)
  Fetches reports for search terms within an ad group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/get-ad-level-reports)*