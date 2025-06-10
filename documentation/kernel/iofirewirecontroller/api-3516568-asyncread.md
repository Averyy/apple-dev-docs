# asyncRead

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15.2+

## Declaration

```swift
virtual IOReturn asyncRead(UInt32 generation, UInt16 nodeID, UInt16 addrHi, UInt32 addrLo, int speed, int label, int size, IOFWAsyncCommand *cmd, IOFWReadFlags flags);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirecontroller/3516568-asyncread)*