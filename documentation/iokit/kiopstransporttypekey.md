# kIOPSTransportTypeKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current power source's data transport type (e.g. the means that the power source conveys power source data to the macOS machine).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
#define kIOPSTransportTypeKey
```

## Discussion

- Apple-defined power sources will publish this key.
- A value of [`kIOPSInternalType`](./kiopsinternaltype.md) describes an internal power source.
- [`kIOPSUSBTransportType`](./kiopsusbtransporttype.md), [`kIOPSNetworkTransportType`](./kiopsnetworktransporttype.md), and [`kIOPSSerialTransportType`](./kiopsserialtransporttype.md) usually describe UPS's.
- For power source creators: Providing this key is REQUIRED.
- Type CFStringRef. Valid transport types are kIOPSSerialTransportType, kIOPSUSBTransportType, kIOPSNetworkTransportType, kIOPSInternalType


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopstransporttypekey)*