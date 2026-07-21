# StopDevice

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t StopDevice(IOUserVideoObjectID in_object_id, IOUserVideoStartStopFlags in_flags);
```

#### Return Value

Returns kern_return_t

#### Discussion

Tells the driver to stop IO on a IOUserVideoDevice.

Default implementation will always return kIOReturnSuccess. Subclass and override this method to handle any hardware specific things when IO is stopping, then call super class to update IO state. StopIO will be called on the video device.

## Parameters

- `in_object_id`: IOUserVideoObjectID of the device to stop IO.
- `in_flags`: IOUserVideoStartStopFlags to indicate how IO is stopping.

## See Also

- [StartDevice](iouservideodriver/startdevice.md)
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/stopdevice)*