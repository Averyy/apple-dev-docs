# Working with generic spatial accessories

**Framework**: visionOS

Use generic spatial accessories to track purpose-built devices in your visionOS app.

#### Overview

Specialized apps become more immersive when they respond to people using purpose-built devices, like medical instruments, steering rigs, or industrial tooling. [`ARKit`](https://developer.apple.com/documentation/ARKit) recognizes these devices as *generic spatial accessories*, but they’re distinct from spatial controllers and styli, which have their own dedicated APIs.

Manufacturers create generic spatial accessories by following the [`Accessory Design Guidelines`](https://developer.apple.comhttps://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf), paying close attention to the Spatial Accessories section. ARKit provides precise, low-latency tracking of these accessories in Apple Vision Pro across varied lighting conditions, and continues tracking orientation even when an accessory moves outside the field of view or becomes visually obscured. [`Game Controller`](https://developer.apple.com/documentation/GameController) also provides input and haptic feedback for these accessories.

#### Configure Access to a Reference Accessory File

To support a generic spatial accessory, your app needs a `.referenceaccessory` file which describes the device’s physical characteristics. ARKit uses the metadata in this file to recognize and track the device in physical space.

> **Note**: Manufacturers create `.referenceaccessory` files by training an accessory tracker model in Create ML. For more information on creating a reference accessory, see [`Preparing spatial accessories for tracking in your visionOS app`](https://developer.apple.com/documentation/ARKit/preparing-spatial-accessories-for-tracking-in-your-visionos-app).

When your app initializes an [`Accessory`](https://developer.apple.com/documentation/ARKit/Accessory) from a connected [`GCSpatialAccessory`](https://developer.apple.com/documentation/GameController/GCSpatialAccessory), ARKit resolves the corresponding `.referenceaccessory` file using the Uniform Type Identifier (UTI) registered by the system. If ARKit can’t find a matching file, initialization fails. For more information, see [`Uniform Type Identifiers`](https://developer.apple.com/documentation/UniformTypeIdentifiers).

> **Note**: The configuration process depends on whether your app owns the accessory type.

If you’re the accessory manufacturer, bundle the `.referenceaccessory` file in your app and declare it under `UTExportedTypeDeclarations` in your `Info.plist`. This both enables your app to use the file and registers the type system-wide, so any other app installed on the device can also use the file as long as your app is present.

To access generic spatial accessories from other manufacturers, check with the manufacturer to see if they have a `.referenceaccessory` file available. If so, bundle it in your app and declare it under `UTImportedTypeDeclarations` in your `Info.plist` so your app works even when the manufacturer’s app isn’t installed. An imported declaration tells the system you depend on the type but don’t own it. If more than one app declares an imported type for the same identifier, the system resolves to one of them.

If your app includes a `UTImportedTypeDeclarations` entry and the manufacturer’s app with a matching `UTExportedTypeDeclarations` entry is also installed, ARKit always gives the exported declaration precedence.

To bundle a `.referenceaccessory` file, drag it into your Xcode project and click the checkbox next to your app target in the dialog that appears. Then add a `UTExportedTypeDeclarations` entry to your `Info.plist` if your app owns the type, or a `UTImportedTypeDeclarations` entry if you depend on a type defined by someone else.

```xml
<key>UTImportedTypeDeclarations</key>   <!-- Or `UTExportedTypeDeclarations` if your app defines the type. -->
<array>
    <dict>
        <key>UTTypeConformsTo</key>
        <array>
            <!-- Confirm with the manufacturer -->
            <string>com.apple.spatial-device</string>
        </array>
        <key>UTTypeIdentifier</key>
        <!-- Replace with the manufacturer's identifier -->
        <string>com.example.mycontroller</string>
        <key>UTTypeReferenceAccessoryFile</key>
        <!-- Filename of a `.referenceaccessory` bundled in your app's resources. -->
        <string>my_controller.referenceaccessory</string>
        <key>UTTypeDescription</key>
        <!-- Human-readable name -->
        <string>My Controller</string>
    </dict>
</array>
```

- **`UTTypeConformsTo`**: The parent type in the UTI conformance hierarchy. Check with the manufacturer for the correct value; `com.apple.spatial-device` is a reasonable default for spatial accessories.
- **`UTTypeIdentifier`**: The unique reverse-DNS identifier for this accessory type, provided by the manufacturer. Use the exact value of the `uniformTypeId` defined for the object class when training the `.referenceaccessory` in Create ML.
- **`UTTypeReferenceAccessoryFile`**: The exact filename of the `.referenceaccessory` bundle included in your app.
- **`UTTypeDescription`**: A human-readable name the system uses for display and debugging.

For more information on Uniform Type Identifiers, see [`Defining file and data types for your app`](https://developer.apple.com/documentation/UniformTypeIdentifiers/defining-file-and-data-types-for-your-app).

If the manufacturer doesn’t make the `.referenceaccessory` file available for bundling, your app can instead rely on ARKit to find the file when the manufacturer’s app is installed. In that case, handle initialization failures gracefully. When [`init(device:)`](https://developer.apple.com/documentation/ARKit/Accessory/init(device:)) throws, display an error that directs people to install the required app.

```swift
do {
    let trackedAccessory = try await Accessory(device: accessory)
    // Use the tracked accessory.
} catch {
    logger.error("Failed to create accessory: \(error)")
    // Prompt the person to install the manufacturer's app.
}
```

#### Add the Accessory Tracking Capability

To help protect people’s privacy, visionOS limits app access to spatial accessory data and other sensor data on Apple Vision Pro. Add the Accessory Tracking capability to your app’s target and provide a usage description that explains how your app uses spatial accessory data. People see that description when the system prompts for access to accessory-tracking data. For more information on app capabilities, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

#### Obtain Authorization to Track Accessories

To read an accessory’s transform, your app needs Accessory Tracking authorization. Monitor the authorization status so your app can enable or disable features that require the transform.

At startup, use an [`ARKitSession`](https://developer.apple.com/documentation/ARKit/ARKitSession) to query the current authorization status.

```swift
// Query initial authorization status.
let authorizationStatus = await arkitSession.queryAuthorization(for: [.accessoryTracking])[.accessoryTracking] ?? .notDetermined
// Use authorization status to initialize your app.
```

Observe authorization changes on the same session so your app can respond when people grant or revoke permission:

```swift
// Observe and respond to authorization changes.
for await event in arkitSession.events {
    switch event {
    case .authorizationChanged(.accessoryTracking, let status):
        // Handle changes to authorization status.
    default:
        break
    }
}
```

> **Note**: Your app doesn’t need authorization to anchor content to an accessory, respond to its input, or play haptics through the accessory.

#### Discover Connected Accessories

Before your app can anchor content to an accessory, track it, or respond to its input, your app needs a reference to the [`GCSpatialAccessory`](https://developer.apple.com/documentation/GameController/GCSpatialAccessory) instance for the connected accessory.

Query [`spatialAccessories`](https://developer.apple.com/documentation/GameController/GCSpatialAccessory/spatialAccessories) for a list of connected accessories:

```swift
for accessory in GCSpatialAccessory.spatialAccessories {
    // Keep a reference to the accessory.
}
```

Listen for connect notifications to handle accessories that connect later:

```swift
for await notification in NotificationCenter.default.notifications(named: .GCSpatialAccessoryDidConnect) {
    if let accessory = notification.object as? GCSpatialAccessory {
        // Keep a reference to the accessory.
    }
}
```

Listen for disconnect notifications to release references when accessories disconnect:

```swift
for await notification in NotificationCenter.default.notifications(named: .GCSpatialAccessoryDidDisconnect) {
    if let accessory = notification.object as? GCSpatialAccessory {
        // Release the reference to the accessory.
    }
}
```

#### Load a 3d Model of the Accessory

The accessory manufacturer may bundle a USDZ of the accessory your app can render.

Create an [`AnchoringComponent.AccessoryAnchoringSource`](https://developer.apple.com/documentation/RealityKit/AnchoringComponent/AccessoryAnchoringSource) from the connected accessory to access the USDZ file:

```swift
let anchoringSource = try await AnchoringComponent.AccessoryAnchoringSource(device: accessory)
```

Use the source to load the USDZ as an [`Entity`](https://developer.apple.com/documentation/RealityKit/Entity), falling back to a placeholder if it’s unavailable or loading fails:

```swift
let referenceEntity: Entity
if let usdzURL = anchoringSource.underlyingAccessory?.usdzFile {
    do {
        referenceEntity = try await Entity(contentsOf: usdzURL)
    } catch {
        logger.warning("Failed to load USDZ: \(error)")
        referenceEntity = makeFallbackEntity()
    }
} else {
    referenceEntity = makeFallbackEntity()
}
```

#### Anchor Entities to Named Accessory Locations

Use an [`AnchorEntity`](https://developer.apple.com/documentation/RealityKit/AnchorEntity) to render content that tracks an accessory. Create the anchor entity from the accessory’s anchoring source and a location on the device:

```swift
let anchorEntity = AnchorEntity(
    .accessory(from: anchoringSource, location: .origin),
    trackingMode: .continuous
)
```

You can anchor content to the origin of any generic accessory. Some accessories also let you anchor content to distinct points the manufacturer defines on the device. Query the supported named locations using the `accessoryLocations` property on [`AnchoringComponent.AccessoryAnchoringSource`](https://developer.apple.com/documentation/RealityKit/AnchoringComponent/AccessoryAnchoringSource):

```swift
let availableLocations = anchoringSource.accessoryLocations
```

The tracking mode controls the trade-off between latency and accuracy. Use [`continuous`](https://developer.apple.com/documentation/RealityKit/AnchoringComponent/TrackingMode-swift.struct/continuous) for higher accuracy with increased latency, or [`predicted`](https://developer.apple.com/documentation/RealityKit/AnchoringComponent/TrackingMode-swift.struct/predicted) for lower latency with less accuracy.

Reading an anchor entity’s transform requires a running [`SpatialTrackingSession`](https://developer.apple.com/documentation/RealityKit/SpatialTrackingSession) configured to track accessories. Entities parented to an `AnchorEntity` render at the accessory’s latest pose. Reading the transform programmatically yields a value one frame behind. Use [`AccessoryTrackingProvider`](https://developer.apple.com/documentation/ARKit/AccessoryTrackingProvider), covered in the next section, for the lowest-latency transform access.

#### Track an Accessory Using Arkit

Use [`AccessoryTrackingProvider`](https://developer.apple.com/documentation/ARKit/AccessoryTrackingProvider) when your app needs the accessory’s transform in code. For example, when your app:

- displays content in a volume, whose fixed bounds can prevent an anchored entity from following the accessory past the edges.
- renders outside of RealityKit.
- predicts the accessory’s position at a future timestamp.

Create an `AccessoryTrackingProvider` from one or more [`Accessory`](https://developer.apple.com/documentation/ARKit/Accessory) instances, then run the provider using an [`ARKitSession`](https://developer.apple.com/documentation/ARKit/ARKitSession):

```swift
let trackedAccessory = try await Accessory(device: accessory)
let provider = AccessoryTrackingProvider(accessories: [trackedAccessory])
try await arkitSession.run([provider])
```

To respond to accessory anchor updates, iterate the provider’s `anchorUpdates` async sequence:

```swift
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

For the lowest-latency rendering, predict where the accessory will be at a future timestamp using [`predictAnchor(for:at:)`](https://developer.apple.com/documentation/ARKit/AccessoryTrackingProvider/predictAnchor(for:at:)). Pass a timestamp offset that matches your rendering latency.

```swift
let predictedAnchor = provider.predictAnchor(
    for: anchor,
    at: CACurrentMediaTime() + renderLatencyCompensation
)
```

Read the world-space transform from the anchor using its coordinate space. Pass `.rendered` to align the transform with the rendering pipeline, or `.none` for the raw measured value:

```swift
let anchorSpace = predictedAnchor.coordinateSpace(correction: .rendered)
let worldTransform = Transform(projectiveTransform: anchorSpace.ancestorFromSpaceTransformFloat())
```

When the connected accessory changes, call [`updateAccessories(_:)`](https://developer.apple.com/documentation/ARKit/AccessoryTrackingProvider/updateAccessories(_:)) on the running provider instead of stopping and restarting it:

```swift
let trackedAccessory = try await Accessory(device: accessory)
try await provider.updateAccessories([trackedAccessory])
```

For more information on using `AccessoryTrackingProvider`, see [`Drawing in the air and on surfaces with a spatial stylus`](drawing-in-the-air-and-on-surfaces-with-a-spatial-stylus.md).

For information on tracking in a volume, see [`Tracking accessories in volumetric windows`](https://developer.apple.com/documentation/ARKit/tracking-accessories-in-volumetric-windows). For information on using an accessory’s transform to drive interactive content, see [`Tracking a handheld accessory as a virtual sculpting tool`](https://developer.apple.com/documentation/ARKit/tracking-a-handheld-accessory-as-a-virtual-sculpting-tool).

#### Respond to Accessory Input

Some accessories have buttons. The accessory’s `input` property provides the familiar [`Game Controller`](https://developer.apple.com/documentation/GameController) interface.

For example, set an [`elementValueDidChangeHandler`](https://developer.apple.com/documentation/GameController/GCDevicePhysicalInput/elementValueDidChangeHandler) to respond to button presses:

```swift
guard let accessory = GCSpatialAccessory.spatialAccessories.first else { return }
accessory.input?.elementValueDidChangeHandler = { _, element in
    if let button = element as? GCButtonElement, button.pressedInput.isPressed {
        // Handle the button press.
    }
}
```

For more information on callback and polling approaches to input handling, see [`Handling input events`](https://developer.apple.com/documentation/GameController/handling-input-events).

#### Play Haptic Feedback

Some accessories support haptic feedback. The accessory’s `haptics` property provides access to [`Core Haptics`](https://developer.apple.com/documentation/CoreHaptics).

For example, create a [`CHHapticEngine`](https://developer.apple.com/documentation/CoreHaptics/CHHapticEngine) on the default locality:

```swift
guard let accessory = GCSpatialAccessory.spatialAccessories.first else { return }
let engine = accessory.haptics?.createEngine(withLocality: .default)
try await engine?.start()
```

With the engine running, play haptic patterns using [`Core Haptics`](https://developer.apple.com/documentation/CoreHaptics).

For more information on input and haptics with accessories, see [`Discovering and tracking spatial game controllers and styli`](https://developer.apple.com/documentation/GameController/discovering-and-tracking-spatial-game-controllers-and-styli).

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