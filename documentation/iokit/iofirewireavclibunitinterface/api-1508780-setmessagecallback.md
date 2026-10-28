# setMessageCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets callback for user space message routine.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
void (*setMessageCallback)(void *self, void *refCon, IOFWAVCMessageCallback callback);
```

## Discussion

In FireWire and AVC, bus status messages are delivered via IOKit's message routine. This routine is emulated in user space for AVC and FireWire messages via this callback. You should register here for bus reset and reconnect messages.

## Parameters

- `self`: Pointer to IOFireWireAVCLibUnitInterface.
- `refCon`: RefCon to be returned as first argument of completion routine.
- `callback`: Address of completion routine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibunitinterface/1508780-setmessagecallback)*