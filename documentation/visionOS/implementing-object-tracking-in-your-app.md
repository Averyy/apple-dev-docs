# Implementing object tracking in your app

**Framework**: visionOS

Create engaging interactions by training models to recognize and track real-world objects in people’s surroundings.

#### Overview

When implementing object tracking in your iOS or visionOS app, you can seamlessly integrate real-world objects in people’s surroundings to enhance their immersive experiences. By tracking the 3D position and orientation of an object, or several objects, your app can augment the objects with virtual content and measure the relative spatial distance between them.

Use object tracking to provide virtual interactions with objects in a person’s surroundings, such as:

- Verifying that a tool is held and positioned correctly during an assembly process.
- Guiding someone through using an item’s features, reading about its history, or learning about its behaviors when they look at it in their surroundings.
- Helping people troubleshoot issues with household items and appliances with a virtual manual.
- Creating an immersive storytelling experience to make collectables and toys come to life.

To add object tracking to your app, start with a physical object’s 3D model, train a machine learning model in Create ML with that 3D model to obtain a reference object file, then use the resulting reference object file to track the physical object. The reference object file has a `.referenceobject` file extension, specifically for object tracking in iOS or visionOS.

![A flow diagram of four items with arrows between them. From left to right, the images are an illustration of a globe; the Create ML app icon; a grouping of the RealityKit icon, the ARKit icon, and the Reality Composer Pro icon; and an illustration of a globe within a bounding box.](https://docs-assets.developer.apple.com/published/c744bc815682f39888c01eadb57ca074/workflow%402x.png)

Implementing object tracking requires either an iPhone with iOS 27 or later, or an Apple Vision Pro with visionOS 2 or later. The machine learning training in Create ML requires a Mac with Apple silicon and macOS 15 or later. Reference object files trained with macOS 27 and Xcode 27 or later require iOS 27 or visionOS 27 and later.

#### Ensure Your Objects Are Suitable for Object Tracking

For object tracking to work best in your app, make sure your object is *rigid*. A rigid object maintains its shape and appearance during tracking. For example, a pair of scissors is challenging to track because it changes shape while a person uses it.

By default, object tracking delivers pose updates at a lower frequency and consumes less power. This works well for stationary objects, or cases where virtual content doesn’t need to match the object’s exact position on every frame.

For moving or handheld objects, like surgical instruments or power tools, set [`highFrameRateTrackingEnabled`](https://developer.apple.com/documentation/ARKit/ReferenceObject/Configuration/highFrameRateTrackingEnabled) when you create the object tracking session in visionOS, or assign the object to [`trackingObjects`](https://developer.apple.com/documentation/ARKit/ARWorldTrackingConfiguration/trackingObjects) in iOS. This gives you a precise pose update on every frame. For best results, train your reference object in extended mode. For more information, see [`Train a machine learning model with the 3D model asset in Create ML`](https://developer.apple.com#Train-a-machine-learning-model-with-the-3D-model-asset-in-Create-ML) later in this article.

#### Obtain a 3d Model of Your Object

You use [`Create ML`](https://developer.apple.comhttps://developer.apple.com/machine-learning/create-ml/) to begin the machine learning training to obtain your reference object file. Create ML requires a 3D model asset in the USDZ file format that represents your real-world object. You can obtain your 3D model using computer-aided design (CAD) software to accurately model an object’s geometry and apply physically based rendering (PBR) materials to it, and save it in the USDZ file format. Using this method, the 3D model can realistically represent objects that consist of multiple parts made from different materials, like glass, metal, plastic, wood, and other common materials. This method is helpful for capturing objects that are entirely or partly transparent, shiny, or reflective. The better the 3D model represents the appearance of the physical object, the better the quality of tracking is in visionOS.

Another way to create your 3D model is by using the Object Capture feature in the Reality Composer app in iOS or iPadOS. You can use your iPhone or iPad to capture images of an object, and then save the USDZ file to import into your app. For more information about using the Object Capture feature to create a 3D model, see [`Meet Object Capture for iOS`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10191/) and [`Scanning objects using Object Capture`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/scanning-objects-using-object-capture).

Before beginning the training process in Create ML with the 3D model asset, keep the following guidelines in mind to ensure it works well for object tracking in visionOS:

- Ensure the 3D model is as photorealistic as possible — essentially a digital twin of your real-world object.
- Ensure the scale of the 3D model is as precise as possible and matches its specified units. If the scale doesn’t match the real-world object, the augmentation appears offset in the viewing direction, and may appear either in front of or behind the object.

> **Note**: While training the machine learning model with the 3D model asset, Create ML ignores any animations, virtual cameras, and lights within the asset, treating them as static.

#### Train a Machine Learning Model with the 3d Model Asset in Create Ml

Object tracking requires a reference object file to track the spatial location and orientation of the corresponding real-world object. You use Create ML to train a machine learning model to create a reference object file unique to your object. The training of machine learning models with your 3D asset and the creation of the reference object file both run locally on your Mac. You can either train a model with the Create ML developer tool that comes with Xcode, or with the Create ML command-line tool.

The following are the steps to train a model in the Create ML app:

1. Open Xcode and choose Xcode > Open Developer Tool > Create ML.
2. Create a new project or open an existing project.
3. In the Choose a Template dialog, select Object Tracking template, which is in the Spatial category, and click Next.
4. Give your project a name.
5. Optionally, add a description or license to the model.
6. Click Next.
7. Choose where to save your project and click Create.
8. Create ML opens a training configuration view with an empty 3D viewport. Drag the USDZ file of your 3D model asset into the 3D viewport.

The 3D viewport is an interactive space where you can view your 3D model asset from different angles. After it appears in the viewport, check the appearance of the 3D model asset and confirm that it matches the absolute dimensions of your real-world object. Also make sure that the dimensions of the 3D model asset at the bottom right of the viewport match the actual dimensions of your object. If the scale doesn’t match, one option is to use Reality Composer Pro to rescale the 3D model and then add the adjusted USDZ file to Create ML.

![A Create ML screenshot of a flashlight in the 3D viewport with the Object dimensions displaying at the bottom right.](https://docs-assets.developer.apple.com/published/f925e803014948a94eea6712d2ce657e/importing%402x.png)

The next step is to select the best viewing angle for your real-world object. Consider how people view and interact with the object in your app, and decide which angle you need for tracking it. The “Viewing angles” setting appears below the 3D viewport, and has three viewing angles you can use: All Angles, Upright, or Front.

![A Create ML screenshot of the 3D viewport showing the Viewing angles options. The All Angles option is highlighted.](https://docs-assets.developer.apple.com/published/a8476105ea8d8bd34d68b077fc313ea6/viewing-angles%402x.png)

- **All Angles**: Includes views from every angle. It works best for tracking handheld objects that people move in different orientations, such as a power drill that a person holds while securing an object.
- **Upright**: Tracks objects that stand upright on a surface, such as a microscope that sits on a counter and stays in the same position as people interact with it. This option disables tracking from the bottom viewing angle.
- **Front**: Tracks objects that stand upright on a surface where the back of the object isn’t visible, such as a coffee machine that sits on a counter while people operate it from the front. This option disables tracking from both the bottom and rear viewing angles.

> **Note**: Only choose the All Angles option if you want to track your object from all sides. Tracking is more accurate for objects trained with restricted viewing angles.

After selecting a viewing angle, choose a training mode. Create ML offers two training modes, *standard* and *extended*:

- **Standard**: The default mode that works well for most use cases.
- **Extended**: Uses more training data and a larger model, producing the highest tracking quality. Takes several times longer to train than standard mode.

> **Note**: If you plan to track the object using high frame rate tracking, training with extended mode is recommended.

![A Create ML screenshot of the training mode picker with the Extended mode option selected.](https://docs-assets.developer.apple.com/published/ee1e09e4265b21ccbe70d1f9c486f3a8/training-model-selection%402x.png)

If there’s an object in a person’s surroundings that’s similar to the object you want to track, the object-tracking feature might recognize and track it instead of your object. To prevent this from happening, add the similar object as a negative example when training the machine learning model with your reference object. Below the 3D viewport, choose More Options > Objects to avoid. Use this section to add USDZ samples of similar items to ensure the machine learning model doesn’t identify them as the object you want to track.

![A Create ML screenshot of the Objects to avoid settings.](https://docs-assets.developer.apple.com/published/2a78bf93fca8c3385c5b29f9787e39bf/objects-to-avoid%402x.png)

Create ML supports training multiple machine learning models in the same object-tracking project. In the Model Sources section in the left pane, you can click the Add button (+) to add more 3D model assets to your Create ML project. Use this feature to track multiple objects in your app at the same time.

![A Create ML screenshot of the Model Sources section in the left pane.](https://docs-assets.developer.apple.com/published/722d2bf2eb337f46f15da3aeffc87b60/adding-objects%403x.png)

After inspecting your 3D model asset and configuring the training settings, click Train to begin the training process. A progress bar indicates the amount of time until the machine learning training is complete. The machine learning training can take a few hours, depending on the configuration of your Mac. A more advanced processor and additional RAM significantly improve the training time.

##### Train Your Assets with the Create Ml Command Line Tool

Starting with Xcode 26, which requires macOS 15.4 or later, you can train a machine learning model with your 3D asset by running the Create ML developer tool from a command line prompt. With an asset in the USDZ file format, you can use the tool to train the asset and get a reference object file to use for object tracking.

The Create ML command-line tool automates object tracking tasks in your workflow, like using your scripts and cloud-based parallel setups to run the training process. You can also use the tool when you need to automate training a large number of objects while you continue to work on other tasks.

You need to have Xcode command-line tools installed before using the Create ML tool, which you can check by running the following command:

```shell
% xcode-select -p
```

> **Note**: You can use the Create ML command line tool if the command’s output refers to a `Contents/Developer` directory in Xcode or to the `/Library/Developer/CommandLineTools` directory. If the command returns an error that indicates that Xcode or the command-line tools can’t find the directory, install the command-line tools package by running the `xcode-select --install` command.

Begin the training process by invoking the Create ML command-line tool with the `xcrun` command. You need to modify the example below to provide the locations on your system for the commands inputs and outputs.

```shell
% xcrun createml objecttracker -s source.usdz -o tracker.referenceobject
```

The system uses the `xcrun` prefix to locate the path of the training tool in the Xcode command-line tools. The `-s` option points to the source path for the 3D asset of the physical object you want to train, and the `-o` option points to the output path to store the final trained reference object file. Before running this command, update it to include the name of the source and output of your object. By default, the tool trains the asset in standard mode.

To use extended training mode, pass the `-m` option with the mode specified as `extended`:

```shell
% xcrun createml objecttracker -s source.usdz -o tracker.referenceobject -m extended --all-angles
```

For more information on training modes, see [`Train a machine learning model with the 3D model asset in Create ML`](https://developer.apple.com#Train-a-machine-learning-model-with-the-3D-model-asset-in-Create-ML) earlier in this article.

After you run the tool, it starts training your object. Use the help option (`-h`) for more information on training and topics like viewing angles, objects to avoid, and redirection to alternative pipes:

```shell
% xcrun createml objecttracker -h
```

#### Export the Reference Object File

When training is complete, Create ML provides the reference object file for you to use in your app. Click the Output tab and save the resulting reference object file.

The reference object file contains the machine learning model you trained, packaged with the 3D model asset, in the USDZ file format. You can use the USDZ file for visualizing the tracking quality by rendering it as an overlay on the real-world object, and as a guide for adding immersive effects. The USDZ file may take up a lot of space in your app if your 3D model asset is large, so you can remove it from the reference object file if you need to optimize space.

Use the Reference Object Compiler in Xcode to remove the USDZ data from the reference object file during the build process. Select your project in Xcode, click the Build Settings tab, and enable the Strip USDZ Files from Reference Object option. This setting contains the `REFERENCEOBJECT_STRIP_USDZ` build option. The default setting of the option is `No`, so Xcode copies any reference object files you add to the project as-is unless you change the setting.

![An Xcode screenshot of the Build Settings pane showing the Remove USDZ files from Reference Object option enabled.](https://docs-assets.developer.apple.com/published/0d75053c5b7292d5a5af7e7d9e926235/stripping-usd%402x.png)

#### Integrate the Reference Object File Into Your App

After generating the reference object file, set up object tracking in your app using Reality Composer Pro, RealityKit, or ARKit. For more information about each of these methods, see [`Using a reference object with Reality Composer Pro`](using-a-reference-object-with-reality-composer-pro.md), [`Using a reference object with RealityKit`](using-a-reference-object-with-realitykit.md), [`Using a reference object with ARKit in visionOS`](using-a-reference-object-with-arkit-in-visionos.md), and [`Using a reference object with ARKit in iOS`](using-a-reference-object-with-arkit-in-ios.md).

> ❗ **Important**: In a visionOS app, object tracking works only in an [`ImmersiveSpace`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/immersivespace). Attempting to use object tracking in a window or volume results in a silent failure.

For more information about object tracking, watch the WWDC24 session, [`Explore object tracking for visionOS`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10101/), and the WWDC26 session, [`Explore enhancements to visionOS object tracking`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2026/283/). For an example of using ARKit for object tracking, see [`Exploring object tracking with ARKit`](https://developer.apple.comhttps://developer.apple.com/documentation/visionos/exploring_object_tracking_with_arkit).

## Topics

### Object tracking within an app
- [Using a reference object with Reality Composer Pro](using-a-reference-object-with-reality-composer-pro.md)
  Import a reference object file to track a real-world object in your visionOS app.
- [Using a reference object with RealityKit](using-a-reference-object-with-realitykit.md)
  Import a reference object file to track a real-world object in your visionOS app.
- [Using a reference object with ARKit in visionOS](using-a-reference-object-with-arkit-in-visionos.md)
  Import a reference object file and track a real-world object in your app.
- [Using a reference object with ARKit in iOS](using-a-reference-object-with-arkit-in-ios.md)
  Track a real-world object in your iOS app by using a reference-object file.

## See Also

- [Reality Composer Pro](../RealityComposerPro/RealityComposerPro.md)
  Build, design, and orchestrate 3D content for your RealityKit apps.
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
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.
- [Manipulating entities with solid collisions](manipulating-entities-with-solid-collisions.md)
  Extend the capabilities of your app by using entities, components, and systems to maintain solid collisions when manipulating entities.
- [Gaussian splats on visionOS](gaussian-splats-on-visionos.md)
  Use the new Gaussian splat APIs available in RealityKit in visionOS 27.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/implementing-object-tracking-in-your-app)*