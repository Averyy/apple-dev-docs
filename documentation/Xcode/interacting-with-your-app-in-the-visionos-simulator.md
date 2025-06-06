# Interacting with your app in the visionOS simulator

**Framework**: Xcode

Use your Mac to navigate spaces and control interactions with your visionOS apps in Simulator.

#### Overview

Use Simulator to run apps in visionOS without installing them on a physical device. When you run your app in Simulator, you can see a monoscopic view of your app’s windows and 3D content inside an immersive space. Use your Mac to alter the viewpoint of the app within the space and navigate the app’s interface.

![The visionOS simulator.](https://docs-assets.developer.apple.com/published/8b5ed68e325ae707d2202e5e58ddaf96/interacting-with-your-app-in-the-visionos-simulator%402x.png)

##### Interact with Your App

To use your Mac’s pointer and keyboard to create gestures, choose “Select to interact with the scene” from the buttons at the bottom-right of a visionOS simulator window. You pointer movements control where your eyes look when you hover over content within the space.

Use the following actions to trigger gestures:

| Gesture | To simulate |
| --- | --- |
| Tap | Click. |
| Double-tap | Double-click. |
| Touch and hold | Click and hold. |
| Drag (left, right, up, and down) | Drag left, right, up, and down. |
| Drag (forward and back) | Shift-drag up and down. |
| Two-handed gestures | Press and hold the Option key to display touch points. Move the pointer while pressing the Option key to change the distance between the touch points. Move the pointer and hold the Shift and Option keys to reposition the touch points. |

Activate device buttons using menu items or by clicking the controls in the simulator window toolbar.

##### Navigate the Space

Use your Mac’s pointer and the keyboard to reposition your viewpoint in a visionOS simulator window:

| Movement | To simulate |
| --- | --- |
| Forward | Press the W key (or Up Arrow key), or perform a pinch gesture moving two fingers away from each other on a trackpad. |
| Backward | Press the S key (or Down Arrow key), or perform a pinch gesture moving two fingers toward each other on a trackpad. |
| Left | Press the A key (or Left Arrow key), or scroll left using a trackpad or Magic Mouse. |
| Right | Press the D key (or Right Arrow key), or scroll right using a trackpad or Magic Mouse. |
| Up | Press the E key, or scroll up using a trackpad or Magic Mouse. |
| Down | Press the Q key, or scroll down using a trackpad or Magic Mouse. |

You can also control the viewpoint with a standard drag. To do so, choose “Drag to pan the camera” from the buttons at the bottom-right of the simulator window to move the viewpoint left, right, up or down and choose “Drag to dolly the camera” to move it forward or backward.

To change your viewing angle, Control-drag inside a visionOS simulator window. You can choose “Drag to tilt the camera” from the buttons at the bottom-right of the simulator window to use a drag without the Control key.

To reset the viewpoint and viewing angle for a visionOS simulator, choose the Reset Camera button at the bottom-right of its window.

> **Note**: To direct pointer and keyboard input to the simulated device, select the Capture Pointer or Capture Keyboard buttons in the toolbar at the top-right of a visionOS simulator window. These buttons bypass the use of pointer and keyboard input for the host Mac and prevent them from controlling the viewpoint in a visionOS simulator window. To re-direct the input to the host Mac, press the Esc (Escape) key.

When moving with a trackpad or Magic Mouse, Simulator respects the natural scrolling setting on macOS.

You can also use a game controller to control your movement. Use the left stick to move left, right, forward or back. Use R2 and L2 to move up and down. Use the right stick on a game controller to pan around the space.

##### Switch Between Simulated Scenes

Simulator provides multiple built-in scenes you can use to simulate passthrough in different surroundings. These include unique room layouts and furniture for different testing scenarios, each available in different lighting conditions.

Use the simulated scene to test:

- Readability of your app in varying backgrounds and varying lighting conditions.
- Different scenarios, including limited and cluttered surroundings, to see how your app adapts to them.
- Content layout, positioning, and scale.
- Spatial audio and acoustics.

To change the simulated scene, click the Simulated Scenes button in the toolbar at the top-right of a visionOS simulator window and choose a different scene.

##### Test Shareplay Experiences in Facetime

Launch and test your app’s SharePlay experiences in the simulator using FaceTime. To start a FaceTime session, choose Features > FaceTime, and then choose an option from the submenu. After choosing an option, the selected number of Spatial and Non-Spatial Participants appear in space. Use this session to launch and test your app’s SharePlay Group Activities, and other FaceTime experiences.

> **Note**: Simulator supports SharePlay experiences in Xcode 16 and later.

## See Also

- [Interacting with your app in the iOS and iPadOS simulator](interacting-with-your-app-in-the-ios-or-ipados-simulator.md)
  Use your Mac to control interactions with your iOS and iPadOS apps in Simulator.
- [Interacting with your app in the tvOS simulator](interacting-with-your-app-in-the-tvos-simulator.md)
  Use your Mac to control interactions with your tvOS apps in Simulator.
- [Interacting with your app in the watchOS simulator](interacting-with-your-app-in-the-watchos-simulator.md)
  Use your Mac to control interactions with your watchOS apps in Simulator.
- [Configuring Simulator for your working environment](configuring-a-simulator-for-your-environment.md)
  Adjust Simulator settings for window or screen size, light or dark appearance, and audio settings, and restart or reset a simulated device.
- [Simulating an external display or CarPlay](simulating-an-external-display-or-carplay.md)
  Test how your app handles an external display or CarPlay from Simulator.
- [Capturing screenshots and videos from Simulator](capturing-screenshots-and-videos-from-simulator.md)
  Record and share test results, or prepare for App Store distribution with screenshots and videos of your app from Simulator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/interacting-with-your-app-in-the-visionos-simulator)*