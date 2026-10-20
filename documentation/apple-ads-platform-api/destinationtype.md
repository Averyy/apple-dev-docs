# DestinationType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

Specifies where an ad sends users after they tap it.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string DestinationType
```

## Possible Values

- `APP_STORE_PRODUCT_PAGE`: Directs users to the app’s product page in the App Store. Used with `DEFAULT_PRODUCT_PAGE` and `CUSTOM_PRODUCT_PAGE` creative types.
- `LOCAL_ADS_PLACECARD`: Directs users to the brand’s Maps place card. The only supported destination for Apple Maps ad creatives.

#### Discussion

The [`Destination`](./destination.md) object sets `DestinationType`, which is immutable after ad creative creation. Changing the destination type requires creating a new ad creative.

## See Also

- [type CreativeType](./creativetype.md)
  Enum identifying the visual format and placement context of an ad creative.
- [type CreativeSystemStatus](./creativesystemstatus.md)
  System-evaluated validation state for an ad creative.
- [type CreativeSystemStatusReason](./creativesystemstatusreason.md)
  A reason code explaining why an ad creative isn’t valid or is pending review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/destinationtype)*