# CreativeSystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias

System-evaluated validation state for an ad creative.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
string CreativeSystemStatus
```

#### Discussion

`CreativeSystemStatus` is a read-only field that reflects whether an ad creative has passed all system validation checks and is eligible to serve.

When the status isn’t `VALID`, inspect `systemStatusReasons` on the [`Creative`](creative.md) object to determine the specific blocking condition.

## See Also

- [type CreativeType](creativetype.md)
  Enum identifying the visual format and placement context of an ad creative.
- [type CreativeSystemStatusReason](creativesystemstatusreason.md)
  A reason code explaining why an ad creative is not valid or is pending review.
- [type DestinationType](destinationtype.md)
  Specifies where an ad sends users after they tap it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creativesystemstatus)*