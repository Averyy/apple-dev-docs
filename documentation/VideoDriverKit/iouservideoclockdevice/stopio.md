# StopIO

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the clock device to stop IO.

**Availability**:
- DriverKit 27.0+

## Declaration

```cpp
virtual kern_return_t StopIO(IOUserVideoStartStopFlags in_flags);
```

## Discussion

The default implementation always returns `kIOReturnSuccess`. Subclass and override this method to handle any hardware specific things when IO is stopping, then call the superclass implementation to update IO state.

## Parameters

- `in_flags`: IOUserVideoStartStopFlags to indicate how IO is stopping.

## See Also

### Performing I/O
- [StartIO](./startio.md)
  Tells the clock device to start IO.
- [IOUserVideoStartStopFlags](../videodriverkit-page/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/stopio)*