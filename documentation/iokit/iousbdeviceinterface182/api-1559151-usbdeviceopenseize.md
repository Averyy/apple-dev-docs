# USBDeviceOpenSeize

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Opens the IOUSBDevice for exclusive access.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*USBDeviceOpenSeize)(void *self);
```

#### Return Value

Returns kIOReturnExclusiveAccess if some other task has the device opened already and refuses to close it, kIOReturnError if the connection with the kernel can not be established or kIOReturnSuccess if successful.

#### Discussion

This function opens the IOUSBDevice for exclusive access. If another client has the device opened, an attempt is made to get that client to close it before returning. Before the client can issue commands that change the state of the device, it must have succeeded in opening the device. This establishes an exclusive link between the client's task and the actual device.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface182/1559151-usbdeviceopenseize)*