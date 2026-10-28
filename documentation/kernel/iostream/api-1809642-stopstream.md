# stopStream

**Framework**: Kernel  
**Kind**: instm

Stop sending data on a stream.

## Declaration

```cpp
virtual IOReturn stopStream(
 void);
```

## Return Value

Returns kIOReturnSuccess if the stream was successfully stopped.

## Overview

This must be implemented by a subclass.

## See Also

### Stream control
- [getStreamMode](./api-1809626-getstreammode.md)
  Returns the mode of the stream, either input or output.
- [setStreamMode](./api-1809631-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](./api-1809638-startstream.md)
  Start sending data on a stream.
- [suspendStream](./api-1809648-suspendstream.md)
  Temporarily suspend data flow on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809642-stopstream)*