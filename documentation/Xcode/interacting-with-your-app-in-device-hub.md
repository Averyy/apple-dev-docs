# Interacting with your app in Device Hub

**Framework**: Xcode  
**Role**: Article

Use Device Hub to control interactions with your apps on simulated and physical devices.

#### Overview

You use similar controls on your Mac to interact with your app on a simulated and physical device that appears in the Device Hub canvas.

When you launch your app on a simulated device, Device Hub opens to show the device screen in a compact window. When you launch your app on a physical device, Xcode runs it on the device. To interact with the device in Device Hub, select the device in the sidebar and click View Screen in the canvas area.

Device Hub surrounds the screen content with a bezel that resembles the target device. In visionOS, it displays a synthetic space to mimic the experience someone would have when they wear the device. Each device bezel and space has specific controls to support interactions. To show or hide bezels in the canvas, choose View > Show Bezels or View > Hide Bezels.

![A screenshot of Device Hub showing an iOS simulator in compact view running a sample code app.](https://developer.apple.com/tutorials/images/com.apple.Xcode/running-app-in-ios-simulator@2x.png)

To interact with a simulated Apple Vision Pro device in Device Hub, see [Interacting with your visionOS app in Device Hub](./interacting-with-your-visionos-app-in-device-hub.md). To take screenshots and record videos, see [Capturing screenshots and videos from devices](./capturing-screenshots-and-videos-from-devices.md).

#### Interact with your iOS or iPadOS app in the canvas

Use your Mac’s pointer, trackpad or Magic Mouse, keyboard, menu items, and buttons to make gestures on a simulated iOS or iPadOS device.

| Gesture | To simulate |
| --- | --- |
| Tap | Click. |
| Double-tap | Double-click. |
| Touch and hold | Click and hold. |
| Drag and drop | Click and hold until the drag item appears, then drag the item to the target. |
| Activate Siri | Hold the Sleep/Wake button on the device bezel or choose Controls > Siri. |
| Shake the device | Choose Controls > Shake. |
| Rotate the simulator to the left | Click the rotate button under the device bezel or choose Controls > Rotate Left. |
| Rotate the simulator to the right | Option-click the rotate button under the device bezel or choose Controls > Rotate Right. |
| Set the orientation of the device | Choose an orientation from the Device > Orientation submenu. Face Up and Face Down do not rotate the simulator. |

Activate device buttons by clicking on parts of the device bezel:

| Button | To simulate |
| --- | --- |
| Click the Home button | Click the Home button below the device bezel or choose Controls > Home. |
| Click the Sleep/Wake button | Click the Sleep/Wake button on the device bezel or choose Controls > Lock. |
| Click or hold Volume Up | Click or hold the Volume Up button on the device bezel or choose Device > Sound > Increase Volume. |
| Click or hold Volume Down | Click or hold the Volume Down button on the device bezel or choose Device > Sound > Decrease Volume. |
| Click the Action button | Click the Action button on the device bezel. |

#### Interact with your iOS app on an iPhone Duo simulator

To ensure your iOS app adapts seamlessly to both iPhone Duo displays, simulate folding an iPhone Duo using the controls below the bezel in the canvas:

- To close the iPhone Duo, click the Closed button on the right of the Rotate Right button.
- To partially open the iPhone Duo, click the Partially Open button in the middle of the three device pose buttons.
- To fully open the iPhone Duo, click the Open button on the far right.

To fold the device to any angle, hold the Option key while dragging the slider that appears below the bezel.

![A screenshot of Device Hub that shows an iPhone Duo simulator running a sample code app in the partially open device pose. The device pose buttons appear below the bezel.](https://developer.apple.com/tutorials/images/com.apple.Xcode/running-app-in-iphone-duo-simulator@2x.png)

#### Interact with your watchOS app in the canvas

Use the pointer, trackpad or Magic Mouse, keyboard, and menu items to make gestures on a simulated watchOS device.

| Gesture | To simulate |
| --- | --- |
| Tap | Click. |
| Double-tap | Double-click. |
| Touch and hold | Click and hold. |
| Activate Siri | Hold the Sleep/Wake button on the device bezel or choose Controls > Siri. |

Activate device buttons using menu items or by clicking on parts of the device bezel:

| Button | To simulate |
| --- | --- |
| Push in the Digital Crown | Click the Digital Crown on the device bezel. |
| Rotate the Digital Crown clockwise or counterclockwise | Place the pointer over the Digital Crown on the device bezel and scroll using a mouse wheel or trackpad. If the bezel is hidden, move the pointer over the simulator window, then scroll using a mouse wheel or trackpad. |
| Click the Side button | Click the Side button on the device bezel. |
| Click the Action button | Click the Action button on the device bezel or choose Controls > Action Button. |

#### Interact with your tvOS app in the canvas

Use the pointer, keyboard, and menu items to make gestures on a simulated tvOS device.

| Gesture | To simulate |
| --- | --- |
| Move the focus to the left | Press the Left Arrow key. |
| Move the focus to the right | Press the Right Arrow key. |
| Move the focus up | Press the Up Arrow key. |
| Move the focus down | Press the Down Arrow key. |
| Trigger the action for the current focus | Press the Return key. |
| Move up one level in the navigation hierarchy | Press the Escape key. |

##### Slow down animations to diagnose problems

You can slow down the rate of animations to help identify any layout, logic, or performance issues that interfere with smooth animations. To turn on or off slow animations, choose Device > Slow Animations.

#### Handle camera and microphone access conflicts on physical devices

You can’t access the camera or microphone while interacting with a physical device in Device Hub.

Before you can start interacting with a physical device in Device Hub, quit any apps on the device that access the camera or microphone. Then select the device in the sidebar and click View Screen in the canvas to interact with the device.

While you interact with the device, lower-priority apps that access the camera or microphone, such as Camera and Voice Memos, don’t have access to those sensors and may record silence and empty video.

If you launch higher-priority apps on the device that access the camera or microphone, such as Phone or FaceTime, Device Hub stops the interaction. To continue interacting with the device, quit the apps that use the camera or microphone on the device and click View Screen in Device Hub again.

## See Also

### Device interactions
- [Configuring the environment of a simulated device](./configuring-the-environment-of-a-simulated-device.md)
  Modify the settings of a simulated device.
- [Interacting with your visionOS app in Device Hub](./interacting-with-your-visionos-app-in-device-hub.md)
  Use Device Hub to navigate spaces and control interactions with your visionOS apps running on simulated visionOS devices.
- [Capturing screenshots and videos from devices](./capturing-screenshots-and-videos-from-devices.md)
  Record interactions and capture screenshots of your app for sharing, review, or App Store submission.
- [Interacting with devices using the command line](./interacting-with-devices-using-the-command-line.md)
  Manage simulated and physical devices from the command line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/interacting-with-your-app-in-device-hub)*