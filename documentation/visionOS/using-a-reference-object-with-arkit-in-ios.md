# Using a reference object with ARKit in iOS

**Framework**: visionOS

Track a real-world object in your iOS app by using a reference-object file.

#### Overview

ARKit enables your iOS app to track real-world objects and attach virtual content to them. For example, you can track a power tool and overlay an animated guide showing how to operate it, or track a household item and highlight a part that needs repair with step-by-step instructions.

Object tracking uses the [`ARSession`](https://developer.apple.com/documentation/ARKit/ARSession) and [`ARWorldTrackingConfiguration`](https://developer.apple.com/documentation/ARKit/ARWorldTrackingConfiguration) APIs. You load a reference-object file trained in Create ML, configure a world-tracking session, and respond to anchor updates as ARKit recognizes and follows the object. If you already have `.referenceobject` files from a visionOS app, you can use them in your iOS app without retraining.

> **Note**: Object tracking requires an iPad or iPhone running iOS 27 or later.

For information about creating a reference object file in Create ML, see [`Implementing object tracking in your app`](implementing-object-tracking-in-your-app.md).

#### Configure Object Tracking for Your Use Case

ARKit provides two properties on [`ARWorldTrackingConfiguration`](https://developer.apple.com/documentation/ARKit/ARWorldTrackingConfiguration) for tracking `.referenceobject` files, based on how the object behaves in the scene. You can assign different `.referenceobject` files to each property in the same session.

- **[`detectionObjects`](https://developer.apple.com/documentation/ARKit/ARWorldTrackingConfiguration/detectionObjects)**: Use for objects that are mostly stationary in the scene. The system keeps the pose stable in world space, consuming less power. Virtual content stays aligned with the object as long as it doesn’t move. If the object moves, the system may delay the overlay update.
- **[`trackingObjects`](https://developer.apple.com/documentation/ARKit/ARWorldTrackingConfiguration/trackingObjects)**: Use for moving or handheld objects that require precise pose updates. Assigning a reference object to `trackingObjects` is the iOS equivalent of enabling [`highFrameRateTrackingEnabled`](https://developer.apple.com/documentation/ARKit/ReferenceObject/Configuration/highFrameRateTrackingEnabled) on visionOS. The system tracks the object at the full frame rate of the selected [`videoFormat`](https://developer.apple.com/documentation/ARKit/ARConfiguration/videoFormat-swift.property). For the available formats on the current device, see [`supportedVideoFormats`](https://developer.apple.com/documentation/ARKit/ARConfiguration/supportedVideoFormats).

Both [`ARWorldTrackingConfiguration`](https://developer.apple.com/documentation/ARKit/ARWorldTrackingConfiguration) and [`ARGeoTrackingConfiguration`](https://developer.apple.com/documentation/ARKit/ARGeoTrackingConfiguration) support these properties. Use `ARWorldTrackingConfiguration` for indoor, room-sized AR experiences. Use `ARGeoTrackingConfiguration` to localize a position in outdoor environments where GPS signals may be weak.

> ❗ **Important**: You can’t use `.arobject` and `.referenceobject` files in the same session. The older `.arobject` format, introduced for [`Scanning and Detecting 3D Objects`](https://developer.apple.com/documentation/ARKit/scanning-and-detecting-3d-objects) in iOS 12, only works with `detectionObjects` and doesn’t support the `trackingObjects` property.

#### Configure a Tracking Session

To load a `.referenceobject` file, use the [`init(archiveURL:)`](https://developer.apple.com/documentation/ARKit/ARReferenceObject/init(archiveURL:)) initializer with the file’s URL.

> **Note**: A session supports a maximum of 10 `.referenceobject` files combined across `detectionObjects` and `trackingObjects`.

After loading the reference objects, create an [`ARWorldTrackingConfiguration`](https://developer.apple.com/documentation/ARKit/ARWorldTrackingConfiguration) and assign each object to either `detectionObjects` or `trackingObjects` based on how the object behaves in the scene. Then set the session’s delegate and run the configuration:

```swift
import ARKit
import RealityKit

class ObjectTrackingARSessionDelegate: NSObject, ARSessionDelegate {
    let arView = ARView(frame: .zero)

    // Load reference objects and start AR session.
    func start() throws {
        guard let movingURL = Bundle.main.url(
            forResource: "moving", withExtension: "referenceobject"),
              let stationaryURL = Bundle.main.url(
            forResource: "stationary", withExtension: "referenceobject")
        else {
            throw URLError(.fileDoesNotExist)
        }

        let movingObject = try ARReferenceObject(archiveURL: movingURL)
        let stationaryObject = try ARReferenceObject(archiveURL: stationaryURL)

        let configuration = ARWorldTrackingConfiguration()
        configuration.trackingObjects = [movingObject] // Moving or handheld.
        configuration.detectionObjects = [stationaryObject] // Mostly stationary.

        arView.session.delegate = self
        arView.session.run(configuration)
    }
}
```

When the session starts, ARKit begins looking for objects that match the reference objects. When it recognizes one, it provides an [`ARObjectAnchor`](https://developer.apple.com/documentation/ARKit/ARObjectAnchor) to the session’s delegate.

> ❗ **Important**: High frame-rate tracking with `trackingObjects` significantly increases power consumption and processing load. Only assign objects to `trackingObjects` when they require precise, per-frame pose updates, such as handheld or moving objects.

#### Handle Anchor Updates

As ARKit tracks reference objects, it sends anchor updates through the [`ARSessionDelegate`](https://developer.apple.com/documentation/ARKit/ARSessionDelegate) protocol:

```swift
var entities: [UUID: AnchorEntity] = [:]

// Store the entity for the new anchor.
func session(_ session: ARSession, didAdd anchors: [ARAnchor]) {
    for case let anchor as ARObjectAnchor in anchors {
        let entity = AnchorEntity(anchor: anchor)
        entities[anchor.identifier] = entity
        arView.scene.addAnchor(entity)
    }
}

// Toggle visibility based on tracking state.
func session(_ session: ARSession, didUpdate anchors: [ARAnchor]) {
    for case let anchor as ARObjectAnchor in anchors {
        entities[anchor.identifier]?.isEnabled = anchor.isTracked
    }
}

 // Clean up after removing an anchor.
func session(_ session: ARSession, didRemove anchors: [ARAnchor]) {
    for case let anchor as ARObjectAnchor in anchors {
        if let entity = entities.removeValue(forKey: anchor.identifier) {
            arView.scene.removeAnchor(entity)
        }
    }
}
```

ARKit calls [`session(_:didAdd:)`](https://developer.apple.com/documentation/ARKit/ARSessionDelegate/session(_:didAdd:)) when it first recognizes an object, providing an [`ARObjectAnchor`](https://developer.apple.com/documentation/ARKit/ARObjectAnchor). Store a reference to the entity you create so you can find it again on update and remove.

In [`session(_:didUpdate:)`](https://developer.apple.com/documentation/ARKit/ARSessionDelegate/session(_:didUpdate:)-3qtt8), the [`isTracked`](https://developer.apple.com/documentation/ARKit/ARObjectAnchor/isTracked) property indicates whether the system actively tracks the object. When a tracked object leaves the camera’s field of view, ARKit sets `isTracked` to `false`. Setting `isEnabled` on the entity hides virtual content without removing it, so it reappears instantly when tracking resumes.

ARKit doesn’t call [`session(_:didRemove:)`](https://developer.apple.com/documentation/ARKit/ARSessionDelegate/session(_:didRemove:)) for object anchors automatically. Object anchors remain in the session until your app explicitly removes them. If your app does remove an anchor, clean up the corresponding entity from the scene.

#### Access the Embedded Usdz File

Each `.referenceobject` file can contain an embedded USDZ model of the object from Create ML training. Use the [`usdzFile`](https://developer.apple.com/documentation/ARKit/ARReferenceObject/usdzFile) property to access this model at runtime:

```swift
if let usdzURL = referenceObject.usdzFile {
    // Use the USDZ model for visualization or as occlusion geometry.
}
```

You can use the USDZ to display a preview of the object so people know what to look for before tracking begins, or as occlusion geometry to make virtual content appear behind the tracked object. The `usdzFile` property returns `nil` if the build process strips the USDZ from the reference object file. For more information about stripping USDZ data, see the “Export the reference object file” section in [`Implementing object tracking in your app`](implementing-object-tracking-in-your-app.md).

## See Also

- [Using a reference object with Reality Composer Pro](using-a-reference-object-with-reality-composer-pro.md)
  Import a reference object file to track a real-world object in your visionOS app.
- [Using a reference object with RealityKit](using-a-reference-object-with-realitykit.md)
  Import a reference object file to track a real-world object in your visionOS app.
- [Using a reference object with ARKit in visionOS](using-a-reference-object-with-arkit-in-visionos.md)
  Import a reference object file and track a real-world object in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/using-a-reference-object-with-arkit-in-ios)*