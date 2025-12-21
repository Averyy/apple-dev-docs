# Simulating an external display or CarPlay

**Framework**: Xcode

Test how your app handles an external display or CarPlay from Simulator.

#### Overview

Some iPhone and iPad devices support a wired connection to an external display. When you plug your compatible device into a supported external display, the device mirrors its display to the external display.

In addition to external displays, iPhone devices running iOS 12.0 and later support connecting to CarPlay compatible vehicles. For more information on supporting CarPlay in your app, see [`CarPlay`](https://developer.apple.com/documentation/CarPlay).

Test your app’s support of external displays or CarPlay in Simulator during development, then test on actual devices.

##### Enable an External Display or Carplay

First, build and run your app in Simulator. For more information, see [`Running your app in Simulator or on a device`](running-your-app-in-simulator-or-on-a-device.md).

When your app is running in Simulator, choose I/O > External Displays, then select an external display size or CarPlay. The supported options are:

- 640x480
- 720x480
- 1024x768
- 1280x720 (720p)
- 1920x1080 (1080p)
- 3840x2160 (4K)
- CarPlay

Simulator opens a new window for the external display with the selected size.

Close the external display window, or choose I/O > External Displays > Disable to simulate unplugging from the external display.

## See Also

- [Interacting with your app in the iOS and iPadOS simulator](interacting-with-your-app-in-the-ios-or-ipados-simulator.md)
  Use your Mac to control interactions with your iOS and iPadOS apps in Simulator.
- [Interacting with your app in the tvOS simulator](interacting-with-your-app-in-the-tvos-simulator.md)
  Use your Mac to control interactions with your tvOS apps in Simulator.
- [Interacting with your app in the watchOS simulator](interacting-with-your-app-in-the-watchos-simulator.md)
  Use your Mac to control interactions with your watchOS apps in Simulator.
- [Interacting with your app in the visionOS simulator](interacting-with-your-app-in-the-visionos-simulator.md)
  Use your Mac to navigate spaces and control interactions with your visionOS apps in Simulator.
- [Configuring Simulator for your working environment](configuring-a-simulator-for-your-environment.md)
  Adjust Simulator settings for window or screen size, the light or dark appearance, and audio settings, and restart or reset a simulated device.
- [Capturing screenshots and videos from Simulator](capturing-screenshots-and-videos-from-simulator.md)
  Record and share test results, or prepare for App Store distribution with screenshots and videos of your app from Simulator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/simulating-an-external-display-or-carplay)*