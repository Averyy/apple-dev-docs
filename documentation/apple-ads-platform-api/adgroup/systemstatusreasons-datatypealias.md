# AdGroup.SystemStatusReasons

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Reasons that can cause an ad group’s system status to be `NOT_RUNNING`.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string AdGroup.SystemStatusReasons
```

#### Discussion

These reasons range from scheduling and audience-size conditions on the ad group itself to a parent campaign that isn’t running, as with `CAMPAIGN_NOT_RUNNING`.

##### Example

```json
{
  "systemStatusReasons": [
    "SCHEDULE_PENDING"
  ]
}
```

See [`AdGroupSystemStatusReason`](adgroupsystemstatusreason.md) for the full field reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/systemstatusreasons-data.typealias)*