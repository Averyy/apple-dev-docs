# SendOutputBufferNotification

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SendOutputBufferNotification();
```

#### Return Value

Returns kIOReturnSuccess if the notification was successfully sent.

#### Discussion

Send a notification to the host that data is available for reading on the output queue.  This will result in the user’s output handler being called, if they registered one.

## See Also

- [GetBufferCount](iouservideostream/getbuffercount.md)
- [GetBufferList](iouservideostream/getbufferlist.md)
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffer](iouservideostream/addbuffer.md)
- [addBuffers](iouservideostream/addbuffers.md)
- [enqueueOutputBuffer](iouservideostream/enqueueoutputbuffer.md)
- [IOUserVideoBuffer](iouservideobuffer.md)
- [removeAllBuffers](iouservideostream/removeallbuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/sendoutputbuffernotification)*