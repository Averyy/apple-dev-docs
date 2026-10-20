# GetAddress

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the address of the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t GetAddress(uint8_t *address) const;
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `address`: A pointer to a variable. On output, the variable contains the device’s address.

## See Also

### Getting Device Information
- [GetSpeed](./getspeed.md)
  Retrieves the device’s operational speed.
- [GetFrameNumber](./getframenumber.md)
  Gets the current frame number of the USB controller.
- [GetPortStatus](./getportstatus.md)
  Returns the current port status of the device.
- [tIOUSBHostConnectionSpeed](../tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.
- [tIOUSBHostPortStatus](../tiousbhostportstatus.md)
  Constants indicating the state of a port.
- [tIOUSBHostPortType](../tiousbhostporttype.md)
  Constants indicating a port’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/getaddress)*