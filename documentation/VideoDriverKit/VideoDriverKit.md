# VideoDriverKit

**Framework**: VideoDriverKit  
**Kind**: module

Develop drivers for video capture and playback devices.

**Availability**:
- DriverKit 27.0+ (Beta)

#### Overview

The VideoDriverKit framework supports the development of DriverKit-based video extensions that communicate with [`Core Media`](https://developer.apple.com/documentation/CoreMedia). VideoDriverKit handles all of the necessary user client communication between CoreMedia and the driver extension, which eliminates the need to use `IOVideoFamily` kexts and [`Device Abstraction Layer (DAL) Plug-Ins`](https://developer.apple.com/documentation/CoreMediaIO/device-abstraction-layer-dal-plug-ins).

Develop your driver by subclassing [`IOUserVideoDriver`](iouservideodriver.md). Then use the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade your driver.

> **Note**: VideoDriverKit is available on macOS.

## Topics

### Essentials
- [IOUserVideoObject](iouservideoobject.md)
- [IOUserVideoDriver](iouservideodriver.md)
### Video devices
- [IOUserVideoClockDevice](iouservideoclockdevice.md)
- [IOUserVideoDevice](iouservideodevice.md)
### Video objects
- [IOUserVideoBox](iouservideobox.md)
### Video streams
- [IOUserVideoStream](iouservideostream.md)
### Video controls
- [IOUserVideoControl](iouservideocontrol.md)
- [IOUserVideoBooleanControl](iouservideobooleancontrol.md)
- [IOUserVideoStereoPanControl](iouservideostereopancontrol.md)
- [IOUserVideoSliderControl](iouservideoslidercontrol.md)
- [IOUserVideoDirectionControl](iouservideodirectioncontrol.md)
- [IOUserVideoSelectorControl](iouservideoselectorcontrol.md)
- [IOUserVideoLevelControl](iouservideolevelcontrol.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/VideoDriverKit)*