# __reserved1

**Framework**: IOKit  
**Kind**: structp

Set to zero.

## See Also

### Fields
- [notifyRef](../../kernel/iopmsystemcapabilitychangeparameters/api-1522218-notifyref.md)
  An identifier for this message notification. Clients with pending I/O can signal completion by calling `allowPowerChange()` with this value as the argument. Clients that are able to process the notification synchronously should ignore this field.
- [maxWaitForReply](../../kernel/iopmsystemcapabilitychangeparameters/api-1522348-maxwaitforreply.md)
  A return value to the caller indicating the maximum time in microseconds to wait for the `allowPowerChange()` call. The default value is zero, which indicates the client processing has finished, and power management should not wait for an `allowPowerChange()` call.
- [changeFlags](../../kernel/iopmsystemcapabilitychangeparameters/api-1522278-changeflags.md)
  Flags will be set to indicate whether the notification precedes the capability change (`kIOPMSystemCapabilityWillChange`), or after the capability change has occurred (`kIOPMSystemCapabilityDidChange`).
- [fromCapabilities](../../kernel/iopmsystemcapabilitychangeparameters/api-1522166-fromcapabilities.md)
  The system capabilities at the start of the transition.
- [toCapabilities](../../kernel/iopmsystemcapabilitychangeparameters/api-1522492-tocapabilities.md)
  The system capabilities at the end of the transition.
- [__reserved2](./api-1810631-_reserved2.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopmsystemcapabilitychangeparameters/1810535-_reserved1)*