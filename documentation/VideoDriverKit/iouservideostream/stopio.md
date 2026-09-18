# StopIO

**Framework**: VideoDriverKit  
**Kind**: method

Tells the stream to stop IO.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t StopIO(IOUserVideoStartStopFlags in_flags);
```

#### Discussion

The default implementation always return s`kIOReturnSuccess`. Subclass and override this method to handle any hardware specific things when IO is stopping, then call the superclass implementation to update IO state.

## Parameters

- `in_flags`: Flags to indicate how IO is stopping.

## See Also

- [StartIO](iouservideostream/startio.md)
  Tells the stream to start IO.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
- [InputNotification](iouservideostream/inputnotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/stopio)*