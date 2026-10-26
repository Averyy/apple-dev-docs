# setSubunitPlugSignalFormat

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the signal format of the specifed plug.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*setSubunitPlugSignalFormat)(void *self, UInt32 subunitTypeAndID, IOFWAVCPlugTypes plugType, UInt32 plugNum, UInt32 signalFormat);
```

## Parameters

- `self`: Pointer to IOFireWireAVCLibProtocolInterface.
- `subunitTypeAndID`: The subunit type and ID of the plug.
- `plugType`: The plug type.
- `plugNum`: The plug number.
- `signalFormat`: The 32-bit signal format value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508809-setsubunitplugsignalformat)*