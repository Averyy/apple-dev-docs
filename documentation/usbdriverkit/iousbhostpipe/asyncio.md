# AsyncIO

**Framework**: USBDriverKit  
**Kind**: method

Enqueues an asynchronous request on a bulk or interrupt endpoint.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t AsyncIO(IOMemoryDescriptor * dataBuffer, uint32_t dataBufferLength, OSAction * completion, uint32_t completionTimeoutMs);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

This method performs an appropriate USB I/O request on the device and notifies your completion handler asynchronously when that transfer completes.

## Parameters

- `dataBuffer`: The data buffer to use for the request. When transferring data to the device, this buffer contains the data to send. When receiving data from the device, this buffer is empty initially.
- `dataBufferLength`: The length of the data buffer.
- `completion`: An action object containing the callback method to execute when the transfer finishes.
- `completionTimeoutMs`: The timeout value in milliseconds. Specify   if you don’t want the request to time out. You must specify   when transferring data on an interrupt endpoint.

## See Also

- [IO](iousbhostpipe/io.md)
  Performs a synchronous request on a bulk or interrupt endpoint.
- [CompleteAsyncIO](iousbhostpipe/completeasyncio.md)
  Handles the completion of an asynchronous I/O request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/asyncio)*