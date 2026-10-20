# AdGroupServingStateReasons

**Framework**: Apple Ads  
**Kind**: typealias  
**Role**: Type

A list of reasons that displays when an ad group isn’t running.

**Availability**:
- Search Ads 4.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
string AdGroupServingStateReasons
```

## Possible Values

- `AD_GROUP_PAUSED_BY_USER`: The user paused the ad group.
- `APP_NOT_SUPPORT`: The system can’t process the ad group data.
- `DELETED_BY_USER`: The user deleted the ad group.
- `ADGROUP_END_DATE_REACHED`: The ad group end date is in the past.
- `AUDIENCE_BELOW_THRESHOLD`: The targeting parameters are below the threshold.
- `CAMPAIGN_END_DATE_REACHED`: The campaign linked to the ad group ended.
- `CAMPAIGN_NOT_RUNNING`: The campaign isn’t running.
- `CAMPAIGN_START_DATE_IN_FUTURE`: The campaign linked to the ad group is set to start at a future date.
- `START_DATE_IN_THE_FUTURE`: The ad group start date is in the future.
- `NO_AVAILABLE_ADS`: The ad group has no available ads.
- `PENDING_AUDIENCE_VERIFICATION`: The targeting parameters are inaccurate.
- `TARGETED_DEVICE_CLASS_NOT_SUPPORTED_SUPPLY_SOURCE`: The targeting parameter is unsupported. See Today tab compatibility subsection of  [`SupplySource`](./supplysource.md).

## See Also

### Data Types
- [type AdGroupDisplayStatus](./adgroupdisplaystatus.md)
  The status of the ad group.
- [type AdGroupServingStatus](./adgroupservingstatus.md)
  The status of whether the ad group is serving.
- [type AdGroupStatus](./adgroupstatus.md)
  The status of whether the ad group is enabled or not.
- [type DeviceClass](./deviceclass.md)
  The defined targeted audience to include by device type.
- [type Gender](./gender.md)
  The defined targeted audience in a campaign.
- [type PricingModel](./pricingmodel.md)
  The type of pricing model for a bid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/adgroupservingstatereasons)*