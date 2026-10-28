# GetUSBDeviceInformation

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns status information about the USB device, such as whether the device is captive or whether it is in the suspended state.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
IOReturn (*GetUSBDeviceInformation)(void *self, UInt32 *info);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnUnsupported is the bus doesn't support this function.

## Discussion

The device does not have to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.
- `info`: Pointer to a buffer that returns a bit field of information on the device (see the USBDeviceInformationBits in USB.h).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface320/1559006-getusbdeviceinformation)*