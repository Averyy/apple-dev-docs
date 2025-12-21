# Interacting with your app in the tvOS simulator

**Framework**: Xcode

Use your Mac to control interactions with your tvOS apps in Simulator.

#### Overview

Simulator offers an environment to run apps in tvOS without installing them on a physical device. When running your app in Simulator, use your Mac to navigate the app’s interface.

##### Navigate Your Interface

Use the pointer, keyboard, and menu items to make gestures on a simulated tvOS device.

| Gesture | To simulate |
| --- | --- |
| Move the focus to the left | Press the Left Arrow key. |
| Move the focus to the right | Press the Right Arrow key. |
| Move the focus up | Press the Up Arrow key. |
| Move the focus down | Press the Down Arrow key. |
| Trigger the action for the current focus | Press the Return key. |
| Move up one level in the navigation hierarchy | Press the Escape key. |

Simulator also provides a simulated tvOS remote, which you display by choosing Windows > Show Apple TV Remote. To simulate interactions with the touch surface, move the pointer along the surface while pressing the Option key. Select a focus item by Option-clicking. Open a contextual menu by Option-clicking and holding. Use the other buttons of the remote to simulate the corresponding functions.

##### Navigate Using a Physical Remote Control

To use a physical Apple TV Remote or MFi controller with Simulator:

1. Unpair the remote or controller if it is already paired with another device.
2. Turn off the remote or controller.
3. On the Mac, open Bluetooth in System Settings.
4. In Bluetooth settings, turn Bluetooth on.
5. Turn on the remote or controller.
6. In Bluetooth settings, wait for the remote to appear in the Devices list.
7. Click the Pair button next to the device to pair it with the Mac.

Some remotes and controllers don’t appear in Bluetooth settings unless you put them into pairing mode. To enter pairing mode on an Apple TV remote, hold down the Menu and Volume Up (+) buttons for 5 seconds. For information on how to enter pairing mode on other devices, see the documentation for your device.

## See Also

- [Interacting with your app in the iOS and iPadOS simulator](interacting-with-your-app-in-the-ios-or-ipados-simulator.md)
  Use your Mac to control interactions with your iOS and iPadOS apps in Simulator.
- [Interacting with your app in the watchOS simulator](interacting-with-your-app-in-the-watchos-simulator.md)
  Use your Mac to control interactions with your watchOS apps in Simulator.
- [Interacting with your app in the visionOS simulator](interacting-with-your-app-in-the-visionos-simulator.md)
  Use your Mac to navigate spaces and control interactions with your visionOS apps in Simulator.
- [Configuring Simulator for your working environment](configuring-a-simulator-for-your-environment.md)
  Adjust Simulator settings for window or screen size, the light or dark appearance, and audio settings, and restart or reset a simulated device.
- [Simulating an external display or CarPlay](simulating-an-external-display-or-carplay.md)
  Test how your app handles an external display or CarPlay from Simulator.
- [Capturing screenshots and videos from Simulator](capturing-screenshots-and-videos-from-simulator.md)
  Record and share test results, or prepare for App Store distribution with screenshots and videos of your app from Simulator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/interacting-with-your-app-in-the-tvos-simulator)*