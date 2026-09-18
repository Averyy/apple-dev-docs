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
  A video driver.
### Freeing a video buffer
- [free](iouservideobuffer/free.md)
### Getting information about the class
- [GetClassID](iouservideobuffer/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideobuffer/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Working with memory descriptors
- [SetDataMemoryDescriptor](iouservideobuffer/setdatamemorydescriptor.md)
  Sets a new IOMemoryDescriptor to use for video IO on the IOUserVideoStream.
- [GetDataMemoryDescriptor](iouservideobuffer/getdatamemorydescriptor.md)
  Gets the memory descriptor used for video IO that was initialized with or set on the video stream.
- [SetControlMemoryDescriptor](iouservideobuffer/setcontrolmemorydescriptor.md)
  Sets a new IOMemoryDescriptor to use for video IO on the IOUserVideoStream.
- [GetControlMemoryDescriptor](iouservideobuffer/getcontrolmemorydescriptor.md)
  Gets the memory descriptior used for video IO that was initialized with or set on the video stream.
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
  Returns the number of buffers in the buffer queue.
- [GetBufferList](iouservideostream/getbufferlist.md)
  Gets an array containing all the buffers in the video stream.
- [GetBufferWithID](iouservideostream/getbufferwithid.md)
- [addBuffer](iouservideostream/addbuffer.md)
  Add a buffer to a video stream.
- [addBuffers](iouservideostream/addbuffers.md)
- [enqueueOutputBuffer](iouservideostream/enqueueoutputbuffer.md)
- [removeAllBuffers](iouservideostream/removeallbuffers.md)
  Removes all buffers from the video stream.
- [SendOutputBufferNotification](iouservideostream/sendoutputbuffernotification.md)
  Sends a notification to the host that data is available for reading on the output queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobuffer)*