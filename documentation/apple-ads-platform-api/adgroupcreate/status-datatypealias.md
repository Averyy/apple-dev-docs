# AdGroupCreate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable serving status for an ad group.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AdGroupCreate.Status
```

#### Discussion

Include `status` in the create request to determine whether the new ad group begins competing for delivery immediately or starts paused.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdGroupStatus`](adgroupstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupcreate/status-data.typealias)*