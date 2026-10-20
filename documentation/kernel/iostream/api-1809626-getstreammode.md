# getStreamMode

**Framework**: Kernel  
**Kind**: instm

Returns the mode of the stream, either input or output.

## Declaration

```cpp
virtual IOStreamMode getStreamMode(
 void);
```

#### Return Value

The mode of the stream, either kIOStreamModeInput (from user space to kernel space) or the default kIOStreamModeOutput (from kernel space to user space).

## See Also

### Stream control
- [setStreamMode](./api-1809631-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](./api-1809638-startstream.md)
  Start sending data on a stream.
- [stopStream](./api-1809642-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](./api-1809648-suspendstream.md)
  Temporarily suspend data flow on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809626-getstreammode)*