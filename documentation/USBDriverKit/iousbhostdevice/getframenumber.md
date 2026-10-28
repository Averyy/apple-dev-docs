# GetFrameNumber

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the current frame number of the USB controller.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t GetFrameNumber(uint64_t *frameNumber, uint64_t *theTime);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Discussion

This method returns the current frame number of the USB controller, omitting the microframe. Use this information to schedule future isochronous requests.

## Parameters

- `frameNumber`: A pointer to a variable. On return, this variable contains the current frame number.
- `theTime`: A pointer to a variable. On return, this variable contains the current time.

## See Also

### Getting Device Information
- [GetAddress](./getaddress.md)
  Returns the address of the device.
- [GetSpeed](./getspeed.md)
  Retrieves the device’s operational speed.
- [GetPortStatus](./getportstatus.md)
  Returns the current port status of the device.
- [tIOUSBHostConnectionSpeed](../tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.
- [tIOUSBHostPortStatus](../tiousbhostportstatus.md)
  Constants indicating the state of a port.
- [tIOUSBHostPortType](../tiousbhostporttype.md)
  Constants indicating a port’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/getframenumber)*