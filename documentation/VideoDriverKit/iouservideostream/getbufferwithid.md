# GetBufferWithID

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit 27.0+

## Declaration

```c
OSSharedPtr<IOUserVideoBuffer> GetBufferWithID(uint32_t bufferID);
```

## Return Value

The buffer, or `NULL` if the buffer identifier was invalid for this stream.

## Parameters

- `bufferID`: The buffer identifier of the buffer in the queue.

## See Also

### Working with video buffers
- [GetBufferCount](./getbuffercount.md)
  Returns the number of buffers in the buffer queue.
- [GetBufferList](./getbufferlist.md)
  Gets an array containing all the buffers in the video stream.
- [addBuffer](./addbuffer.md)
  Add a buffer to a video stream.
- [addBuffers](./addbuffers.md)
- [enqueueOutputBuffer](./enqueueoutputbuffer.md)
- [IOUserVideoBuffer](../iouservideobuffer.md)
- [removeAllBuffers](./removeallbuffers.md)
  Removes all buffers from the video stream.
- [SendOutputBufferNotification](./sendoutputbuffernotification.md)
  Sends a notification to the host that data is available for reading on the output queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getbufferwithid)*