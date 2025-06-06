# Abort

**Framework**: USBDriverKit  
**Kind**: method

Aborts all of the pipe’s pending I/O requests.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t Abort(IOOptionBits options, kern_return_t withError, IOService * forClient);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If the `options` argument includes `kAbortSynchronous`, this method blocks all new I/O requests except those submitted by an aborted completion routine.

## Parameters

- `options`: Options for how to abort the requests. For a list of possible values, see  .
- `withError`: The error value to report for each request. Specify   for this parameter.
- `forClient`: The service that initiated the requests. Specify a non   value for this parameter only for pipes associated with a control endpoint; specify   for other endpoint types. For a control endpoint, you can also specify   to abort all requests.

## See Also

- [IOUSBAbortOptions](iousbabortoptions.md)
  Options to use when aborting an I/O request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/abort)*