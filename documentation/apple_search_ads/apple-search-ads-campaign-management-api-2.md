# Apple Search Ads Campaign Management API 2

**Framework**: Apple Search Ads

Apple no longer supports this API.

#### Overview

> **Note**:  As of February 2021, Apple no longer supports the Apple Search Ads Campaign Management API 2. A 301 RESOURCE_MOVED_PERMANENTLY error occurs if you use an API 2 endpoint. API usage requires version 3 or later.

The Apple Search Ads API 2 broadens international support by allowing advertisers to include multiple countries or regions within a single campaign.

API 2 campaigns aren’t compatible with API 3 resources, however, API 2 reports are forward-compatible. Negative keywords and ad groups were decoupled from the campaign object. Negative keywords and targeting keywords were decoupled from ad groups.

The API now represents App Store territories as follows:

Report field changes are as follows:

|  |  |
| --- | --- |
| `installs` | `conversions` |
| `latOnInstalls` | `conversionsLATOn` |
| `latOffInstalls` | `conversionsLATOff` |
| `newDownloads` | `conversionsNewDownloads` |
| `redownloads` | `conversionsRedownloads` |

See [`ExtendedSpendRow`](extendedspendrow.md) and [`SpendRow`](spendrow.md) for field descriptions.

API 2 includes the following new features for [`Creative Sets`](creative-sets.md):

- Creating new Creative Sets and linking to an ad group.
- Reassigning Creative Sets to an ad group.
- Retrieving associated app assets for Creative Sets in campaigns.
- Deleting associated Creative Sets for ad groups.

The following Apple Search Ads Campaign Management API 1 fields are no longer in the corresponding API object and don’t apply to API 2 and later:

## See Also

- [Apple Search Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)
  Learn about changes to Apple Search Ads Campaign Management API 5.
- [Apple Search Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)
  Learn about changes to Apple Search Ads Campaign Management API 4.
- [Apple Search Ads Campaign Management API 3](apple-search-ads-campaign-management-api-3.md)
  Apple no longer supports this API.
- [Apple Search Ads Campaign Management API 1](apple-search-ads-campaign-management-api-1.md)
  Apple no longer supports this API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/apple-search-ads-campaign-management-api-2)*