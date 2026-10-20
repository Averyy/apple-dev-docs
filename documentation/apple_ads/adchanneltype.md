# AdChannelType

**Framework**: Apple Ads  
**Kind**: typealias  
**Role**: Type

The channel type of an ad in a campaign.

**Availability**:
- Search Ads 4.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
string AdChannelType
```

## Possible Values

- `SEARCH`: When the [`SupplySource`](./supplysource.md) is `APPSTORE_SEARCH_RESULTS`, the [`AdChannelType`](./adchanneltype.md) needs to be `SEARCH`.
- `DISPLAY`: When `the` [`SupplySource`](./supplysource.md) is `APPSTORE_SEARCH_TAB, APPSTORE_PRODUCT_PAGES_BROWSE`, or `APPSTORE_TODAY_TAB`, the [`AdChannelType`](./adchanneltype.md) needs to be `DISPLAY`.

## Mentions

- [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md)

#### Discussion

See also [`BillingEventType`](./billingeventtype.md) and [`Campaign`](./campaign.md) object.

## See Also

### Data Types
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
- [type SupplySource](./supplysource.md)
  The ad placements for a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/adchanneltype)*