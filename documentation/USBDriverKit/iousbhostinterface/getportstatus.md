# GetPortStatus

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the current port status.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t GetPortStatus(uint32_t *portStatus);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `portStatus`: A pointer to a variable. On return, the variable contains the port status. For a list of possible port status values, see [`tIOUSBHostPortStatus`](../tiousbhostportstatus.md).

## See Also

### Configuring the Interface
- [GetFrameNumber](./getframenumber.md)
  Gets the current frame number of the USB controller.
- [SelectAlternateSetting](./selectalternatesetting.md)
  Selects an alternative setting for this interface.
- [GetIdlePolicy](./getidlepolicy.md)
  Gets the current idle suspend timeout for the interface.
- [SetIdlePolicy](./setidlepolicy.md)
  Sets the desired idle suspend timeout for the interface.
- [tIOUSBHostPortStatus](../tiousbhostportstatus.md)
  Constants indicating the state of a port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/getportstatus)*