# AVKit updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to AVKit.

## Overview

Browse notable changes in [AVKit](../AVKit/AVKit.md).

## September 2026

### Camera facing direction

- Determine the direction a capture device faces in relation to a view, and get updated each time that direction changes, using [`AVCaptureDeviceDirectionCoordinator`](../AVKit/avcapturedevicedirectioncoordinator.md).
- Create a coordinator with [`init(view:deviceTypes:changeHandler:)`](../AVKit/avcapturedevicedirectioncoordinator/init%28view,devicetypes,changehandler%29.md), specifying the view and the device types to monitor. Read [`deviceDirections`](../AVKit/avcapturedevicedirectioncoordinator/devicedirections.md) for the current state, or supply a change handler to learn about later changes.
- Read the cameras that face the same direction as a view, and those that face away from it, from an [`AVCaptureDeviceDirectionMap`](../AVKit/avcapturedevicedirectionmap.md) using its [`forwardFacingDeviceDescriptors`](../AVKit/avcapturedevicedirectionmap/forwardfacingdevicedescriptors.md) and [`backwardFacingDeviceDescriptors`](../AVKit/avcapturedevicedirectionmap/backwardfacingdevicedescriptors.md) properties.
- Identify a capture device from its sendable [`AVCaptureDeviceDescriptor`](../AVKit/avcapturedevicedescriptor.md) representation, which exposes the device’s [`deviceType`](../AVKit/avcapturedevicedescriptor/devicetype.md), [`mediaTypes`](../AVKit/avcapturedevicedescriptor/mediatypes.md), [`position`](../AVKit/avcapturedevicedescriptor/position.md), [`uniqueID`](../AVKit/avcapturedevicedescriptor/uniqueid.md), and [`localizedName`](../AVKit/avcapturedevicedescriptor/localizedname.md), and match the unique identifier to get the actual [`AVCaptureDevice`](../AVFoundation/avcapturedevice.md).

## See Also

### Technology and frameworks
- [Accelerate updates](./accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](./accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](./activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](./adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](./appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](./appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](./apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](./applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](./applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](./arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/avkit)*