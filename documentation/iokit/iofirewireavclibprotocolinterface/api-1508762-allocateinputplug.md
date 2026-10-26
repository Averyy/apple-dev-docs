# allocateInputPlug

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Allocates an input plug.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*allocateInputPlug)(void *self, void *refcon, IOFWAVCPCRCallback func, UInt32 *plug);
```

## Parameters

- `self`: Pointer to IOFireWireAVCLibProtocolInterface.
- `refcon`: Arbitrary value passed back as first argument of callback.
- `func`: Callback function when a successful lock transaction to the plug has been performed.
- `plug`: Set to the plug number if a plug is successfully allocated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508762-allocateinputplug)*