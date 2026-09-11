# removeAllBuffers

**Framework**: VideoDriverKit  
**Kind**: method

Removes all buffers from the video stream.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t removeAllBuffers();
```

#### Return Value

`kIOReturnSuccess` if all the buffers were successfully removed.

#### Discussion

Buffers cannot be removed while the stream is open, as this will change the buffer identifiers of existing buffers.

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
- [SendOutputBufferNotification](iouservideostream/sendoutputbuffernotification.md)
  Sends a notification to the host that data is available for reading on the output queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/removeallbuffers)*