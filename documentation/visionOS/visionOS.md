# visionOS

**Framework**: visionOS

Create a new universe of apps and games for Apple Vision Pro.

**Availability**:
- visionOS 1.0+

#### Overview

visionOS is the operating system that powers Apple Vision Pro. Use visionOS together with familiar tools and technologies to build immersive apps and games for spatial computing.

![Three scenes from visionOS apps that show the Music app, a close-up of the tools associated with a window, and a photo browser.](https://docs-assets.developer.apple.com/published/230b02516973a1e9ed5e1ce8f8e62ccc/overview%402x.png)

Developing for visionOS requires a Mac with Apple silicon. Create new apps using SwiftUI to take full advantage of the spectrum of immersion available in visionOS. If you have an existing iPad or iPhone app, add the visionOS destination to your app’s target to gain access to the standard system appearance, and add platform-specific features to create a compelling experience. To provide continuous access to your content in the meantime, deliver a compatible version of your app that runs in visionOS.

##### Expand Your App Into Immersive Spaces

##### Explore New Kinds of Interaction

People can select an element by looking at it and tapping their fingers together. They can also pinch, drag, zoom, and rotate objects using specific hand gestures. [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) provides built-in support for these standard gestures, so rely on them for most of your app’s input. When you want to go beyond the standard gestures, use [`ARKit`](https://developer.apple.com/documentation/ARKit) to create custom gestures.

##### Dive Into Featured Sample Apps

Explore the core concepts for all visionOS apps with Hello World. Understand how to detect custom gestures using ARKit with Happy Beam. Discover streaming 2D and stereoscopic media with Destination Video. And learn how to build 3D scenes with RealityKit and Reality Composer Pro with Diorama and Swift Splash.

## Topics

### App construction
- [Creating your first visionOS app](creating-your-first-visionos-app.md)
  Build a new visionOS app using SwiftUI and add platform-specific features.
- [Adding 3D content to your app](adding-3d-content-to-your-app.md)
  Add depth and dimension to your visionOS app and discover how to incorporate your app’s content into a person’s surroundings.
- [Creating fully immersive experiences in your app](creating-fully-immersive-experiences.md)
  Build fully immersive experiences by combining spaces with content you create using RealityKit or Metal.
- [Drawing sharp layer-based content in visionOS](drawing-sharp-layer-based-content.md)
  Deliver text and vector images at multiple resolutions from custom Core Animation layers in visionOS.
- [Introductory visionOS samples](introductory-visionos-samples.md)
  Learn the fundamentals of building apps for visionOS with beginner-friendly sample code projects.
- [Combining spatial support from multiple frameworks](combining-spatial-support-from-multiple-frameworks.md)
  Integrate the features of an array of frameworks seamlessly to enhance your spatial app.
- [Connecting iPadOS and visionOS apps over the local network](connecting-ipados-and-visionos-apps-over-the-local-network.md)
  Build an iPadOS companion app to control your visionOS app.
### Design
- [Designing for visionOS](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-visionos)
  When people wear Apple Vision Pro, they enter an infinite 3D space where they can engage with your app or game while staying connected to their surroundings.
- [Adopting best practices for privacy and user preferences](adopting-best-practices-for-privacy.md)
  Minimize your use of sensitive information and provide a clear statement of what information you do use and how you use it.
- [Improving accessibility support in your visionOS app](improving-accessibility-support-in-your-app.md)
  Update your code to ensure everyone can access your app’s content in visionOS.
### SwiftUI
- [Canyon Crosser: Building a volumetric hike-planning app](canyon-crosser-building-a-volumetric-hike-planning-app.md)
  Create a hike planning app using SwiftUI and RealityKit.
- [Hello World](world.md)
  Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Presenting windows and spaces](presenting-windows-and-spaces.md)
  Open and close the scenes that make up your app’s interface.
- [Positioning and sizing windows](positioning-and-sizing-windows.md)
  Influence the initial geometry of windows that your app presents.
- [Adopting best practices for persistent UI](adopting-best-practices-for-scene-restoration.md)
  Create persistent and contextually relevant spatial experiences by managing scene restoration, customizing window behaviors, and surface snapping data.
### RealityKit and Reality Composer Pro
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
- [Capturing screenshots and video from Apple Vision Pro for 2D viewing](capturing-screenshots-and-video-from-your-apple-vision-pro-for-2d-viewing.md)
  Create screenshots and record high-quality video of your visionOS app and its surroundings for app previews.
- [Implementing object tracking in your visionOS app](implementing-object-tracking-in-your-visionos-app.md)
  Create engaging interactions by training models to recognize and track real-world objects in your app.
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.
### ARKit
- [Happy Beam](happybeam.md)
  Leverage a Full Space to create a fun game using ARKit.
- [Setting up access to ARKit data](setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [Incorporating real-world surroundings in an immersive experience](incorporating-real-world-surroundings-in-an-immersive-experience.md)
  Create an immersive experience by making your app’s content respond to the local shape of the world.
- [Placing content on detected planes](placing-content-on-detected-planes.md)
  Detect horizontal surfaces like tables and floors, as well as vertical planes like walls and doors.
- [Tracking specific points in world space](tracking-points-in-world-space.md)
  Retrieve the position and orientation of anchors your app stores in ARKit.
- [Tracking preregistered images in 3D space](tracking-images-in-3d-space.md)
  Place content based on the current position of a known image in a person’s surroundings.
- [Exploring object tracking with ARKit](exploring_object_tracking_with_arkit.md)
  Find and track real-world objects in visionOS using reference objects trained with Create ML.
- [Object tracking with Reality Composer Pro experiences](object-tracking-with-reality-composer-pro-experiences.md)
  Use object tracking in visionOS to attach digital content to real objects to create engaging experiences.
- [Building local experiences with room tracking](building-local-experiences-with-room-tracking.md)
  Use room tracking in visionOS to provide custom interactions with physical spaces.
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.
- [Drawing in the air and on surfaces with a spatial stylus](drawing-in-the-air-and-on-surfaces-with-a-spatial-stylus.md)
  Create a spatial stylus drawing experience that balances latency and accuracy for both in-air and on-surface drawing.
### SharePlay
- [Building a guessing game for visionOS](../GroupActivities/building-a-guessing-game-for-visionos.md)
  Create a team-based guessing game for visionOS using Group Activities.
- [Configure your visionOS app for sharing with people nearby](../GroupActivities/configure-your-app-for-sharing-with-people-nearby.md)
  Create shared experiences for people wearing Vision Pro in the same room and those on FaceTime.
- [Adding spatial Persona support to an activity](../GroupActivities/adding-spatial-persona-support-to-an-activity.md)
  Update your SharePlay activities to support spatial Personas and the shared context when running in visionOS.
- [Synchronizing group gameplay with TabletopKit](../TabletopKit/synchronizing-group-gameplay-with-tabletopkit.md)
  Maintain game state across multiple players in a race to capture all the coins.
### Video playback
- [Destination Video](destination-video.md)
  Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Displaying video from connected devices](displaying-video-from-connected-devices.md)
  Show video from devices connected with the Developer Strap in your visionOS app.
- [Playing immersive media with RealityKit](playing-immersive-media-with-realitykit.md)
  Create an immersive video playback experience with RealityKit.
- [Rendering stereoscopic video with RealityKit](../RealityKit/rendering-stereoscopic-video-with-realitykit.md)
  Render stereoscopic video in visionOS with RealityKit.
- [Creating a multiview video playback experience in visionOS](../AVKit/creating-a-multiview-video-playback-experience-in-visionos.md)
  Build an interface that plays multiple videos simultaneously and handles transitions to different experience types gracefully.
- [Configuring your app for media playback](../AVFoundation/configuring-your-app-for-media-playback.md)
  Configure apps to enable standard media playback behavior.
- [Adopting the system player interface in visionOS](../AVKit/adopting-the-system-player-interface-in-visionos.md)
  Provide an optimized viewing experience for watching 3D video content.
- [Controlling the transport behavior of a player](../AVFoundation/controlling-the-transport-behavior-of-a-player.md)
  Play, pause, and seek through a media presentation.
- [Monitoring playback progress in your app](../AVFoundation/monitoring-playback-progress-in-your-app.md)
  Observe the playback of a media asset to update your app’s user-interface state.
- [Trimming and exporting media in visionOS](../AVKit/trimming-and-exporting-media-in-visionos.md)
  Display standard controls in your app to edit the timeline of the currently playing media.
### Xcode and Simulator
- [Configuring your app icon using an asset catalog](../Xcode/configuring-your-app-icon.md)
  Add app icon variations to an asset catalog that represents your app in places such as the App Store, the Home Screen, Settings, and search results.
- [Diagnosing and resolving bugs in your running app](../Xcode/diagnosing-and-resolving-bugs-in-your-running-app.md)
  Inspect your app to isolate bugs, locate crashes, identify excess system-resource usage, visualize memory bugs, and investigate problems in its appearance.
- [Diagnosing issues in the appearance of a running app](../Xcode/diagnosing-issues-in-the-appearance-of-your-running-app.md)
  Inspect your running app to investigate issues in the appearance and placement of the content it displays.
- [Running your app in Simulator or on a device](../Xcode/running-your-app-in-simulator-or-on-a-device.md)
  Launch your app in a simulated iOS, iPadOS, tvOS, visionOS, or watchOS device, or on a device connected to a Mac.
- [Interacting with your app in the visionOS simulator](../Xcode/interacting-with-your-app-in-the-visionos-simulator.md)
  Use your Mac to navigate spaces and control interactions with your visionOS apps in Simulator.
### Performance
- [Creating a performance plan for your visionOS app](creating-a-performance-plan-for-visionos-app.md)
  Identify your app’s performance and power goals and create a plan to measure and assess them.
- [Analyzing the performance of your visionOS app](analyzing-the-performance-of-your-visionos-app.md)
  Use the RealityKit Trace template in Instruments to evaluate and improve the performance of your visionOS app.
- [Reducing the rendering cost of your UI on visionOS](reducing-the-rendering-cost-of-your-ui-on-visionos.md)
  Optimize your 2D user interface rendering on visionOS.
- [Reducing the rendering cost of RealityKit content on visionOS](reducing-the-rendering-cost-of-realitykit-content-on-visionos.md)
  Optimize your app’s 3D augmented reality content to render efficiently on visionOS.
- [Understanding the visionOS render pipeline](understanding-the-visionos-render-pipeline.md)
  Compare how visionOS handles events and manages its rendering loop differently from other Apple platforms.
### iOS migration and compatibility
- [Determining whether to bring your app to visionOS](determining-whether-to-bring-your-app-to-visionos.md)
  Decide whether to bring your existing iPadOS or iOS app to visionOS.
- [Bringing your existing apps to visionOS](bringing-your-app-to-visionos.md)
  Build a version of your iPadOS or iOS app using the visionOS SDK, and update your code for platform differences.
- [Bringing your ARKit app to visionOS](bringing-your-arkit-app-to-visionos.md)
  Update an iPadOS or iOS app that uses ARKit, and provide an equivalent experience in visionOS.
- [Making your existing app compatible with visionOS](making-your-app-compatible-with-visionos.md)
  Modify your iPadOS or iOS app to run successfully in visionOS as a compatible app.
### Enterprise APIs for visionOS
- [Accessing the main camera](accessing-the-main-camera.md)
  Add camera-based features to enterprise apps.
- [Building spatial experiences for business apps with enterprise APIs for visionOS](building-spatial-experiences-for-business-apps-with-enterprise-apis.md)
  Grant enhanced sensor access and increased platform control to your visionOS app by using entitlements.
- [Locating and decoding barcodes in 3D space](locating-and-decoding-barcodes-in-3d-space.md)
  Create engaging, hands-free experiences based on barcodes in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionOS)*