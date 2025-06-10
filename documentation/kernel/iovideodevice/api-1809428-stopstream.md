# stopStream

**Framework**: Kernel  
**Kind**: instm

Stop sending data on a stream.

## Declaration

```swift
virtual IOReturn stopStream(
 IOVideoStream *stream);
```

#### Return_value

Returns kIOReturnSuccess if the stream was successfully started.

#### Overview

This must be implemented by a subclass.

## See Also

- [getStream](iovideodevice/1809409-getstream.md)
- [getStreamCount](iovideodevice/1809412-getstreamcount.md)
- [newUserClient](iovideodevice/1809416-newuserclient.md)
  See the documentation for the IOService method newUserClient.
- [setStreamMode](iovideodevice/1809422-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](iovideodevice/1809424-startstream.md)
  Start sending data on a stream.
- [suspendStream](iovideodevice/1809431-suspendstream.md)
  Temporarily suspend data flow on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideodevice/1809428-stopstream)*