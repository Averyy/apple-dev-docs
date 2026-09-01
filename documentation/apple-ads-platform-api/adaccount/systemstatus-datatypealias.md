# AdAccount.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

The system status for an ad account.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string AdAccount.SystemStatus
```

#### Discussion

This status reflects the ad account specifically, separate from the [`Org.SystemStatus`](org/systemstatus-data.typealias.md) of its parent organization.

##### Example

```json
{
  "systemStatus": "ACTIVE"
}
```

See [`AdAccountSystemStatus`](adaccountsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adaccount/systemstatus-data.typealias)*