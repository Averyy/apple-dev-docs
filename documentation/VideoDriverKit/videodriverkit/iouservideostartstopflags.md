# IOUserVideoStartStopFlags

**Framework**: VideoDriverKit  
**Kind**: enum

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
enum IOUserVideoStartStopFlags : uint64_t;
```

#### Overview

Flags used to indicate how IO is starting or stopping.

IO is starting or stopping for normal IO operation, which should result in enabling/disabling all necessary hardware.

IO is starting or stoping for prewarming.  The minimal hardware should be enabled/disabled to minimize transition to normal IO operation.

Additional bits are reserved for future use

## Topics

### Start/stop behaviors
- [None](videodriverkit/iouservideostartstopflags/none.md)
- [Prewarm](videodriverkit/iouservideostartstopflags/prewarm.md)

## See Also

- [StartIO](iouservideoclockdevice/startio.md)
- [StopIO](iouservideoclockdevice/stopio.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideostartstopflags)*