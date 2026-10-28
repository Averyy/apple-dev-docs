# AdGroup.SystemStatusReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Reasons that can cause an ad group’s system status to be `NOT_RUNNING`.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdGroup.SystemStatusReasons
```

## Possible Values

- `PROCESSING`: The ad group is being processed and is not yet active.
- `PAUSED_BY_SYSTEM`: The ad group was paused by the system.
- `PAUSED_BY_USER`: The ad group was paused by the advertiser.
- `DELETED_BY_USER`: The ad group was deleted by the advertiser.
- `SCHEDULE_PENDING`: The ad group schedule has not yet started.
- `SCHEDULE_EXPIRED`: The ad group schedule has ended.
- `TARGETED_DEVICE_CLASS_NOT_SUPPORTED_SUPPLY_PLACEMENT`: The targeted device class is not supported by the supply placement.
- `PENDING_AUDIENCE_VERIFICATION`: The ad group’s audience targeting is pending verification.
- `AUDIENCE_BELOW_THRESHOLD`: The targeted audience is below the minimum threshold required to serve.
- `CAMPAIGN_NOT_RUNNING`: The parent campaign is not running.
- `ADS_NOT_RUNNING`: All ads in the ad group are not running.
- `AUTOMATED_KEYWORDS_REQUIRED_AD_GROUP_NOT_ALLOWED_IN_MANUAL_CAMPAIGNS`: Automated keyword ad groups are not allowed in manually managed campaigns.
- `KEYWORDS_MISSING`: The ad group requires keywords but none have been added.

## Discussion

These reasons range from scheduling and audience-size conditions on the ad group itself to a parent campaign that isn’t running, as with `CAMPAIGN_NOT_RUNNING`.

### Example

```json
{
  "systemStatusReasons": [
    "SCHEDULE_PENDING"
  ]
}
```

See [`AdGroupSystemStatusReason`](../adgroupsystemstatusreason.md) for the full field reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/systemstatusreasons-data.typealias)*