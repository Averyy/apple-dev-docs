# USBDeviceSuspend

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Tells the USB Family to either suspend or resume the port to which a device is attached.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*USBDeviceSuspend)(void *self, Boolean suspend);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnNotOpen if the device is not open for exclusive access.

#### Discussion

The device must be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.
- `suspend`: TRUE to cause the port to be suspended, FALSE to cause it to be resumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface182/1559768-usbdevicesuspend)*