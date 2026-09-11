# StopIO

**Framework**: VideoDriverKit  
**Kind**: method

Tells the clock device to stop IO.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t StopIO(IOUserVideoStartStopFlags in_flags);
```

#### Discussion

The default implementation always returns `kIOReturnSuccess`. Subclass and override this method to handle any hardware specific things when IO is stopping, then call the superclass implementation to update IO state.

## Parameters

- `in_flags`: IOUserVideoStartStopFlags to indicate how IO is stopping.

## See Also

- [StartIO](iouservideoclockdevice/startio.md)
  Tells the clock device to start IO.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/stopio)*