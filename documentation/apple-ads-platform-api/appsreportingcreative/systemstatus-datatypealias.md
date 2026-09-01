# AppsReportingCreative.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System-evaluated validation state of the creative at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```swift
string AppsReportingCreative.SystemStatus
```

#### Discussion

This is a point-in-time snapshot of validation state; a creative later marked `INVALID` may still show `VALID` in an older report.

##### Example

```json
{
  "systemStatus": "VALID"
}
```

See [`CreativeSystemStatus`](creativesystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appsreportingcreative/systemstatus-data.typealias)*