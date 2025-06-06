# setStreamMode

**Framework**: Kernel  
**Kind**: instm

Sets the mode of the stream, either input or output.

## Declaration

```swift
virtual IOReturn setStreamMode(
 IOStreamMode mode);
```

#### Overview

Subclasses may define whether it is possible to change the mode of a stream.

## See Also

- [getStreamMode](iostream/1809626-getstreammode.md)
  Returns the mode of the stream, either input or output.
- [startStream](iostream/1809638-startstream.md)
  Start sending data on a stream.
- [stopStream](iostream/1809642-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](iostream/1809648-suspendstream.md)
  Temporarily suspend data flow on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809631-setstreammode)*