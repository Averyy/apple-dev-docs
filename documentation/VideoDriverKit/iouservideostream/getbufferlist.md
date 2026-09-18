# GetBufferList

**Framework**: VideoDriverKit  
**Kind**: method

Gets an array containing all the buffers in the video stream.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<OSArray> GetBufferList();
```

#### Return Value

All the buffers in the stream, in order of their buffer identifier.

## See Also

- [GetBufferCount](iouservideostream/getbuffercount.md)
  Returns the number of buffers in the buffer queue.
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffer](iouservideostream/addbuffer.md)
  Add a buffer to a video stream.
- [addBuffers](iouservideostream/addbuffers.md)
- [enqueueOutputBuffer](iouservideostream/enqueueoutputbuffer.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [removeAllBuffers](iouservideostream/removeallbuffers.md)
  Removes all buffers from the video stream.
- [SendOutputBufferNotification](iouservideostream/sendoutputbuffernotification.md)
  Sends a notification to the host that data is available for reading on the output queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getbufferlist)*