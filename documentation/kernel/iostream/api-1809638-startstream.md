# startStream

**Framework**: Kernel  
**Kind**: instm

Start sending data on a stream.

## Declaration

```swift
virtual IOReturn startStream(
 void);
```

#### Return_value

Returns kIOReturnSuccess if the stream was successfully started.

#### Overview

This must be implemented by a subclass.

## See Also

- [getStreamMode](iostream/1809626-getstreammode.md)
  Returns the mode of the stream, either input or output.
- [setStreamMode](iostream/1809631-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [stopStream](iostream/1809642-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](iostream/1809648-suspendstream.md)
  Temporarily suspend data flow on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809638-startstream)*