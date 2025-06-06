# GetAddress

**Framework**: USBDriverKit  
**Kind**: method

Returns the address of the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t GetAddress(uint8_t * address) const;
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `address`: A pointer to a variable. On output, the variable contains the device’s address.

## See Also

- [GetSpeed](iousbhostdevice/getspeed.md)
  Retrieves the device’s operational speed.
- [GetFrameNumber](iousbhostdevice/getframenumber.md)
  Gets the current frame number of the USB controller.
- [GetPortStatus](iousbhostdevice/getportstatus.md)
  Returns the current port status of the device.
- [tIOUSBHostConnectionSpeed](tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.
- [tIOUSBHostPortStatus](tiousbhostportstatus.md)
  Constants indicating the state of a port.
- [tIOUSBHostPortType](tiousbhostporttype.md)
  Constants indicating a port’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/getaddress)*