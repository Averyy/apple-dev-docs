# Interacting with your app in Device Hub

**Framework**: Xcode

Use Device Hub to control interactions with your apps on simulated and physical devices.

#### Overview

You use similar controls on your Mac to interact with your app on a simulated and physical device that appears in the Device Hub canvas.

When you launch your app on a simulated device, Device Hub opens to show the device screen in a compact window. When you launch your app on a physical device, Xcode runs it on the device. To interact with the device in Device Hub, select the device in the sidebar and click View Screen in the canvas area.

Device Hub surrounds the screen content with a bezel that resembles the target device. In visionOS, it displays a synthetic space to mimic the experience someone would have when they wear the device. Each device bezel and space has specific controls to support interactions.

#### Interact with Your Ios or Ipados App in the Canvas

Use your Mac’s pointer, trackpad or Magic Mouse, keyboard, menu items, and buttons to make gestures on a simulated iOS or iPadOS device.

| Gesture | To simulate |
| --- | --- |
| Tap | Click. |
| Double-tap | Double-click. |
| Touch and hold | Click and hold. |
| Drag and drop | Click and hold until the drag item appears, then drag the item to the target. |
| Activate Siri | Hold the Sleep/Wake button on the device bezel or choose Controls > Siri. |
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

#### Interact with Your Watchos App in the Canvas

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

#### Interact with Your Tvos App in the Canvas

Use the pointer, keyboard, and menu items to make gestures on a simulated tvOS device.

| Gesture | To simulate |
| --- | --- |
| Move the focus to the left | Press the Left Arrow key. |
| Move the focus to the right | Press the Right Arrow key. |
| Move the focus up | Press the Up Arrow key. |
| Move the focus down | Press the Down Arrow key. |
| Trigger the action for the current focus | Press the Return key. |
| Move up one level in the navigation hierarchy | Press the Escape key. |

#### Handle Camera and Microphone Access Conflicts on Physical Devices

You can’t access the camera or microphone while interacting with a physical device in Device Hub.

Before you can start interacting with a physical device in Device Hub, quit any apps on the device that access the camera or microphone. Then select the device in the sidebar and click View Screen in the canvas to interact with the device.

While you interact with the device, lower-priority apps that access the camera or microphone, such as Camera and Voice Memos, don’t have access to those sensors and may record silence and empty video.

If you launch higher-priority apps on the device that access the camera or microphone, such as Phone or FaceTime, Device Hub stops the interaction. To continue interacting with the device, quit the apps that use the camera or microphone on the device and click View Screen in Device Hub again.

## See Also

- [Configuring the environment of a simulated device](configuring-the-environment-of-a-simulated-device.md)
  Modify the settings of a simulated device.
- [Capturing screenshots and videos from devices](capturing-screenshots-and-videos-from-devices.md)
  Record interactions and capture screenshots of your app for sharing, review, or App Store submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/interacting-with-your-app-in-device-hub)*