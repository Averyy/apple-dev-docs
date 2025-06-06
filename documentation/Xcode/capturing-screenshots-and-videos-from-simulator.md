# Capturing screenshots and videos from Simulator

**Framework**: Xcode

Record and share test results, or prepare for App Store distribution with screenshots and videos of your app from Simulator.

#### Overview

Screenshots or videos of your app in action are useful for these and other needs:

- Help other people on your team understand a bug or design issue.
- Document how your app responds to accessibility changes.
- Confirm your app layout changes appropriately for localization and internationalization.
- Prepare and update your App Store page to show your app’s best features.

Use Simulator to efficiently capture screenshots and videos of your app in action in different Simulator platforms and devices. Simulator captures screenshots at the full resolution of the simulated device, regardless of the display resolution of your Mac.

> **Note**: Screenshots and videos you capture from a visionOS simulator might have a different size and ratio than those you capture from a physical device. To match App Store requirements, you can resize and crop them. For more information, see [`Screenshot Specifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/screenshot-specifications) and [`App Preview Specifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-preview-specifications).

Screenshots and videos you capture from a visionOS simulator might have a different size and ratio than those you capture from a physical device. To match App Store requirements, you can resize and crop them. For more information, see [`Screenshot Specifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/screenshot-specifications) and [`App Preview Specifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-preview-specifications).

##### Capture a Screenshot of Your App

To take a screenshot, navigate to the place in your app you would like to capture, then:

1. Choose File > Save Screen.
2. Simulator takes the screenshot, then displays a preview of the screenshot next to the Simulator window.
3. If you want to edit the screenshot, tap the preview to open it in an editor. Otherwise, Simulator saves the screenshot to your Desktop folder. Press and hold the Option key when you choose File > Save Screen to choose a location for the screen shot.

Simulator creates a file name with a combination of “Simulator Screen Shot - “, the name of the Simulator device, and the date and time.

##### Record Video of Interactions in Your App

To record video, set up your app in Simulator and navigate to a view where you’d like to start your video, then:

1. Choose File > Record Screen.
2. Simulator begins recording the screen.
3. Interact with your app while recording.
4. Choose File > Stop Recording, or click the stop button in the simulator device’s control bar.
5. Simulator finishes the recording, then displays a preview of the screenshot next to the Simulator window.
6. Simulator saves the recording to your Desktop folder. Press and hold the Option key when you choose File > Record Screen to choose a location for the recording.

Simulator creates a file name with a combination of “Simulator Screen Recording - “, the name of the Simulator device, and the date and time.

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
  Adjust Simulator settings for window or screen size, light or dark appearance, and audio settings, and restart or reset a simulated device.
- [Simulating an external display or CarPlay](simulating-an-external-display-or-carplay.md)
  Test how your app handles an external display or CarPlay from Simulator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/capturing-screenshots-and-videos-from-simulator)*