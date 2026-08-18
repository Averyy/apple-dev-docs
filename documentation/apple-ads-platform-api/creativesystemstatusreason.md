# CreativeSystemStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias

A reason code explaining why an ad creative is not valid or is pending review.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string CreativeSystemStatusReason
```

#### Discussion

One or more `CreativeSystemStatusReason` values appear in the `systemStatusReasons` array on a [`Creative`](creative.md) when `systemStatus` is `INVALID` or `PENDING`. These codes are read-only and system-applied. Use them to diagnose why an ad creative cannot serve and determine the appropriate corrective action.

## See Also

- [type CreativeType](creativetype.md)
  Enum identifying the visual format and placement context of an ad creative.
- [type CreativeSystemStatus](creativesystemstatus.md)
  System-evaluated validation state for an ad creative.
- [type DestinationType](destinationtype.md)
  Specifies where an ad sends users after they tap it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creativesystemstatusreason)*