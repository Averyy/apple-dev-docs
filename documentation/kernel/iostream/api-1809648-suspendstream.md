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

#### Overview

This must be implemented by a subclass.

## See Also

- [getStreamMode](iostream/1809626-getstreammode.md)
  Returns the mode of the stream, either input or output.
- [setStreamMode](iostream/1809631-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](iostream/1809638-startstream.md)
  Start sending data on a stream.
- [stopStream](iostream/1809642-stopstream.md)
  Stop sending data on a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809648-suspendstream)*