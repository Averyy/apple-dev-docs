# getSubunitPlugSignalFormat

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Gets the signal format of the specifed plug.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*getSubunitPlugSignalFormat)(void *self, UInt32 subunitTypeAndID, IOFWAVCPlugTypes plugType, UInt32 plugNum, UInt32 *pSignalFormat);
```

## Parameters

- `self`: Pointer to IOFireWireAVCLibProtocolInterface.
- `subunitTypeAndID`: The subunit type and ID of the plug.
- `plugType`: The plug type.
- `plugNum`: The plug number.
- `pSignalFormat`: A pointer to the location to return the signal format value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508742-getsubunitplugsignalformat)*