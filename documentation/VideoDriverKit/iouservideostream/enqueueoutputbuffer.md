# enqueueOutputBuffer

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t enqueueOutputBuffer(IOUserVideoBuffer *buffer, uint32_t dataOffset, uint32_t dataLength, uint32_t controlOffset, uint32_t controlLength);
```

## Discussion

A convenience method for enqueueing a buffer.

## Parameters

- `buffer`: 
- `dataOffset`: 
- `dataLength`: 
- `controlOffset`: 
- `controlLength`: 

## See Also

### Working with video buffers
- [GetBufferCount](./getbuffercount.md)
  Returns the number of buffers in the buffer queue.
- [GetBufferList](./getbufferlist.md)
  Gets an array containing all the buffers in the video stream.
- [GetBufferWithID](./getbufferwithid.md)
- [addBuffer](./addbuffer.md)
  Add a buffer to a video stream.
- [addBuffers](./addbuffers.md)
- [IOUserVideoBuffer](../iouservideobuffer.md)
- [removeAllBuffers](./removeallbuffers.md)
  Removes all buffers from the video stream.
- [SendOutputBufferNotification](./sendoutputbuffernotification.md)
  Sends a notification to the host that data is available for reading on the output queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/enqueueoutputbuffer)*