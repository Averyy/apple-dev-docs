# asyncWrite

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15.2+

## Declaration

```swift
virtual IOReturn asyncWrite(UInt32 generation, UInt16 nodeID, UInt16 addrHi, UInt32 addrLo, int speed, int label, IOMemoryDescriptor *buf, IOByteCount offset, int size, IOFWAsyncCommand *cmd, IOFWWriteFlags flags);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirecontroller/3516569-asyncwrite)*