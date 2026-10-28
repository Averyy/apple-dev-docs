# GetIdlePolicy

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the current idle suspend timeout for the interface.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t GetIdlePolicy(uint32_t *deviceIdleTimeout);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `deviceIdleTimeout`: A pointer to a variable. On return, the variable contains the amount of time, in milliseconds, to wait after all pipes are idle before suspending the device.

## See Also

### Configuring the Interface
- [GetFrameNumber](./getframenumber.md)
  Gets the current frame number of the USB controller.
- [GetPortStatus](./getportstatus.md)
  Gets the current port status.
- [SelectAlternateSetting](./selectalternatesetting.md)
  Selects an alternative setting for this interface.
- [SetIdlePolicy](./setidlepolicy.md)
  Sets the desired idle suspend timeout for the interface.
- [tIOUSBHostPortStatus](../tiousbhostportstatus.md)
  Constants indicating the state of a port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/getidlepolicy)*