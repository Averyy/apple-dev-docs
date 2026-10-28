# IOPMSystemCapabilityChangeParameters

**Framework**: IOKit  
**Kind**: tag

A structure describing a system capability change.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
struct IOPMSystemCapabilityChangeParameters {
    ...
};
```

## Discussion

A system capability change is a system level transition from a set of system capabilities to a new set of system capabilities. Power management sends a `kIOMessageSystemCapabilityChange` message and provides this structure as the message data (by reference) to `gIOPriorityPowerStateInterest` clients when system capability changes.

## Topics

### Fields
- [notifyRef](./iopmsystemcapabilitychangeparameters/api-1499643-notifyref.md)
  An identifier for this message notification. Clients with pending I/O can signal completion by calling `allowPowerChange()` with this value as the argument. Clients that are able to process the notification synchronously should ignore this field.
- [maxWaitForReply](./iopmsystemcapabilitychangeparameters/api-1499937-maxwaitforreply.md)
  A return value to the caller indicating the maximum time in microseconds to wait for the `allowPowerChange()` call. The default value is zero, which indicates the client processing has finished, and power management should not wait for an `allowPowerChange()` call.
- [changeFlags](./iopmsystemcapabilitychangeparameters/api-1499956-changeflags.md)
  Flags will be set to indicate whether the notification precedes the capability change (`kIOPMSystemCapabilityWillChange`), or after the capability change has occurred (`kIOPMSystemCapabilityDidChange`).
- [__reserved1](./iopmsystemcapabilitychangeparameters/api-1810535-_reserved1.md)
  Set to zero.
- [fromCapabilities](./iopmsystemcapabilitychangeparameters/api-1499569-fromcapabilities.md)
  The system capabilities at the start of the transition.
- [toCapabilities](./iopmsystemcapabilitychangeparameters/api-1499602-tocapabilities.md)
  The system capabilities at the end of the transition.
- [__reserved2](./iopmsystemcapabilitychangeparameters/api-1810631-_reserved2.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopmsystemcapabilitychangeparameters)*