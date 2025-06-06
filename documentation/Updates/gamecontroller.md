# Game Controller updates

**Framework**: Updates

Learn about important changes to Game Controller.

#### Overview

Browse notable changes in [`Game Controller`](https://developer.apple.com/documentation/GameController).

#### June 2024

##### Visionos

- For UIKit apps, add a user interaction that determines whether the system delivers game controller events through the Game Controller framework instead of the [`UIResponder`](https://developer.apple.com/documentation/UIKit/UIResponder) chain. To receive events through the Game Controller framework, add a [`GCEventInteraction`](https://developer.apple.com/documentation/GameController/GCEventInteraction) object to one or more views and set the [`handledEventTypes`](https://developer.apple.com/documentation/GameController/GCEventInteraction/handledEventTypes) property to the types of events you want to handle.

#### June 2023

- Use the classes that conform to the [`GCDevicePhysicalInput`](https://developer.apple.com/documentation/GameController/GCDevicePhysicalInput) protocol to poll for game controller input in your game loop. For more information, see  [`Handling input events`](https://developer.apple.com/documentation/GameController/handling-input-events).
- Add support for arcade sticks. To determine if a controller is an arcade stick, check whether the product category is  [`GCProductCategoryArcadeStick`](https://developer.apple.com/documentation/GameController/GCProductCategoryArcadeStick).
- Add [`GCRequiresControllerUserInteraction`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCRequiresControllerUserInteraction) to your information property list if your app requires a game controller on visionOS or to recommend a game controller on iOS.

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
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
- [Bundle Resources updates](bundleresources.md)
  Learn about important changes to Bundle Resources.
- [ContactsUI updates](contactsui.md)
  Learn about important changes to ContactsUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/gamecontroller)*