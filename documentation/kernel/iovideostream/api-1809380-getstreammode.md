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

### Miscellaneous
- [initWithBuffers](./api-1809391-initwithbuffers.md)
- [setStreamMode](./api-1809395-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](./api-1809402-startstream.md)
  Start sending data on a stream.
- [stopStream](./api-1809407-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](./api-1809411-suspendstream.md)
  Temporarily suspend data flow on the stream.
- [withBuffers](./api-1809420-withbuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideostream/1809380-getstreammode)*