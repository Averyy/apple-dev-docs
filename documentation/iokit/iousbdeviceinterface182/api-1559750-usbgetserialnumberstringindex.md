# USBGetSerialNumberStringIndex

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the serial number string index in the device descriptor.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*USBGetSerialNumberStringIndex)(void *self, UInt8 *snsi);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService.

#### Discussion

The device does not have to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.
- `snsi`: Pointer to UInt8 to hold the string index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface182/1559750-usbgetserialnumberstringindex)*