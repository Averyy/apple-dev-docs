# ExecuteTaskAsync

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to execute the SCSITask asynchronously.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ExecuteTaskAsync)(void *task);
```

## Return Value

Returns a valid IOReturn code such as kIOReturnSuccess, kIOReturnError, kIOReturnVMError, kIOReturnCannotWire, etc. It will return kIOReturnNotPermitted if the client has not called AddCallbackDispatcherToRunLoop on the SCSITaskDeviceInterface. NOTE: IOReturn is defined as kern_return_t and as such, you may get errors back that do not fall under the IOKit subsystem error domain (sys_iokit) defined in IOReturn.h.

## Discussion

This method can be used to execute the SCSITask asynchronously.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575360-executetaskasync)*