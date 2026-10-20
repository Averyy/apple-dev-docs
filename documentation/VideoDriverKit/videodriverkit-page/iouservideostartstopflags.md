# IOUserVideoStartStopFlags

**Framework**: VideoDriverKit  
**Kind**: enum  
**Role**: Enumeration

Flags used to indicate how I/O is starting or stopping.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
enum IOUserVideoStartStopFlags : uint64_t;
```

## Topics

### Start/stop behaviors
- [None](./iouservideostartstopflags/none.md)
  A flag that indicates starting or stopping for normal I/O operation.
- [Prewarm](./iouservideostartstopflags/prewarm.md)
  A flag that indicates starting or stopping for prewarming.

## See Also

### Performing I/O
- [StartIO](../iouservideoclockdevice/startio.md)
  Tells the clock device to start IO.
- [StopIO](../iouservideoclockdevice/stopio.md)
  Tells the clock device to stop IO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideostartstopflags)*