# Implementing object tracking in your visionOS app

**Framework**: Visionos

Create engaging interactions by training models to recognize and track real-world objects in your app.

#### Overview

When you implement object tracking in your visionOS app, you can seamlessly integrate real-world objects in people’s surroundings to enhance their immersive experiences. By tracking the 3D position and orientation of an object, or several objects, your app can augment them with virtual content.

You can use object tracking to provide virtual interactions with objects in a person’s surroundings, such as:

- Guiding someone through using an item’s features, reading about its history, or learning about its behaviors when they look at it in their surroundings.
- Helping people troubleshoot issues with household items and appliances with a virtual manual.
- Creating an immersive storytelling experience to make collectables and toys come to life.

To integrate object tracking into your app, you start with a 3D model of a physical object, train a machine learning model in Create ML with that 3D model asset to obtain a reference object file, and then use the resulting reference object file to track the physical object in your app. The reference object file is a file format with a `.referenceobject` extension, specifically for object tracking in visionOS.

![A flow diagram of four items with arrows between them. From left to right, the images are an illustration of a globe; the Create ML app icon; a grouping of the RealityKit icon, the ARKit icon, and the Reality Composer Pro icon; and an illustration of a globe within a bounding box.](https://docs-assets.developer.apple.com/published/a4b7b3b4369717a62951659789519c9a/workflow-objects-PageImage-card%402x.png)

Implementing object tracking requires an Apple Vision Pro with visionOS 2 or later, and a Mac with Apple silicon and macOS 15 or later for the machine learning training in Create ML.

##### Ensure Your Objects Are Suitable for Object Tracking

Object tracking performs optimally for a specific set of object characteristics. For object tracking to work best in your app, make sure your object is rigid, nonsymmetrical, and stationary.

##### Obtain a 3d Model of Your Object

You use [`Create ML`](https://developer.apple.comhttps://developer.apple.com/machine-learning/create-ml/) to begin the machine learning training to obtain your reference object file. Create ML requires a 3D model asset in the USDZ file format that represents your real-world object. You can obtain your 3D model using computer-aided design (CAD) software to accurately model an object’s geometry and apply physically based rendering (PBR) materials to it, and save it in the USDZ file format. Using this method, the 3D model can realistically represent objects that consist of multiple parts made from different materials, like glass, metal, plastic, wood, and other common materials. This method is helpful for capturing objects that are entirely or partly transparent, shiny, or reflective. The better the 3D model represents the appearance of the physical object, the better the quality of tracking is in visionOS.

Another way to create your 3D model is by using the Object Capture feature in the Reality Composer app in iOS or iPadOS. You can use your iPhone or iPad to capture images of an object, and then save the USDZ file to import into your app. For more information about using the Object Capture feature to create a 3D model, see [`Meet Object Capture for iOS`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10191/) and [`Scanning objects using Object Capture`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/scanning-objects-using-object-capture).

Before beginning the training process in Create ML with the 3D model asset, keep the following guidelines in mind to ensure it works well for object tracking in visionOS:

- Ensure the 3D model is as photorealistic as possible — essentially a digital twin of your real-world object.
- Ensure the scale of the 3D model is as precise as possible and matches its specified units. If the scale doesn’t match the real-world object, the augmentation appears offset in the viewing direction, and may appear either in front of or behind the object.

> **Note**: While training the machine learning model with the 3D model asset, Create ML ignores any animations, virtual cameras, and lights within the asset, treating them as static.

##### Train a Machine Learning Model with the 3d Model Asset in Create Ml

Object tracking requires a reference object file to track the spatial location and orientation of the corresponding real-world object. You use Create ML to train a machine learning model to create a reference object file unique to your object. The training of machine learning models with your 3D asset and the creation of the reference object file both run locally on your Mac.

To set up the training:

1. Open Xcode and choose Xcode > Open Developer Tool > Create ML.
2. In the dialog that appears, click New Document.
3. In the Choose a Template dialog, select the Spatial category in the left pane, select the Object Tracking template, and click Next.
4. Enter your project name and other information, and click Next.
5. Select a location for your project, and click Create.
6. Create ML opens a training configuration view with an empty 3D viewport. Drag the USDZ file of your 3D model asset into the 3D viewport.

The 3D viewport is an interactive space where you can view your 3D model asset from different angles. After it appears in the viewport, check the appearance of the 3D model asset and confirm that it matches the absolute dimensions of your real-world object. Also make sure that the dimensions of the 3D model asset at the bottom right of the viewport match the actual dimensions of your object. If the scale doesn’t match, one option is to use Reality Composer Pro to rescale the 3D model and then add the adjusted USDZ file to Create ML.

![A Create ML screenshot of a gramophone in the 3D viewport with the Object dimensions displaying at the bottom right.](https://docs-assets.developer.apple.com/published/bfa621939020275a8247a497be68d089/importing%402x.png)

The next step is to select the best viewing angle for your real-world object. Consider how people view and interact with the object in your app, and decide which angle you need for tracking it. The “Viewing angles” setting appears below the 3D viewport, and has three viewing angles you can use: All Angles, Upright, or Front. It’s important to choose the best option for your object.

![A Create ML screenshot of the 3D viewport showing the Viewing angles options. The Upright option is highlighted.](https://docs-assets.developer.apple.com/published/b6654e7973970fc2be9f1eb10b7bba60/viewing-angles%402x.png)

The All Angles option includes views from every angle. It works best for tracking objects that have a distinct and unique appearance from all sides, such as a patterned Christmas ornament that people see from all sides as it hangs on a tree.

The Upright option works only for tracking objects that stand upright on a surface, such as a microscope that sits on a counter and stays in the same position as people interact with it. This option disables tracking from the bottom viewing angle.

The Front option works only for tracking objects that stand upright on a surface where the back of the object isn’t visible, such as a coffee machine that sits on a counter while people operate it from the front. This option disables tracking from both the bottom and rear viewing angles.

> **Note**: Only choose the All Angles option if you want to track your object from all sides. The more restricted the viewing angle is, the more accurate the object tracking is in visionOS.

If there’s an object in a person’s surroundings that’s similar to the object you want to track, the object-tracking feature might recognize it and track it instead of your object. To prevent this from happening, add the similar object as a negative example when training the machine learning model with your reference object. Below the 3D viewport, choose More Options > Objects to avoid. Use this section to add USDZ samples of similar items to ensure the machine learning model doesn’t identify them as the object you want to track.

![A Create ML screenshot of the Objects to avoid settings.](https://docs-assets.developer.apple.com/published/62838b26be7ec80c5b25afecfd418ed9/objects-to-avoid%402x.png)

Create ML supports training multiple machine learning models in the same object-tracking project. In the Model Sources section in the left pane, you can click the Add button (+) to add more 3D model assets to your Create ML project. Use this feature to track multiple objects in your app at the same time.

![A Create ML screenshot of the Model Sources section in the left pane.](https://docs-assets.developer.apple.com/published/1d2865d8a7c83978f5bac7dd6ff8a1b1/adding-objects%403x.png)

> **Note**: You can track up to 10 different reference objects simultaneously without an impact to performance.

After inspecting your 3D model asset and configuring the training settings, click Train to begin the training process. A progress bar indicates the amount of time until the machine learning training is complete. The machine learning training can take a few hours, depending on the configuration of your Mac. A more advanced processor and additional RAM significantly improve the training time.

##### Export the Reference Object File

When training is complete, Create ML provides the reference object file for you to use in your app. Click the Output tab and save the resulting reference object file.

The reference object file contains the machine learning model you trained, packaged with the 3D model asset, in the USDZ file format. You can use the USDZ file for visualizing the tracking quality by rendering it as an overlay on the real-world object, and as a guide for adding immersive effects. The USDZ file may take up a lot of space in your app if your 3D model asset is large, so you can remove it from the reference object file if you need to optimize space.

You use the Reference Object Compiler in Xcode to remove the USDZ data from the reference object file during the build process. Select your project in Xcode, click the Build Settings tab, and enable the Strip USDZ Files from Reference Object option. This setting contains the `REFERENCEOBJECT_STRIP_USDZ` build flag. The default setting of the flag is `No`, so Xcode copies any reference object files you add to the project as-is unless you change the setting.

![An Xcode screenshot of the Build Settings pane showing the Remove USDZ files from Reference Object option enabled.](https://docs-assets.developer.apple.com/published/0d75053c5b7292d5a5af7e7d9e926235/stripping-usd%402x.png)

##### Integrate the Reference Object File Into Your App

After you generate the reference object file, you can set up object tracking in your app using Reality Composer Pro, RealityKit, or ARKit. For more information about each of these methods, see [`Using a reference object with Reality Composer Pro`](using-a-reference-object-with-reality-composer-pro.md), [`Using a reference object with RealityKit`](using-a-reference-object-with-realitykit.md), and [`Using a reference object with ARKit`](using-a-reference-object-with-arkit.md).

> **Note**: Object tracking works only in an [`ImmersiveSpace`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/immersivespace) within Xcode. Attempting to use object tracking in a window or volume results in a silent failure.

For more information about object tracking, see [`Explore object tracking for visionOS`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10101/). For an example of using ARKit for object tracking, see [`Exploring object tracking with ARKit`](https://developer.apple.comhttps://developer.apple.com/documentation/visionos/exploring_object_tracking_with_arkit).

## Topics

### Object tracking within an app
- [Using a reference object with Reality Composer Pro](using-a-reference-object-with-reality-composer-pro.md)
  Import a reference object file to track a real-world object in your visionOS app.
- [Using a reference object with RealityKit](using-a-reference-object-with-realitykit.md)
  Import a reference object file to track a real-world object in your visionOS app.
- [Using a reference object with ARKit](using-a-reference-object-with-arkit.md)
  Import a reference object file and track a real-world object in your visionOS app.

## See Also

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
- [Designing RealityKit content with Reality Composer Pro](designing-realitykit-content-with-reality-composer-pro.md)
  Design RealityKit scenes for your visionOS app.
- [Capturing screenshots and video from Apple Vision Pro for 2D viewing](capturing-screenshots-and-video-from-your-apple-vision-pro-for-2d-viewing.md)
  Create screenshots and record high-quality video of your visionOS app and its surroundings for app previews.
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionOS/implementing-object-tracking-in-your-visionos-app)*