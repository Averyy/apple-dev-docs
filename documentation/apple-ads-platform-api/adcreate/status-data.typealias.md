# AdCreate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable status set when creating an ad.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdCreate.Status
```

## Possible Values

- `ENABLED`: The advertiser has set the ad to run, so it can participate in auctions.
- `PAUSED`: The advertiser has paused the ad, so it does not participate in auctions.

#### Discussion

Include `status` in the create request to determine whether the new ad starts competing in auctions immediately or begins paused.

##### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdStatus`](../adstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adcreate/status-data.typealias)*