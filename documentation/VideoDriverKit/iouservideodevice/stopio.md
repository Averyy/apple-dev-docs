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

Tells the device to stop IO.

Default implementation will always return kIOReturnSuccess. Subclass and override this method to handle any hardware specific things when IO is stopping, then call super class to update IO state. StopIO will also be called for all streams that were added to the device.

## Parameters

- `in_flags`: IOUserVideoStartStopFlags to indicate how IO is stopping.

## See Also

- [StartIO](iouservideodevice/startio.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
- [GetCurrentClientIOTime](iouservideodevice/getcurrentclientiotime.md)
- [SetIOOperationHandler](iouservideodevice/setiooperationhandler.md)
- [IOOperationHandler](videodriverkit/iooperationhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/stopio)*