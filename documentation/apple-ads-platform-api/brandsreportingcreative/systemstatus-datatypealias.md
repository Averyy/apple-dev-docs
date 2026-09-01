# BrandsReportingCreative.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System-evaluated validation state of the creative at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string BrandsReportingCreative.SystemStatus
```

#### Discussion

A `VALID` result at report time only confirms system checks had passed as of that snapshot; Apple’s additional creative review can still affect current delivery.

##### Example

```json
{
  "systemStatus": "VALID"
}
```

See [`CreativeSystemStatus`](creativesystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcreative/systemstatus-data.typealias)*