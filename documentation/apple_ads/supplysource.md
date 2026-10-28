# SupplySource

**Framework**: Apple Ads  
**Kind**: typealias  
**Role**: Type

The ad placements for a campaign.

**Availability**:
- Search Ads 4.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
string SupplySource
```

## Possible Values

- `APPSTORE_PRODUCT_PAGES_BROWSE`: Reaches users when they’re browsing apps across the App Store. Your ad appears at the top of the You Might Also Like list when users scroll to the bottom of relevant pages across the App Store.

  An optional [`AppCategoryCriteria`](./appcategorycriteria.md) targeting dimension is eligible to use with the `APPSTORE_PRODUCT_PAGES_BROWSE` supply source.

  See the Discussion section below for the combination of campaign and ad group values to use in campaign payloads with `APPSTORE_PRODUCT_PAGES_BROWSE`.
- `APPSTORE_SEARCH_RESULTS`: The campaign runs in App Store search results.

  See the Discussion section below for the combination of campaign and ad group values to use in campaign payloads with `APPSTORE_SEARCH_RESULTS`.
- `APPSTORE_SEARCH_TAB`: The campaign runs on the App Store Search tab.

  See the Discussion section below for the combination of campaign and ad group values to use in campaign payloads with `APPSTORE_SEARCH_TAB`.

  Ad group validations include:

  - You can’t use a `cpaGoal`.
  - You can’t use keywords.
  - You can’t use the daypart targeting dimension.
  - Search Match (`automatedKeywordsOptIn`) can’t be `true`.
- `APPSTORE_TODAY_TAB`: See the Today tab compatibility subsection below.

## Mentions

- [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md)
- [Apple Ads Campaign Management API 5](./apple-search-ads-campaign-management-api-5.md)

## Discussion

Use the following combination of campaign and ad group values for `supplySources`.

| **Ad channel type** | **Supply source** | **Billing event** | **Pricing model** |
| --- | --- | --- | --- |
| `Search` | `APPSTORE_SEARCH_RESULTS` | `Taps` | `CPC` |
| `Display` | `APPSTORE_TODAY_TAB` | `Taps` | `CPC` |
| `Display` | `APPSTORE_SEARCH_TAB` | `Taps` | `CPC` |
| `Display` | `APPSTORE_PRODUCT_PAGES_BROWSE` | `Taps` | `CPC` |

For payload examples, see [`AdChannelType`](./adchanneltype.md), [`BillingEventType`](./billingeventtype.md), [`PricingModel`](./pricingmodel.md), and [`Campaign`](./campaign.md) object. For more information about campaigns and ad groups, see [`Create a Campaign`](./create-a-campaign.md) and [`Create an Ad Group`](./create-an-ad-group.md).

### Today tab compatibility

Campaigns with an `APPSTORE_TODAY_TAB` `SupplySource` reach users when they come to the App Store to discover apps. For an ad to display in the Today tab, your custom product page metadata — *app name* and *subtitle* — need to be localized in the `defaultLanguage` of all countries or regions where your ad is serving. For example, ads serving in the United States and Mexico require a product page with localized `en-US` and a product page with `es-MX` assets. See [`Get Supported Countries or Regions`](./get-supported-countries-or-regions.md).

iPhone is the only supported [`DeviceClass`](./deviceclass.md) that you can use with a Today tab `SupplySource`. Today tab ad groups not targeting iPhone are placed on hold with the following [`AdGroupServingStateReasons`](./adgroupservingstatereasons.md): `TARGETED_DEVICE_CLASS_NOT_SUPPORTED_SUPPLY_SOURCE`.

As part of review:

- Ads that are pending review are on hold until Apple completes the review.
- Ads that are incompatible with Today tab guidelines don’t receive approval.
- The system doesn’t serve rejected ads.

Use [`Find Ad Creative Rejection Reasons`](./find-ad-creative-rejection-reasons.md) or [`Get Ad Creative Rejection Reasons`](./gets-a-product-page-reason.md) to look up rejection reasons. See [`ProductPageReason`](./productpagereason.md) for rejection reason enumerations.

## See Also

### Data Types
- [type AdChannelType](./adchanneltype.md)
  The channel type of an ad in a campaign.
- [type BillingEventType](./billingeventtype.md)
  The type of billing event for a campaign.
- [type CampaignCountryOrRegionsServingStateReasons](./campaigncountryorregionsservingstatereasons.md)
  Reasons that displays when a campaign can’t run.
- [type CampaignDisplayStatus](./campaigndisplaystatus.md)
  The status of the campaign.
- [type CampaignServingStateReasons](./campaignservingstatereasons.md)
  Reasons the system provides when a campaign can’t run.
- [type CampaignServingStatus](./campaignservingstatus.md)
  The status of the campaign.
- [type CampaignStatus](./campaignstatus.md)
  The status of the campaign.
- [type PaymentModel](./paymentmodel.md)
  The payment model that you set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/supplysource)*