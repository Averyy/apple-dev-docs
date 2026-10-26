# connectTargetPlugs

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Establishes an internal AVC plug connection between subunit/unit plugs.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*connectTargetPlugs)(void *self, UInt32 sourceSubunitTypeAndID, IOFWAVCPlugTypes sourcePlugType, UInt32 *pSourcePlugNum, UInt32 destSubunitTypeAndID, IOFWAVCPlugTypes destPlugType, UInt32 *pDestPlugNum, bool lockConnection, bool permConnection);
```

## Parameters

- `self`: Pointer to IOFireWireAVCLibProtocolInterface.
- `sourceSubunitTypeAndID`: The subunit type and ID for the source plug
- `sourcePlugType`: The source plug type.
- `pSourcePlugNum`: A pointer to the source plug num. Will return the actual source plug num here.
- `destSubunitTypeAndID`: The subunit type and ID for the destination plug.
- `destPlugType`: The dest plug type.
- `pDestPlugNum`: A pointer to the dest plug num. Will return the actual dest plug num here.
- `lockConnection`: A flag to specify if this connection should be locked.
- `permConnection`: A flag to specify if this connection is permanent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508771-connecttargetplugs)*