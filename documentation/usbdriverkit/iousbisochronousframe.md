# IOUSBIsochronousFrame

**Framework**: USBDriverKit  
**Kind**: struct

A structure representing a single frame in an isochronous transfer.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
struct IOUSBIsochronousFrame;
```

## Topics

### Getting the Frame Properties
- [status](iousbisochronousframe/status.md)
  The completion status for this individual frame.
- [requestCount](iousbisochronousframe/requestcount.md)
  The number of bytes to transfer for this frame.
- [completeCount](iousbisochronousframe/completecount.md)
  The number of bytes actually transferred for this frame.
- [reserved](iousbisochronousframe/reserved.md)
  Reserved for future use.
- [timeStamp](iousbisochronousframe/timestamp.md)
  The frame’s observed completion time.

## See Also

- [IsochIO](iousbhostpipe/isochio.md)
  Performs a synchronous or asynchronous request on an isochronous endpoint.
- [CompleteAsyncIsochIO](iousbhostpipe/completeasyncisochio.md)
  Handles the completion of an asynchronous request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbisochronousframe)*