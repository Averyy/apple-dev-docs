# AdUpdate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable status set when updating an ad.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdUpdate.Status
```

## Possible Values

- `ENABLED`: The advertiser has set the ad to run, so it can participate in auctions.
- `PAUSED`: The advertiser has paused the ad, so it does not participate in auctions.

## Discussion

Send `status: PAUSED` to stop an existing ad from competing in auctions, or `ENABLED` to resume it.

### Example

```json
{
  "status": "PAUSED"
}
```

See [`AdStatus`](../adstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adupdate/status-data.typealias)*