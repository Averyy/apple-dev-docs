# GetDeviceAddress

**Framework**: USBDriverKit  
**Kind**: method

Retrieves the address of the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t GetDeviceAddress(uint8_t * address) const;
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `address`: A pointer to a variable. On output, the variable contains the device’s address.

## See Also

- [GetSpeed](iousbhostpipe/getspeed.md)
  Retrieves the device’s operational speed.
- [tIOUSBHostConnectionSpeed](tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/getdeviceaddress)*