# IsochIO

**Framework**: USBDriverKit  
**Kind**: method

Performs a synchronous or asynchronous request on an isochronous endpoint.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t IsochIO(IOMemoryDescriptor * dataBuffer, IOMemoryDescriptor * frameList, uint64_t firstFrameNumber, OSAction * completion);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Use this method to issue isochronous requests. Allocate and initialize an array of [`IOUSBIsochronousFrame`](iousbisochronousframe.md) structures, which describe the frames to transfer. See [`IOUSBIsochronousFrame`](iousbisochronousframe.md) for information regarding structure initialization requirements and usage.

## Parameters

- `dataBuffer`: The buffer to store the data. When transferring data to the device, this buffer contains the data to send. When receiving data from the device, this buffer is empty initially.
- `frameList`: A valid memory descriptor containing the frame list, which is an array of   structures. For example, a frame list with 8 frames should be of size  .
- `firstFrameNumber`: The starting frame number for the request. You can get the current frame number from the   method of   or  . Specify   to begin the transfer on the next available frame (XHCI only).
- `completion`: An optional completion handler. To create a synchronous I/O request, specify  . To create an asynchronous request, provide an appropriate action method with your callback routine. This method copies your action object, so you can allocate that object on the stack if you prefer.

## See Also

- [CompleteAsyncIsochIO](iousbhostpipe/completeasyncisochio.md)
  Handles the completion of an asynchronous request.
- [IOUSBIsochronousFrame](iousbisochronousframe.md)
  A structure representing a single frame in an isochronous transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/isochio)*