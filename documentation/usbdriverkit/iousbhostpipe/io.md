# IO

**Framework**: USBDriverKit  
**Kind**: method

Performs a synchronous request on a bulk or interrupt endpoint.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t IO(IOMemoryDescriptor * dataBuffer, uint32_t dataBufferLength, uint32_t * bytesTransferred, uint32_t completionTimeoutMs);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

This method acquires the service’s workloop lock and performs an appropriate USB I/O request on the device. The method waits for the request to complete, and may call [`commandSleep`](https://developer.apple.com/documentation/kernel/iocommandgate/1573818-commandsleep) during that time.

## Parameters

- `dataBuffer`: The data buffer to use for the request. When transferring data to the device, this buffer contains the data to send. When receiving data from the device, this buffer is empty initially.
- `dataBufferLength`: The length of the data buffer.
- `bytesTransferred`: A pointer to a variable. On output, this variable contains the number of bytes that were actually transferred.
- `completionTimeoutMs`: The timeout value in milliseconds. Specify   if you don’t want the request to time out. You must specify   when transferring data on an interrupt endpoint.

## See Also

- [AsyncIO](iousbhostpipe/asyncio.md)
  Enqueues an asynchronous request on a bulk or interrupt endpoint.
- [CompleteAsyncIO](iousbhostpipe/completeasyncio.md)
  Handles the completion of an asynchronous I/O request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/io)*