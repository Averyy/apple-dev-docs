# newUserClient

**Framework**: Kernel  
**Kind**: instm

See the documentation for the IOService method newUserClient.

## Declaration

```cpp
virtual IOReturn newUserClient(
 task_t owningTask,
 void *securityID,
 UInt32 type,
 OSDictionary *properties,
 IOUserClient **handler);
```

## See Also

### Miscellaneous
- [getStream](./api-1809409-getstream.md)
- [getStreamCount](./api-1809412-getstreamcount.md)
- [setStreamMode](./api-1809422-setstreammode.md)
  Sets the mode of the stream, either input or output.
- [startStream](./api-1809424-startstream.md)
  Start sending data on a stream.
- [stopStream](./api-1809428-stopstream.md)
  Stop sending data on a stream.
- [suspendStream](./api-1809431-suspendstream.md)
  Temporarily suspend data flow on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideodevice/1809416-newuserclient)*