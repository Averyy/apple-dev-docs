# CreativeSystemStatus

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

System-evaluated validation state for an ad creative.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string CreativeSystemStatus
```

## Possible Values

- `VALID`: The ad creative has passed all system validation checks and is ready to serve. The ad creative may still be subject to additional review.
- `INVALID`: The ad creative has failed one or more validation checks. Check `systemStatusReasons` for the cause.
- `PENDING`: The ad creative is undergoing system validation, policy determination, or waiting for asset CDN availability.

## Discussion

The `CreativeSystemStatus` is a read-only field that reflects whether an ad creative has passed all system validation checks and is eligible to serve.

When the status isn’t `VALID`, inspect `systemStatusReasons` on the [`Creative`](./creative.md) object to determine the specific blocking condition.

## See Also

- [type CreativeType](./creativetype.md)
  Enum identifying the visual format and placement context of an ad creative.
- [type CreativeSystemStatusReason](./creativesystemstatusreason.md)
  A reason code explaining why an ad creative isn’t valid or is pending review.
- [type DestinationType](./destinationtype.md)
  Specifies where an ad sends users after they tap it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creativesystemstatus)*