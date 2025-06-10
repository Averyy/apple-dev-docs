# asyncLock

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15.2+

## Declaration

```swift
virtual IOReturn asyncLock(UInt32 generation, UInt16 nodeID, UInt16 addrHi, UInt32 addrLo, int speed, int label, int type, IOMemoryDescriptor *buf, IOByteCount offset, int size, IOFWAsyncCommand *cmd);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirecontroller/3516567-asynclock)*