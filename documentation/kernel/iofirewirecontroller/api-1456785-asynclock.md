# asyncLock

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn asyncLock(UInt32 generation, UInt16 nodeID, UInt16 addrHi, UInt32 addrLo, int speed, int label, int type, void *data, int size, IOFWAsyncCommand *cmd);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirecontroller/1456785-asynclock)*