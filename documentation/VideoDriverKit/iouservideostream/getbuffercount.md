# GetBufferCount

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the number of buffers in the buffer queue.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
uint32_t GetBufferCount();
```

## See Also

### Working with video buffers
- [GetBufferList](./getbufferlist.md)
  Gets an array containing all the buffers in the video stream.
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

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getbuffercount)*