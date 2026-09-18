# AVKit updates

**Framework**: Updates

Learn about important changes to AVKit.

#### Overview

Browse notable changes in [`AVKit`](https://developer.apple.com/documentation/avkit).

#### September 2026

##### Camera Facing Direction

- Determine the direction a capture device faces in relation to a view, and get updated each time that direction changes, using [`AVCaptureDeviceDirectionCoordinator`](https://developer.apple.com/documentation/avkit/avcapturedevicedirectioncoordinator).
- Create a coordinator with [`init(view:deviceTypes:changeHandler:)`](https://developer.apple.com/documentation/avkit/avcapturedevicedirectioncoordinator/init(view:devicetypes:changehandler:)), specifying the view and the device types to monitor. Read [`deviceDirections`](https://developer.apple.com/documentation/avkit/avcapturedevicedirectioncoordinator/devicedirections) for the current state, or supply a change handler to learn about later changes.
- Read the cameras that face the same direction as a view, and those that face away from it, from an [`AVCaptureDeviceDirectionMap`](https://developer.apple.com/documentation/avkit/avcapturedevicedirectionmap) using its [`forwardFacingDeviceDescriptors`](https://developer.apple.com/documentation/avkit/avcapturedevicedirectionmap/forwardfacingdevicedescriptors) and [`backwardFacingDeviceDescriptors`](https://developer.apple.com/documentation/avkit/avcapturedevicedirectionmap/backwardfacingdevicedescriptors) properties.
- Identify a capture device from its sendable [`AVCaptureDeviceDescriptor`](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor) representation, which exposes the device’s [`deviceType`](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/devicetype), [`mediaTypes`](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/mediatypes), [`position`](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/position), [`uniqueID`](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/uniqueid), and [`localizedName`](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/localizedname), and match the unique identifier to get the actual [`AVCaptureDevice`](https://developer.apple.com/documentation/avfoundation/avcapturedevice).

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/avkit)*