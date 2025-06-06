# removeBuffer(IOStreamBuffer *)

**Framework**: Kernel  
**Kind**: instm

Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.

## Declaration

```swift
virtual IOReturn removeBuffer(
 IOStreamBuffer *buffer);
```

#### Return_value

Returns kIOReturnSuccess if the buffer was removed, or kIOReturnNotFound if the buffer was not in this stream.

## Parameters

- `buffer`: A pointer to an IOStreamBuffer object in the stream.

## See Also

- [addBuffer](iostream/1809807-addbuffer.md)
  Add a buffer to an IOStream.
- [addBuffers](iostream/1809814-addbuffers.md)
- [getBufferCount](iostream/1809821-getbuffercount.md)
- [getBuffers](iostream/1809828-getbuffers.md)
  Get an array containing all the buffers in the stream.
- [getBufferWithID](iostream/1809834-getbufferwithid.md)
- [removeAllBuffers()](iostream/1809839-removeallbuffers.md)
- [removeAllBuffers()](iostream/1809846-removeallbuffers.md)
- [removeBuffer(IOStreamBufferID)](iostream/1809860-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809852-removebuffer)*