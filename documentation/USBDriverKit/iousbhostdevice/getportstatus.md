# GetPortStatus

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the current port status of the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t GetPortStatus(uint32_t *portStatus);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `portStatus`: A pointer to a variable. On output, the variable contains the port status. For a list of possible values, see [`tIOUSBHostPortStatus`](../tiousbhostportstatus.md).

## See Also

### Getting Device Information
- [GetAddress](./getaddress.md)
  Returns the address of the device.
- [GetSpeed](./getspeed.md)
  Retrieves the device’s operational speed.
- [GetFrameNumber](./getframenumber.md)
  Gets the current frame number of the USB controller.
- [tIOUSBHostConnectionSpeed](../tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.
- [tIOUSBHostPortStatus](../tiousbhostportstatus.md)
  Constants indicating the state of a port.
- [tIOUSBHostPortType](../tiousbhostporttype.md)
  Constants indicating a port’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/getportstatus)*