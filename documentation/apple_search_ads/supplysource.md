# SupplySource

**Framework**: Apple Search Ads  
**Kind**: typealias

The ad placements for a campaign.

**Availability**:
- Search Ads 4.0+

## Declaration

```swift
string SupplySource
```

## Mentions

- [Apple Search Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use the following combination of campaign and ad group values for `supplySources`.

|  |  |  |  |
| --- | --- | --- | --- |
| `Search` | `APPSTORE_SEARCH_RESULTS` | `Taps` | `CPC` |
| `Display` | `APPSTORE_TODAY_TAB` | `Taps` | `CPC` |
| `Display` | `APPSTORE_SEARCH_TAB` | `Taps` | `CPC` |
| `Display` | `APPSTORE_PRODUCT_PAGES_BROWSE` | `Taps` | `CPC` |

For payload examples, see [`AdChannelType`](adchanneltype.md), [`BillingEventType`](billingeventtype.md), [`PricingModel`](pricingmodel.md), and [`Campaign`](campaign.md) object. For more information about campaigns and ad groups, see [`Create a Campaign`](create-a-campaign.md) and [`Create an Ad Group`](create-an-ad-group.md).

##### Today Tab Compatibility

Campaigns with an `APPSTORE_TODAY_TAB` `SupplySource` reach users when they come to the App Store to discover apps. For an ad to display in the Today tab, your custom product page metadata —  and  — need to be localized in the `defaultLanguage` of all countries or regions where your ad is serving. For example, ads serving in the United States and Mexico require a product page with localized `en-US` and a product page with `es-MX` assets. See [`Get Supported Countries or Regions`](get-supported-countries-or-regions.md).

iPhone is the only supported [`DeviceClass`](deviceclass.md) that you can use with a Today tab `SupplySource`. Today tab ad groups not targeting iPhone are placed on hold with the following [`AdGroupServingStateReasons`](adgroupservingstatereasons.md): `TARGETED_DEVICE_CLASS_NOT_SUPPORTED_SUPPLY_SOURCE`.

As part of review:

- Ads that are pending review are on hold until Apple completes the review.
- Ads that are incompatible with Today tab guidelines don’t receive approval.
- The system doesn’t serve rejected ads.

Use [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md) or [`Get Ad Creative Rejection Reasons`](gets-a-product-page-reason.md) to look up rejection reasons. See [`ProductPageReason`](productpagereason.md) for rejection reason enumerations.

## See Also

- [type AdChannelType](adchanneltype.md)
  The channel type of an ad in a campaign.
- [type BillingEventType](billingeventtype.md)
  The type of billing event for a campaign.
- [type CampaignCountryOrRegionsServingStateReasons](campaigncountryorregionsservingstatereasons.md)
  Reasons that displays when a campaign can’t run.
- [type CampaignDisplayStatus](campaigndisplaystatus.md)
  The status of the campaign.
- [type CampaignServingStateReasons](campaignservingstatereasons.md)
  Reasons the system provides when a campaign can’t run.
- [type CampaignServingStatus](campaignservingstatus.md)
  The status of the campaign.
- [type CampaignStatus](campaignstatus.md)
  The status of the campaign.
- [type PaymentModel](paymentmodel.md)
  The payment model that you set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/supplysource)*