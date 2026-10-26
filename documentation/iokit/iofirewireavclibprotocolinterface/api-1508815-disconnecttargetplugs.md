# disconnectTargetPlugs

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Breaks an internal AVC plug connection between subunit/unit plugs.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*disconnectTargetPlugs)(void *self, UInt32 sourceSubunitTypeAndID, IOFWAVCPlugTypes sourcePlugType, UInt32 sourcePlugNum, UInt32 destSubunitTypeAndID, IOFWAVCPlugTypes destPlugType, UInt32 destPlugNum);
```

## Parameters

- `self`: Pointer to IOFireWireAVCLibProtocolInterface.
- `sourceSubunitTypeAndID`: The subunit type and ID for the source plug.
- `sourcePlugType`: The source plug type.
- `sourcePlugNum`: The source plug num.
- `destSubunitTypeAndID`: The subunit type and ID for the destination plug.
- `destPlugType`: The dest plug type.
- `destPlugNum`: The dest plug num.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508815-disconnecttargetplugs)*