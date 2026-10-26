# updateInputMasterPlug

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Updates the value of the primary input plug (simulating a lock transaction).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*updateInputMasterPlug)(void *self, UInt32 oldVal, UInt32 newVal);
```

## Parameters

- `self`: Pointer to [`IOFireWireAVCLibProtocolInterface`](../iofirewireavclibprotocolinterface.md).
- `oldVal`: Value returned by [`readInputMasterPlug`](./api-1508765-readinputmasterplug.md).
- `newVal`: New value to store in plug if its current value is oldVal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508884-updateinputmasterplug)*