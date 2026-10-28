# RemoveCallbackDispatcherFromRunLoop

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Convenience method to remove asynchronous callback mechanisms from the CFRunLoop.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
void (*RemoveCallbackDispatcherFromRunLoop)(void *self);
```

## Discussion

Once a SCSITaskDeviceInterface is opened, the client may make synchronous or asynchronous requests to the device. This method removes the asynchronous notifications delivered via the CFRunLoop. This should be called only after calling AddCallbackDispatcherToRunLoop.

## Parameters

- `self`: Pointer to a SCSITaskDeviceInterface instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskdeviceinterface/1575354-removecallbackdispatcherfromrunl)*