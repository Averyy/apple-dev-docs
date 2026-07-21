# StartDevice

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t StartDevice(IOUserVideoObjectID in_object_id, IOUserVideoStartStopFlags in_flags);
```

#### Return Value

Returns kern_return_t

#### Discussion

Tells the driver to start IO on a IOUserVideoDevice.

Default implementation will always return kIOReturnSuccess. Subclass and override this method to handle any hardware specific things when IO is starting on the device, then call super class to update IO state. This call is expected to always succeed or fail. The hardware can take as long as necessary in this call such that it always either succeeds (and kIOReturnSuccess) or fails. StartIO will be called on the video device.

## Parameters

- `in_object_id`: IOUserVideoObjectID of the device to start IO.
- `in_flags`: IOUserVideoStartStopFlags to indicate how IO is starting.

## See Also

- [StopDevice](iouservideodriver/stopdevice.md)
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/startdevice)*