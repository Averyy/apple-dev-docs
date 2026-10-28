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

### Configuring the Interface
- [GetPortStatus](./getportstatus.md)
  Gets the current port status.
- [SelectAlternateSetting](./selectalternatesetting.md)
  Selects an alternative setting for this interface.
- [GetIdlePolicy](./getidlepolicy.md)
  Gets the current idle suspend timeout for the interface.
- [SetIdlePolicy](./setidlepolicy.md)
  Sets the desired idle suspend timeout for the interface.
- [tIOUSBHostPortStatus](../tiousbhostportstatus.md)
  Constants indicating the state of a port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/getframenumber)*