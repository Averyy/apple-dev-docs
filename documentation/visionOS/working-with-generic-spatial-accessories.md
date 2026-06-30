# Working with generic spatial accessories

**Framework**: visionOS

Let people place digital replicas of a generic spatial accessory by tracking the accessory with ARKit.

**Availability**:
- visionOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

Specialized apps become more immersive when they respond to people using purpose-built devices, like medical instruments, steering rigs, or industrial tooling. [`ARKit`](https://developer.apple.com/documentation/ARKit) recognizes these devices as *generic spatial accessories*, but they’re distinct from spatial controllers and styli, which have their own dedicated APIs.

Manufacturers create generic spatial accessories by following the [`Accessory Design Guidelines`](https://developer.apple.comhttps://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf), paying close attention to the Spatial Accessories section. ARKit provides precise, low-latency tracking of these accessories in Apple Vision Pro across varied lighting conditions, and continues tracking orientation even when an accessory moves outside the field of view or becomes visually obscured. [`Game Controller`](https://developer.apple.com/documentation/GameController) also provides input and haptic feedback for these accessories.

In an immersive space, the sample lets people place digital replicas of the accessory. In a volume, the sample displays a digital replica that mirrors the accessory’s orientation in real time. Accessory manufacturers can also use the sample to test the tracking, input, and haptic behavior of their accessories.

> **Note**: Simulator doesn’t support accessory tracking. Run the sample on a physical device.

#### Configure the Sample Code Project

The sample works with any generic spatial accessory. Before building the sample, configure the Xcode project to access the `.referenceaccessory` file for the accessory you want to track. For step-by-step instructions, see [`Setting up access to a reference accessory file`](setting-up-access-to-a-reference-accessory-file.md).

> ❗ **Important**: If you run the sample before configuring access to a reference accessory file, the sample displays “Unable to resolve the reference accessory.”

#### Add the Accessory Tracking Capability

To help protect people’s privacy, visionOS limits app access to spatial accessory data and other sensor data on Apple Vision Pro. Add the Accessory Tracking capability to your app’s target and provide a usage description that explains how your app uses spatial accessory data. People see that description when the system prompts for access to accessory-tracking data. For more information on app capabilities, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

#### Obtain Authorization to Track Accessories

To read an accessory’s transform, your app needs Accessory Tracking authorization. The sample monitors the authorization status so it can change the availability of features that require the transform.

At startup, the sample uses an [`ARKitSession`](https://developer.apple.com/documentation/ARKit/ARKitSession) to query the current authorization status:

```swift
// AccessoryModel.swift

authorizationStatus = await arkitSession.queryAuthorization(for: [.accessoryTracking])[.accessoryTracking] ?? .notDetermined
```

The sample then observes authorization changes on the same session so the app can respond when people grant or revoke permission:

```swift
// AccessoryModel.swift

for await event in arkitSession.events {
    switch event {
    case .authorizationChanged(.accessoryTracking, let status):
        authorizationStatus = status
    default:
        break
    }
}
```

> **Note**: Your app doesn’t need authorization to anchor content to an accessory, respond to its input, or play haptics through the accessory.

#### Discover Connected Accessories

Before your app can anchor content to an accessory, track it, or respond to its input, your app needs a reference to the [`GCSpatialAccessory`](https://developer.apple.com/documentation/GameController/GCSpatialAccessory) instance for the connected accessory.

The sample uses a custom `AccessoryModel` to manage this reference, tracking the most recently connected accessory throughout the app’s life cycle.

At startup, `AccessoryModel` checks [`spatialAccessories`](https://developer.apple.com/documentation/GameController/GCSpatialAccessory/spatialAccessories) for an already-connected accessory:

```swift
// AccessoryModel.swift

if let accessory = GCSpatialAccessory.spatialAccessories.first {
    self.accessoryDevice = accessory
}
```

To handle accessories that connect later, `AccessoryModel` listens for connect notifications:

```swift
// AccessoryModel.swift

private func observeAccessoryConnectNotifications() async {
    for await notification in NotificationCenter.default.notifications(named: .GCSpatialAccessoryDidConnect) {
        if let accessory = notification.object as? GCSpatialAccessory {
            self.accessoryDevice = accessory
        }
    }
}
```

To release the reference when the active accessory disconnects, `AccessoryModel` listens for disconnect notifications:

```swift
// AccessoryModel.swift

private func observeAccessoryDisconnectNotifications() async {
    for await notification in NotificationCenter.default.notifications(named: .GCSpatialAccessoryDidDisconnect) {
        if let accessory = notification.object as? GCSpatialAccessory,
           accessory == self.accessoryDevice {
            self.accessoryDevice = nil
        }
    }
}
```

#### Load a 3d Model of the Accessory

When a person opens the immersive space, the app displays a semi-transparent digital replica of the accessory. The accessory manufacturer can include a `.usdz` model of the accessory in the `.referenceaccessory` file. When an accessory connects, `AccessoryModel` retrieves the model through an [`AnchoringComponent.AccessoryAnchoringSource`](https://developer.apple.com/documentation/RealityKit/AnchoringComponent/AccessoryAnchoringSource) and loads it as an [`Entity`](https://developer.apple.com/documentation/RealityKit/Entity). If the `.referenceaccessory` file doesn’t include a `.usdz`, or loading fails, `AccessoryModel` falls back to a placeholder entity:

```swift
// AccessoryModel.swift

private func loadReferenceEntity(from anchoringSource: AnchoringComponent.AccessoryAnchoringSource) async {
    if let usdzURL = anchoringSource.underlyingAccessory?.usdzFile {
        do {
            referenceEntity = try await Entity(contentsOf: usdzURL)
        } catch {
            logger.warning("Failed to load USDZ file, using missing reference entity fallback: \(error)")
            referenceEntity = Entity.createMissingReferenceEntity()
        }
    } else {
        referenceEntity = Entity.createMissingReferenceEntity()
    }
}
```

#### Anchor Entities to Named Accessory Locations

The app uses an [`AnchorEntity`](https://developer.apple.com/documentation/RealityKit/AnchorEntity) to keep the replica locked to the physical accessory’s origin as a person moves the accessory:

```swift
// ImmersiveView.swift

private func createReferenceAnchorEntity(
    for source: AnchoringComponent.AccessoryAnchoringSource,
    trackingMode: AnchoringComponent.TrackingMode
) -> Entity? {
    guard let referenceEntity = appModel.accessoryModel.referenceEntity else {
        return nil
    }

    let anchorEntity = AnchorEntity(
        .accessory(from: source, location: .origin),
        trackingMode: trackingMode,
        physicsSimulation: .none
    )
    anchorEntity.addChild(referenceEntity.clone(recursive: true))
    anchorEntity.components.set(OpacityComponent(opacity: 0.5))

    return anchorEntity
}
```

All generic accessories support anchoring entities to their origin, and some support anchoring to other named locations the manufacturer defines. The sample queries the [`accessoryLocations`](https://developer.apple.com/documentation/RealityKit/AnchoringComponent/AccessoryAnchoringSource/accessoryLocations) property on `AccessoryAnchoringSource` to discover an accessory’s supported locations, then presents a toggle for each in `AccessorySettingsForm`. When a person turns on a location toggle, the sample anchors a white sphere at that location.

The form also presents a picker for the tracking mode. The tracking mode controls the trade-off between latency and accuracy. Use [`continuous`](https://developer.apple.com/documentation/RealityKit/AnchoringComponent/TrackingMode-swift.struct/continuous) for higher accuracy with increased latency, or [`predicted`](https://developer.apple.com/documentation/RealityKit/AnchoringComponent/TrackingMode-swift.struct/predicted) for lower latency with less accuracy.

#### Read the Accessorys Transform Using Realitykit

When a person taps the “Place digital replica” button in `ContentView`, `ImmersiveView` reads the reference anchor entity’s transform, clones the reference entity at that position, and logs the underlying [`AccessoryAnchor`](https://developer.apple.com/documentation/ARKit/AccessoryAnchor) to demonstrate how to access it:

```swift
// ImmersiveView.swift

private func placeDigitalReplica() {
    guard let referenceAnchorEntity = referenceRoot.children.first else { return }

    guard let referenceEntity = appModel.accessoryModel.referenceEntity else {
        // ...
        return
    }

    let replica = referenceEntity.clone(recursive: true)
    replica.transform.matrix = referenceAnchorEntity.transformMatrix(relativeTo: nil)

    if let arkitComponent = referenceAnchorEntity.components[ARKitAnchorComponent.self],
       let underlyingAnchor = arkitComponent.anchor as? AccessoryAnchor {
        // Access the anchor associated with an anchor entity.
        logger.debug("Underlying anchor: \(underlyingAnchor)")
    }

    digitalReplicaRoot.addChild(replica)
}
```

Reading an anchor entity’s transform requires a running [`SpatialTrackingSession`](https://developer.apple.com/documentation/RealityKit/SpatialTrackingSession) configured to track accessories.

Entities parented to an `AnchorEntity` always render at the accessory’s latest pose. When placing a digital replica, the sample instead clones the reference entity and applies the anchor entity’s transform to the clone. This pattern introduces a one-frame lag, because by the time RealityKit renders the clone, the accessory has moved to a new pose. This approach is simple and works well when the one-frame lag is acceptable. For content that needs continuous low-latency tracking, see the [`Track an accessory using ARKit`](working-with-generic-spatial-accessories#Track-an-accessory-using-ARKit.md) section.

#### Track an Accessory Using Arkit

Use [`AccessoryTrackingProvider`](https://developer.apple.com/documentation/ARKit/AccessoryTrackingProvider) when your app needs to choose how and when it reads the accessory’s transform, or when it needs more control over rendering than RealityKit provides. For example, when your app:

- displays content in a volume, whose fixed bounds can prevent an anchored entity from following the accessory past the edges.
- renders outside of RealityKit.
- predicts the accessory’s position at a future timestamp.

The `AccessoryModel` creates an `AccessoryTrackingProvider` for the connected [`Accessory`](https://developer.apple.com/documentation/ARKit/Accessory) and runs it on an [`ARKitSession`](https://developer.apple.com/documentation/ARKit/ARKitSession):

```swift
// AccessoryModel.swift

let accessory = try await Accessory(device: accessoryDevice)
let provider = AccessoryTrackingProvider(accessories: [accessory])
try await arkitSession.run([provider])
```

The connected accessory may change during the app’s life cycle. When it does, the sample updates the running provider rather than stopping and restarting it, using [`updateAccessories(_:)`](https://developer.apple.com/documentation/ARKit/AccessoryTrackingProvider/updateAccessories(_:)):

```swift
// AccessoryModel.swift

let accessories = await buildAccessoriesForTrackingProvider()
try await accessoryTrackingProvider.updateAccessories(accessories)
```

With the provider running, the app can respond when a person moves the accessory. When a person taps the “Show the Volume” button in `ContentView`, the app displays `VolumeView` containing a digital replica that rotates in real time to mirror the physical accessory’s orientation:

```swift
// VolumeView.swift

RealityView { content in
    guard let sourceEntity = appModel.accessoryModel.referenceEntity else { return }
    let clone = sourceEntity.clone(recursive: true)

    content.add(clone)
    // ...
    scaleToFit(clone)

    subscription = content.subscribe(to: SceneEvents.Update.self) { _ in
        if let accessoryAnchor = appModel.accessoryModel.queryLatestAccessoryAnchor(),
           let rotation = accessoryAnchor.coordinateSpace(correction: .rendered).ancestorFromSpaceTransformFloat().rotation {
            clone.transform.rotation = unsafe rotation.quaternion
        } else {
            clone.transform.rotation = simd_quatf()
        }
    }
}
```

Typically, apps iterate the provider’s [`anchorUpdates`](https://developer.apple.com/documentation/ARKit/AccessoryTrackingProvider/anchorUpdates) to react to accessory anchor updates, for example:

```swift
// Reference snippet: This isn't part of the project's sample code.

for await update in provider.anchorUpdates {
    switch update.event {
    case .added, .updated:
        let anchor = update.anchor
        // Use the anchor.
    case .removed:
        // Clean up the anchor.
    }
}
```

However, the sample takes a different approach. Rather than relying on [`anchorUpdates`](https://developer.apple.com/documentation/ARKit/AccessoryTrackingProvider/anchorUpdates), this project subscribes to [`SceneEvents.Update`](https://developer.apple.com/documentation/RealityKit/SceneEvents/Update) from a render loop in RealityKit. This bypasses an update cycle in [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) which otherwise invalidates views at the provider’s high frame rate.

To keep the replica’s rotation in sync with the accessory, `VolumeView` reads the accessory’s pose each frame by calling `queryLatestAccessoryAnchor`. In predicted mode, `queryLatestAccessoryAnchor` uses [`predictAnchor(for:at:)`](https://developer.apple.com/documentation/ARKit/AccessoryTrackingProvider/predictAnchor(for:at:)) to estimate the accessory’s pose a few frames into the future:

```swift
// AccessoryModel.swift

func queryLatestAccessoryAnchor() -> AccessoryAnchor? {
    guard let accessoryTrackingProvider,
          accessoryTrackingProvider.state == .running,
          let latestAnchor = accessoryTrackingProvider.latestAnchors.first else {
        return nil
    }

    if trackingMode == .predicted {
        return accessoryTrackingProvider.predictAnchor(for: latestAnchor, at: CACurrentMediaTime() + renderLatencyCompensation)
    }

    return latestAnchor
}
```

The `VolumeView` passes [`ARKitCoordinateSpace.Correction.rendered`](https://developer.apple.com/documentation/ARKit/ARKitCoordinateSpace/Correction/rendered) to `coordinateSpace` because it applies the rotation to a rendered entity. A non-rendering use case, like a measuring app, would pass [`ARKitCoordinateSpace.Correction.none`](https://developer.apple.com/documentation/ARKit/ARKitCoordinateSpace/Correction/none) to read the raw rotation.

The `VolumeView` only reads the rotation from the accessory’s transform. To obtain the accessory’s full transform, wrap `ancestorFromSpaceTransformFloat()` in a [`Transform`](https://developer.apple.com/documentation/RealityKit/Transform):

```swift
// Reference snippet: This isn't part of the project's sample code.

let worldTransform = Transform(
    projectiveTransform: accessoryAnchor
        .coordinateSpace(correction: .rendered)
        .ancestorFromSpaceTransformFloat()
)
```

For more information on using `AccessoryTrackingProvider`, see [`Drawing in the air and on surfaces with a spatial stylus`](drawing-in-the-air-and-on-surfaces-with-a-spatial-stylus.md).

For information on tracking in a volume, see [`Tracking accessories in volumetric windows`](https://developer.apple.com/documentation/ARKit/tracking-accessories-in-volumetric-windows). For information on using an accessory’s transform to drive interactive content, see [`Tracking a handheld accessory as a virtual sculpting tool`](https://developer.apple.com/documentation/ARKit/tracking-a-handheld-accessory-as-a-virtual-sculpting-tool).

#### Respond to Accessory Input

Some accessories have buttons. The accessory’s `input` property provides the familiar [`Game Controller`](https://developer.apple.com/documentation/GameController) interface. If the connected accessory has buttons, a person can press any button to initiate the same functionality as the “Place digital replica” button in `ContentView`.

When an accessory connects, `AccessoryModel` sets an [`elementValueDidChangeHandler`](https://developer.apple.com/documentation/GameController/GCDevicePhysicalInput/elementValueDidChangeHandler) on the accessory’s input to call `initiateDigitalReplicaPlacement` on every button press:

```swift
// AccessoryModel.swift

private func handleAccessoryDeviceChange() {
    // ...

    accessoryDevice.input?.elementValueDidChangeHandler = { [weak self] (_, element) in
        guard let self else { return }
        if let button = element as? GCButtonElement,
           button.pressedInput.isPressed {
            logger.info("Button pressed: \(element.localizedName ?? "Unnamed element")")
            initiateDigitalReplicaPlacement()
        }
    }

    // ...
}
```

For more information on callback and polling approaches to input handling, see [`Handling input events`](https://developer.apple.com/documentation/GameController/handling-input-events).

#### Play Haptic Feedback

Some accessories support haptic feedback. The accessory’s `haptics` property provides access to [`Core Haptics`](https://developer.apple.com/documentation/CoreHaptics). If the connected accessory supports haptics, a person can tap the “Play haptics” button in `ContentView` to provide feedback on the accessory.

When `HapticModel` initializes, it creates a [`CHHapticEngine`](https://developer.apple.com/documentation/CoreHaptics/CHHapticEngine) on the accessory’s default locality and starts it:

```swift
// HapticModel.swift

init(accessory: GCSpatialAccessory) async {
    guard let engine = accessory.haptics?.createEngine(withLocality: .default) else {
        logger.info("The accessory doesn't support haptics.")
        return
    }

    do {
        try await engine.start()
        hapticEngine = engine
        logger.info("The haptic engine started successfully.")
    } catch {
        logger.error("Failed to start the haptic engine: \(error)")
        hapticEngine = nil
    }
}
```

With the engine running, the sample plays haptic patterns using [`CHHapticPattern`](https://developer.apple.com/documentation/CoreHaptics/CHHapticPattern) whenever a person taps “Play haptics”.

For more information on input and haptics with accessories, see [`Discovering and tracking spatial game controllers and styli`](https://developer.apple.com/documentation/GameController/discovering-and-tracking-spatial-game-controllers-and-styli).

## Topics

### Working with reference accessory files
- [Preparing spatial accessories for tracking in your visionOS app](../ARKit/preparing-spatial-accessories-for-tracking-in-your-visionos-app.md)
  Prepare a spatial accessory for tracking by training a reference accessory file and integrating it into your visionOS app.
- [Setting up access to a reference accessory file](setting-up-access-to-a-reference-accessory-file.md)
  Track a generic spatial accessory by helping ARKit find the device’s reference accessory file.

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
- [Exploring object tracking with ARKit](exploring_object_tracking_with_arkit.md)
  Find and track real-world objects in visionOS using reference objects you train with Create ML.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/working-with-generic-spatial-accessories)*