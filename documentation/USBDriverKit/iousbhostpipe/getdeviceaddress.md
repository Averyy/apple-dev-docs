# GetDeviceAddress

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the address of the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t GetDeviceAddress(uint8_t *address) const;
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `address`: A pointer to a variable. On output, the variable contains the device’s address.

## See Also

### Getting the Device Attributes
- [GetSpeed](./getspeed.md)
  Retrieves the device’s operational speed.
- [tIOUSBHostConnectionSpeed](../tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/getdeviceaddress)*