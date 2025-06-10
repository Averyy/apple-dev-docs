# suspendStream

**Framework**: Kernel  
**Kind**: instm

Temporarily suspend data flow on the stream.

## Declaration

```swift
virtual IOReturn suspendStream(
 void);
```

#### Return_value

Returns kIOReturnSuccess if the stream was successfully suspended.

## See Also

- [getStreamMode](iovideostream/1809380-getstreammode.md)
  Returns the mode of the stream, either input or output.
- [initWithBuffers](iovideostream/1809391-initwithbuffers.md)
- [setStreamMode](iovideostream/1809395-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](iovideostream/1809402-startstream.md)
  Start sending data on a stream.
- [stopStream](iovideostream/1809407-stopstream.md)
  Stop sending data on a stream.
- [withBuffers](iovideostream/1809420-withbuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideostream/1809411-suspendstream)*