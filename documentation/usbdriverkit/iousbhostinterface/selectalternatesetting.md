# SelectAlternateSetting

**Framework**: USBDriverKit  
**Kind**: method

Selects an alternative setting for this interface.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t SelectAlternateSetting(uint8_t bAlternateSetting);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Use this method to select an alternative setting for the interface. The system aborts all pending I/O on the interface’s pipes, and closes any open pipes. The system selects the new alternative setting using the `SET_INTERFACE` control request (USB 2.0, section 9.4.10).

## Parameters

- `bAlternateSetting`: The alternative interface number to activate.

## See Also

- [GetFrameNumber](iousbhostinterface/getframenumber.md)
  Gets the current frame number of the USB controller.
- [GetPortStatus](iousbhostinterface/getportstatus.md)
  Gets the current port status.
- [GetIdlePolicy](iousbhostinterface/getidlepolicy.md)
  Gets the current idle suspend timeout for the interface.
- [SetIdlePolicy](iousbhostinterface/setidlepolicy.md)
  Sets the desired idle suspend timeout for the interface.
- [tIOUSBHostPortStatus](tiousbhostportstatus.md)
  Constants indicating the state of a port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/selectalternatesetting)*