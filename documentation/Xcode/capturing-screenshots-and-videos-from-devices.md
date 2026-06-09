# Capturing screenshots and videos from devices

**Framework**: Xcode

Record interactions and capture screenshots of your app for sharing, review, or App Store submission.

#### Overview

Use Device Hub to capture screenshots and record videos of your app in action to:

- Help other people on your team understand a bug or design issue.
- Document how your app responds to accessibility changes.
- Verify translations and interface adjustments for different languages.
- Prepare and update your App Store page to show your app’s best features.

> **Note**: Screenshots and videos you capture from a visionOS simulator might have a different size and ratio than those you capture from a physical device. To match App Store requirements, you can resize and crop them. For more information, see [`Screenshot Specifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/screenshot-specifications) and [`App Preview Specifications`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/reference/app-preview-specifications).

#### Capture Screenshots on Simulated and Physical Devices

To take a screenshot, run your app on a simulated or physical device in Device Hub. Navigate to the place in your app where you want to capture a screenshot. Then click the Screenshot button below the device in the canvas. Device Hub captures the screenshot at the full resolution of the simulated or physical device, regardless of the display resolution of your Mac. Device Hub saves the screenshot to the Desktop folder on your Mac.

![A screenshot of Device Hub showing a compact window of an iPhone simulator running the Landmarks sample code app with the Screenshot and Record button below the device.](https://docs-assets.developer.apple.com/published/ca999ea628e2f9bfd34ece670a1b2e92/capture-device-screenshot-and-video%402x.png)

#### Record Videos on Simulated Devices

To record a video of your app, run your app on a simulated device in Device Hub and navigate to where you want to the video to start. Click the Record button below the device in the canvas or choose Controls > Record Screen. Then begin interacting with your app while recording. To stop the recording, click the Stop button below the device or choose Controls > Stop Recording. Device Hub saves the video file to your Desktop folder. The filename begins with `Screen Recording` followed by the device name and timestamp.

## See Also

- [Configuring the environment of a simulated device](configuring-the-environment-of-a-simulated-device.md)
  Modify the settings of a simulated device.
- [Interacting with your app in Device Hub](interacting-with-your-app-in-device-hub.md)
  Use Device Hub to control interactions with your apps on simulated and physical devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/capturing-screenshots-and-videos-from-devices)*