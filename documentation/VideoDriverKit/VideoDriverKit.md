# VideoDriverKit

**Framework**: VideoDriverKit  
**Kind**: module

Develop drivers for video capture and playback devices.

**Availability**:
- DriverKit 27.0+ (Beta)

#### Overview

The VideoDriverKit framework supports the development of DriverKit-based video extensions that communicate with [`Core Media`](https://developer.apple.com/documentation/coremedia). VideoDriverKit handles all of the necessary user client communication between CoreMedia and the driver extension, which eliminates the need to use `IOVideoFamily` kexts and [`Device Abstraction Layer (DAL) Plug-Ins`](https://developer.apple.com/documentation/coremediaio/device-abstraction-layer-dal-plug-ins).

Develop your driver by subclassing [`IOUserVideoDriver`](iouservideodriver.md). Then use the [`System Extensions`](https://developer.apple.com/documentation/systemextensions) framework to install and upgrade your driver.

> **Note**: VideoDriverKit is available on macOS.

## Topics

### Essentials
- [IOUserVideoObject](iouservideoobject.md)
  The base class for all video objects.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
### Video devices
- [IOUserVideoClockDevice](iouservideoclockdevice.md)
  A clock device.
- [IOUserVideoDevice](iouservideodevice.md)
  A video device.
### Video objects
- [IOUserVideoBox](iouservideobox.md)
  A container for other objects.
### Video streams
- [IOUserVideoStream](iouservideostream.md)
  A video stream.
### Video controls
- [IOUserVideoControl](iouservideocontrol.md)
  A base class for control objects.
- [IOUserVideoBooleanControl](iouservideobooleancontrol.md)
  A control object that supports Boolean values.
- [IOUserVideoStereoPanControl](iouservideostereopancontrol.md)
  A control object that supports panning between stereo channels.
- [IOUserVideoSliderControl](iouservideoslidercontrol.md)
  A control object that supports a 32-bit unsigned integer value slider.
- [IOUserVideoDirectionControl](iouservideodirectioncontrol.md)
  A control object that supports Boolean values.
- [IOUserVideoSelectorControl](iouservideoselectorcontrol.md)
  A control object that supports a 32-bit unsigned integer selector value.
- [IOUserVideoLevelControl](iouservideolevelcontrol.md)
  A control object that supports a float value level.
### Namespaces
- [VideoDriverKit](videodriverkit.md)
  A namespace that holds supporting types used by VideoDriverKit functions.
### Macros
- [DebugMsg](debugmsg.md)
- [FailIf](failif.md)
- [FailIfError](failiferror.md)
- [FailIfNULL](failifnull.md)
- [kIOStreamBufferIDInvalid](kiostreambufferidinvalid.md)
- [kIOUserVideoDriverUserClientType](kiouservideodriveruserclienttype.md)
  User client type required for connection to the Host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/VideoDriverKit)*