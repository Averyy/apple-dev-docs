# setStreamMode

**Framework**: Kernel  
**Kind**: instm

Sets the mode of the stream, either input or output.

## Declaration

```cpp
virtual IOReturn setStreamMode(
 IOStreamMode mode);
```

## Overview

Subclasses may define whether it is possible to change the mode of a stream.

## See Also

### Stream control
- [getStreamMode](./api-1809626-getstreammode.md)
  Returns the mode of the stream, either input or output.
- [startStream](./api-1809638-startstream.md)
  Start sending data on a stream.
- [stopStream](./api-1809642-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](./api-1809648-suspendstream.md)
  Temporarily suspend data flow on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809631-setstreammode)*