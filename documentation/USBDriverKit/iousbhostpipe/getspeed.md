# GetSpeed

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the device’s operational speed.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t GetSpeed(uint8_t *speed) const;
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `speed`: A pointer to a variable. On output, the variable contains the operational speed of the device. For a list of possible values, see [`tIOUSBHostConnectionSpeed`](../tiousbhostconnectionspeed.md).

## See Also

### Getting the Device Attributes
- [GetDeviceAddress](./getdeviceaddress.md)
  Retrieves the address of the device.
- [tIOUSBHostConnectionSpeed](../tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/getspeed)*