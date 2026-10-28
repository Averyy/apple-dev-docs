# PricingModel

**Framework**: Apple Ads  
**Kind**: typealias  
**Role**: Type

The type of pricing model for a bid.

**Availability**:
- Search Ads 4.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
string PricingModel
```

## Possible Values

- `CPC`: The average cost for each ad tap in a campaign.
- `CPM`: The cost per 1000 impressions in a campaign.

## Mentions

- [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md)

## Discussion

> ❗ **Important**:  > Apple Ads Campaign Management API 4.4 deprecates CPM. You can’t update CPM campaigns to CPC campaigns. You need to use CPC when creating a new campaign. See section 4.4 in  [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md) for additional details.

## Discussion

See also [`AdChannelType`](./adchanneltype.md), [`BillingEventType`](./billingeventtype.md), and [`Campaign`](./campaign.md) object. See [`Create a Campaign`](./create-a-campaign.md) and [`Create an Ad Group`](./create-an-ad-group.md) for payload examples.

## See Also

### Data Types
- [type AdGroupDisplayStatus](./adgroupdisplaystatus.md)
  The status of the ad group.
- [type AdGroupServingStateReasons](./adgroupservingstatereasons.md)
  A list of reasons that displays when an ad group isn’t running.
- [type AdGroupServingStatus](./adgroupservingstatus.md)
  The status of whether the ad group is serving.
- [type AdGroupStatus](./adgroupstatus.md)
  The status of whether the ad group is enabled or not.
- [type DeviceClass](./deviceclass.md)
  The defined targeted audience to include by device type.
- [type Gender](./gender.md)
  The defined targeted audience in a campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/pricingmodel)*