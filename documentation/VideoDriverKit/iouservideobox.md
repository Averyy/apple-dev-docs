# IOUserVideoBox

**Framework**: VideoDriverKit  
**Kind**: class

A container for other objects.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
class IOUserVideoBox;
```

#### Overview

The objects in a video box are typically [`IOUserVideoDevice`](iouservideodevice.md) and [`IOUserVideoClockDevice`](iouservideoclockdevice.md) objects. An [`IOUserVideoBox`](iouservideobox.md) publishes identifying information about itself and can be enabled or disabled. A box’s contents are only available to the system when the box is enabled.

## Topics

### Creating a video box
- [Create](iouservideobox/create.md)
  Static factory method to allocate and initialize an IOUserVideoBox.
- [init](iouservideobox/init.md)
  Initializes a video box.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
### Freeing a video device
- [free](iouservideobox/free.md)
  Frees the IOUserVideoBox.
### Getting information about the class
- [GetClassID](iouservideobox/getclassid.md)
  Gets the class identifier of the object
- [GetBaseClassID](iouservideobox/getbaseclassid.md)
  Gets the class identifier of the base class object
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Identifying the box
- [GetUID](iouservideobox/getuid.md)
  Gets the unique identifier of the video box.
### Managing box contents
- [AddDevice](iouservideobox/adddevice.md)
  Adds a video device to the video box.
- [RemoveDevice](iouservideobox/removedevice.md)
  Removes a video device from the video box.
- [IOUserVideoDevice](iouservideodevice.md)
  A video device.
- [AddClockDevice](iouservideobox/addclockdevice.md)
  Adds a clock device video box.
- [RemoveClockDevice](iouservideobox/removeclockdevice.md)
  Removes aa clock device from the video box.
- [IOUserVideoClockDevice](iouservideoclockdevice.md)
  A clock device.
### Managing protection state
- [SetIsProtected](iouservideobox/setisprotected.md)
  Sets the value indicating the box’s protection state.
- [IsProtected](iouservideobox/isprotected.md)
  A Boolean value indicating if box is protected.
### Managing acquirability
- [HandleChangeAcquireBox](iouservideobox/handlechangeacquirebox.md)
  Called when host is attempting to the change the box acquisition
- [SetIsAcquired](iouservideobox/setisacquired.md)
  Sets the value indicating the box’s acquisition state.
- [IsAcquired](iouservideobox/isacquired.md)
  A Boolean value indicating if box is acquired.
- [SetIsAcquirable](iouservideobox/setisacquirable.md)
  Sets the value for the box’s acquirability.
- [IsAcquirable](iouservideobox/isacquirable.md)
  A Boolean value indicating if box can be acquired.
- [SetAcquisitionFailure](iouservideobox/setacquisitionfailure.md)
  Sets the error for the box’s acquisition failure.
- [GetAcquisitionFailure](iouservideobox/getacquisitionfailure.md)
  Gets the acquisition failure of the video box.
### Determining media support
- [SetHasAudio](iouservideobox/sethasaudio.md)
  Sets the value indicating the box’s audio support.
- [HasAudio](iouservideobox/hasaudio.md)
  A Boolean value indicating if box has audio capabilities.
- [SetHasVideo](iouservideobox/sethasvideo.md)
  Sets the value indicating the box’s video support.
- [HasVideo](iouservideobox/hasvideo.md)
  A Boolean value indicating if box has video capabilities.
- [SetHasMIDI](iouservideobox/sethasmidi.md)
  Sets the value indicating the box’s MIDI support
- [HasMIDI](iouservideobox/hasmidi.md)
  A Boolean value indicating if box has MIDI capabilities.
### Working with transport types
- [GetTransportType](iouservideobox/gettransporttype.md)
  Gets the transport type of the video box.
- [SetTransportType](iouservideobox/settransporttype.md)
  Sets the transport type of the IOUserVideoBox.
- [IOUserVideoTransportType](videodriverkit/iouservideotransporttype.md)
  The transport type of a video stream.

## Relationships

### Inherits From
- [IOUserVideoObject](iouservideoobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideobox)*