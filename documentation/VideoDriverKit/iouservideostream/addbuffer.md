# addBuffer

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t addBuffer(IOUserVideoBuffer *buffer);
```

#### Discussion

Add a buffer to an IOUserVideoStream.

Adds an IOUserVideoBuffer to an IOUserVideoStream.  It will be added to the end of the buffer array, so the buffer ID of existing buffers will not change.

## Parameters

- `buffer`: 

## See Also

- [GetBufferCount](iouservideostream/getbuffercount.md)
- [GetBufferList](iouservideostream/getbufferlist.md)
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffers](iouservideostream/addbuffers.md)
- [enqueueOutputBuffer](iouservideostream/enqueueoutputbuffer.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [removeAllBuffers](iouservideostream/removeallbuffers.md)
- [SendOutputBufferNotification](iouservideostream/sendoutputbuffernotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/addbuffer)*