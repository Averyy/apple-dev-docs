# IOUserVideoBox

**Framework**: VideoDriverKit  
**Kind**: class

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoBox;
```

#### Overview

IOUserVideoBox class is a subclass of the VideoObject class. An VideoBox is a container for other objects (typically IOUserVideoDevice and IOUserVideoClockDevice objects). An IOUserVideoBox publishes identifying information about itself and can be enabled or disabled. A box’s contents are only available to the system when the box is enabled

## Topics

### Creating a video box
- [Create](iouservideobox/create.md)
- [init](iouservideobox/init.md)
- [IOUserVideoDriver](iouservideodriver.md)
### Freeing a video device
- [free](iouservideobox/free.md)
### Getting information about the class
- [GetClassID](iouservideobox/getclassid.md)
- [GetBaseClassID](iouservideobox/getbaseclassid.md)
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
### Identifying the box
- [GetUID](iouservideobox/getuid.md)
### Managing box contents
- [AddDevice](iouservideobox/adddevice.md)
- [RemoveDevice](iouservideobox/removedevice.md)
- [IOUserVideoDevice](iouservideodevice.md)
- [AddClockDevice](iouservideobox/addclockdevice.md)
- [RemoveClockDevice](iouservideobox/removeclockdevice.md)
- [IOUserVideoClockDevice](iouservideoclockdevice.md)
### Managing protection state
- [SetIsProtected](iouservideobox/setisprotected.md)
- [IsProtected](iouservideobox/isprotected.md)
### Managing acquirability
- [HandleChangeAcquireBox](iouservideobox/handlechangeacquirebox.md)
- [SetIsAcquired](iouservideobox/setisacquired.md)
- [IsAcquired](iouservideobox/isacquired.md)
- [SetIsAcquirable](iouservideobox/setisacquirable.md)
- [IsAcquirable](iouservideobox/isacquirable.md)
- [SetAcquisitionFailure](iouservideobox/setacquisitionfailure.md)
- [GetAcquisitionFailure](iouservideobox/getacquisitionfailure.md)
### Determining media support
- [SetHasAudio](iouservideobox/sethasaudio.md)
- [HasAudio](iouservideobox/hasaudio.md)
- [SetHasVideo](iouservideobox/sethasvideo.md)
- [HasVideo](iouservideobox/hasvideo.md)
- [SetHasMIDI](iouservideobox/sethasmidi.md)
- [HasMIDI](iouservideobox/hasmidi.md)
### Working with transport types
- [GetTransportType](iouservideobox/gettransporttype.md)
- [SetTransportType](iouservideobox/settransporttype.md)
- [IOUserVideoTransportType](videodriverkit/iouservideotransporttype.md)

## Relationships

### Inherits From
- [IOUserVideoObject](iouservideoobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox)*