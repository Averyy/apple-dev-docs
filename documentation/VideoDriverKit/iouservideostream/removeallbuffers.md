# removeAllBuffers

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Removes all buffers from the video stream.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t removeAllBuffers();
```

#### Return Value

`kIOReturnSuccess` if all the buffers were successfully removed.

#### Discussion

Buffers cannot be removed while the stream is open, as this will change the buffer identifiers of existing buffers.

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
- [SendOutputBufferNotification](./sendoutputbuffernotification.md)
  Sends a notification to the host that data is available for reading on the output queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/removeallbuffers)*