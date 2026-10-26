# addCallbackDispatcherToRunLoop

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Adds a dispatcher for kernel callbacks to the specified run loop.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*addCallbackDispatcherToRunLoop)(void *self, CFRunLoopRef cfRunLoopRef);
```

#### Return Value

Returns kIOReturnSuccess on success.

#### Discussion

The user space portions of the AVC API communicate with the in-kernel services by messaging the kernel. Similarly, the kernel messages the user space services in response. These responses need to be picked up by a piece of code. This call adds that code to the specified run loop. Most drivers will call this method on the run loop that was created when your task was created. To avoid deadlock you must avoid sleeping (or spin waiting) the run loop to wait for AVC response. If you do this the dispatcher will never get to run and you will wait forever.

## Parameters

- `self`: Pointer to IOFireWireAVCLibProtocolInterface.
- `cfRunLoopRef`: Reference to a run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508773-addcallbackdispatchertorunloop)*