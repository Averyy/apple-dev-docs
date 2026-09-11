# Interacting with your visionOS app in Device Hub

**Framework**: Xcode

Use Device Hub to navigate spaces and control interactions with your visionOS apps running on simulated visionOS devices.

#### Overview

Before interacting with your app, you need to build and run your app on a simulated visionOS device. In Xcode, choose a simulated visionOS device as the run destination and click the Run button. For more information, see [`Running your app on simulated or physical devices`](running-your-app-on-simulated-or-physical-devices.md).

After your app successfully builds, Device Hub opens to show the simulated device in a compact window running your app. Use the controls in the Device Hub canvas to alter the viewpoint of the app within the space and navigate the app’s interface.

![A screenshot of Device Hub showing an Apple Vision Pro simulator in compact view running the TabletopKit sample code app.](/images/com.apple.Xcode/running-app-in-visionos-simulator@2x.png)

To take screenshots and record videos, see [`Capturing screenshots and videos from devices`](capturing-screenshots-and-videos-from-devices.md).

> 💡 **Tip**: If you build and run your app on a physical device, you can interact with Xcode running side-by-side. For more information, see [`Use Mac Virtual Display on Apple Vision Pro`](https://developer.apple.comhttps://support.apple.com/guide/apple-vision-pro/use-mac-virtual-display-tan357ede966/26/visionos/26).

#### Interact with Your Visionos App in the Canvas

To use your Mac’s pointer and keyboard to create gestures, choose “Select to interact with the visionOS content” from the segmented control at the bottom of the canvas. Your pointer movements control where your eyes look when you hover over content within the space.

Use the following actions to trigger gestures:

| Gesture | To simulate |
| --- | --- |
| Tap | Click. |
| Pinch and hold | Click and hold. |
| Pinch and drag (left, right, up, and down) | Drag left, right, up, and down. |
| Pinch and drag (forward and back) | Shift-drag up and down. |
| Swipe | Click and swipe. |

Activate other actions using device controls at the bottom of the canvas or from the Controls menu:

| Action | To simulate |
| --- | --- |
| Open Home View | Click the Home button from the buttons at the bottom-left of the canvas or choose Controls > Home. |
| Open Control Center | Hover over and click the Control Center indicator at the top-center of the view. |
| Adjust volume (up) | Choose Device > Sound > Increase Volume. |
| Adjust volume (down) | Choose Device > Sound > Decrease Volume. |

![A screenshot of Device Hub showing an Apple Vision Pro simulator running the TabletopKit sample code app with the Control Center displayed.](/images/com.apple.Xcode/opening-control-center@2x.png)

#### Navigate the Space

Use your Mac’s pointer and the keyboard to reposition your viewpoint:

| Movement | To simulate |
| --- | --- |
| Forward | Press the W key (or Up Arrow key), or perform a pinch gesture moving two fingers away from each other on a trackpad. |
| Backward | Press the S key (or Down Arrow key), or perform a pinch gesture moving two fingers toward each other on a trackpad. |
| Left | Press the A key (or Left Arrow key), or scroll left using a trackpad or Magic Mouse. |
| Right | Press the D key (or Right Arrow key), or scroll right using a trackpad or Magic Mouse. |
| Up | Press the E key, or scroll up using a trackpad or Magic Mouse. |
| Down | Press the Q key, or scroll down using a trackpad or Magic Mouse. |

You can also control the viewpoint with a standard drag. To move the viewpoint left, right, up, or down, select “Drag to pan the camera” from the segmented control at the bottom of the canvas. To move it forward or backward, select “Drag to dolly the camera”.

To change your viewing angle, Control-drag inside the canvas. To use a drag without the Control key, select “Drag to tilt the camera” from the segmented control at the bottom of the canvas.

To reset the viewpoint and viewing angle, click the Reset Camera button at the bottom-right of the canvas.

To direct pointer input to a simulated device, click Capture Pointer from the buttons at the bottom-right of the canvas. To direct keyboard input, choose Device > Keyboard > Keyboard Capture. These controls bypass the use of pointer and keyboard input for the host Mac and prevent them from controlling the viewpoint in the canvas. To redirect the input to your Mac, press the Escape key.

When moving with a trackpad or Magic Mouse, Device Hub respects the natural scrolling setting on macOS.

You can also use a game controller to control your movement. Use the left stick to move left, right, forward, or back. Use R2 and L2 to move up and down. Use the right stick on a game controller to pan around the space.

#### Switch Between Simulated Scenes

Device Hub provides multiple built-in scenes you can use to simulate passthrough in different surroundings. These include unique room layouts and furniture for different testing scenarios, each available in different lighting conditions.

Use the Simulated Scenes to test:

- Readability of your app in varying backgrounds and varying lighting conditions.
- Different scenarios, including limited and cluttered surroundings, to see how your app adapts to them.
- Content layout, positioning, and scale.
- Spatial audio and acoustics.

![A screenshot of Device Hub showing an Apple Vision Pro simulator in expanded view with the Simulated Scenes popover in the inspector open.](/images/com.apple.Xcode/change-simulated-scene@2x.png)

To change the Simulated Scene, in the Settings inspector, click Select next to Simulated Scenes and choose a scene from the popover.

#### Test Shareplay Experiences in Facetime

Launch and test your app’s SharePlay experiences in a simulator using FaceTime. To start a FaceTime session, choose Device > FaceTime, then choose an option from the submenu, such as “User and 3 Spatial Participants”. After choosing an option, the selected number of Spatial and Non-Spatial Participants appear in space. Use this session to launch and test your app’s SharePlay Group Activities, and other FaceTime experiences.

## See Also

- [Configuring the environment of a simulated device](configuring-the-environment-of-a-simulated-device.md)
  Modify the settings of a simulated device.
- [Interacting with your app in Device Hub](interacting-with-your-app-in-device-hub.md)
  Use Device Hub to control interactions with your apps on simulated and physical devices.
- [Capturing screenshots and videos from devices](capturing-screenshots-and-videos-from-devices.md)
  Record interactions and capture screenshots of your app for sharing, review, or App Store submission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/interacting-with-your-visionos-app-in-device-hub)*