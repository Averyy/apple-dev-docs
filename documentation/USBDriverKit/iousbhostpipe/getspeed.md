# GetSpeed

**Framework**: USBDriverKit  
**Kind**: method

Retrieves the device’s operational speed.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
virtual kern_return_t GetSpeed(uint8_t *speed) const;
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

## Parameters

- `speed`: A pointer to a variable. On output, the variable contains the operational speed of the device. For a list of possible values, see [`tIOUSBHostConnectionSpeed`](tiousbhostconnectionspeed.md).

## See Also

- [GetDeviceAddress](iousbhostpipe/getdeviceaddress.md)
  Retrieves the address of the device.
- [tIOUSBHostConnectionSpeed](tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/getspeed)*