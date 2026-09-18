# addBuffer

**Framework**: VideoDriverKit  
**Kind**: method

Add a buffer to a video stream.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t addBuffer(IOUserVideoBuffer *buffer);
```

#### Discussion

Adds an IOUserVideoBuffer to an IOUserVideoStream. It will be added to the end of the buffer array, so the buffer ID of existing buffers will not change.

## See Also

- [GetBufferCount](iouservideostream/getbuffercount.md)
  Returns the number of buffers in the buffer queue.
- [GetBufferList](iouservideostream/getbufferlist.md)
  Gets an array containing all the buffers in the video stream.
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffers](iouservideostream/addbuffers.md)
- [enqueueOutputBuffer](iouservideostream/enqueueoutputbuffer.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [removeAllBuffers](iouservideostream/removeallbuffers.md)
  Removes all buffers from the video stream.
- [SendOutputBufferNotification](iouservideostream/sendoutputbuffernotification.md)
  Sends a notification to the host that data is available for reading on the output queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/addbuffer)*