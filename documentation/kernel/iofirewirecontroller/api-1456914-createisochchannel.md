# createIsochChannel

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOFWIsochChannel * createIsochChannel(bool doIRM, UInt32 packetSize, IOFWSpeed prefSpeed, FWIsochChannelForceStopNotificationProc stopProc, void *stopRefCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirecontroller/1456914-createisochchannel)*