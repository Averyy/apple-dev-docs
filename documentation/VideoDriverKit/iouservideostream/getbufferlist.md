# GetBufferList

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets an array containing all the buffers in the video stream.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
OSSharedPtr<OSArray> GetBufferList();
```

## Return Value

All the buffers in the stream, in order of their buffer identifier.

## See Also

### Working with video buffers
- [GetBufferCount](./getbuffercount.md)
  Returns the number of buffers in the buffer queue.
- [GetBufferWithID](./getbufferwithid.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getbufferlist)*