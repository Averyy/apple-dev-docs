# asyncWrite

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn asyncWrite(UInt32 generation, UInt16 nodeID, UInt16 addrHi, UInt32 addrLo, int speed, int label, IOMemoryDescriptor *buf, IOByteCount offset, int size, IOFWAsyncCommand *cmd);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirecontroller/1457091-asyncwrite)*