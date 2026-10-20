# addBuffer

**Framework**: Kernel  
**Kind**: instm

Add a buffer to an IOStream.

## Declaration

```cpp
virtual IOReturn addBuffer(
 IOStreamBuffer *buffer);
```

#### Overview

Adds an IOStreamBuffer to an IOStream. It will be added to the end of the buffer array, so the buffer ID of existing buffers will not change.

## Parameters

- `buffer`: 

## See Also

### Managing buffers in an IOStream
- [addBuffers](./api-1809814-addbuffers.md)
- [getBufferCount](./api-1809821-getbuffercount.md)
- [getBuffers](./api-1809828-getbuffers.md)
  Get an array containing all the buffers in the stream.
- [getBufferWithID](./api-1809834-getbufferwithid.md)
- [removeAllBuffers()](./api-1809839-removeallbuffers.md)
- [removeAllBuffers()](./api-1809846-removeallbuffers.md)
- [removeBuffer(IOStreamBuffer *)](./api-1809852-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.
- [removeBuffer(IOStreamBufferID)](./api-1809860-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809807-addbuffer)*