# USBInterfaceOpenSeize

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Opens the IOUSBInterface for exclusive access.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*USBInterfaceOpenSeize)(void *self);
```

#### Return Value

Returns kIOReturnExclusiveAccess if some other task has the interface open already and refuses to close it, kIOReturnError if the connection with the kernel cannot be established or kIOReturnSuccess if successful.

#### Discussion

If another client has the device open, an attempt is made to get that client to close it before returning.

Before the client can issue commands that change the state of the device, it must have succeeded in opening the device. This establishes an exclusive link between the clients task and the actual device.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface183/1559513-usbinterfaceopenseize)*