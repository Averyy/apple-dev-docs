# Using a reference object with ARKit in visionOS

**Framework**: visionOS

Import a reference object file and track a real-world object in your app.

#### Overview

With ARKit, you use reference objects to track and attach virtual content to real-world objects in a person’s surroundings. For example, with a reference object, you can track a household item — like a lamp — and add a highlight to a part that’s broken and show how to fix it.

To create a reference object, you obtain a 3D model asset, train a machine learning model with that 3D model asset in Create ML, then import the resulting reference object file into your app. You use ARKit to import the reference object file, track objects and handle changes to the scene, and adjust the object-tracking properties.

For more information about creating a reference object file, see [`Implementing object tracking in your app`](implementing-object-tracking-in-your-app.md).

#### Import the Reference Object File

ARKit provides two ways to import a reference object file:

- Include the reference object in the Xcode project so the app loads it directly from the bundle:

```swift
let referenceObject = try await ReferenceObject(named: "MyObject", from: Bundle.main)
```

- Alternatively, use a URL-based loader in your app to load reference object files from other sources, like a website or local file:

```swift
let referenceObject = try await ReferenceObject(from: url)
```

For more information, see [`Exploring object tracking with ARKit`](exploring_object_tracking_with_arkit.md).

#### Enable High Frame Rate Tracking

By default, ARKit tracks objects at a lower frequency so apps consume less power. This works best with stationary objects where the virtual content doesn’t need to follow an object’s precise position on every frame. With default tracking, the anchor also persists briefly when the object leaves the field of view, while high frame rate tracking removes the anchor immediately.

If you have an object that moves and changes its position frequently, like a handheld device, enable [`highFrameRateTrackingEnabled`](https://developer.apple.com/documentation/arkit/referenceobject/configuration/highframeratetrackingenabled) for that object. The [`ReferenceObject.Configuration`](https://developer.apple.com/documentation/arkit/referenceobject/configuration) allows you set the tracking behavior for a chosen object at load time, independently of any other objects in your session. Using the reference object configuration and initializers require visionOS 27 or later.

To enable high frame rate tracking, create a [`ReferenceObject.Configuration`](https://developer.apple.com/documentation/arkit/referenceobject/configuration) and pass it at load time:

```swift
var configuration = ReferenceObject.Configuration()
configuration.highFrameRateTrackingEnabled = true
let referenceObject = try await ReferenceObject(named: "MyObject", from: Bundle.main, configuration: configuration)
```

> ❗ **Important**: High frame rate tracking significantly increases power and performance consumption. Enable it only for objects that require precise, per-frame pose updates, such as handheld or moving objects.

#### Run Object Tracking on a Session

You use an [`ObjectTrackingProvider`](https://developer.apple.com/documentation/arkit/objecttrackingprovider) to track your reference object in a spatial location and receive [`ObjectAnchor`](https://developer.apple.com/documentation/arkit/objectanchor) updates. `ObjectTrackingProvider` gets the live position and orientation of the real-world object. The system can track a maximum of 10 reference objects at once. To receive this data and begin tracking, configure an [`ARKitSession`](https://developer.apple.com/documentation/arkit/arkitsession).

```swift
func configureAndRunObjectTracking() async -> ObjectTrackingProvider? {
    let referenceObjects = referenceObjectLoader.enabledReferenceObjects

    guard !referenceObjects.isEmpty else {
        fatalError("No reference objects to start tracking")
    }

    // Run a new provider each time the app enters the immersive space.
    let objectTracking = ObjectTrackingProvider(referenceObjects: referenceObjects)
    do {
        // Begin an `ARKitSession` with the provider.
        try await arkitSession.run([objectTracking])
    } catch {
        print("Error: \(error)")
        return nil
    }
    self.objectTracking = objectTracking
    return objectTracking
}
```

#### Handle Changes in the Scene

As your app tracks the reference object file, ARKit sends asynchronous updates when it detects changes in a person’s surroundings. Account for those changes and update the scene accordingly.

An [`Anchor`](https://developer.apple.com/documentation/arkit/anchor) represents the position of your real-world object within Apple Vision Pro. The [`ARKitSession`](https://developer.apple.com/documentation/arkit/arkitsession) structure provides events about the anchors, including adding a new anchor, removing an anchor, and updates on an anchor’s pose and tracking state. You can place visualizations at those anchors to render content on real-world objects.

```swift
Task {
    let objectTracking = await appState.configureAndRunObjectTracking()
    guard let objectTracking else {
        return
    }
    
    // Wait for object anchor updates.
    for await anchorUpdate in objectTracking.anchorUpdates {
        let anchor = anchorUpdate.anchor
        let referenceObject = anchor.referenceObject
        
        switch anchorUpdate.event {
        case .added: 
            // The system detects a new object anchor.
            print("Added: \(anchor)")
        case .updated:
            if anchor.isTracked {
                // The update for the detected anchor.
                print("Updated tracked anchor: \(anchor)")
            } else {
                // The system is no longer tracking the object anchor.
                print("Anchor is untracked: \(anchor)")
            }
        case .removed: 
            // The system removed the object anchor.
            print("Removed: \(anchor)")
        }
    }
}
```

#### Obtain Metric Poses

By default, the system optimizes an object anchor’s transform for placing virtual content over the tracked object in the [`mixed`](https://developer.apple.com/documentation/swiftui/immersionstyle/mixed) immersion style.

When querying a tracked object’s position, the [`ARKitCoordinateSpace.Correction`](https://developer.apple.com/documentation/arkit/arkitcoordinatespace/correction) API provides two options:

- **[`ARKitCoordinateSpace.Correction.rendered`](https://developer.apple.com/documentation/arkit/arkitcoordinatespace/correction/rendered)**: Returns the position with display corrections applied. This keeps virtual content visually aligned with the real-world object.
- **[`ARKitCoordinateSpace.Correction.none`](https://developer.apple.com/documentation/arkit/arkitcoordinatespace/correction/none)**: Returns the object’s position in metric space, without display corrections. This is useful for measuring the distance between tracked objects or determining where an object sits in physical space.

```swift
let metricSpace = myObjectAnchor.coordinateSpace(correction: .none)
```

The resulting coordinate space corresponds to real-world measurements and remains unaltered by display corrections.

#### Adjust the Object Tracking Properties for Your App

If you have an enterprise app, you can further adjust object-tracking properties to track more objects with a higher frequency. Use the [`Object-tracking parameter adjustment`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.arkit.object-tracking-parameter-adjustment.allow) key to configure object-tracking properties.

> **Note**: The object-tracking parameter adjustment key doesn’t allow you to change the maximum of 10 reference objects that the system can detect at once.

For more information on the Enterprise program, see [`Apple Developer Enterprise Program`](https://developer.apple.comhttps://developer.apple.com/programs/enterprise/).

To configure the entitlement within your app:

1. Select your Xcode project and click the Signing & Capabilities tab.
2. Click the Add Capability button (+).
3. Scroll to the Object Tracking Parameter Adjustment option and double-click it to add it.

This creates an entitlement file with the `com.apple.developer.arkit.object-tracking-parameter-adjustment.allow` key.

![An Xcode screenshot of the Capabilities library dialog with the Object Tracking Parameter Adjustment option selected.](/images/com.apple.visionOS/capabilities@2x.png)

For more information on how to add capabilities in your app, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app).

![An Xcode screenshot showing the com.apple.developer.arkit.object-tracking-parameter-adjustment.allow key selected in the Signing & Capabilities pane.](/images/com.apple.visionOS/key@2x.png)

To configure the object tracking parameters, initialize a [`init(referenceObjects:trackingConfiguration:)`](https://developer.apple.com/documentation/arkit/objecttrackingprovider/init(referenceobjects:trackingconfiguration:)).

```swift
var trackingConfiguration = ObjectTrackingProvider.TrackingConfiguration()
```

With a tracking configuration in place, you can optimize the detection parameters for your app by adjusting the following properties:

- **[`maximumTrackableInstances`](https://developer.apple.comhttps://developer.apple.com/documentation/arkit/objecttrackingprovider/trackingconfiguration/4380072-maximumtrackableinstances)**: The maximum number of instances that you can track across different object types at the same time.
- **[`maximumInstancesPerReferenceObject`](https://developer.apple.comhttps://developer.apple.com/documentation/arkit/objecttrackingprovider/trackingconfiguration/4380071-maximuminstancesperreferenceobje)**: The maximum number of instances of each reference object type. The default value is `1`.
- **[`detectionRate`](https://developer.apple.comhttps://developer.apple.com/documentation/arkit/objecttrackingprovider/trackingconfiguration/4380069-detectionrate)**: The frequency for detecting objects to track.

Use `TrackingConfiguration` to adjust the values of these properties in your app:

```swift
trackingConfiguration.maximumInstancesPerReferenceObject = 2
```

Pass the `trackingConfiguration` to [`ObjectTrackingProvider`](https://developer.apple.com/documentation/arkit/objecttrackingprovider) alongside your reference objects, then run the session as described earlier in the section, [`Run object tracking on a session`](https://developer.apple.com#Run-object-tracking-on-a-session).

```swift
dataProvider = ObjectTrackingProvider(referenceObjects: referenceObjects,
                                      trackingConfiguration: trackingConfiguration)
```

## See Also

- [Using a reference object with Reality Composer Pro](using-a-reference-object-with-reality-composer-pro.md)
  Import a reference object file to track a real-world object in your visionOS app.
- [Using a reference object with RealityKit](using-a-reference-object-with-realitykit.md)
  Import a reference object file to track a real-world object in your visionOS app.
- [Using a reference object with ARKit in iOS](using-a-reference-object-with-arkit-in-ios.md)
  Track a real-world object in your iOS app by using a reference-object file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/using-a-reference-object-with-arkit-in-visionos)*