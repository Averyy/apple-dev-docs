# USBGetProductStringIndex

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the product string index in the device descriptor.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*USBGetProductStringIndex)(void *self, UInt8 *psi);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService.

#### Discussion

The device does not have to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.
- `psi`: Pointer to UInt8 to hold the string index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface182/1558836-usbgetproductstringindex)*