# setAVCRequestCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

This function has been deprecated. Use installAVCCommandHandler instead.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*setAVCRequestCallback)(void *self, UInt32 subUnitType, UInt32 subUnitID, void *refCon, IOFWAVCRequestCallback callback);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508881-setavcrequestcallback)*