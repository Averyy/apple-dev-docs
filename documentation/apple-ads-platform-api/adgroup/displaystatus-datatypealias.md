# AdGroup.DisplayStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Derived display status for an ad group, combining advertiser-set status with system status.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AdGroup.DisplayStatus
```

#### Discussion

Because it rolls up the full hierarchy, an ad group can show `CAMPAIGN_ON_HOLD` even when its own status and system conditions are otherwise fine.

##### Example

```json
{
  "displayStatus": "RUNNING"
}
```

See [`AdGroupDisplayStatus`](adgroupdisplaystatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroup/displaystatus-data.typealias)*