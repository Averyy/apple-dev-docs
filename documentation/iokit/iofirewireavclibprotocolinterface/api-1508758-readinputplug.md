# readInputPlug

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the current value of an input plug.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
UInt32 (*readInputPlug)(void *self, UInt32 plug);
```

## Parameters

- `self`: Pointer to IOFireWireAVCLibProtocolInterface.
- `plug`: Value returned by allocateInputPlug.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508758-readinputplug)*