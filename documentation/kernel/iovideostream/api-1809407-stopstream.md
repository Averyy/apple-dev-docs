# stopStream

**Framework**: Kernel  
**Kind**: instm

Stop sending data on a stream.

## Declaration

```cpp
virtual IOReturn stopStream(
 void);
```

#### Return Value

Returns kIOReturnSuccess if the stream was successfully started.

## See Also

### Miscellaneous
- [getStreamMode](./api-1809380-getstreammode.md)
  Returns the mode of the stream, either input or output.
- [initWithBuffers](./api-1809391-initwithbuffers.md)
- [setStreamMode](./api-1809395-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](./api-1809402-startstream.md)
  Start sending data on a stream.
- [suspendStream](./api-1809411-suspendstream.md)
  Temporarily suspend data flow on the stream.
- [withBuffers](./api-1809420-withbuffers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideostream/1809407-stopstream)*