# startStream

**Framework**: Kernel  
**Kind**: instm

Start sending data on a stream.

## Declaration

```swift
virtual IOReturn startStream(
 void);
```

#### Return_value

Returns kIOReturnSuccess if the stream was successfully started.

## See Also

- [getStreamMode](iovideostream/1809380-getstreammode.md)
  Returns the mode of the stream, either input or output.
- [initWithBuffers](iovideostream/1809391-initwithbuffers.md)
- [setStreamMode](iovideostream/1809395-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [stopStream](iovideostream/1809407-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](iovideostream/1809411-suspendstream.md)
  Temporarily suspend data flow on the stream.
- [withBuffers](iovideostream/1809420-withbuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideostream/1809402-startstream)*