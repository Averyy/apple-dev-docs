# IOUserVideoBuffer

**Framework**: VideoDriverKit  
**Kind**: class

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoBuffer;
```

## Topics

### Creating a video buffer
- [Create](iouservideobuffer/create.md)
- [init](iouservideobuffer/init.md)
- [IOUserVideoDriver](iouservideodriver.md)
### Freeing a video buffer
- [free](iouservideobuffer/free.md)
### Getting information about the class
- [GetClassID](iouservideobuffer/getclassid.md)
- [GetBaseClassID](iouservideobuffer/getbaseclassid.md)
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
### Working with memory descriptors
- [SetDataMemoryDescriptor](iouservideobuffer/setdatamemorydescriptor.md)
- [GetDataMemoryDescriptor](iouservideobuffer/getdatamemorydescriptor.md)
- [SetControlMemoryDescriptor](iouservideobuffer/setcontrolmemorydescriptor.md)
- [GetControlMemoryDescriptor](iouservideobuffer/getcontrolmemorydescriptor.md)
### Accessing buffer ID
- [getBufferID](iouservideobuffer/getbufferid.md)
- [setBufferID](iouservideobuffer/setbufferid.md)
- [IOStreamBufferID](iostreambufferid.md)
- [kIOStreamBufferIDMask](kiostreambufferidmask.md)

## Relationships

### Inherits From
- [IOUserVideoObject](iouservideoobject.md)

## See Also

- [GetBufferCount](iouservideostream/getbuffercount.md)
- [GetBufferList](iouservideostream/getbufferlist.md)
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffer](iouservideostream/addbuffer.md)
- [addBuffers](iouservideostream/addbuffers.md)
- [enqueueOutputBuffer](iouservideostream/enqueueoutputbuffer.md)
- [removeAllBuffers](iouservideostream/removeallbuffers.md)
- [SendOutputBufferNotification](iouservideostream/sendoutputbuffernotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobuffer)*