# toCapabilities

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

The system capabilities at the end of the transition.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
uint32_t toCapabilities;
```

## See Also

### Fields
- [notifyRef](./api-1499643-notifyref.md)
  An identifier for this message notification. Clients with pending I/O can signal completion by calling `allowPowerChange()` with this value as the argument. Clients that are able to process the notification synchronously should ignore this field.
- [maxWaitForReply](./api-1499937-maxwaitforreply.md)
  A return value to the caller indicating the maximum time in microseconds to wait for the `allowPowerChange()` call. The default value is zero, which indicates the client processing has finished, and power management should not wait for an `allowPowerChange()` call.
- [changeFlags](./api-1499956-changeflags.md)
  Flags will be set to indicate whether the notification precedes the capability change (`kIOPMSystemCapabilityWillChange`), or after the capability change has occurred (`kIOPMSystemCapabilityDidChange`).
- [__reserved1](./api-1810535-_reserved1.md)
  Set to zero.
- [fromCapabilities](./api-1499569-fromcapabilities.md)
  The system capabilities at the start of the transition.
- [__reserved2](./api-1810631-_reserved2.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopmsystemcapabilitychangeparameters/1499602-tocapabilities)*