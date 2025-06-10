# asyncStreamWrite

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn asyncStreamWrite(UInt32 generation, int speed, int tag, int sync, int channel, IOMemoryDescriptor *buf, IOByteCount offset, int size, IOFWAsyncStreamCommand *cmd);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirecontroller/1457295-asyncstreamwrite)*