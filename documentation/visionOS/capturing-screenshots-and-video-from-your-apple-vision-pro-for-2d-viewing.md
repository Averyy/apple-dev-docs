# Capturing screenshots and video from Apple Vision Pro for 2D viewing

**Framework**: visionOS

Create screenshots and record high-quality video of your visionOS app and its surroundings for app previews.

#### Overview

Use screenshots and short videos of your visionOS app to showcase your user interface, highlight functionality, and demonstrate usage. Help people understand what to expect from an immersive experience by recording content from Apple Vision Pro that includes your app and its surroundings.

The system renders content with spatial effects and optimizations for viewing during immersive experiences. One optimization, *foveated rendering*, displays higher resolution where an enrolled person is looking, while reducing image resolution in their periphery. The system only applies foveated rendering for enrolled users who calibrate the device for their eyes and hands. Techniques that improve rendering performance during normal operation are intended to be unnoticeable for enrolled people wearing Apple Vision Pro; however, they don’t translate well to 2D displays.

To produce content for people to view on 2D displays, turn on high-quality recording in Settings on Apple Vision Pro. With high-quality recording turned on, the system reconfigures rendering during a recording so that Apple Vision Pro captures unfoveated content from a single eye and saves it to the Photos app. Because capturing this content is resource intensive, Apple Vision Pro limits each high-quality recording to three minutes.

> **Note**: For guidance on the screenshots and previews you include in your app’s product page, see [`Submit your apps to the App Store for Apple Vision Pro`](https://developer.apple.comhttps://developer.apple.com/visionos/submit/).

#### Prepare to Capture Your App and Its Surroundings

Select a well-lit location that’s free from clutter. Avoid including objects that might distract the audience or get in the way of your app’s windows and 3D content. Include enough detail in the scene to provide context and anchoring points.

> ❗ **Important**: Avoid material that you don’t have permission to capture, including people, screens, branded products, logos, artwork, and other intellectual property.

Use the version of your app that you intend to share with your audience. Build and install your app using a release configuration. This configuration enables code optimizations for better runtime performance and turns off debugging information. Debug configurations typically turn off code optimizations and might include interface elements you don’t intend to share. Don’t use them to record video for previews you intend to share. Build schemes manage the build configuration Xcode uses during build actions. For more information, see [`Customizing the build schemes for a project`](https://developer.apple.com/documentation/xcode/customizing-the-build-schemes-for-a-project).

Plan the tasks you intend to capture ahead of time and keep them short and focused. Launch your app and go to the state where you plan to begin the capture. Reduce unnecessary processing overhead on Apple Vision Pro by quitting other apps and avoiding background tasks.

#### Turn on High Quality Recording

Before you record your video, turn on high-quality recording in Settings on Apple Vision Pro:

1. Open Settings and tap General.
2. Tap Captures & Recordings, then choose High Quality.
3. Tap Turn On.

![A confirmation dialog titled High Quality Recording that explains the three-minute recording limit, with Turn On and Cancel buttons.](/images/com.apple.visionOS/high-quality-recording-turn-on@2x.png)

High-quality recording stays on until you turn it off in Settings. Because it reconfigures rendering, high-quality recording reduces render quality on Apple Vision Pro during a recording; what the recording captures may not exactly match what you see in your view. High-quality recording also excludes microphone audio and limits each session to three minutes.

![An alert with a warning icon titled Capture Finished, indicating that the view capture reached its time limit, above an OK button.](/images/com.apple.visionOS/capture-finished@2x.png)

#### Capture a Screenshot

To capture a screenshot of your view, do one of the following:

- Simultaneously press the Digital Crown and the top button.
- Say, “Siri, take a screenshot.”

Apple Vision Pro saves the screenshot to the Photos app. Keep relevant content centered and in-frame. The aspect ratio of screenshots crops content that appears at the sides of an experience.

#### Record Video in High Quality

After you turn on high-quality recording in Settings, open Control Center and tap Record My View. High Quality appears below Record My View to indicate that the recording is captured in high quality. To stop recording, open Control Center and tap Record My View again.

![Control Center with Record My View highlighted in red and labeled High Quality, above Mac Virtual Display, Mirror My View, and Guest User options.](/images/com.apple.visionOS/record-my-view-high-quality@2x.png)

As the recording begins, the view on Apple Vision Pro changes because the system reconfigures rendering to capture content for viewing in 2D. You might notice reduced responsiveness from the device during the session as it devotes more processing to render and capture the video.

While recording, perform your planned interactions. Keep relevant content centered and in frame. The aspect ratio crops content that appears at the sides of an experience. Keep your head stable, and use slow, steady movement to transition the focus of the device when necessary. When viewing the video you capture in 2D, small head movements appear amplified and might be jarring to the audience.

> **Note**: To begin a capture, the device must start at low power and thermal levels to stay below thresholds necessary to achieve consistent frame rates. When capturing multiple sessions, you might need to wait between each session.

![An alert with a warning icon titled Capture Unavailable, indicating the device can't start a view capture and to try again after a few minutes, above an OK button.](/images/com.apple.visionOS/capture-unavailable@2x.png)

#### Review the Recorded Video

Apple Vision Pro saves each recording to the Photos app. Review the video to make sure that it includes all the content you planned and it doesn’t include any unexpected elements. Ensure that the transitions and animations are smooth and frame rates are consistent.

Transfer the video from Apple Vision Pro to your Mac or another device for editing. Use video-editing tools to trim, edit, and apply post-processing, such as stabilization, to the video to create a high-quality preview.

## See Also

- [Reality Composer Pro](../realitycomposerpro/realitycomposerpro.md)
  Build, design, and orchestrate 3D content for your RealityKit apps.
- [Chaparral Village: Building an immersive visionOS adventure game](chaparral-village-building-an-immersive-visionos-adventure-game.md)
  Create an adventure game using SwiftUI, RealityKit, and Reality Composer Pro 3.
- [Designing no-code games with Reality Composer Pro 3](designing-no-code-games-in-reality-composer-pro-3.md)
  Build a video game in Reality Composer Pro without code using Script Graphs.
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
- [Combining 2D and 3D views in an immersive app](../realitykit/combining-2d-and-3d-views-in-an-immersive-app.md)
  Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Understanding the modular architecture of RealityKit](understanding-the-realitykit-modular-architecture.md)
  Learn how everything fits together in RealityKit.
- [Using transforms to move, scale, and rotate entities](understanding-transforms.md)
  Learn how to use Transforms to move, scale, and rotate entities in RealityKit.
- [Implementing object tracking in your app](implementing-object-tracking-in-your-app.md)
  Create engaging interactions by training models to recognize and track real-world objects in people’s surroundings.
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.
- [Manipulating entities with solid collisions](manipulating-entities-with-solid-collisions.md)
  Extend the capabilities of your app by using entities, components, and systems to maintain solid collisions when manipulating entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/capturing-screenshots-and-video-from-your-apple-vision-pro-for-2d-viewing)*