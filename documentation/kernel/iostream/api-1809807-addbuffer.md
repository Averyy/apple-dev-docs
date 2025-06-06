# addBuffer

**Framework**: Kernel  
**Kind**: instm

Add a buffer to an IOStream.

## Declaration

```swift
virtual IOReturn addBuffer(
 IOStreamBuffer *buffer);
```

#### Overview

Adds an IOStreamBuffer to an IOStream. It will be added to the end of the buffer array, so the buffer ID of existing buffers will not change.

## Parameters

- `buffer`: 

## See Also

- [addBuffers](iostream/1809814-addbuffers.md)
- [getBufferCount](iostream/1809821-getbuffercount.md)
- [getBuffers](iostream/1809828-getbuffers.md)
  Get an array containing all the buffers in the stream.
- [getBufferWithID](iostream/1809834-getbufferwithid.md)
- [removeAllBuffers()](iostream/1809839-removeallbuffers.md)
- [removeAllBuffers()](iostream/1809846-removeallbuffers.md)
- [removeBuffer(IOStreamBuffer *)](iostream/1809852-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.
- [removeBuffer(IOStreamBufferID)](iostream/1809860-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809807-addbuffer)*