# AdGroupCreate.Status

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Advertiser-configurable serving status for an ad group.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdGroupCreate.Status
```

## Possible Values

- `ENABLED`: The ad group is active and eligible to serve ads.
- `PAUSED`: The ad group is paused and will not serve ads.

## Discussion

Include `status` in the create request to determine whether the new ad group begins competing for delivery immediately or starts paused.

### Example

```json
{
  "status": "ENABLED"
}
```

See [`AdGroupStatus`](../adgroupstatus.md) for additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adgroupcreate/status-data.typealias)*