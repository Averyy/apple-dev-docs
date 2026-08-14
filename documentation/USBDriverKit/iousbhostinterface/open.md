# Open

**Framework**: USBDriverKit  
**Kind**: method

Opens a session to the host interface.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
virtual kern_return_t Open(IOService *forClient, IOOptionBits options, uint8_t *arg);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

#### Discussion

This method opens a session to the [`IOUSBHostInterface`](iousbhostinterface.md), and acquires the service’s workloop lock. Only one service at a time may open a session to the interface.

## Parameters

- `forClient`: The service object that is opening the session.
- `options`: The options to use when opening the session. Specify [`kUSBHostOpenOptionSelectAlternateSetting`](https://developer.apple.com/documentation/kernel/3143215-anonymous/kusbhostopenoptionselectalternatesetting) to select an alternative setting for this interface immediately. Specify the alternative setting in the `arg` parameter.
- `arg`: Additional arguments to the function. If you specify [`kUSBHostOpenOptionSelectAlternateSetting`](https://developer.apple.com/documentation/kernel/3143215-anonymous/kusbhostopenoptionselectalternatesetting) for the `options` parameter, use this value to specify the value for the alternative setting; otherwise, specify `NULL`.

## See Also

- [Close](iousbhostinterface/close.md)
  Closes the session to the host interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/open)*