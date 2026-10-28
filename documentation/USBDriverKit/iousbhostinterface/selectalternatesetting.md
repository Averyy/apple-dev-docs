# SelectAlternateSetting

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Selects an alternative setting for this interface.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t SelectAlternateSetting(uint8_t bAlternateSetting);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Discussion

Use this method to select an alternative setting for the interface. The system aborts all pending I/O on the interface’s pipes, and closes any open pipes. The system selects the new alternative setting using the `SET_INTERFACE` control request (USB 2.0, section 9.4.10).

## Parameters

- `bAlternateSetting`: The alternative interface number to activate.

## See Also

### Configuring the Interface
- [GetFrameNumber](./getframenumber.md)
  Gets the current frame number of the USB controller.
- [GetPortStatus](./getportstatus.md)
  Gets the current port status.
- [GetIdlePolicy](./getidlepolicy.md)
  Gets the current idle suspend timeout for the interface.
- [SetIdlePolicy](./setidlepolicy.md)
  Sets the desired idle suspend timeout for the interface.
- [tIOUSBHostPortStatus](../tiousbhostportstatus.md)
  Constants indicating the state of a port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/selectalternatesetting)*