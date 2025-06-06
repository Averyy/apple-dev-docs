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

- [setStreamMode](iostream/1809631-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](iostream/1809638-startstream.md)
  Start sending data on a stream.
- [stopStream](iostream/1809642-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](iostream/1809648-suspendstream.md)
  Temporarily suspend data flow on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809626-getstreammode)*