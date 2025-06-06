# GetPortStatus

**Framework**: USBDriverKit  
**Kind**: method

Gets the current port status.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t GetPortStatus(uint32_t * portStatus);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `portStatus`: A pointer to a variable. On return, the variable contains the port status. For a list of possible port status values, see  .

## See Also

- [GetFrameNumber](iousbhostinterface/getframenumber.md)
  Gets the current frame number of the USB controller.
- [SelectAlternateSetting](iousbhostinterface/selectalternatesetting.md)
  Selects an alternative setting for this interface.
- [GetIdlePolicy](iousbhostinterface/getidlepolicy.md)
  Gets the current idle suspend timeout for the interface.
- [SetIdlePolicy](iousbhostinterface/setidlepolicy.md)
  Sets the desired idle suspend timeout for the interface.
- [tIOUSBHostPortStatus](tiousbhostportstatus.md)
  Constants indicating the state of a port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/getportstatus)*