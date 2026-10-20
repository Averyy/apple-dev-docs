# Ad.SystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

System-computed delivery status of an ad.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Ad.SystemStatus
```

## Possible Values

- `RUNNING`: The ad is active and eligible to serve.
- `NOT_RUNNING`: The system has identified a condition preventing the ad from delivering.

#### Discussion

The `SystemStatus` reports whether the platform currently allows the ad to serve, distinct from the advertiser-set [`Ad.Status`](./status-data.typealias.md).

##### Example

```json
{
  "systemStatus": "RUNNING"
}
```

See [`AdSystemStatus`](../adsystemstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/ad/systemstatus-data.typealias)*