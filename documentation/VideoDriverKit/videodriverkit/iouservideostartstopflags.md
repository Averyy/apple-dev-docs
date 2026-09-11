# IOUserVideoStartStopFlags

**Framework**: VideoDriverKit  
**Kind**: enum

Flags used to indicate how I/O is starting or stopping.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
enum IOUserVideoStartStopFlags : uint64_t;
```

## Topics

### Start/stop behaviors
- [None](videodriverkit/iouservideostartstopflags/none.md)
  A flag that indicates starting or stopping for normal I/O operation.
- [Prewarm](videodriverkit/iouservideostartstopflags/prewarm.md)
  A flag that indicates starting or stopping for prewarming.

## See Also

- [StartIO](iouservideoclockdevice/startio.md)
  Tells the clock device to start IO.
- [StopIO](iouservideoclockdevice/stopio.md)
  Tells the clock device to stop IO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideostartstopflags)*