# StopDevice

**Framework**: VideoDriverKit  
**Kind**: method

Tells the driver to stop IO on an video device.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t StopDevice(IOUserVideoObjectID in_object_id, IOUserVideoStartStopFlags in_flags);
```

#### Discussion

The default implementation always returns `kIOReturnSuccess`. Subclass and override this method to handle any hardware specific things when IO is stopping, then call the superclass implementation to update IO state. StopIO will be called on the video device.

## Parameters

- `in_object_id`: IOUserVideoObjectID of the device to stop IO.
- `in_flags`: IOUserVideoStartStopFlags to indicate how IO is stopping.

## See Also

- [StartDevice](iouservideodriver/startdevice.md)
  Tells the driver to start IO on an video device.
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
  A handle for a a specific video object.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver/stopdevice)*