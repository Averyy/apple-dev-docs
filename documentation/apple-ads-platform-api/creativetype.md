# CreativeType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Enum identifying the visual format and placement context of an ad creative.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string CreativeType
```

## Possible Values

- `CUSTOM_PRODUCT_PAGE`: Uses a Custom Product Page as the pre-tap experience. Requires `productPageId` in the destination.
- `DEFAULT_PRODUCT_PAGE`: Uses the app’s default App Store listing as the pre-tap experience. No `productPageId` required.
- `LOCAL_ADS_SEARCH_CREATIVE`: Ad creative for Ads on Apple Maps.

#### Discussion

The `CreativeType` is set at creation time and is immutable. It determines which `creativeSpec` variant to supply and which ad placements the ad creative can serve on.

## See Also

- [type CreativeSystemStatus](./creativesystemstatus.md)
  System-evaluated validation state for an ad creative.
- [type CreativeSystemStatusReason](./creativesystemstatusreason.md)
  A reason code explaining why an ad creative isn’t valid or is pending review.
- [type DestinationType](./destinationtype.md)
  Specifies where an ad sends users after they tap it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creativetype)*