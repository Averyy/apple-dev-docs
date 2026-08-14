# Open

**Framework**: USBDriverKit  
**Kind**: method

Opens a session to a host device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
virtual kern_return_t Open(IOService *forClient, IOOptionBits options, uintptr_t arg);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

#### Discussion

This method opens a session to the [`IOUSBHostDevice`](iousbhostdevice.md), and acquires the service’s workloop lock. Child [`IOUSBHostInterface`](iousbhostinterface.md) objects may open simultaneous sessions, but only one [`IOUSBHostDevice`](iousbhostdevice.md) object at a time may open a session to the device.

## Parameters

- `forClient`: The service object that is opening the session.
- `options`: The options to use when opening the session. Specify `0` for this parameter.
- `arg`: Additional arguments to the function. Specify `NULL` for this parameter.

## See Also

- [Close](iousbhostdevice/close.md)
  Closes the session to the host device.
- [Reset](iousbhostdevice/reset.md)
  Terminates the device and attempts to reenumerate it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/open)*