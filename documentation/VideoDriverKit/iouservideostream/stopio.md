# StopIO

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t StopIO(IOUserVideoStartStopFlags in_flags);
```

#### Return Value

Returns kern_return_t

#### Discussion

Tells the stream to stop IO.

Default implementation will always return kIOReturnSuccess. Subclass and override this method to handle any hardware specific things when IO is stopping, then call super class to update IO state.

## Parameters

- `in_flags`: IOUserVideoStartStopFlags to indicate how IO is stopping.

## See Also

- [StartIO](iouservideostream/startio.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
- [InputNotification](iouservideostream/inputnotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/stopio)*