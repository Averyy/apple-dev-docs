# Apple Ads Campaign Management API 5

**Framework**: Apple Ads

Learn about changes to Apple Ads Campaign Management API 5.

#### Overview

API 5 is the current version.

##### 54

Released in December, 2025

- New reporting metrics have been added to support App Store preorders: `tapPreOrdersPlaced`, `viewPreOrdersPlaced` and `totalPreOrdersPlaced`. See [`SpendRow`](spendrow.md) and [`ExtendedSpendRow`](extendedspendrow.md) for descriptions.

##### 53

Released in August, 2025.

- The [`Create a Budget Order`](create-a-budget-order.md) endpoint no longer supports a single placement type. All responses to API requests you make to create new budget orders contain all possible values for [`SupplySource`](supplysource.md).

##### 521

Released in May, 2025.

- The [`Create a Campaign`](create-a-campaign.md) endpoint supports an optional `budgetAmount` to manage the total budget of a campaign. You can only add a `budgetAmount` at the time of campaign creation. You can’t update a campaign to use `budgetAmount`. For more information, see [`Campaign`](campaign.md).

##### 52

Released in March, 2025.

- Added endpoints to retrieve app details and localized app details. See [`Get App Details`](get-app-details.md) and [`Get Localized App Details`](get-localized-app-details.md).
- `APPSTORE_SEARCH_TAB` campaigns require that you [`Create a Creative`](create-a-creative.md) using either a default product page or a custom product page as the tap destination. As of API version 5.2, you need to create a default product page ad to use with `APPSTORE_SEARCH_TAB` campaigns. At the release of API version 5.2 Apple automatically creates a default product page ad for all existing, running `APPSTORE_SEARCH_TAB` campaigns. See also [`CreativeType`](creativetype.md).
- The [`Find App Assets`](find-app-assets.md) endpoint now supports default product page ads. The [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md) endpoint now supports rejection reasons related to default product pages and product page optimization.
- Added support to use custom product pages as an ad’s tap destination. `APPSTORE_SEARCH_TAB` ad-level metrics are reported through [`Get Ad-Level Reports`](get-ad-level-reports.md). Historical ad-level metrics (before API version 5.2 release) are reported against `adId=-1`. For ad-level metrics after API version 5.2 release, all default product page ads are reported against a new, real `adID` in reporting payloads.
- `APPSTORE_SEARCH_TAB` campaigns can optionally include a deep link. See [`ProductPageDetail`](productpagedetail.md).

##### 51

Released in October, 2024.

- A read-only `deepLink` field has been added to the [`ProductPageDetail`](productpagedetail.md) response. Advertisers can add deep links to custom product pages through [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com). Retrieve your product page metadata with [`Get Product Pages`](get-product-pages.md) and [`Get Product Pages by Identifier`](get-product-pages-by-identifier.md) endpoints. Deep links are available on iOS 18 and later for Today tab and search results ads, and iPadOS 18 and later for search results ads.
- A correction has been made to the [`Find Ad Groups`](find-ad-groups.md) endpoint. The selector [`Condition`](condition.md) operator accepts only EQUALS in requests.

##### 50

Released in May, 2024.

- View-through reporting metrics provide details on Apple Search Ads campaign performance. Installs, new downloads, and redownloads are available as a standalone total, tap-through, and view-through. All reports reflect the new metrics. See [`SpendRow`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_ads/spendrow) and [`ExtendedSpendRow`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_ads/extendedspendrow).
- Get Keyword-Level Reports and Get Keyword-Level within Ad Group Reports reflect a new suggestedBidAmount field, replacing deprecated `bidMin` and `bidMax` fields. See [`KeywordBidRecommendation`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_ads/keywordbidrecommendation).
- Get [`Search Term-Level Reports`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_ads/gets-reports-on-search-terms-within-a-campaign.-the-information-per-campaign-is-composed-of-the-metrics,-dimensions-requested-in-the-request-parameter) and [`Get Search Term-Level within Ad Group Reports`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_ads/gets-reports-on-targeting-searchterm-within-a-adgroup.-the-information-per-adgroup-is-composed-of-the-metrics,-dimensions-requested-in-the-request-parameter) require the timezone to be ORTZ.

Other new features include:

- Prior to API 5, new campaigns required a `dailyBudgetAmount` or a `budgetAmount`, or both. A `dailyBudgetAmount` is now a required field for all new campaigns. See [`Create a campaign`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_ads/creates-a-campaign).
- Multiple default languages are supported for [`countries or regions`](https://developer.apple.comhttps://developer.apple.com/documentation/apple_ads/countryorregion).

Deprecations:

All [`Creative Sets`](creative-sets.md) endpoints are deprecated and unavailable in API 5.

## See Also

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)
  Learn about changes to Apple Ads Campaign Management API 4.
- [Apple Ads Campaign Management API 3](apple-search-ads-campaign-management-api-3.md)
  Apple no longer supports this API.
- [Apple Ads Campaign Management API 2](apple-search-ads-campaign-management-api-2.md)
  Apple no longer supports this API.
- [Apple Ads Campaign Management API 1](apple-search-ads-campaign-management-api-1.md)
  Apple no longer supports this API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/apple-search-ads-campaign-management-api-5)*