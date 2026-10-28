# USBDeviceReEnumerate

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Tells the IOUSBFamily to reenumerate the device.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*USBDeviceReEnumerate)(void *self, UInt32 options);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnNotOpen if the device is not open for exclusive access.

## Discussion

This function will send a terminate message to all clients of the IOUSBDevice (such as IOUSBInterfaces and their drivers, as well as the current User Client), emulating an unplug of the device. The IOUSBFamily will then enumerate the device as if it had just been plugged in. This call should be used by clients wishing to take advantage of the Device Firmware Update Class specification. The device must be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.
- `options`: A UInt32 reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface187/1559027-usbdevicereenumerate)*