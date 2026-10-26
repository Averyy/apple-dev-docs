# updateInputPlug

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Updates the value of an input plug (simulating a lock transaction).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*updateInputPlug)(void *self, UInt32 plug, UInt32 oldVal, UInt32 newVal);
```

## Parameters

- `self`: Pointer to IOFireWireAVCLibProtocolInterface.
- `plug`: Value returned by allocateInputPlug.
- `oldVal`: Value returned by readInputPlug.
- `newVal`: New value to store in plug if its current value is oldVal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508858-updateinputplug)*