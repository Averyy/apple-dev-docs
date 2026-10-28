# AddCallbackDispatcherToRunLoop

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Convenience method to add asynchronous callback mechanisms to the CFRunLoop of choice.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*AddCallbackDispatcherToRunLoop)(void *self, CFRunLoopRef cfRunLoopRef);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnNoMemory if a mach port could not be allocated and initialized properly.

## Discussion

Once a SCSITaskDeviceInterface is opened, the client may make synchronous or asynchronous requests to the device. This method creates and initializes a mach_port_t for receiving asynchronous callback notifications via the CFRunLoop mechanism.

## Parameters

- `self`: Pointer to a SCSITaskDeviceInterface instance.
- `cfRunLoopRef`: The CFRunLoop to which asynchronous callback notifications should be attached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskdeviceinterface/1575415-addcallbackdispatchertorunloop)*