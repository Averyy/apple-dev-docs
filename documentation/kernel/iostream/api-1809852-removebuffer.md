# removeBuffer(IOStreamBuffer *)

**Framework**: Kernel  
**Kind**: instm

Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.

## Declaration

```cpp
virtual IOReturn removeBuffer(
 IOStreamBuffer *buffer);
```

## Return Value

Returns kIOReturnSuccess if the buffer was removed, or kIOReturnNotFound if the buffer was not in this stream.

## Parameters

- `buffer`: A pointer to an IOStreamBuffer object in the stream.

## See Also

### Managing buffers in an IOStream
- [addBuffer](./api-1809807-addbuffer.md)
  Add a buffer to an IOStream.
- [addBuffers](./api-1809814-addbuffers.md)
- [getBufferCount](./api-1809821-getbuffercount.md)
- [getBuffers](./api-1809828-getbuffers.md)
  Get an array containing all the buffers in the stream.
- [getBufferWithID](./api-1809834-getbufferwithid.md)
- [removeAllBuffers()](./api-1809839-removeallbuffers.md)
- [removeAllBuffers()](./api-1809846-removeallbuffers.md)
- [removeBuffer(IOStreamBufferID)](./api-1809860-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809852-removebuffer)*