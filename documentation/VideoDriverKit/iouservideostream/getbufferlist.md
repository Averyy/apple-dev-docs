# GetBufferList

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
OSSharedPtr<OSArray> GetBufferList();
```

#### Discussion

Get an array containing all the buffers in the IOUserVideoStream.

Returns an OSArray containing all the buffers in the stream in order of their buffer ID.

## See Also

- [GetBufferCount](iouservideostream/getbuffercount.md)
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffer](iouservideostream/addbuffer.md)
- [addBuffers](iouservideostream/addbuffers.md)
- [enqueueOutputBuffer](iouservideostream/enqueueoutputbuffer.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [removeAllBuffers](iouservideostream/removeallbuffers.md)
- [SendOutputBufferNotification](iouservideostream/sendoutputbuffernotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getbufferlist)*