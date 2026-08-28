# AdGroupUpdate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Advertiser-configurable serving status for an ad group.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string AdGroupUpdate.Status
```

#### Discussion

Send `status: PAUSED` to stop an existing ad group from competing for delivery, or `ENABLED` to resume it.

##### Example

```json
{
  "status": "PAUSED"
}
```

See [`AdGroupStatus`](adgroupstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupupdate/status-data.typealias)*