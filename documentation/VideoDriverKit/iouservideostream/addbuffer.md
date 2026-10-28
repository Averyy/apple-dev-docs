# addBuffer

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Add a buffer to a video stream.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t addBuffer(IOUserVideoBuffer *buffer);
```

## Discussion

Adds an IOUserVideoBuffer to an IOUserVideoStream. It will be added to the end of the buffer array, so the buffer ID of existing buffers will not change.

## See Also

### Working with video buffers
- [GetBufferCount](./getbuffercount.md)
  Returns the number of buffers in the buffer queue.
- [GetBufferList](./getbufferlist.md)
  Gets an array containing all the buffers in the video stream.
- [GetBufferWithID](./getbufferwithid.md)
- [addBuffers](./addbuffers.md)
- [enqueueOutputBuffer](./enqueueoutputbuffer.md)
- [IOUserVideoBuffer](../iouservideobuffer.md)
- [removeAllBuffers](./removeallbuffers.md)
  Removes all buffers from the video stream.
- [SendOutputBufferNotification](./sendoutputbuffernotification.md)
  Sends a notification to the host that data is available for reading on the output queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/addbuffer)*