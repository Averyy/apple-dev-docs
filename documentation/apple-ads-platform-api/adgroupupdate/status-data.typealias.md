# AdGroupUpdate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable serving status for an ad group.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdGroupUpdate.Status
```

## Possible Values

- `ENABLED`: The ad group is active and eligible to serve ads.
- `PAUSED`: The ad group is paused and will not serve ads.

## Discussion

Send `status: PAUSED` to stop an existing ad group from competing for delivery, or `ENABLED` to resume it.

### Example

```json
{
  "status": "PAUSED"
}
```

See [`AdGroupStatus`](../adgroupstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupupdate/status-data.typealias)*