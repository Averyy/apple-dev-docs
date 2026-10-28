# getStream

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOVideoStream* getStream(
 UInt32streamIndex);
```

## Return Value

Returns the number of streams of the device.

## Parameters

- `streamIndex`: The index for which the underlying stream is desired.

## See Also

### Miscellaneous
- [getStreamCount](./api-1809412-getstreamcount.md)
- [newUserClient](./api-1809416-newuserclient.md)
  See the documentation for the IOService method newUserClient.
- [setStreamMode](./api-1809422-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](./api-1809424-startstream.md)
  Start sending data on a stream.
- [stopStream](./api-1809428-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](./api-1809431-suspendstream.md)
  Temporarily suspend data flow on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideodevice/1809409-getstream)*