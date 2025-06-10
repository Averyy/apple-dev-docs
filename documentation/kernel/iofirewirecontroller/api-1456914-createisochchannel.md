# createIsochChannel

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOFWIsochChannel * createIsochChannel(bool doIRM, UInt32 packetSize, IOFWSpeed prefSpeed, FWIsochChannelForceStopNotificationProc stopProc, void *stopRefCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirecontroller/1456914-createisochchannel)*