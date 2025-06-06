# getBufferWithID

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOStreamBuffer *getBufferWithID(
 IOStreamBufferIDbufferID);
```

#### Return_value

A pointer to an IOStreamBuffer object, or NULL if the buffer ID was invalid for this stream.

## Parameters

- `bufferID`: The ID of the buffer to get.

## See Also

- [addBuffer](iostream/1809807-addbuffer.md)
  Add a buffer to an IOStream.
- [addBuffers](iostream/1809814-addbuffers.md)
- [getBufferCount](iostream/1809821-getbuffercount.md)
- [getBuffers](iostream/1809828-getbuffers.md)
  Get an array containing all the buffers in the stream.
- [removeAllBuffers()](iostream/1809839-removeallbuffers.md)
- [removeAllBuffers()](iostream/1809846-removeallbuffers.md)
- [removeBuffer(IOStreamBuffer *)](iostream/1809852-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.
- [removeBuffer(IOStreamBufferID)](iostream/1809860-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809834-getbufferwithid)*