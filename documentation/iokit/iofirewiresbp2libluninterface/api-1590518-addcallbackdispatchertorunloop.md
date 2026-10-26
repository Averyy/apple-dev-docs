# addCallbackDispatcherToRunLoop

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Adds a dispatcher for kernel callbacks to the specified runloop.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*addCallbackDispatcherToRunLoop)(void *self, CFRunLoopRef cfRunLoopRef);
```

#### Return Value

Returns kIOReturnSuccess on success.

#### Discussion

The user space portions of the SBP2 api communicate with the in-kernel services by messaging the kernel. Similarly, the kernel messages the user space services in response. These responses need to be picked up by a piece of code. This call adds that code to the specified runloop. Most drivers will call this method on the runloop that was created when your task was created. To avoid deadlock you must avoid sleeping (or spin waiting) the runloop to wait for SBP2 response. If you do this the dispatcher will never get to run and you will wait forever.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLUNInterface.
- `cfRunLoopRef`: Reference to a runloop


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libluninterface/1590518-addcallbackdispatchertorunloop)*