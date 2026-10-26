# USBDeviceAbortPipeZero

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Aborts a transaction on the default control pipe.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*USBDeviceAbortPipeZero)(void *self);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnNotOpen if the device is not open for exclusive access.

#### Discussion

The device must be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface182/1559458-usbdeviceabortpipezero)*