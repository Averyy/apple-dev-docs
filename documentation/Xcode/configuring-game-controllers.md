# Configuring game controllers

**Framework**: Xcode

Enhance gameplay input by enabling the discovery, configuration, and use of physical game controllers.

#### Overview

Game controllers provide physical controls to trigger actions in your game. Apple specifies the look and behavior of the controls to MFi accessory manufacturers, which means you can rely on a consistent set of high-quality controls in all supported game controllers.

A game that supports game controllers enables one or more different  — objects that map physical controls on a device to the inputs your game requires — such as Extended, Micro, and Directional. The game also specifies the preferred order of use for these profiles. After retrieving a profile from the connected game controller, your game periodically requests the device’s current values or installs handlers that the system invokes when those values change.

Before you can select the profiles your game supports, follow the steps in [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) to add the Game Controllers capability to your game’s target.

![A screenshot of Xcode’s Capabilities library with a list of available capabilities on the left and an information pane on the right. The list shows a range of capabilities from Game Controllers to Keychain Sharing, and the Game Controllers capability is in a selected state. The text on the information pane explains that the Game Controllers capability adds supports for game controllers to your app.](https://docs-assets.developer.apple.com/published/45e1533715f8be6bb269bff3e898b86b/game-controllers%402x.png)

After you add the Game Controllers capability to your game’s target, Xcode appends the [`GCSupportsControllerUserInteraction`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportsControllerUserInteraction) key to its `Info.plist` file with a value of `true` to indicate to the system that your game supports game controllers.

> **Note**: The Game Controllers capability is only available to games that target iOS, iPadOS, tvOS, and visionOS.

The Game Controllers capability is only available to games that target iOS, iPadOS, tvOS, and visionOS.

##### Select the Supported Game Controller Profiles

When you add support for game controllers to your app, you don’t integrate with specific hardware. Instead, you integrate one or more of the game-controller profiles that the [`Game Controller`](https://developer.apple.com/documentation/GameController) framework provides. Each profile maps to a control layout that Apple defines, and that profile describes a set of physical controls that the hardware manufacturer guarantees to be available on the controller.

To indicate to the system which game-controller profiles your game supports, perform the following steps:

1. Select your project in Xcode’s Project navigator.
2. Select the game’s target from the Targets list.
3. Click the Signing & Capabilities tab in the project editor.
4. Find the Game Controllers capability.
5. Select the appropriate game controller profiles by checking their checkboxes.

![A screenshot of the Game Controllers capability after you add it to a target. The Extended Gamepad, Micro Gamepad, and Directional Gamepad profiles are in an enabled state.](https://docs-assets.developer.apple.com/published/ca459e7915dba4bfc87d56726c0e8b30/game-controller-types%402x.png)

Xcode adds the [`GCSupportedGameControllers`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportedGameControllers) array to your game’s `Info.plist` file, if it’s not already present, and populates it with names of the selected game-controller profiles. For more information about each profile, see [`GCExtendedGamepad`](https://developer.apple.com/documentation/GameController/GCExtendedGamepad), [`GCMicroGamepad`](https://developer.apple.com/documentation/GameController/GCMicroGamepad), and [`GCDirectionalGamepad`](https://developer.apple.com/documentation/GameController/GCDirectionalGamepad).

Hardware controllers can support multiple profiles; if you enable more than one game controller profile, drag the profiles and arrange them in your preferred order. For example, if your game supports both the Extended and Micro profiles, but optimizes gameplay for the Micro profile, place that profile at the top of the list.

For more information, see the video [`Tap into virtual and physical game controllers`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10081) and the sample code [`Supporting Game Controllers`](https://developer.apple.com/documentation/GameController/supporting-game-controllers).

## See Also

- [Configuring background execution modes](configuring-background-execution-modes.md)
  Indicate the background services your app requires to continue executing in the background in iOS, iPadOS, tvOS, visionOS, and watchOS.
- [Configuring custom fonts](configuring-custom-fonts.md)
  Register your app as a provider or consumer of systemwide custom fonts.
- [Configuring Maps support](configuring-maps-support.md)
  Register your iOS routing app to provide point-to-point directions to Maps and other apps.
- [Configuring Siri support](configuring-siri-support.md)
  Enable your app and its Intents extension to resolve, confirm, and handle user-driven Siri requests for your app’s services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-game-controllers)*