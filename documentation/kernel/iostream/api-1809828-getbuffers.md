# getBuffers

**Framework**: Kernel  
**Kind**: instm

Get an array containing all the buffers in the stream.

## Declaration

```swift
virtual OSArray *getBuffers(
 void );
```

#### Overview

Returns an OSArray containing all the buffers in the stream in order of their buffer ID.

## See Also

- [addBuffer](iostream/1809807-addbuffer.md)
  Add a buffer to an IOStream.
- [addBuffers](iostream/1809814-addbuffers.md)
- [getBufferCount](iostream/1809821-getbuffercount.md)
- [getBufferWithID](iostream/1809834-getbufferwithid.md)
- [removeAllBuffers()](iostream/1809839-removeallbuffers.md)
- [removeAllBuffers()](iostream/1809846-removeallbuffers.md)
- [removeBuffer(IOStreamBuffer *)](iostream/1809852-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.
- [removeBuffer(IOStreamBufferID)](iostream/1809860-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809828-getbuffers)*