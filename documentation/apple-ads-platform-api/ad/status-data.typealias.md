# Ad.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable serving status for an ad.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string Ad.Status
```

## Possible Values

- `ENABLED`: The advertiser has set the ad to run, so it can participate in auctions.
- `PAUSED`: The advertiser has paused the ad, so it does not participate in auctions.

#### Discussion

The `Status` field controls auction eligibility directly, while the system-computed [`Ad.SystemStatus`](./systemstatus-data.typealias.md) reflects whether the ad is actually delivering.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdStatus`](../adstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/ad/status-data.typealias)*