# Exploring object tracking with ARKit

**Framework**: visionOS

Find and track real-world objects in visionOS using reference objects you train with Create ML.

**Availability**:
- visionOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

This sample app demonstrates how to use a reference object to discover and track a specific object in a person’s surroundings. A reference object is a trained representation of a physical object that ARKit uses to recognize and track that object. You create a reference object in Create ML from a USDZ file of the physical object. Create ML writes the reference object to a `.referenceobject` file, which your app loads and passes to ARKit. When ARKit detects the object, you can attach digital content to it, for example, a diagram of a machine’s assembly for someone testing or repairing the machine, or labels annotating parts of the device.

The sample bundles a reference object that ARKit uses to recognize an Apple Magic Keyboard in someone’s surroundings, and exposes toggles you can use to change the tracking frequency and visualize the object’s metric coordinates.

> **Note**: This sample code project is associated with WWDC24 [`Session 10101 — Explore object tracking for visionOS`](https://developer.apple.comhttps://developer.apple.com/wwdc24/10101/), and the sample also covers improvements to object tracking demonstrated in WWDC26 [`Session 283 - Explore enhancements to visionOS object tracking`](https://developer.apple.comhttps://developer.apple.com/wwdc26/283).

#### Configure the Sample Code Project

> **Note**: This app requires Xcode 27 and visionOS 27 or later, and an Apple Vision Pro. The visionOS simulator doesn’t support object tracking.

1. In the project’s settings, select Signing & Capabilities.
2. Select your team name from the drop-down menu.
3. Pair Xcode with your device wirelessly or by using the developer strap.
4. Click Run or press Command-R to launch the app.

#### Configure the Object Tracking Capability

To help protect people’s privacy, visionOS limits app access to object-tracking data and other sensors in Apple Vision Pro. Add the World Sensing capability to your app’s target and provide a usage description that explains how your app uses world-sensing data, including object tracking. People see that description when the system prompts for access to object tracking and other world-sensing data. For more information about app capabilities, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

#### Load Reference Objects Into the Sample

The sample loads reference objects from two sources. The first source is the sample app’s bundle.

```swift
func loadBuiltInReferenceObjects() async {
    // Only allow one loading operation at any given time.
    guard !didStartLoading else { return }
    didStartLoading = true
    
    print("Looking for reference objects in the main bundle ...")

    // Get a list of all reference object files in the app's main bundle and attempt to load each.
    var referenceObjectFiles: [String] = []
    if let resourcesPath = Bundle.main.resourcePath {
        try? referenceObjectFiles = FileManager.default.contentsOfDirectory(atPath: resourcesPath)
            .filter { $0.lowercased().hasSuffix(".referenceobject") }
    }
    
    fileCount = referenceObjectFiles.count
    updateProgress()
    
    await withTaskGroup(of: Void.self) { group in
        for file in referenceObjectFiles {
            let objectURL = Bundle.main.bundleURL.appending(path: file)
            group.addTask {
                await self.loadReferenceObject(objectURL)
                await self.finishedOneFile()
            }
        }
    }
}
```

The second source is a file you pick at runtime by tapping the plus button in the sidebar and selecting a `.referenceobject` file in the file importer, which is useful to validate any reference object without rebuilding the app.

```swift
.fileImporter(isPresented: $fileImporterIsOpen, allowedContentTypes: [referenceObjectUTType], allowsMultipleSelection: true) { results in
    switch results {
    case .success(let fileURLs):
        Task {
            // Try to load each selected file as a reference object.
            for fileURL in fileURLs {
                guard fileURL.startAccessingSecurityScopedResource() else {
                    print("Failed to get sandboxed access to the file \(fileURL)")
                    return
                }
                await appState.referenceObjectLoader.addReferenceObject(fileURL)
                fileURL.stopAccessingSecurityScopedResource()
            }
        }
    case .failure(let error):
        print("Failed to open file with error: \(error)")
    }
}
```

#### Run Object Tracking on a Session

To start receiving tracking anchors, create an [`ObjectTrackingProvider`](https://developer.apple.com/documentation/ARKit/ObjectTrackingProvider) and initialize it with a reference object. Then start an [`ARKitSession`](https://developer.apple.com/documentation/ARKit/ARKitSession) with the provider.

```swift
func startTracking() async -> ObjectTrackingProvider? {
    // Run a new provider every time when entering the immersive space.
    let objectTracking = ObjectTrackingProvider(referenceObjects: referenceObjects)
    do {
        try await arkitSession.run([objectTracking])
    } catch {
        print("Error: \(error)")
        return nil
    }
    self.objectTracking = objectTracking
    return objectTracking
}
```

#### Respond to Anchor Updates

ARKit delivers an asynchronous stream of updates as it detects changes in the scene. The sample app handles these events on the [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) inside `ObjectTrackingRealityView`.

```swift
.task {
    guard let objectTracking = await appState.startTracking() else { return }

    // Wait for object anchor updates and maintain a dictionary of visualizations
    // that attach to those anchors.
    for await anchorUpdate in objectTracking.anchorUpdates {
        let anchor = anchorUpdate.anchor
        let id = anchor.id
        
        switch anchorUpdate.event {
        case .added:
            // Create a new visualization for the reference object that ARKit just detected.
            // The app displays the USDZ file with which Create ML trained the reference object as
            // a wireframe over the real-world object, if the .referenceobject file contains
            // that USDZ file. If the original USDZ isn't available, the app displays a bounding box instead.
            let model = appState.referenceObjectLoader.usdzsPerReferenceObjectID[anchor.referenceObject.id]
            let visualization = ObjectAnchorVisualization(
                for: anchor,
                withModel: model,
                showsMetricCoordinateLabel: appState.showsMetricCoordinateLabel
            )
            self.objectVisualizations[id] = visualization
            root.addChild(visualization.entity)
        case .updated:
            objectVisualizations[id]?.update(with: anchor)
        case .removed:
            objectVisualizations[id]?.entity.removeFromParent()
            objectVisualizations.removeValue(forKey: id)
        }
    }
}
```

When the provider adds an anchor, the sample creates an `ObjectAnchorVisualization` that renders the reference object’s USDZ as a wireframe over the real-world object, or a bounding box when the USDZ isn’t available. When the provider updates the anchor, the sample moves the visualization to match. When the provider removes the anchor, the sample removes the visualization from the scene.

#### Opt in to High Frame Rate Tracking

By default, ARKit tracks reference objects at a low frame rate, which works well for stationary objects. For handheld and moving objects, opt in to high frame-rate tracking, at the cost of additional power and performance. To enable high frame-rate tracking, create a [`ReferenceObject.Configuration`](https://developer.apple.com/documentation/ARKit/ReferenceObject/Configuration) and set its `highFrameRateTrackingEnabled` property to `true`. Pass the configuration to the [`ReferenceObject`](https://developer.apple.com/documentation/ARKit/ReferenceObject) initializer, then create an [`ObjectTrackingProvider`](https://developer.apple.com/documentation/ARKit/ObjectTrackingProvider) with that reference object.

```swift
var configuration = ReferenceObject.Configuration()
configuration.highFrameRateTrackingEnabled = true

let referenceObject = try await ReferenceObject(from: url, configuration: configuration)
let objectTracking = ObjectTrackingProvider(referenceObjects: [referenceObject])
```

The steps for high frame-rate tracking differ if your app uses an [`AnchorEntity`](https://developer.apple.com/documentation/RealityKit/AnchorEntity) instead of handling [`ObjectAnchor`](https://developer.apple.com/documentation/ARKit/ObjectAnchor) updates:

- Use an `ObjectTrackingProvider` configured for high frame-rate tracking.
- When the provider adds an anchor, construct an `AnchorEntity` with that anchor and add it to your `RealityView`. Remove the `AnchorEntity` when the provider removes the anchor.
- When the provider updates the anchor, check the anchor’s `isTracked` property and react to lost tracking, for example, hide the `AnchorEntity` or reduce its opacity when ARKit loses tracking on the underlying anchor. RealityKit updates the `AnchorEntity`‘s transform automatically, so you don’t need to do that.

#### Choose Between Perceived and Metric Poses

ARKit reports an object’s pose in two coordinate spaces: perceived and metric. The system applies display corrections so that rendered content stays visually stable to the person wearing the device even as they move. Use the perceived pose, the default `coordinateSpace(correction: .rendered)`, when you render an [`Entity`](https://developer.apple.com/documentation/RealityKit/Entity) that needs to stay visually fixed to the tracked object as the person moves around the object. Use the metric pose, `coordinateSpace(correction: .none)`, for measurement, because display correction doesn’t affect it.

```swift
let metricSpace = anchor.coordinateSpace(correction: .none)
let translation = metricSpace.ancestorFromSpaceTransformFloat().translation
```

This sample demonstrates how to read the metric pose and display it in a SwiftUI label that `ObjectAnchorVisualization` attaches above the tracked keyboard using a [`ViewAttachmentComponent`](https://developer.apple.com/documentation/RealityKit/ViewAttachmentComponent).

#### Create Your Own Reference Objects

To create a reference object, train a model with a USDZ file of the physical object using Create ML on a Mac with an M2 chip or later. If you don’t already have a USDZ, you can produce one from scans, for example, using Object Capture on an iPhone or iPad, or author one in a 3D modeling tool. For a step-by-step walkthrough of the training workflow, see [`Implementing object tracking in your app`](implementing-object-tracking-in-your-app.md).

#### Consider Retraining Reference Objects

As of visionOS 27, Create ML creates reference objects capable of more accurate and lower-latency tracking. To pick up the improvements, retrain your reference objects with the latest version of Create ML. Reference objects you trained with previous versions continue to work with your existing code.

The training mode you specify in Create ML affects tracking accuracy and per-frame compute cost.

- Standard mode, which is the default, produces a lighter model with lower per-frame cost but reduced precision.
- Extended mode produces the most precise tracking at any frame rate, at the cost of a larger model and higher per-frame compute. Reach for extended mode when you need the highest tracking quality, for example, when your app needs to track a handheld object.

## See Also

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
- [Object tracking with Reality Composer Pro experiences](object-tracking-with-reality-composer-pro-experiences.md)
  Use object tracking in visionOS to attach digital content to real objects to create engaging experiences.
- [Building local experiences with room tracking](building-local-experiences-with-room-tracking.md)
  Use room tracking in visionOS to provide custom interactions with physical spaces.
- [Placing entities using head and device transform](placing-entities-using-head-and-device-transform.md)
  Query and react to changes in the position and rotation of Apple Vision Pro.
- [Drawing in the air and on surfaces with a spatial stylus](drawing-in-the-air-and-on-surfaces-with-a-spatial-stylus.md)
  Create a spatial stylus drawing experience that balances latency and accuracy for both in-air and on-surface drawing.
- [Preparing spatial accessories for tracking in your visionOS app](../ARKit/preparing-spatial-accessories-for-tracking-in-your-visionos-app.md)
  Prepare a spatial accessory for tracking by training a reference accessory file and integrating it into your visionOS app.
- [Working with generic spatial accessories](working-with-generic-spatial-accessories.md)
  Use generic spatial accessories to track purpose-built devices in your visionOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/exploring_object_tracking_with_arkit)*