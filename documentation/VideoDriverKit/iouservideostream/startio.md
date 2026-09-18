# StartIO

**Framework**: VideoDriverKit  
**Kind**: method

Tells the stream to start IO.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t StartIO(IOUserVideoStartStopFlags in_flags);
```

#### Discussion

The default implementation always returns `kIOReturnSuccess`. Subclass and override this method to handle any hardware specific things when IO is starting, then call the superclass implementation to update IO state. This call is expected to always succeed or fail. The hardware can take as long as necessary in this call such that it always either succeeds (and `kIOReturnSuccess`) or fails.

## Parameters

- `in_flags`: Flags to indicate how IO is starting.

## See Also

- [StopIO](iouservideostream/stopio.md)
  Tells the stream to stop IO.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
- [InputNotification](iouservideostream/inputnotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/startio)*