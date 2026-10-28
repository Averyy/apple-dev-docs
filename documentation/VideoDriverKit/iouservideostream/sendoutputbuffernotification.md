# SendOutputBufferNotification

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sends a notification to the host that data is available for reading on the output queue.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SendOutputBufferNotification();
```

## Return Value

`kIOReturnSuccess` if the notification was successfully sent.

## Discussion

This will result in the user’s output handler being called, if they registered one.

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
- [enqueueOutputBuffer](./enqueueoutputbuffer.md)
- [IOUserVideoBuffer](../iouservideobuffer.md)
- [removeAllBuffers](./removeallbuffers.md)
  Removes all buffers from the video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/sendoutputbuffernotification)*