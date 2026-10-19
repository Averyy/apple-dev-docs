# GetBufferWithID

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
OSSharedPtr<IOUserVideoBuffer> GetBufferWithID(uint32_t bufferID);
```

#### Return Value

The buffer, or `NULL` if the buffer identifier was invalid for this stream.

## Parameters

- `bufferID`: The buffer identifier of the buffer in the queue.

## See Also

- [GetBufferCount](iouservideostream/getbuffercount.md)
  Returns the number of buffers in the buffer queue.
- [GetBufferList](iouservideostream/getbufferlist.md)
  Gets an array containing all the buffers in the video stream.
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

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getbufferwithid)*