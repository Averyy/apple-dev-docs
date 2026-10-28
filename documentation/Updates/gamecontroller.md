# Game Controller updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to Game Controller.

## Overview

Browse notable changes in [Game Controller](../GameController/GameController.md).

## June 2025

- Add support for spatial game controllers. To determine if a controller is a spatial game controller, check whether the product category is  [`GCProductCategorySpatialController`](../GameController/gcproductcategoryspatialcontroller.md).
- Add support for a physical stylus with a [`GCStylus`](../GameController/gcstylus.md) object.
- Add [`NSAccessoryTrackingUsageDescription`](../BundleResources/information-property-list/nsaccessorytrackingusagedescription.md) to your information property list if your app requires access to accessory-tracking data for a spatial game controller or stylus.
- Add [`GCSupportedGameControllers`](../BundleResources/information-property-list/gcsupportedgamecontrollers.md) to your information property list — with a value of `SpatialGamepad` — if your app supports spatial game controllers.

## June 2024

### visionOS

- For UIKit apps, add a user interaction that determines whether the system delivers game controller events through the Game Controller framework instead of the [`UIResponder`](../UIKit/uiresponder.md) chain. To receive events through the Game Controller framework, add a [`GCEventInteraction`](../GameController/gceventinteraction.md) object to one or more views and set the [`handledEventTypes`](../GameController/gceventinteraction/handledeventtypes.md) property to the types of events you want to handle.

## June 2023

- Use the classes that conform to the [`GCDevicePhysicalInput`](../GameController/gcdevicephysicalinput.md) protocol to poll for game controller input in your game loop. For more information, see  [Handling input events](../GameController/handling-input-events.md).
- Add support for arcade sticks. To determine if a controller is an arcade stick, check whether the product category is  [`GCProductCategoryArcadeStick`](../GameController/gcproductcategoryarcadestick.md).
- Add [`GCRequiresControllerUserInteraction`](../BundleResources/information-property-list/gcrequirescontrolleruserinteraction.md) to your information property list if your app requires a game controller on visionOS or to recommend a game controller on iOS.

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

*[View on Apple Developer](https://developer.apple.com/documentation/updates/gamecontroller)*