# Creative.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

System validation status reflecting whether the ad creative can serve.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Creative.SystemStatus
```

## Possible Values

- `VALID`: The ad creative has passed all system validation checks and is ready to serve. The ad creative may still be subject to additional review.
- `INVALID`: The ad creative has failed one or more validation checks. Check `systemStatusReasons` for the cause.
- `PENDING`: The ad creative is undergoing system validation, policy determination, or waiting for asset CDN availability.

#### Discussion

A `VALID` result only confirms system checks passed; Apple’s additional creative review can still affect whether the ad creative ultimately serves.

##### Example

```json
{
  "systemStatus": "VALID"
}
```

See [`CreativeSystemStatus`](../creativesystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creative/systemstatus-data.typealias)*