# getStreamMode

**Framework**: Kernel  
**Kind**: instm

Returns the mode of the stream, either input or output.

## Declaration

```swift
virtual IOStreamMode getStreamMode(
 void);
```

#### Return_value

The mode of the stream, either kIOStreamModeInput (from user space to kernel space) or the default kIOStreamModeOutput (from kernel space to user space).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideostream/1809380-getstreammode)*