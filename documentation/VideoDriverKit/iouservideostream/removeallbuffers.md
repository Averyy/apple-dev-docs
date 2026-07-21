# removeAllBuffers

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t removeAllBuffers();
```

#### Return Value

Returns kIOReturnSuccess if all the buffers were successfully removed.   Buffers cannot be removed while the stream is open, as this will change the buffer IDs of existing buffers.

## See Also

- [GetBufferCount](iouservideostream/getbuffercount.md)
- [GetBufferList](iouservideostream/getbufferlist.md)
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffer](iouservideostream/addbuffer.md)
- [addBuffers](iouservideostream/addbuffers.md)
- [enqueueOutputBuffer](iouservideostream/enqueueoutputbuffer.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [SendOutputBufferNotification](iouservideostream/sendoutputbuffernotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/removeallbuffers)*