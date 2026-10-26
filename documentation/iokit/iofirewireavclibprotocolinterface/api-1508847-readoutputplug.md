# readOutputPlug

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the current value of an output plug.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
UInt32 (*readOutputPlug)(void *self, UInt32 plug);
```

## Parameters

- `self`: Pointer to IOFireWireAVCLibProtocolInterface.
- `plug`: Value returned by allocateOutputPlug.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508847-readoutputplug)*