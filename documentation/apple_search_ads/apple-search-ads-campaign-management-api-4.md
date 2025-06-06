# Apple Search Ads Campaign Management API 4

**Framework**: Apple Search Ads

Learn about changes to Apple Search Ads Campaign Management API 4.

#### Overview

API 4 calls are able to access resources created with [`Apple Search Ads Campaign Management API 5`](apple-search-ads-campaign-management-api-5.md).

##### 411

Released in April, 2024.

- Added guidance for suggested keyword bid amount to help you increase the likelihood of your ad showing in the App Store.  See [`KeywordBidRecommendation`](keywordbidrecommendation.md) for a summary of changes to [`Get Keyword-Level Reports`](get-keyword-level-reports.md).
- You can now create and update budget orders through the API.  Added two endpoints: [`Create a Budget Order`](create-a-budget-order.md) and [`Update a Budget Order`](update-a-budget-order.md). See [`Budget Orders`](budget-orders.md).

##### 410

Released in November, 2023.

- Added an endpoint to provide app eligibility according to available supply sources, device classes, age criteria, and countries or regions. See [`Find App Eligibility Records`](find-app-eligibility-records.md).
- The [`Find Targeting Keywords in a Campaign`](find-targeting-keywords-in-a-campaign.md) endpoint now supports filtering and sorting by `modificationTime` and `creationTime`.

##### 49

Released in July, 2023.

Updates to [`SupplySource`](supplysource.md):

- Campaigns with a Today tab `SupplySource` no longer serve impressions to iPad.
- Removed minimum asset requirements.

Updates to the [`ProductPageReason`](productpagereason.md) object:

- Updated ad creative rejection reasons.
- Added a [`ReasonLevel`](reasonlevel.md) to support the ad approval process.

> ❗ **Important**:  With the 4.9 release, all previously rejected Today tab ad creatives were `PAUSED` and resubmitted for re-review. The status was updated to `ENABLED` after the re-review. For more information about updating an ad status, see [`Update an Ad`](update-an-ad.md).

 With the 4.9 release, all previously rejected Today tab ad creatives were `PAUSED` and resubmitted for re-review. The status was updated to `ENABLED` after the re-review. For more information about updating an ad status, see [`Update an Ad`](update-an-ad.md).

##### 48

Released in April, 2023.

- Added endpoints to support the ad creative approval process for campaigns using the `APPSTORE_TODAY_TAB` or `APPSTORE_SEARCH_RESULTS` [`SupplySource`](supplysource.md).
- [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md) and [`Get Ad Creative Rejection Reasons`](gets-a-product-page-reason.md) can help you resolve a [`ProductPageReason`](productpagereason.md) for rejected ad creatives based on [`Custom Product Pages`](custom-product-pages.md).
- [`Find App Assets`](find-app-assets.md) returns your app asset metadata that may need adjusting.

##### 47

Released in January, 2023.

- Added [`Impression Share Reports`](impression-share-reports.md).

##### 461

Released in October, 2022.

- Added a new section on [`Rate Limits`](calling-the-apple-search-ads-api#Rate-Limits.md).
- Updated the script for [`Create a Client Secret`](implementing-oauth-for-the-apple-search-ads-api#Create-a-Client-Secret.md) in the OAuth procedures.
- Added a new [`Find Ad Groups (org-level)`](find-ad-groups-(org-level).md) endpoint to find ad groups within your organization.
- Added a new [`Find Ads (org-level)`](find-ads-(org-level).md) endpoint to find `ads` within your organization.

##### 46

Released in September, 2022.

Advertisers can book ads using two new ad placements: `APPSTORE_TODAY_TAB` and `APPSTORE_PRODUCT_PAGES_BROWSE`. See [`SupplySource`](supplysource.md).

- `APPSTORE_TODAY_TAB` requires an approved ad creative based on eligible [`Custom Product Pages`](custom-product-pages.md) (CPPs).
- Your CPP needs to be in the `defaultLanguage` of your campaign. See [`SupplySource`](supplysource.md).
- The default languages of Hong Kong (HK) and Macau (MO) have been updated from `yue-Hant` to `zh-Hant`. Use the [`Get Supported Countries or Regions`](get-supported-countries-or-regions.md) endpoint to fetch supported languages and language codes.
- `APPSTORE_PRODUCT_PAGES_BROWSE` places your ad at the top of the You Might Also Like list when users scroll to the bottom of relevant pages across the App Store.
- An optional app categories targeting dimension is eligible to use with `APPSTORE_PRODUCT_PAGES_BROWSE`. See [`AppCategoryCriteria`](appcategorycriteria.md).

##### 44

Released in June, 2022.

- Advertisers are able to book campaigns with a cost-per-tap (`CPC`) pricing model and the `APPSTORE_SEARCH_TAB` [`SupplySource`](supplysource.md).
- The cost-per-thousand-impressions (`CPM`) [`PricingModel`](pricingmodel.md) has been deprecated. You can’t update a `CPM` campaign to a CPC campaign. You must create new campaigns using `CPC`.
- A lifetime budget is now optional. New campaigns require either a `dailyBudgetAmount` or a `budgetAmount` (lifetime budget), or both. See [`Create a Campaign`](create-a-campaign.md) and [`Update a Campaign`](update-a-campaign.md) for payload examples.
- Campaign `endTime` and `startTime` attributes are now configurable. See the [`Campaign`](campaign.md) object for validations.

##### 43

Released in April, 2022.

- Added delete keywords endpoints. See [`Delete Targeting Keywords`](delete-targeting-keywords.md) and [`Find Targeting Keywords in a Campaign`](find-targeting-keywords-in-a-campaign.md).
- Enhancements to the geolocation search service.

##### 42

Released in March, 2022.

- Added `creationTime` field to the [`Creative`](creative.md), [`Ad`](ad.md) object, [`AdCreate`](adcreate.md), [`AdUpdate`](adupdate.md), [`ReportingAd`](reportingad.md), and `ReportingCreativeSet`.
- Reports now include [`Get Keyword-Level within Ad Group Reports`](get-keyword-level-within-ad-group-reports.md) and [`Get Search Term-Level within Ad Group Reports`](get-search-term-level-within-ad-group-reports.md).

##### 41

Released in January, 2022.

[`Custom Product Pages`](custom-product-pages.md) replaces Creative Sets functionality. The Apple Search Ads API no longer supports Creative Sets and `AdGroupCreativeSets`. Creative Sets APIs return `200 OK` responses with an invalid state. Your Creative Sets data remains available through `Get Creative Set-Level Reports`.

Custom Product Pages reports now include [`Get Ad-Level Reports`](get-ad-level-reports.md), available for campaigns using the `APPSTORE_SEARCH_RESULTS` [`SupplySource`](supplysource.md).

##### 40

Released in May, 2021. You can use calls from the 4.x API to access all of your resources that you created in Apple Search Ads Campaign Management API 3.

###### Oauth

Beginning in 2021, the Apple Search Ads Campaign Management API uses OAuth 2 for API account authentication. Apple Search Ads users no longer use API certificates to manage access to their Search Ads accounts. For more information, see [`Implementing OAuth for the Apple Search Ads API`](implementing-oauth-for-the-apple-search-ads-api.md).

To make calls to the Apple Search Ads Campaign Management API with OAuth, see [`Calling the Apple Search Ads API`](calling-the-apple-search-ads-api.md).

###### Access Control Lists

Access control lists have the following updates:

- The `parentOrgId` field is a new field in the [`UserAcl`](useracl.md) object. This distinguishes the account from an `orgId` belonging to a suborganization. See [`Calling the Apple Search Ads API`](calling-the-apple-search-ads-api.md) for details.
- The [`Get Me Details`](get-me-details.md) endpoint has been added with its [`MeDetailResponse`](medetailresponse.md) object.
- The `certExpirationDate` field is no longer a property of the `UserAcl` object.

###### Ad Groups

The `defaultCpcBid` field in the [`AdGroup`](adgroup.md) object has been renamed to `defaultBidAmount`.

###### Reports

[`Campaign`](campaign.md) objects now include new fields: [`SupplySource`](supplysource.md), [`AdChannelType`](adchanneltype.md), and [`BillingEventType`](billingeventtype.md). The [`AdGroup`](adgroup.md) object now includes a new field: [`PricingModel`](pricingmodel.md).  Note, in the [`AdGroup`](adgroup.md) object, the `defaultCpcBid` field used in API 3 is now the `defaultBidAmount` field in API 4.

- [`Get Campaign-Level Reports`](get-campaign-level-reports.md) returns `supplySources`,  [`AdChannelType`](adchanneltype.md), `BillingEventType`, and `avgCPM` in the metadata.
- [`Get Ad Group-Level Reports`](get-ad-group-level-reports.md) returns `PricingModel`, `defaultBidAmount`, and `avgCPM` in the metadata.
- [`Get Keyword-Level Reports`](get-keyword-level-reports.md), [`Get Search Term-Level Reports`](get-search-term-level-reports.md), and `Get Creative Set-Level Reports`  aren’t supported with `supplySources` and [`AdChannelType`](adchanneltype.md) fields.

## See Also

- [Apple Search Ads Campaign Management API 5](apple-search-ads-campaign-management-api-5.md)
  Learn about changes to Apple Search Ads Campaign Management API 5.
- [Apple Search Ads Campaign Management API 3](apple-search-ads-campaign-management-api-3.md)
  Apple no longer supports this API.
- [Apple Search Ads Campaign Management API 2](apple-search-ads-campaign-management-api-2.md)
  Apple no longer supports this API.
- [Apple Search Ads Campaign Management API 1](apple-search-ads-campaign-management-api-1.md)
  Apple no longer supports this API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/apple-search-ads-campaign-management-api-4)*