# BrandsReportingCreative.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

System-evaluated validation state of the creative at report time.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string BrandsReportingCreative.SystemStatus
```

## Possible Values

- `VALID`: The creative has passed all system validation checks and is ready to serve. The creative may still be subject to additional review.
- `INVALID`: The creative has failed one or more validation checks. Check `systemStatusReasons` for the cause.
- `PENDING`: The creative is undergoing system validation, policy determination, or waiting for asset CDN availability.

#### Discussion

A `VALID` result at report time only confirms system checks had passed as of that snapshot; Apple’s additional creative review can still affect current delivery.

##### Example

```json
{
  "systemStatus": "VALID"
}
```

See [`CreativeSystemStatus`](../creativesystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brandsreportingcreative/systemstatus-data.typealias)*