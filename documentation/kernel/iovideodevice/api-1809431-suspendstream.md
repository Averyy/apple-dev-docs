# suspendStream

**Framework**: Kernel  
**Kind**: instm

Temporarily suspend data flow on the stream.

## Declaration

```cpp
virtual IOReturn suspendStream(
 IOVideoStream *stream);
```

## Return Value

Returns kIOReturnSuccess if the stream was successfully suspended.

## Overview

This must be implemented by a subclass.

## See Also

### Miscellaneous
- [getStream](./api-1809409-getstream.md)
- [getStreamCount](./api-1809412-getstreamcount.md)
- [newUserClient](./api-1809416-newuserclient.md)
  See the documentation for the IOService method newUserClient.
- [setStreamMode](./api-1809422-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](./api-1809424-startstream.md)
  Start sending data on a stream.
- [stopStream](./api-1809428-stopstream.md)
  Stop sending data on a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideodevice/1809431-suspendstream)*