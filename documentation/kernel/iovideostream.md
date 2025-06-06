# IOVideoStream

**Framework**: Kernel  
**Kind**: cl

A class representing a stream of video data buffers passed from kernel to user space and back again.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class IOVideoStream : IOStream
```

#### Overview

The IOVideoStream class defines a mechanism for moving buffers of data from kernel space to user space or vice-versa. The policy for which direction the data flows and the nature of the data is left up the the implementer of the driver which uses IOStream.

Although it is expected that the client of an IOVideoStream will be in user space, this is not required.

References to "output" mean "from the IOVideoStream to the user client", and "input" means "from the user client to the IOVideoStream."

## Topics

### Miscellaneous
- [getStreamMode](iovideostream/1809380-getstreammode.md)
  Returns the mode of the stream, either input or output.
- [initWithBuffers](iovideostream/1809391-initwithbuffers.md)
- [setStreamMode](iovideostream/1809395-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](iovideostream/1809402-startstream.md)
  Start sending data on a stream.
- [stopStream](iovideostream/1809407-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](iovideostream/1809411-suspendstream.md)
  Temporarily suspend data flow on the stream.
- [withBuffers](iovideostream/1809420-withbuffers.md)
### Instance Methods
- [- getDevice](iovideostream/1552971-getdevice.md)
- [- getMetaClass](iovideostream/1552968-getmetaclass.md)
- [- getStreamMode](iovideostream/1552977-getstreammode.md)
- [- initWithBuffers](iovideostream/1552970-initwithbuffers.md)
- [- setStreamMode](iovideostream/1552972-setstreammode.md)
- [- startStream](iovideostream/1552976-startstream.md)
- [- stopStream](iovideostream/1552969-stopstream.md)
- [- suspendStream](iovideostream/1552973-suspendstream.md)
### Type Methods
- [+ withBuffers](iovideostream/1552975-withbuffers.md)

## Relationships

### Inherits From
- [IOStream](iostream.md)

## See Also

- [IOVideoDevice](iovideodevice.md)
  A class that represents a video device.
- [IONVRAMController](ionvramcontroller.md)
- [IOVideoControlDictionary](iovideocontroldictionary.md)
- [IOVideoStreamDictionary](iovideostreamdictionary.md)
- [IOVideoStreamFormatDictionary](iovideostreamformatdictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideostream)*