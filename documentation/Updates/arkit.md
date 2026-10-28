# ARKit updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to ARKit.

## Overview

Browse notable changes to [ARKit](../ARKit/ARKit.md).

## June 2026

### General

- Convert coordinates between SwiftUI, RealityKit and ARKit by getting a coordinate space for any tracked anchor with the new [`ARKitCoordinateSpaceProviding`](../ARKit/arkitcoordinatespaceproviding.md) protocol, adopted by anchor types across ARKit.

### visionOS

- Track how well an app’s content covers a person’s field of view, receive device fit updates, and present coaching alerts with [`VisualFidelityProvider`](../ARKit/visualfidelityprovider.md) and [`FieldOfViewAnchor`](../ARKit/fieldofviewanchor.md).
- Update the set of accessories a running [`AccessoryTrackingProvider`](../ARKit/accessorytrackingprovider.md) tracks without restarting the session using [`updateAccessories(_:)`](../ARKit/accessorytrackingprovider/updateaccessories%28_%29.md).
- Configure reference objects for high-frame-rate tracking with [`ReferenceObject.Configuration`](../ARKit/referenceobject/configuration.md).

### iOS

- Drive AR views from a rotation angle instead of a `UIInterfaceOrientation` with [`viewRotationAngle`](../ARKit/arsession/viewrotationangle-8847g.md) and the new orientation-independent variants on [`ARCamera`](../ARKit/arcamera.md) and [`ARFrame`](../ARKit/arframe.md).
- Attach an [`ARSession`](../ARKit/arsession.md) to a specific `CALayer` with [`viewLayer`](../ARKit/arsession/viewlayer.md).
- Receive `AVFoundation` metadata objects, such as detected faces, alongside camera frames with [`metadataObjects`](../ARKit/arframe/metadataobjects.md).
- Detect and track physical objects in world-tracking sessions with [`trackingObjects`](../ARKit/arworldtrackingconfiguration/trackingobjects.md).
- Generate environment textures during face-tracking sessions from rear-camera imagery with [`isEnvironmentTexturingEnabled`](../ARKit/arfacetrackingconfiguration/isenvironmenttexturingenabled.md).

## June 2025

### General

- Bring ARKit to Mac apps by using [`ARKitSession`](../ARKit/arkitsession.md) with [`WorldTrackingProvider`](../ARKit/worldtrackingprovider.md) to query device pose and manage world anchors on macOS.
- Classify surfaces consistently across plane, mesh, and room anchors using the unified [`SurfaceClassification`](../ARKit/surfaceclassification.md) enumeration.
- Opt into higher-fidelity hand data with [`fidelity`](../ARKit/handanchor/fidelity-swift.property.md).

### Spatial accessories

- Track spatial accessories, such as styli, controllers, and purpose-built devices, with [`AccessoryTrackingProvider`](../ARKit/accessorytrackingprovider.md) and [`AccessoryAnchor`](../ARKit/accessoryanchor.md).
- Prepare an accessory for tracking by following [Preparing spatial accessories for tracking in your visionOS app](../ARKit/preparing-spatial-accessories-for-tracking-in-your-visionos-app.md) and adopt the workflow in [Tracking accessories in volumetric windows](../ARKit/tracking-accessories-in-volumetric-windows.md).

### Shared experiences

- Share a world coordinate space among nearby participants with [`SharedCoordinateSpaceProvider`](../ARKit/sharedcoordinatespaceprovider.md).
- Persist world anchors across nearby devices by opting in with [`isSharedWithNearbyParticipants`](../ARKit/worldanchor/issharedwithnearbyparticipants.md), and observe availability with [`worldAnchorSharingAvailability`](../ARKit/worldtrackingprovider/worldanchorsharingavailability-swift.property.md).

### Camera

- Capture from a defined region of space in enterprise apps with [`CameraRegionProvider`](../ARKit/cameraregionprovider.md) and [`CameraRegionAnchor`](../ARKit/cameraregionanchor.md).
- Access the right-eye camera feed and choose between mono- and stereo-corrected frames using [`CameraFrameProvider.CameraPosition.right`](../ARKit/cameraframeprovider/cameraposition/right.md) and [`CameraFrameProvider.CameraRectification`](../ARKit/cameraframeprovider/camerarectification.md).

## June 2024

- Detect physical objects and attach digital content to them with [`ObjectTrackingProvider`](../ARKit/objecttrackingprovider.md).
- Use the [`RoomTrackingProvider`](../ARKit/roomtrackingprovider.md) to understand the shape and size of the room that people are in and detect when they enter a different room.

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
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.
- [AVKit updates](./avkit.md)
  Learn about important changes to AVKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/arkit)*