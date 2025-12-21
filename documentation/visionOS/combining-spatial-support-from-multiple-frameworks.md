# Combining spatial support from multiple frameworks

**Framework**: visionOS

Integrate the features of an array of frameworks seamlessly to enhance your spatial app.

#### Overview

When building spatial computing experiences on visionOS, developers leverage a powerful combination of [`ARKit`](https://developer.apple.com/documentation/ARKit), [`RealityKit`](https://developer.apple.com/documentation/RealityKit), and [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) that work seamlessly together. This article demonstrates how these frameworks interoperate by walking through the creation of a bouncing ball game that interacts with the physical world around you.

![A screenshot of showing a person using the bouncing ball app on Apple Vision Pro. The person throws a virtual bouncing ball above a table, highlighted in light blue, with an attached SwiftUI view stating '20 points'.](https://docs-assets.developer.apple.com/published/29cc7ed32cc0ff594b3627b116e262f2/throwing-bouncing-ball%402x.png)

#### Create a Realistic Bouncing Ball

Begin by creating a bouncing ball entity that has physics simulation, collision detection, and input handling. The `setupBouncingBall()` method configures a RealityKit entity with multiple components:

```swift
func setupBouncingBall(_ content: (inout RealityViewContent) {
    // Create a bouncing ball with without physics simulation by default.
    bouncingBall.position = SIMD3<Float>(x: 0, y: 1.3, z: -0.9)
    bouncingBall.physicsBody = PhysicsBodyComponent(mode: .kinematic)
    bouncingBall.collision = CollisionComponent(shapes: [ShapeResource.generateSphere(radius: ImmersiveView.ballRadius)])
    bouncingBall.name = "Bouncing Ball"
    bouncingBall.components.set(InputTargetComponent())
    
    // Add the bouncing ball to the reality view content.
    content.add(bouncingBall)
}
```

The [`PhysicsBodyComponent`](https://developer.apple.com/documentation/RealityKit/PhysicsBodyComponent) enables physics simulation, initially set to [`PhysicsBodyMode.kinematic`](https://developer.apple.com/documentation/RealityKit/PhysicsBodyMode/kinematic) mode for manual control. [`CollisionComponent`](https://developer.apple.com/documentation/RealityKit/CollisionComponent) defines the collision shape using a sphere matching the visual mesh. Setting the [`InputTargetComponent`](https://developer.apple.com/documentation/RealityKit/InputTargetComponent) allows the entity to receive gestures, enabling a player to interact with the model. The method receives a [`RealityViewContent`](https://developer.apple.com/documentation/RealityKit/RealityViewContent) object the [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) `make:` closure provides and places the bouncing ball entity within it.

#### Recognize Your Environment

To make the ball interactive, your app needs hand tracking, gesture, and spatial recognition support. Configure the [`SpatialTrackingSession`](https://developer.apple.com/documentation/RealityKit/SpatialTrackingSession) to track hands and planes in addition to scene understanding:

```swift
@State var spatialTrackingSession = SpatialTrackingSession()

/// Run a spatial tracking session within the reality view content.
func runSpatialTrackingSession(_ content: (inout RealityViewContent)) async {
    // Request spatial tracking of hands and planes with scene understanding 
    // for collisions and physics.
    let configuration = SpatialTrackingSession.Configuration(
        tracking: [.hand, .plane], 
        sceneUnderstanding: [.collision, .physics]
    )
    
    if let unavailableCapabilities = await spatialTrackingSession.run(configuration) {
        // Handle any unavailable capabilities.
    }
}
```

These capabilities form the basis of the bouncing ball entity, allowing it to interact with the player and the environment.

#### Add Ui Gestures to Spatial Entities

An example of cross-framework interoperability is how the SwiftUI gesture system integrates with RealityKit entities through the [`GestureComponent`](https://developer.apple.com/documentation/RealityKit/GestureComponent). This component allows you to attach SwiftUI gestures directly to RealityKit entities:

```swift
// Create an anchor entity to the player's right hand index finger tip.
let rightIndexFingerTip = AnchorEntity(.hand(.right, location: .indexFingerTip))

// ...

if let container = bouncingBall.parent {
    bouncingBall.components.set(GestureComponent(
        // Add a drag gesture to the bouncing ball's gesture component so people 
        // can throw the ball.
        DragGesture(coordinateSpace3D: container)
            .onChanged { value in
                // Reset the bouncing ball's `physicsBody` to `.kinematic` mode 
                // during the drag gesture so it doesn't react to physics.
                bouncingBall.physicsBody = PhysicsBodyComponent(mode: .kinematic)
                
                // Track the bouncing ball with the player's finger during the drag.
                if let fingerTransform = rightIndexFingerTip.transformMatrix(relativeTo: .immersiveSpace) {
                    bouncingBall.move(to: fingerTransform,
                                   relativeTo: container,
                                   duration: 0,
                                   timingFunction: .easeInOut)
                }
                
                // Record the timestamp and position during the drag.
            }
            .onEnded { value in
                // Release the ball by setting it's physics body mode to `.dynamic` 
                // with a high bounce value.
                let material = PhysicsMaterialResource.generate(friction: 0.2, restitution: 1.0)
                bouncingBall.physicsBody = PhysicsBodyComponent(material: material, mode: .dynamic)
            
                // Determine the release velocity vector by comparing the 
                // previous timestamp and position to the current timestamp 
                // and position.
                
                // Apply the velocity to the bouncing ball.
            }
    ))
}
```

The [`DragGesture`](https://developer.apple.com/documentation/SwiftUI/DragGesture) structure’s initializer,  [`init(minimumDistance:coordinateSpace3D:)`](https://developer.apple.com/documentation/SwiftUI/DragGesture/init(minimumDistance:coordinateSpace3D:)), is a spatial SwiftUI gesture that supports motion in three dimensions. During the gesture, switch the physics body to [`PhysicsBodyMode.kinematic`](https://developer.apple.com/documentation/RealityKit/PhysicsBodyMode/kinematic) mode, to allow manual positioning. While dragging, the ball follows your index finger using an [`AnchorEntity`](https://developer.apple.com/documentation/RealityKit/AnchorEntity) which ARKit attaches to your right finger tip making it appear as if you are moving the bouncing ball with your hand. On release, switch the physics body to [`PhysicsBodyMode.dynamic`](https://developer.apple.com/documentation/RealityKit/PhysicsBodyMode/dynamic) mode to re-engage physics simulation on the ball and provide an impulse the app bases on the calculating the velocity from position and time deltas. With this interaction, you can throw the ball in a natural gesture.

> **Note**: For a more complete hand tracking sample with throwing support, see doc://com.apple.developer/documentation/realitykit/integrating-virtual-objects-with-your-environment.

#### Define How the Ball Interacts with the Scene

The key to making the ball interact with the real world is to:

- Enable [`physics`](https://developer.apple.com/documentation/RealityKit/SpatialTrackingSession/Configuration/SceneUnderstandingCapability/physics) and [`collision`](https://developer.apple.com/documentation/RealityKit/SpatialTrackingSession/Configuration/SceneUnderstandingCapability/collision) for the `sceneUnderstanding` parameter in the spatial tracking session. RealityKit requires data on the surfaces surrounding the player to determine where the ball will bounce.
- Provide [`physicsBody`](https://developer.apple.com/documentation/RealityKit/HasPhysicsBody/physicsBody) and [`collision`](https://developer.apple.com/documentation/RealityKit/HasCollision/collision) components to the bouncing ball entity. The ball derives mass, restitution, and shape from these attributes defining its interaction with the player’s environment.

RealityKit uses the information to detect and create collision geometry for surfaces in the physical environment without explicitly invoking ARKit APIs. Allowing RealityKit to perform this work on your behalf can be convenience if you don’t require the detailed information `ARKit` API provides. The scene understanding happens entirely within the RealityKit physics simulation system. After enabling scene understanding, the ball bounces off real-world surfaces like floors, walls, tables, and ceilings.

#### Visualize the Physical World with Plane Anchors

While scene understanding provides invisible collision geometry, you might want to visualize the surfaces or create targets to hit. You provide this support by adding [`AnchorEntity`](https://developer.apple.com/documentation/RealityKit/AnchorEntity) instances for different plane classifications:

```swift
// Create anchor entitites for various objects in the real world.
let wallEntity = AnchorEntity(.plane(.vertical, classification: .wall, minimumBounds: [1, 1]))
content.add(wallEntity)

let floorEntity = AnchorEntity(.plane(.horizontal, classification: .floor, minimumBounds: [1, 1]))
content.add(floorEntity)

let ceilingEntity = AnchorEntity(.plane(.horizontal, classification: .ceiling, minimumBounds: [1, 1]))
content.add(ceilingEntity)

let tableEntity = AnchorEntity(.plane(.horizontal, classification: .table, minimumBounds: [0.1, 0.1]))
content.add(tableEntity)
```

These anchor entities automatically position themselves in scene space when RealityKit detects planes matching their classification, including walls, floors, ceilings, and tables in the player’s environment. You can access the ARKit plane anchor directly from the entity’s [`ARKitAnchorComponent`](https://developer.apple.com/documentation/RealityKit/ARKitAnchorComponent) in the event. When necessary, you have access to all the detail ARKit has to provide in the convenient context of RealityKit event handling. To visualize these planes, subscribe to anchor events and add plane entities to your scene:

```swift
@State var didAnchor: EventSubscription? = nil

// ...

// Subscribe to anchor events.
didAnchor = content.subscribe(to: AnchorStateEvents.DidAnchor.self, { event in
    if event.reason == .newAnchor,
       let anchorComponent = event.entity.components[ARKitAnchorComponent.self],
       let planeAnchor = anchorComponent.anchor as? PlaneAnchor {
        
        // Create visual plane meshes for the plane anchors for recognition 
        // by Apple Vision Pro.
        let planeModel = ModelEntity(
            mesh: MeshResource.generatePlane(
                width: planeAnchor.geometry.extent.width,
                depth: planeAnchor.geometry.extent.height
            ),
            materials: [SimpleMaterial(
                color: UIColor(hue: 0.66, saturation: 0.5, brightness: 1.0, alpha: 0.2),
                isMetallic: false
            )]
        )
        
        planeModel.transform = Transform(matrix: planeAnchor.originFromAnchorTransform)
        
        if let container = bouncingBall.parent {
            container.addChild(planeModel)
        }
    }
})
```

This subscription creates a semitransparent blue plane mesh for each surface RealityKit detects, providing visual feedback about where the ball can bounce.

#### Attach Views to Spatial Entities

You can attach SwiftUI views directly to RealityKit entities using the `ViewAttachmentComponent` initializer, [`init(rootView:)`](https://developer.apple.com/documentation/RealityKit/ViewAttachmentComponent/init(rootView:)). In the context of the game example, it allows you to display game point values or other UI elements that track with the planes:

```swift
// Attach a `PlaneView` showing the number of points in each registered plane anchor.
let wallEntity = AnchorEntity(.plane(.vertical, classification: .wall, minimumBounds: [0.1, 0.1]))

wallEntity.components[ViewAttachmentComponent.self] = ViewAttachmentComponent(
    rootView: PlaneView(text: "30 points")
)

content.add(wallEntity)
```

The SwiftUI renders views as part of the 3D scene and automatically positions them with their container entities.

#### Observe Spatial Entities in Views

SwiftUI views can observe RealityKit entities in nearly the same manner as SwiftUI `@State` and `@Binding` properties. By creating the bouncing ball entity up one level, at the app level in this case, and passing it to both the immersive space and a tracking view, you can observe changes in the bouncing ball in SwiftUI:

```swift
@main
struct BouncingBallApp: App {
    @State var appModel = AppModel()
    
    // Make the bouncing ball entity avialable to the immersive view and 
    // the observing tracking view.
    @State var bouncingBall = ModelEntity(
        mesh: MeshResource.generateSphere(radius: ImmersiveView.ballRadius),
        materials: [SimpleMaterial(color: .red, isMetallic: false)]
    )
    
    var body: some SwiftUI.Scene {
        WindowGroup {
            ContentView()
                .environment(appModel)
            TrackingView(bouncingBall: bouncingBall)
                .environment(appModel)
        }
        
        ImmersiveSpace(id: appModel.immersiveSpaceID) {
            ImmersiveView(bouncingBall: bouncingBall)
                .environment(appModel)
        }
    }
}
```

`TrackingView` observes the ball’s position in real time using the entity’s [`observable`](https://developer.apple.com/documentation/RealityKit/Entity/observable-swift.property) property:

```swift
struct TrackingView: View {
    let bouncingBall: ModelEntity

    var body: some View {
        VStack {
            Button {
                // Reset the bouncing ball to its initial state when pressing the button.
                bouncingBall.position = SIMD3<Float>(x: 0, y: 1.3, z: -0.9)
                bouncingBall.physicsBody = PhysicsBodyComponent(mode: .kinematic)
            } label: {
                Text("Reset bouncing ball")
            }
            .disabled(distance() < 5) // Enable the reset button when the bouncing ball is too far away.
        }
        .padding()
    }

    /// Calculate the bouncing ball's distance from the origin.
    func distance() -> Float {
        let position = bouncingBall.observable.position
    
        return sqrt(position.x * position.x + position.y * position.y + position.z * position.z)
    }
}
```

As the ball moves in the immersive space, the tracking view automatically updates in the separate window. Explicit use of the `observable` property is the only difference from standard `@State` property observation. When the distance is greater than `5` meters, it can be difficult for the player to recall the ball with the pinch gesture. In this condition, the `TrackingView` enables the bouncing ball’s Reset button, allowing the player to return the ball to its original state. This demonstrates how you can fully integrate RealityKit entities with the SwiftUI observation system, allowing seamless data flow between 3D spatial content and traditional and a 2D UI.

## See Also

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
- [Connecting iPadOS and visionOS apps over the local network](connecting-ipados-and-visionos-apps-over-the-local-network.md)
  Build an iPadOS companion app to control your visionOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/combining-spatial-support-from-multiple-frameworks)*