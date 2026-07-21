# StartIO

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t StartIO(IOUserVideoStartStopFlags in_flags);
```

#### Return Value

Returns kern_return_t

#### Discussion

Tells the clock device to start IO.

Default implementation will always return kIOReturnSuccess. Subclass and override this method to handle any hardware specific things when IO is starting, then call super class to update IO state. This call is expected to always succeed or fail. The hardware can take as long as necessary in this call such that it always either succeeds (and kIOReturnSuccess) or fails.

## Parameters

- `in_flags`: IOUserVideoStartStopFlags to indicate how IO is starting.

## See Also

- [StopIO](iouservideoclockdevice/stopio.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/startio)*