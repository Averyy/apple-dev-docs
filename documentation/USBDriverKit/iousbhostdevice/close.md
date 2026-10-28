# Close

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Closes the session to the host device.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t Close(IOService *forClient, IOOptionBits options);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Discussion

This method closes a session to a device that you previously opened using the [`Open`](./open.md) method. The method acquires the service’s workloop lock, and aborts any I/O initiated by the client service. This method may call [`commandSleep`](../../kernel/iocommandgate/api-1573818-commandsleep.md) to allow for the processing of aborted I/O before returning.

## Parameters

- `forClient`: The service object that is closing the session.
- `options`: Options to use when closing the service. Specify `0` for this parameter.

## See Also

### Managing the Device Session
- [Open](./open.md)
  Opens a session to a host device.
- [Reset](./reset.md)
  Terminates the device and attempts to reenumerate it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/close)*