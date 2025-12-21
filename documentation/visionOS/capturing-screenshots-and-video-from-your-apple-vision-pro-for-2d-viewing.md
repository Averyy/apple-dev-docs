# Capturing screenshots and video from Apple Vision Pro for 2D viewing

**Framework**: visionOS

Create screenshots and record high-quality video of your visionOS app and its surroundings for app previews.

#### Overview

Use screenshots and short videos of your visionOS app to showcase your user interface, highlight functionality, and demonstrate usage. Help people understand what to expect from an immersive experience by recording content from Apple Vision Pro that includes your app and its surroundings.

The system renders content with spatial effects and optimizations for viewing during immersive experiences. One optimization, , displays higher resolution where an enrolled person is looking, while reducing image resolution in their periphery. The system only applies foveated rendering for enrolled users who calibrate the device for their eyes and hands. Techniques that improve rendering performance during normal operation are intended to be unnoticeable for enrolled people wearing Apple Vision Pro; however, they don’t translate well to 2D displays.

To produce high-resolution content for people to view on 2D displays, the system needs to render without these effects and drop some optimizations. Use Developer Capture in Reality Composer Pro to notify the system to reconfigure rendering, and capture screenshots or high-resolution video, including sound, from Apple Vision Pro. Because capturing high-resolution video from device is resource intensive, Reality Composer Pro limits the duration of device video capture.

> **Note**: For guidance on the screenshots and previews you include in your app’s product page, see [`Submit your apps to the App Store for Apple Vision Pro`](https://developer.apple.comhttps://developer.apple.com/visionos/submit/).

##### Pair Your Apple Vision Pro to Xcode

Before capturing screenshots and video from your device, pair it with a Mac that has Xcode and the visionOS SDK installed. For instructions on pairing your device, see [`Running your app in Simulator or on a device`](https://developer.apple.com/documentation/Xcode/running-your-app-in-simulator-or-on-a-device).

##### Prepare to Capture Your App and Its Surroundings

Select a well-lit location that’s free from clutter. Avoid including objects that might distract the audience or get in the way of your app‘s windows and 3D content. Include enough detail in the scene to provide context and anchoring points. Avoid material that you don’t have permission to capture, including people, screens, branded products, logos, artwork, and other intellectual property.

Use the version of your app that you intend to share with your audience. Build and install your app using a release configuration. This configuration enables code optimizations for better runtime performance and disables the generation of debugging information. Debug configurations typically disable code optimizations and might include UI you donʼt intend to share. Don’t use them to record video for previews you intend to share. Build schemes manage the build configuration Xcode uses during build actions, for more information see [`Customizing the build schemes for a project`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/customizing-the-build-schemes-for-a-project).

Plan the tasks you intend to capture ahead of time and keep them short and focused. Launch your app and go to the state where you plan to begin the capture. Reduce unnecessary processing overhead on Apple Vision Pro by quitting other apps and avoiding background tasks.

To capture screenshots or video from a device, select your device from the capture dialog in Reality Composer Pro:

1. Launch Reality Composer Pro. Choose Open Developer Tool > Reality Composer Pro from the Xcode menu.
2. Choose File > Developer Capture to bring up the Developer Capture dialog.
3. Select the device to capture from the pop-up menu.

![A screenshot of the Developer Capture dialog that includes a camera button and a video button on the left to begin and end screenshot and video capture sessions, respectively; a pop-up menu to select devices on the right; and a status message below the pop-up menu that lists ready next to checkmark in a circle.](https://docs-assets.developer.apple.com/published/b492114b52f3506f230772e9fcc6176d/developer-capture-dialog%402x.png)

If you see the message “Preparing, wait for the device to be ready”. You can click the info button that appears to the right of the pop-up menu for more information.

##### Capture Screenshots

To begin capturing screenshots from Apple Vision Pro, click the button with the still camera icon in the capture dialog. The system begins your capture session:

![A screenshot of the Developer Capture dialog that includes a stop button on the left to end the capture session, a countdown button to capture a screenshot, an unavailable pop-up menu with your device selected. Below the pop-up menu, a message counting down the time remaining in the current capture session reads: 00:46 Remaining.](https://docs-assets.developer.apple.com/published/bb46eb086fc77d93fdd674dc0e0ca32b/developer-capture-time-remaining%402x.png)

To capture a screenshot immediately, without a countdown, press the spacebar. Click the countdown button to capture a screenshot after a 3 second countdown. Continue to keep relevant content centered and in frame for screenshots. The aspect ratio of screenshots crops content that appears at the sides of an experience.

The status area of the capture dialog displays the time remaining before the system ends the capture session. Click the stop button from your Mac to end the capture session yourself.

##### Capture Video

To begin capturing video from the device, click the video camera button in the Developer Capture dialog, which begins a short countdown. When that countdown reaches `0`, the capture session begins, replacing the countdown with a capture session timer. As the capture process happens, the video changes because the system reconfigures to render content for viewing in 2D. You might notice reduced responsiveness from the device during the session as it devotes more processing to render and capture the video.

While recording on the device, perform your planned interactions. Keep relevant content centered and in frame. The aspect ratio of the video you capture crops content that appears at the sides of an experience. Keep your head stable, and use slow, steady movement to transition the focus of the device when necessary. When viewing the video you capture in 2D, small head movements appear amplified and might be jarring to the audience.

The capture session ends when the capture session timer reaches `0`. You can click the record button again from your Mac to end the session sooner.

> **Note**: To begin a capture, the device must have a stable connection to your Mac and start at low power and thermal levels to stay below thresholds necessary to achieve consistent frame rates. When capturing multiple sessions, you might need to wait between each session.

##### Review the Captured Video File

Each recording session creates a QuickTime Movie file (`.mov`) and saves it to the desktop of your Mac. The file includes video captured at 30 FPS using 10-bit HEVC in HDTV Rec. 709 color space with system audio recorded in 32-bit floating-point linear PCM.

Review the video to make sure that it includes all the content you planned and it doesn’t include any unexpected elements. Ensure that the transitions and animations are smooth and frame rates are consistent.

Use additional video-editing tools to trim, edit, and apply post-processing, such as stabilization, to the video to create a high-quality preview.

## See Also

- [Reality Composer Pro](../RealityComposerPro/RealityComposerPro.md)
  Build, create, and design 3D content for your RealityKit apps.
- [Petite Asteroids: Building a volumetric visionOS game](petite-asteroids-building-a-volumetric-visionos-game.md)
  Use the latest RealityKit APIs to create a beautiful video game for visionOS.
- [BOT-anist](bot-anist.md)
  Build a multiplatform app that uses windows, volumes, and animations to create a robot botanist’s greenhouse.
- [Swift Splash](swift-splash.md)
  Use RealityKit to create an interactive ride in visionOS.
- [Diorama](diorama.md)
  Design scenes for your visionOS app using Reality Composer Pro.
- [Building an immersive media viewing experience](building-an-immersive-media-viewing-experience.md)
  Add a deeper level of immersion to media playback in your app with RealityKit and Reality Composer Pro.
- [Enabling video reflections in an immersive environment](enabling-video-reflections-in-an-immersive-environment.md)
  Create a more immersive experience by adding video reflections in a custom environment.
- [Combining 2D and 3D views in an immersive app](../RealityKit/combining-2d-and-3d-views-in-an-immersive-app.md)
  Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Understanding the modular architecture of RealityKit](understanding-the-realitykit-modular-architecture.md)
  Learn how everything fits together in RealityKit.
- [Using transforms to move, scale, and rotate entities](understanding-transforms.md)
  Learn how to use Transforms to move, scale, and rotate entities in RealityKit.
- [Implementing object tracking in your visionOS app](implementing-object-tracking-in-your-visionos-app.md)
  Create engaging interactions by training models to recognize and track real-world objects in your app.
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/capturing-screenshots-and-video-from-your-apple-vision-pro-for-2d-viewing)*