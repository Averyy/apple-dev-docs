# Configuring Simulator for your working environment

**Framework**: Xcode

Adjust Simulator settings for window or screen size, light or dark appearance, and audio settings, and restart or reset a simulated device.

#### Overview

When you’re testing your app, taking screenshots, or inspecting your user interface, you may want to configure Simulator to help accomplish your task. There are several options you can adjust:

- Light mode or dark mode
- Window or screen size
- Bezel display
- Audio settings

When you need to test your app after a device restart, or you want to simulate loading your app in a new device, you can restart or reset a simulated device.

##### Toggle Light and Dark Appearance

Test your app in both light and dark mode on supported platforms to confirm that your user interface looks correct for both appearances. To switch appearances, choose Features > Toggle Appearance.

##### Resize a Simulator Window

You can change the size of the window to match the physical device characteristics. For example, display the same number of pixels as the hardware device’s screen to check alignment of controls, images, and colors used in your app.

To change the window size to the hardware device’s screen size, choose Window > Physical size.

To change the window size to the same scale factor as the physical device, choose Window > Point Accurate.

To change the window size to the same number of pixels as the physical device, choose Window > Pixel Accurate.

Alternatively, hold the pointer over a corner of the window until it changes to the resize cursor, then drag the window frame to the desired size.

##### Show the Simulator Bezel

The simulator bezel for iOS and watchOS devices includes elements for the buttons and switches found on those devices that you can click to simulate pressing.

Select a simulator window, then choose Window > Show Device Bezels to show or hide the simulator bezel. A checkmark next to Show Device Bezels indicates the bezel is visible.

##### Set the Audio Input and Output

Set the audio input and audio output that simulated devices use.

To set audio input, choose a device from the I/O > Audio Input submenu. Choose System to use the same audio input as the Mac.

To set audio output, choose a device from the I/O > Audio Output submenu. Choose System to use the same audio output as the Mac.

To adjust audio volume choose I/O > Increase Volume or I/O > Decrease Volume.

Simulator keeps track of the most recent selections for input and for output. Simulator attempts to connect to the previously selected device when the currently selected device is disconnected.

> **Note**: When Bluetooth headphones are selected as the input source, playing or listening to audio in Simulator sets the headphones to phone call mode which lowers the quality of the audio. To hear sound at full quality, choose a different audio input source for Simulator.

When Bluetooth headphones are selected as the input source, playing or listening to audio in Simulator sets the headphones to phone call mode which lowers the quality of the audio. To hear sound at full quality, choose a different audio input source for Simulator.

##### Restart or Reset a Simulated Device

Restart a simulated device to simulate turning off and turning back on a device. To do this, choose Device > Restart.

Reset a simulated device to factory settings to clear out all installed apps and any data you may have added to the simulated device. To do this, choose Device > Erase All Contents and Settings…, and then choose Erase from the confirmation dialog.

## See Also

- [Interacting with your app in the iOS and iPadOS simulator](interacting-with-your-app-in-the-ios-or-ipados-simulator.md)
  Use your Mac to control interactions with your iOS and iPadOS apps in Simulator.
- [Interacting with your app in the tvOS simulator](interacting-with-your-app-in-the-tvos-simulator.md)
  Use your Mac to control interactions with your tvOS apps in Simulator.
- [Interacting with your app in the watchOS simulator](interacting-with-your-app-in-the-watchos-simulator.md)
  Use your Mac to control interactions with your watchOS apps in Simulator.
- [Interacting with your app in the visionOS simulator](interacting-with-your-app-in-the-visionos-simulator.md)
  Use your Mac to navigate spaces and control interactions with your visionOS apps in Simulator.
- [Simulating an external display or CarPlay](simulating-an-external-display-or-carplay.md)
  Test how your app handles an external display or CarPlay from Simulator.
- [Capturing screenshots and videos from Simulator](capturing-screenshots-and-videos-from-simulator.md)
  Record and share test results, or prepare for App Store distribution with screenshots and videos of your app from Simulator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-a-simulator-for-your-environment)*