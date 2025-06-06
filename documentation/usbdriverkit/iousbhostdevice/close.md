# Close

**Framework**: USBDriverKit  
**Kind**: method

Closes the session to the host device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t Close(IOService * forClient, IOOptionBits options);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

This method closes a session to a device that you previously opened using the [`Open`](iousbhostdevice/open.md) method. The method acquires the service’s workloop lock, and aborts any I/O initiated by the client service. This method may call [`commandSleep`](https://developer.apple.com/documentation/kernel/iocommandgate/1573818-commandsleep) to allow for the processing of aborted I/O before returning.

## Parameters

- `forClient`: The service object that is closing the session.
- `options`: Options to use when closing the service. Specify   for this parameter.

## See Also

- [Open](iousbhostdevice/open.md)
  Opens a session to a host device.
- [Reset](iousbhostdevice/reset.md)
  Terminates the device and attempts to reenumerate it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/close)*