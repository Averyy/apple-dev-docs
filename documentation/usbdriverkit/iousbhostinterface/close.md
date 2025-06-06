# Close

**Framework**: USBDriverKit  
**Kind**: method

Closes the session to the host interface.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t Close(IOService * forClient, IOOptionBits options);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

This method closes a session to an interface that you previously opened using the [`Open`](iousbhostinterface/open.md) method. The method acquires the service’s workloop lock, and aborts any I/O for the interface and its endpoints. This method may also call [`commandSleep`](https://developer.apple.com/documentation/kernel/iocommandgate/1573818-commandsleep) to allow for the processing of aborted I/O before returning.

## Parameters

- `forClient`: The service object that is closing the session.
- `options`: Options to use when closing the service. Specify   for this parameter.

## See Also

- [Open](iousbhostinterface/open.md)
  Opens a session to the host interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/close)*