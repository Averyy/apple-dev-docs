# SendOutputBufferNotification

**Framework**: VideoDriverKit  
**Kind**: method

Sends a notification to the host that data is available for reading on the output queue.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SendOutputBufferNotification();
```

#### Return Value

`kIOReturnSuccess` if the notification was successfully sent.

#### Discussion

This will result in the user’s output handler being called, if they registered one.

## See Also

- [GetBufferCount](iouservideostream/getbuffercount.md)
  Returns the number of buffers in the buffer queue.
- [GetBufferList](iouservideostream/getbufferlist.md)
  Gets an array containing all the buffers in the video stream.
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffer](iouservideostream/addbuffer.md)
  Add a buffer to a video stream.
- [addBuffers](iouservideostream/addbuffers.md)
- [enqueueOutputBuffer](iouservideostream/enqueueoutputbuffer.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [removeAllBuffers](iouservideostream/removeallbuffers.md)
  Removes all buffers from the video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/sendoutputbuffernotification)*