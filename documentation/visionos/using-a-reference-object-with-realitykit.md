# Using a reference object with RealityKit

**Framework**: visionOS

Import a reference object file to track a real-world object in your visionOS app.

#### Overview

You can use reference objects in your visionOS app to track real-world objects in a person’s surroundings. With this capability, you can attach virtual content to those real-world objects to create engaging experiences. For example, with a reference object, you can track a household item and add virtual content to it, like highlighting a part and showing how to fix it.

To create a reference object, first, obtain a 3D model asset, train a machine learning model with that 3D model asset in Create ML, and then import the resulting reference object file into your app. You can use RealityKit to import the reference object file, track objects, and add virtual content for interactiveness.

For more information about creating a reference object file, see [`Implementing object tracking in your visionOS app`](implementing-object-tracking-in-your-visionos-app.md).

##### Add Your Reference Object and Track It with an Anchoring Component

After generating the `.referenceobject` file with Create ML, add the reference object file to your Xcode project’s main bundle. Then, create an [`AnchoringComponent`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/anchoringcomponent) to track the position of the reference object file. This allows the system to move the anchoring component to follow your real-world object, and to anchor virtual content to it. Using this `AnchoringComponent` is equivalent to setting the Anchoring option on your component in Reality Composer Pro.

In the `ImmersiveView` file, initialize either an `AnchoringComponent` or an [`AnchorEntity`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/anchorentity) with the [`referenceObject`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/referenceobject(from:)) target, and create an [`ObjectAnchoringSource`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/anchoringcomponent/objectanchoringsource) to configure the anchoring.

```swift
// ImmersiveView.swift
struct ImmersiveView: View {
    var body: some View {
        RealityView { content in
            // Find the URL of the reference object file.
            let objectURL = Bundle.main.url(forResource: "VintageGramophone", withExtension: ".referenceobject")!
            
            // Create an object-anchoring entity.
            let anchorSource = AnchoringComponent.ObjectAnchoringSource(objectURL)
            let objectAnchor = AnchorEntity(.referenceObject(from: anchorSource))
            content.add(objectAnchor)
        }
    }
}
```

##### Import the Usdz File to Visualize the Model

Reference object files can optionally bundle with the USDZ file that Create ML uses for training. Adding the USDZ file directly, even if your reference object doesn’t have the model file packaged within it, lets you directly load the `objectURL` into your project. Retrieve this USDZ file through ARKit and use it as a guide for RealityKit content creation.

```swift
import ARKit

// Use the same reference object file URL to load the object. 
guard let referenceObject = try? await ReferenceObject(from: objectURL) else {
    print("Failed to load reference object")
    return
}

// Load the USDZ file from your reference object.
guard let modelURL = referenceObject.usdzFile else {
    print("The USDZ file isn't bundled in the reference object")
    return
}
```

##### Add Occlusion to Your Object

The RealityKit [`OcclusionMaterial`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/occlusionmaterial/) provides a way to render an entity that blocks and occludes other entities to reveal camera passthrough. This is useful in creating the correct depth perception between the real-world object the system tracks and the virtual content you add to your app. You can use the imported USDZ file from your reference object file to create a [`ModelEntity`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/modelentity) that generates a virtual representation of your physical object, so you can add occlusion behavior to it.

![An image of a globe with multiple spacecrafts circling it. The globe is partially occluding two of the spacecrafts as they pass behind it.](https://docs-assets.developer.apple.com/published/216a6e342c7b5ab9da77adba7b8bcf1d/ambient-occlusion%402x.png)

```swift
// Load the `modelEntity` with the `modelURL` containing the USDZ file.
let modelEntity = try! await ModelEntity(contentsOf: modelURL)

// Swap out the material of the `modelEntity` with `OcclusionMaterial`.
modelEntity.model?.materials = [OcclusionMaterial()]
objectAnchor.addChild(modelEntity)
```

##### Add Attachments to the Model

Before adding interaction, incorporate guidance in your app so that anyone can navigate through using it. Use [`attachments`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/realityview/init(make:update:attachments:)) to combine SwiftUI content with RealityKit content to create these guiding features. Attach SwiftUI labels and interfaces to the object-tracking entities.

![An image of a globe highlighting a continent with an attachment of a label and a window with selections.](https://docs-assets.developer.apple.com/published/37064d18ac85dd8e08a111c021eb5fba/attachments-globe%402x.png)

```swift
RealityView { content, attachments in
        // Set up the object-tracking `AnchorEntity`.

        // Add an attachment to the object anchor.
        if let attachment = attachments.entity(for: "TextPrompt") {
            objectAnchor.addChild(attachment)
        }
    
} attachments: {
        Attachment(id: "TextPrompt") {
            Text("Hello World")
        }
}
```

##### Add Interaction and Virtual Content to Your App

RealityKit provides a seamless way to incorporate virtual content within your app. Use virtual effects to increase interaction with features like occlusion, physics simulation, collisions, and SwiftUI gestures. To add effects, use ARKit to load the model and add content on top of the real-world object.

##### Access the Transform with a Tracking Session

Before adding any interaction or virtual content to your app, you have the option to configure a [`SpatialTrackingSession`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/spatialtrackingsession/).  A `SpatialTrackingSession` requests world-tracking permission from the user, and provides the accurate position and rotation of the object.

Creating an `AnchoringComponent` allows the system to properly track and anchor virtual content to the object. However, due to privacy reasons, transform information for the component isn’t available without user authorization. The transform information allows you to track the accurate position and orientation in the real world.

To ask for world-tracking authorization from the user, set up the `SpatialTrackingSession` with [`object`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/spatialtrackingsession/configuration/anchorcapability/object) anchor capability. If you’re using the ARKit framework in your app, this authorization is always required.

To set up a `SpatialTrackingSession` that your app shares, configure the session within `AppModel`.

```swift
// AppModel.swift
import RealityKit

@MainActor
@Observable

class AppModel {
    // Other existing properties in `AppModel`.

    let spatialTrackingSession = SpatialTrackingSession()
} 
```

In the `ImmersiveView` file, configure the `SpatialTrackingSession` to begin tracking the object.

```swift
struct ImmersiveView: View {
    @Environment(AppModel.self) private var appModel

    var body: some View {
        RealityView { content in
            // Initialize a spatial-tracking session.
            let configuration = SpatialTrackingSession.Configuration(tracking: [.object])
            await appModel.spatialTrackingSession.run(configuration)
        }
    }
}
```

##### Set Up Collision and Physics Simulation on Your Objects

Incorporate virtual actions into your app by adding collisions and physics simulations.

> **Note**: `SpatialTrackingSession` is required when using an `AnchorEntity` physics simulation. Follow the guidelines above to configure a `SpatialTrackingSession`.

To enable collision and physics on your object-tracking entity, configure the [`PhysicsSimulation`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/anchoringcomponent/physicssimulation-swift.enum) property of your `AnchorEntity`. This property allows you to select entities with an `AnchoringComponent`  to interact with each other physically.

```swift
let objectAnchor = AnchorEntity(.referenceObject(from: anchorSource), trackingMode: .continuous, physicsSimulation: .none)
```

With your `PhysicsSimulation` in place, add a [`CollisionComponent`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/collisioncomponent) with the object’s shape. This creates a collision effect with other entities that are also collision components.

```swift
// Create a `MeshResource` to define a high-level representation of your model. 
let referenceModel: MeshResource = modelEntity.model!.mesh

//  Use `ShapeResource` to create the shape of your model to apply collision to. 
let referenceShape= try! await ShapeResource.generateConvex(from: referenceModel)
modelEntity.components.set(CollisionComponent(shapes: [referenceShape], mode: .colliding))
```

With the collision feature in place, use [`CollisionEvents`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/collisionevents) to detect collisions when they begin, update, and end for your entities.

##### Configure Interaction with Gestures

To respond to SwiftUI gestures like [`SpatialTapGesture`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/spatialtapgesture/), [`DragGesture`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/draggesture/), and [`RotateGesture3D`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/rotategesture3d/), the object-anchored entity needs to have a `CollisionComponent` for input detection and an [`InputTargetComponent`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/inputtargetcomponent/) to handle all forms of input in your app.

```swift
modelEntity.components.set(InputTargetComponent(allowedInputTypes: .all))
```

Additionally, to make the object respond to a person’s gaze with a highlight, add a [`HoverEffectComponent`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/hovereffectcomponent/).

```swift
modelEntity.components.set(HoverEffectComponent())
```

## See Also

- [Using a reference object with Reality Composer Pro](using-a-reference-object-with-reality-composer-pro.md)
  Import a reference object file to track a real-world object in your visionOS app.
- [Using a reference object with ARKit](using-a-reference-object-with-arkit.md)
  Import a reference object file and track a real-world object in your visionOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/using-a-reference-object-with-realitykit)*