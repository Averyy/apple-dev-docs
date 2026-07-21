# enqueueOutputBuffer

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t enqueueOutputBuffer(IOUserVideoBuffer *buffer, uint32_t dataOffset, uint32_t dataLength, uint32_t controlOffset, uint32_t controlLength);
```

#### Discussion

A convenience method for enqueueing a buffer.

## Parameters

- `buffer`: 
- `dataOffset`: 
- `dataLength`: 
- `controlOffset`: 
- `controlLength`: 

## See Also

- [GetBufferCount](iouservideostream/getbuffercount.md)
- [GetBufferList](iouservideostream/getbufferlist.md)
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffer](iouservideostream/addbuffer.md)
- [addBuffers](iouservideostream/addbuffers.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [removeAllBuffers](iouservideostream/removeallbuffers.md)
- [SendOutputBufferNotification](iouservideostream/sendoutputbuffernotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/enqueueoutputbuffer)*