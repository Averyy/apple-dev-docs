# ARKit updates

**Framework**: Updates

Learn about important changes to ARKit.

#### Overview

Browse notable changes to [`ARKit`](https://developer.apple.com/documentation/arkit).

#### June 2026

##### General

- Convert coordinates between SwiftUI, RealityKit and ARKit by getting a coordinate space for any tracked anchor with the new [`ARKitCoordinateSpaceProviding`](https://developer.apple.com/documentation/arkit/arkitcoordinatespaceproviding) protocol, adopted by anchor types across ARKit.

##### Visionos

- Track how well an app’s content covers a person’s field of view, receive device fit updates, and present coaching alerts with [`VisualFidelityProvider`](https://developer.apple.com/documentation/arkit/visualfidelityprovider) and [`FieldOfViewAnchor`](https://developer.apple.com/documentation/arkit/fieldofviewanchor).
- Update the set of accessories a running [`AccessoryTrackingProvider`](https://developer.apple.com/documentation/arkit/accessorytrackingprovider) tracks without restarting the session using [`updateAccessories(_:)`](https://developer.apple.com/documentation/arkit/accessorytrackingprovider/updateaccessories(_:)).
- Configure reference objects for high-frame-rate tracking with [`ReferenceObject.Configuration`](https://developer.apple.com/documentation/arkit/referenceobject/configuration).

##### Ios

- Drive AR views from a rotation angle instead of a `UIInterfaceOrientation` with doc://com.apple.documentation/documentation/arkit/arsession/viewrotationangle and the new orientation-independent variants on [`ARCamera`](https://developer.apple.com/documentation/arkit/arcamera) and [`ARFrame`](https://developer.apple.com/documentation/arkit/arframe).
- Attach an [`ARSession`](https://developer.apple.com/documentation/arkit/arsession) to a specific `CALayer` with [`viewLayer`](https://developer.apple.com/documentation/arkit/arsession/viewlayer).
- Receive `AVFoundation` metadata objects, such as detected faces, alongside camera frames with [`metadataObjects`](https://developer.apple.com/documentation/arkit/arframe/metadataobjects).
- Detect and track physical objects in world-tracking sessions with [`trackingObjects`](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/trackingobjects).
- Generate environment textures automatically with doc://com.apple.documentation/documentation/arkit/arworldtrackingconfiguration/environmenttexturingenabled.

#### June 2025

##### General

- Bring ARKit to Mac apps by using [`ARKitSession`](https://developer.apple.com/documentation/arkit/arkitsession) with [`WorldTrackingProvider`](https://developer.apple.com/documentation/arkit/worldtrackingprovider) to query device pose and manage world anchors on macOS.
- Classify surfaces consistently across plane, mesh, and room anchors using the unified [`SurfaceClassification`](https://developer.apple.com/documentation/arkit/surfaceclassification) enumeration.
- Opt into higher-fidelity hand data with doc://com.apple.documentation/documentation/arkit/handanchor/fidelity.

##### Spatial Accessories

- Track spatial accessories, such as styli, controllers, and purpose-built devices, with [`AccessoryTrackingProvider`](https://developer.apple.com/documentation/arkit/accessorytrackingprovider) and [`AccessoryAnchor`](https://developer.apple.com/documentation/arkit/accessoryanchor).
- Prepare an accessory for tracking by following [`Preparing spatial accessories for tracking in your visionOS app`](https://developer.apple.com/documentation/arkit/preparing-spatial-accessories-for-tracking-in-your-visionos-app) and adopt the workflow in [`Tracking accessories in volumetric windows`](https://developer.apple.com/documentation/arkit/tracking-accessories-in-volumetric-windows).

##### Shared Experiences

- Share a world coordinate space among nearby participants with [`SharedCoordinateSpaceProvider`](https://developer.apple.com/documentation/arkit/sharedcoordinatespaceprovider).
- Persist world anchors across nearby devices by opting in with [`isSharedWithNearbyParticipants`](https://developer.apple.com/documentation/arkit/worldanchor/issharedwithnearbyparticipants), and observe availability with [`worldAnchorSharingAvailability`](https://developer.apple.com/documentation/arkit/worldtrackingprovider/worldanchorsharingavailability-swift.property).

##### Camera

- Capture from a defined region of space in enterprise apps with [`CameraRegionProvider`](https://developer.apple.com/documentation/arkit/cameraregionprovider) and [`CameraRegionAnchor`](https://developer.apple.com/documentation/arkit/cameraregionanchor).
- Access the right-eye camera feed and choose between mono- and stereo-corrected frames using [`CameraFrameProvider.CameraPosition.right`](https://developer.apple.com/documentation/arkit/cameraframeprovider/cameraposition/right) and [`CameraFrameProvider.CameraRectification`](https://developer.apple.com/documentation/arkit/cameraframeprovider/camerarectification).

#### June 2024

- Detect physical objects and attach digital content to them with [`ObjectTrackingProvider`](https://developer.apple.com/documentation/arkit/objecttrackingprovider).
- Use the [`RoomTrackingProvider`](https://developer.apple.com/documentation/arkit/roomtrackingprovider) to understand the shape and size of the room that people are in and detect when they enter a different room.

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
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.
- [AVKit updates](avkit.md)
  Learn about important changes to AVKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/arkit)*