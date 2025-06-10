# asyncLockResponse

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn asyncLockResponse(UInt32 generation, UInt16 nodeID, int speed, IOMemoryDescriptor *buf, IOByteCount offset, int len, IOFWRequestRefCon refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirecontroller/1457232-asynclockresponse)*