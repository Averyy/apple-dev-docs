# Creative.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System validation status reflecting whether the ad creative can serve.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string Creative.SystemStatus
```

#### Discussion

A `VALID` result only confirms system checks passed; Apple’s additional creative review can still affect whether the ad creative ultimately serves.

##### Example

```json
{
  "systemStatus": "VALID"
}
```

See [`CreativeSystemStatus`](creativesystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creative/systemstatus-data.typealias)*