# DestinationType

**Framework**: Apple Ads Platform API  
**Kind**: typealias

Specifies where an ad sends users after they tap it.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string DestinationType
```

#### Discussion

The [`Destination`](destination.md) object sets `DestinationType`, which is immutable after ad creative creation. Changing the destination type requires creating a new ad creative.

## See Also

- [type CreativeType](creativetype.md)
  Enum identifying the visual format and placement context of an ad creative.
- [type CreativeSystemStatus](creativesystemstatus.md)
  System-evaluated validation state for an ad creative.
- [type CreativeSystemStatusReason](creativesystemstatusreason.md)
  A reason code explaining why an ad creative is not valid or is pending review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/destinationtype)*