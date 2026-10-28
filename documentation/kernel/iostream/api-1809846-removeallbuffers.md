# removeAllBuffers()

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOItemCount getBufferCount(
 void );
```

## Return Value

Returns kIOReturnSuccess if all the buffers were successfully removed. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.

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
- [removeBuffer(IOStreamBuffer *)](./api-1809852-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.
- [removeBuffer(IOStreamBufferID)](./api-1809860-removebuffer.md)
  Removes a buffer from the stream. Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809846-removeallbuffers)*