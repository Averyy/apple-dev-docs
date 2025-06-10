# getStream

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOVideoStream* getStream(
 UInt32streamIndex);
```

#### Return_value

Returns the number of streams of the device.

## Parameters

- `streamIndex`: The index for which the underlying stream is desired.

## See Also

- [getStreamCount](iovideodevice/1809412-getstreamcount.md)
- [newUserClient](iovideodevice/1809416-newuserclient.md)
  See the documentation for the IOService method newUserClient.
- [setStreamMode](iovideodevice/1809422-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](iovideodevice/1809424-startstream.md)
  Start sending data on a stream.
- [stopStream](iovideodevice/1809428-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](iovideodevice/1809431-suspendstream.md)
  Temporarily suspend data flow on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideodevice/1809409-getstream)*